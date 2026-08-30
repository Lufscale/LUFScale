"""Calculs purs partagés par les traitements et l'interface LUFScale."""

from __future__ import annotations

import math
from typing import Any

from ..audio.core import measurements_are_finite


DECIMAL_COMMA_LANGUAGES = {
    "bg",
    "cs",
    "da",
    "el",
    "fr",
    "es",
    "de",
    "fi",
    "hr",
    "hu",
    "it",
    "lt",
    "lv",
    "no",
    "pt",
    "pt_BR",
    "nl",
    "pl",
    "ro",
    "ru",
    "sk",
    "sl",
    "sr",
    "sv",
    "tr",
    "uk",
}


def format_duration(seconds: float, language: str = "fr") -> str:
    if seconds < 60:
        value = f"{seconds:.1f} s"
        return value.replace(".", ",") if language in DECIMAL_COMMA_LANGUAGES else value
    minutes, remaining = divmod(int(round(seconds)), 60)
    if minutes < 60:
        return f"{minutes} min {remaining:02d} s"
    hours, minutes = divmod(minutes, 60)
    return f"{hours} h {minutes:02d} min {remaining:02d} s"


def format_decimal(value: float, language: str, places: int = 2) -> str:
    rendered = f"{float(value):.{max(0, int(places))}f}"
    if language in DECIMAL_COMMA_LANGUAGES:
        return rendered.replace(".", ",")
    return rendered


def format_elapsed_clock(seconds: float) -> str:
    total_seconds = max(0, int(seconds))
    minutes, remaining = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{remaining:02d}"
    return f"{minutes:02d}:{remaining:02d}"


def format_24_hour_duration(seconds: float) -> str:
    """Render a duration without locale-specific 12-hour clock markers."""
    total_seconds = max(0, int(seconds))
    minutes, remaining = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{remaining:02d}"


def distribute_elapsed_time_by_workload(
    elapsed_seconds: float,
    analysis_work_seconds: float,
    conversion_work_seconds: float,
    quality_work_seconds: float,
) -> tuple[float, float, float]:
    """Répartit le temps mural proportionnellement en préservant son total."""
    elapsed = max(0.0, elapsed_seconds)
    work = [
        max(0.0, analysis_work_seconds),
        max(0.0, conversion_work_seconds),
        max(0.0, quality_work_seconds),
    ]
    work_total = sum(work)
    if elapsed <= 0.0 or work_total <= 0.0:
        return 0.0, 0.0, 0.0

    scale = 10 if elapsed < 60.0 else 1
    total_units = max(0, int(round(elapsed * scale)))
    exact_units = [value * total_units / work_total for value in work]
    allocated_units = [math.floor(value) for value in exact_units]
    remaining_units = total_units - sum(allocated_units)
    order = sorted(
        range(len(work)),
        key=lambda index: (
            exact_units[index] - allocated_units[index],
            work[index],
        ),
        reverse=True,
    )
    for index in order[:remaining_units]:
        allocated_units[index] += 1
    return tuple(value / scale for value in allocated_units)


def measurement_value(
    measurements: dict[str, str] | None, key: str
) -> str:
    if not measurements or not measurements_are_finite(measurements):
        return ""
    return f"{float(measurements[key]):.2f}"


def expected_output_loudness(
    report: dict[str, Any],
    target: float,
    operation: str,
) -> float | None:
    """Return the expected per-file output loudness."""
    if operation in {"convert", "replaygain"}:
        expected = float(target)
    else:
        return None
    return expected if math.isfinite(expected) else None


def loudness_comparison_values(
    report: dict[str, Any],
    target: float,
    operation: str,
) -> tuple[float, float, float, float] | None:
    """Return source/output values plus display and QC targets."""
    expected = expected_output_loudness(
        report,
        target,
        operation,
    )
    try:
        before = float(report.get("lufs_avant") or "")
        if operation == "replaygain":
            # ReplayGain leaves the physical stream unchanged.  The second
            # graph therefore represents compatible-player playback: the
            # source loudness plus the exact gain written to the Track tag.
            # It is an estimate, not an output-file measurement.
            after = before + float(report.get("gain_db") or "")
        else:
            after = float(report.get("lufs_apres") or "")
    except (TypeError, ValueError):
        return None
    display_target = float(target)
    if expected is None or not all(
        math.isfinite(value)
        for value in (before, after, display_target, expected)
    ):
        return None
    return before, after, display_target, expected


def estimate_remaining_seconds(
    elapsed_seconds: float,
    completed: int,
    total: int,
) -> float | None:
    if elapsed_seconds <= 0 or completed <= 0 or total <= completed:
        return None
    return max(0.0, elapsed_seconds * (total - completed) / completed)


def estimate_total_duration_seconds(
    elapsed_seconds: float,
    remaining_seconds: float | None,
) -> float | None:
    if remaining_seconds is None:
        return None
    return max(0.0, elapsed_seconds) + max(0.0, remaining_seconds)


def estimate_calibration_sample_count(
    total_items: int,
    parallel_jobs: int,
) -> int:
    total = max(0, total_items)
    if total <= 1:
        return 0
    percentage_sample = min(10, max(2, (total + 9) // 10))
    parallel_sample = min(10, max(1, parallel_jobs))
    return min(total - 1, max(percentage_sample, parallel_sample))


def estimate_calibration_is_ready(
    observed_seconds: float,
    completed_items: int,
    total_items: int,
    parallel_jobs: int,
) -> bool:
    required = estimate_calibration_sample_count(total_items, parallel_jobs)
    return (
        observed_seconds >= 4.0
        and required > 0
        and completed_items >= required
    )


def freeze_estimated_total_duration_seconds(
    current_total_seconds: float | None,
    elapsed_seconds: float,
    remaining_seconds: float | None,
) -> float | None:
    if current_total_seconds is not None:
        return current_total_seconds
    return estimate_total_duration_seconds(elapsed_seconds, remaining_seconds)


def refresh_estimated_total_duration_seconds(
    current_total_seconds: float | None,
    elapsed_seconds: float,
    remaining_seconds: float | None,
    *,
    smoothing_factor: float = 0.35,
) -> float | None:
    """Refresh a total-duration estimate without abrupt visual jumps."""
    candidate = estimate_total_duration_seconds(
        elapsed_seconds,
        remaining_seconds,
    )
    if candidate is None:
        return current_total_seconds
    if current_total_seconds is None:
        return candidate
    weight = max(0.0, min(1.0, float(smoothing_factor)))
    refreshed = current_total_seconds + weight * (
        candidate - current_total_seconds
    )
    return max(float(elapsed_seconds), refreshed)


__all__ = [
    "distribute_elapsed_time_by_workload",
    "estimate_calibration_is_ready",
    "estimate_calibration_sample_count",
    "estimate_remaining_seconds",
    "estimate_total_duration_seconds",
    "expected_output_loudness",
    "format_decimal",
    "format_duration",
    "format_24_hour_duration",
    "format_elapsed_clock",
    "freeze_estimated_total_duration_seconds",
    "measurement_value",
    "loudness_comparison_values",
    "refresh_estimated_total_duration_seconds",
]
