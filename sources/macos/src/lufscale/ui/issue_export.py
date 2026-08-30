"""Pure helpers for exporting retained warnings and errors."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable, Sequence


def csv_export_path(filename: str | Path) -> Path:
    """Return *filename* with CSV as its enforced output format."""
    path = Path(filename)
    if path.suffix.lower() == ".csv":
        return path
    return path.with_suffix(".csv")


def write_issue_csv(
    path: str | Path,
    headers: Sequence[object],
    rows: Iterable[Sequence[object]],
) -> None:
    """Write a spreadsheet-friendly UTF-8 CSV with standard quoting."""
    with Path(path).open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(rows)


__all__ = ["csv_export_path", "write_issue_csv"]
