"""Hybrid storage for conversion result sets."""

from __future__ import annotations

import json
import os
import sqlite3
import tempfile
from pathlib import Path
from typing import Any, Iterator


DEFAULT_MEMORY_LIMIT = 10_000


class ReportStore:
    """Keep ordinary reports in memory and spill very large runs to SQLite."""

    def __init__(self, memory_limit: int = DEFAULT_MEMORY_LIMIT) -> None:
        self.memory_limit = max(0, int(memory_limit))
        self.path: Path | None = None
        self._connection: sqlite3.Connection | None = None
        self._reports: list[dict[str, Any]] = []
        self._count = 0
        self._analysis_seconds = 0.0
        self._conversion_seconds = 0.0
        self._quality_seconds = 0.0
        self._compliant_count = 0
        self._closed = False

    @property
    def disk_backed(self) -> bool:
        return self._connection is not None

    @property
    def workload_totals(self) -> tuple[float, float, float]:
        return (
            self._analysis_seconds,
            self._conversion_seconds,
            self._quality_seconds,
        )

    @property
    def compliant_count(self) -> int:
        return self._compliant_count

    def append(self, report: dict[str, Any]) -> None:
        self._require_open()
        if self._connection is None and len(self._reports) < self.memory_limit:
            self._reports.append(report)
        else:
            if self._connection is None:
                self._spill_to_disk()
            connection = self._require_connection()
            connection.execute(
                "INSERT INTO reports(sequence, source_key, payload) VALUES (?, ?, ?)",
                self._serialized_row(self._count + 1, report),
            )
            if (self._count + 1) % 256 == 0:
                connection.commit()
        self._count += 1
        self._accumulate(report)

    @staticmethod
    def _serialized_row(sequence: int, report: dict[str, Any]) -> tuple[int, str, str]:
        return (
            sequence,
            str(report.get("source", "")).casefold(),
            json.dumps(
                report,
                ensure_ascii=False,
                separators=(",", ":"),
            ),
        )

    @staticmethod
    def _seconds(report: dict[str, Any], field: str) -> float:
        try:
            return float(report.get(field) or 0.0)
        except (TypeError, ValueError):
            return 0.0

    def _accumulate(self, report: dict[str, Any]) -> None:
        self._analysis_seconds += self._seconds(report, "_analysis_seconds")
        self._conversion_seconds += self._seconds(report, "_conversion_seconds")
        self._quality_seconds += self._seconds(report, "_quality_seconds")
        if (
            bool(report.get("_copied_compliant"))
            and str(report.get("_status_code") or "") == "ok"
        ):
            self._compliant_count += 1

    def _spill_to_disk(self) -> None:
        descriptor, raw_path = tempfile.mkstemp(
            prefix="lufscale_reports_",
            suffix=".sqlite3",
        )
        os.close(descriptor)
        path = Path(raw_path)
        connection: sqlite3.Connection | None = None
        try:
            connection = sqlite3.connect(path)
            connection.execute("PRAGMA journal_mode=OFF")
            connection.execute("PRAGMA synchronous=OFF")
            connection.execute(
                "CREATE TABLE reports ("
                "sequence INTEGER PRIMARY KEY, "
                "source_key TEXT NOT NULL, "
                "payload TEXT NOT NULL)"
            )
            if self._reports:
                connection.executemany(
                    "INSERT INTO reports(sequence, source_key, payload) "
                    "VALUES (?, ?, ?)",
                    (
                        self._serialized_row(sequence, report)
                        for sequence, report in enumerate(self._reports, start=1)
                    ),
                )
                connection.commit()
        except Exception:
            if connection is not None:
                connection.close()
            path.unlink(missing_ok=True)
            raise
        self.path = path
        self._connection = connection
        self._reports.clear()

    def __bool__(self) -> bool:
        return self._count > 0

    def __len__(self) -> int:
        return self._count

    def __iter__(self) -> Iterator[dict[str, Any]]:
        self._require_open()
        if self._connection is None:
            yield from self._reports
            return
        yield from self._iterate_database(source_order=False)

    def sorted_by_source(self) -> Iterator[dict[str, Any]]:
        self._require_open()
        if self._connection is None:
            yield from sorted(
                self._reports,
                key=lambda report: str(report.get("source", "")).casefold(),
            )
            return
        yield from self._iterate_database(source_order=True)

    def _iterate_database(
        self,
        *,
        source_order: bool,
    ) -> Iterator[dict[str, Any]]:
        connection = self._require_connection()
        connection.commit()
        if source_order:
            cursor = connection.execute(
                "SELECT payload FROM reports ORDER BY source_key, sequence"
            )
        else:
            cursor = connection.execute("SELECT payload FROM reports ORDER BY sequence")
        for (payload,) in cursor:
            value = json.loads(payload)
            if isinstance(value, dict):
                yield value

    def _require_open(self) -> None:
        if self._closed:
            raise RuntimeError("ReportStore is closed")

    def _require_connection(self) -> sqlite3.Connection:
        if self._connection is None:
            raise RuntimeError("ReportStore is not disk-backed")
        return self._connection

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        connection = self._connection
        self._connection = None
        if connection is not None:
            connection.close()
        if self.path is not None:
            self.path.unlink(missing_ok=True)
        self._reports.clear()

    def __enter__(self) -> "ReportStore":
        return self

    def __exit__(self, *_args: object) -> None:
        self.close()

    def __del__(self) -> None:
        try:
            self.close()
        except OSError:
            pass


__all__ = ["DEFAULT_MEMORY_LIMIT", "ReportStore"]
