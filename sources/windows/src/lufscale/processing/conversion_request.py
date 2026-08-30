"""Contrat immuable transmis au worker de conversion."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..audio.core import LoudnessSettings


@dataclass(frozen=True)
class ConversionRequest:
    """Regroupe les paramètres validés d'un lancement de traitement."""

    ffmpeg: str
    inputs: tuple[Path, ...]
    output: Path
    settings: LoudnessSettings
    overwrite: bool
    operation: str
    max_parallel: int
    resume_enabled: bool
    quality_control: bool
    generate_report: bool
    language: str
    skip_compliant: bool
    analysis_method: str = "historical"

    @property
    def loudness_comparison_state(self) -> str:
        """Initial state of the measured before/after comparison."""
        if self.operation == "analyze":
            return "analysis_only"
        if self.operation == "replaygain":
            return "replaygain"
        if self.operation not in {"convert", "replaygain"}:
            return "not_applicable"
        if self.operation == "convert" and not self.quality_control:
            return "needs_qc"
        return "waiting"

    def worker_parameters(self) -> dict[str, Any]:
        """Retourne le contrat nommé historique de ``WorkerCoordinator``."""
        return {
            "ffmpeg": self.ffmpeg,
            "inputs": list(self.inputs),
            "output": self.output,
            "settings": self.settings,
            "overwrite": self.overwrite,
            "operation": self.operation,
            "max_parallel": self.max_parallel,
            "resume_enabled": self.resume_enabled,
            "quality_control": self.quality_control,
            "generate_report": self.generate_report,
            "language": self.language,
            "skip_compliant": self.skip_compliant,
            "analysis_method": self.analysis_method,
        }


__all__ = ["ConversionRequest"]
