"""État testable des sources et de la destination de traitement."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from ..audio.core import canonicalize_inputs, iter_audio_files


def _path_key(path: Path) -> str:
    return os.path.normcase(str(path.resolve()))


@dataclass(slots=True)
class SourceSelectionState:
    """Conserve les chemins choisis sans dépendre des widgets Qt."""

    paths: list[Path] = field(default_factory=list)
    output_path: Path | None = None

    def add_paths(self, raw_paths: Iterable[Path | str]) -> int:
        """Ajoute les entrées valides et renvoie leur nombre réel."""
        previous_keys = {_path_key(path) for path in self.paths}
        combined = canonicalize_inputs([*self.paths, *raw_paths])
        accepted = sum(
            _path_key(path) not in previous_keys for path in combined
        )
        self.paths = combined
        return accepted

    def remove_rows(self, selected_rows: Iterable[int]) -> None:
        rows = set(selected_rows)
        self.paths = [
            path
            for index, path in enumerate(self.paths)
            if index not in rows
        ]

    def clear(self) -> None:
        self.paths.clear()

    def audio_file_count(self) -> int:
        """Return the number of supported audio files represented by sources."""
        total = 0
        for path in self.paths:
            if path.is_dir():
                total += sum(1 for _path in iter_audio_files(path))
            elif path.is_file():
                total += 1
        return total


def paths_from_clipboard(mime_data) -> list[str]:
    """Extrait les chemins locaux d'un objet MIME de presse-papiers."""
    paths: list[str] = []
    if mime_data.hasUrls():
        paths.extend(
            url.toLocalFile()
            for url in mime_data.urls()
            if url.isLocalFile()
        )
    if paths or not mime_data.hasText():
        return paths
    for line in mime_data.text().splitlines():
        candidate = line.strip().strip('"').strip("'")
        if candidate and Path(candidate).expanduser().exists():
            paths.append(candidate)
    return paths
