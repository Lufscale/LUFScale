"""Cache persistant des mesures de sonie FFmpeg."""

from __future__ import annotations

import hashlib
import json
import os
import threading
import uuid
from pathlib import Path
from typing import Any, Sequence


def analysis_record_key(sources: Sequence[Path]) -> str:
    raw = "\0".join(str(source.resolve()) for source in sources).encode(
        "utf-8"
    )
    return hashlib.sha256(raw).hexdigest()


def analysis_source_signatures(
    sources: Sequence[Path],
) -> list[dict[str, Any]]:
    return [
        {
            "path": str(source.resolve()),
            "signature": {
                "size": (stat := source.stat()).st_size,
                "mtime_ns": stat.st_mtime_ns,
            },
        }
        for source in sources
    ]


class AnalysisCache:
    """Thread-safe, atomic cache for reusable FFmpeg loudness analyses."""

    FORMAT_VERSION = 1

    def __init__(self, path: Path) -> None:
        self.path = path
        self.journal_path = path.with_name(f"{path.name}.journal")
        self._lock = threading.RLock()
        self._records: dict[str, dict[str, Any]] = {}
        self._dirty = False
        self._load()

    @property
    def has_pending_changes(self) -> bool:
        with self._lock:
            return self._dirty

    def _load(self) -> None:
        try:
            payload = json.loads(self.path.read_text(encoding="utf-8"))
            if payload.get("format_version") == self.FORMAT_VERSION:
                records = payload.get("records", {})
                if isinstance(records, dict):
                    self._records = records
        except (OSError, ValueError, TypeError):
            self._records = {}
        self._replay_journal()

    def _replay_journal(self) -> None:
        try:
            handle = self.journal_path.open("r", encoding="utf-8")
        except OSError:
            return
        with handle:
            for line in handle:
                try:
                    update = json.loads(line)
                except (ValueError, TypeError):
                    continue
                if not isinstance(update, dict):
                    continue
                key = update.get("key")
                record = update.get("record")
                if isinstance(key, str) and isinstance(record, dict):
                    self._records[key] = record

    def measurements(
        self,
        sources: Sequence[Path],
        configuration: dict[str, Any],
    ) -> dict[str, str] | None:
        key = analysis_record_key(sources)
        with self._lock:
            record = self._records.get(key)
            if not record:
                return None
            try:
                valid = (
                    record.get("configuration") == configuration
                    and record.get("source_signatures")
                    == analysis_source_signatures(sources)
                )
            except OSError:
                return None
            if not valid:
                return None
            measurements = record.get("measurements")
            if not isinstance(measurements, dict):
                return None
            return {
                str(name): str(value)
                for name, value in measurements.items()
            }

    def store(
        self,
        sources: Sequence[Path],
        configuration: dict[str, Any],
        measurements: dict[str, str],
    ) -> None:
        key = analysis_record_key(sources)
        with self._lock:
            record = {
                "configuration": configuration,
                "source_signatures": analysis_source_signatures(sources),
                "measurements": dict(measurements),
            }
            if self._records.get(key) == record:
                return
            self._records[key] = record
            if not self.path.is_file() and not self.journal_path.is_file():
                self._dirty = True
                self._write_locked()
                self._dirty = False
            else:
                self._dirty = True
                self._append_journal_locked(key, record)

    def _append_journal_locked(
        self,
        key: str,
        record: dict[str, Any],
    ) -> None:
        self.journal_path.parent.mkdir(parents=True, exist_ok=True)
        with self.journal_path.open("a", encoding="utf-8") as handle:
            handle.write(
                json.dumps(
                    {"key": key, "record": record},
                    ensure_ascii=False,
                    separators=(",", ":"),
                )
            )
            handle.write("\n")

    def flush(self) -> bool:
        """Compact updates made by this instance, if any."""
        with self._lock:
            if not self._dirty or not self._records:
                return False
            self._write_locked()
            self.journal_path.unlink(missing_ok=True)
            self._dirty = False
            return True

    def _write_locked(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_name(
            f".{self.path.name}.{uuid.uuid4().hex}.tmp"
        )
        payload = {
            "format_version": self.FORMAT_VERSION,
            "records": self._records,
        }
        try:
            temporary.write_text(
                json.dumps(payload, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            os.replace(temporary, self.path)
        finally:
            temporary.unlink(missing_ok=True)


__all__ = [
    "AnalysisCache",
    "analysis_record_key",
    "analysis_source_signatures",
]
