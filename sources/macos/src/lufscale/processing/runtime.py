"""Utilitaires d'exécution et de parallélisme indépendants de l'interface."""

from __future__ import annotations

import os
import subprocess
from typing import Any

from ..i18n.loader import translate

try:
    import psutil
except ImportError:
    psutil = None


def process_flags() -> int:
    return subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0


def concise_ffmpeg_error(stderr: str, language: str = "fr") -> str:
    lines = [line.strip() for line in stderr.splitlines() if line.strip()]
    useful = [
        line
        for line in lines
        if "error" in line.lower()
        or "invalid" in line.lower()
        or "failed" in line.lower()
        or "unable" in line.lower()
    ]
    selected = useful[-3:] if useful else lines[-3:]
    return " | ".join(selected) or translate(
        language, "ffmpeg_error_no_detail"
    )


def sample_cpu_percent(provider: Any | None = None) -> float | None:
    source = psutil if provider is None else provider
    if source is None:
        return None
    try:
        value = float(source.cpu_percent(interval=None))
    except (AttributeError, OSError, RuntimeError, TypeError, ValueError):
        return None
    return max(0.0, min(100.0, value))


def automatic_parallel_ceiling(provider: Any | None = None) -> int:
    source = psutil if provider is None else provider
    count: int | None = None
    if source is not None:
        try:
            reported = source.cpu_count(logical=True)
            count = int(reported) if reported else None
        except (AttributeError, OSError, RuntimeError, TypeError, ValueError):
            count = None
    if count is None:
        count = max(1, os.cpu_count() or 1)
    return min(16, max(1, count))


def adjusted_parallel_limit(
    current: int,
    maximum: int,
    cpu_percent: float,
) -> int:
    current = max(1, min(current, maximum))
    if cpu_percent < 70.0 and current < maximum:
        return current + 1
    if cpu_percent > 92.0 and current > 1:
        return current - 1
    return current


__all__ = [
    "adjusted_parallel_limit",
    "automatic_parallel_ceiling",
    "concise_ffmpeg_error",
    "process_flags",
    "psutil",
    "sample_cpu_percent",
]
