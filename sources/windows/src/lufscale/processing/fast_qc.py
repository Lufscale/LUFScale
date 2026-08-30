"""Runtime accounting for guarded MP3 quality control.

The fast path may certify only results that sit comfortably inside both QC
limits.  Any boundary result, malformed measurement, or ebur128 failure locks
that file to loudnorm for the current attempt and every later retry.
"""

from __future__ import annotations

import statistics
import threading
from collections import Counter
from dataclasses import asdict, dataclass, replace
from typing import Mapping

from .hybrid_analysis import (
    HYBRID_COMPARISON_TOLERANCES,
    compare_measurements,
)


def _finite_qc_fields(measurements: Mapping[str, str] | None) -> dict[str, float]:
    values: dict[str, float] = {}
    if measurements is None:
        return values
    for field in HYBRID_COMPARISON_TOLERANCES:
        try:
            values[field] = float(measurements[field])
        except (KeyError, TypeError, ValueError):
            continue
    return values


@dataclass(frozen=True, slots=True)
class FastQCAttempt:
    label: str
    attempt_index: int
    attempt_kind: str
    selected_as_final: bool
    strategy: str
    permanent_reference_before: bool
    permanent_reference_after: bool
    fast_measurements: dict[str, float]
    reference_measurements: dict[str, float]
    differences: dict[str, float]
    fast_seconds: float
    reference_seconds: float
    candidate_eligible: bool
    fallback_reason: str
    quality_passed: bool
    retry_required: bool | None
    error: str


class FastQCController:
    """Collect thread-safe evidence about every MP3 QC attempt."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._attempts: list[FastQCAttempt] = []

    def record(
        self,
        *,
        label: str,
        attempt_index: int,
        attempt_kind: str,
        strategy: str,
        permanent_reference_before: bool,
        permanent_reference_after: bool,
        fast: Mapping[str, str] | None,
        reference: Mapping[str, str] | None,
        fast_seconds: float,
        reference_seconds: float,
        candidate_eligible: bool,
        fallback_reason: str,
        quality_passed: bool,
        retry_required: bool | None,
        error: str = "",
    ) -> FastQCAttempt:
        differences: dict[str, float] = {}
        if fast is not None and reference is not None:
            _accepted, differences = compare_measurements(fast, reference)
        attempt = FastQCAttempt(
            label=str(label),
            attempt_index=max(0, int(attempt_index)),
            attempt_kind=str(attempt_kind),
            selected_as_final=False,
            strategy=str(strategy),
            permanent_reference_before=bool(permanent_reference_before),
            permanent_reference_after=bool(permanent_reference_after),
            fast_measurements=_finite_qc_fields(fast),
            reference_measurements=_finite_qc_fields(reference),
            differences=differences,
            fast_seconds=max(0.0, float(fast_seconds)),
            reference_seconds=max(0.0, float(reference_seconds)),
            candidate_eligible=bool(candidate_eligible),
            fallback_reason=str(fallback_reason),
            quality_passed=bool(quality_passed),
            retry_required=(
                None if retry_required is None else bool(retry_required)
            ),
            error=str(error),
        )
        with self._lock:
            self._attempts.append(attempt)
        return attempt

    def mark_selected_attempt(self, label: str, attempt_index: int) -> bool:
        selected = (str(label), max(0, int(attempt_index)))
        with self._lock:
            found = False
            for index, attempt in enumerate(self._attempts):
                if (attempt.label, attempt.attempt_index) == selected:
                    self._attempts[index] = replace(
                        attempt, selected_as_final=True
                    )
                    found = True
            return found

    @staticmethod
    def _timing(values: list[float]) -> dict[str, float | int | None]:
        return {
            "count": len(values),
            "total_seconds": sum(values),
            "minimum_seconds": min(values) if values else None,
            "maximum_seconds": max(values) if values else None,
            "mean_seconds": statistics.fmean(values) if values else None,
            "median_seconds": statistics.median(values) if values else None,
        }

    @staticmethod
    def _summary(attempts: list[dict[str, object]]) -> dict[str, object]:
        strategies = Counter(str(item["strategy"]) for item in attempts)
        fallback_reasons = Counter(
            str(item["fallback_reason"])
            for item in attempts
            if str(item["fallback_reason"])
        )
        fast_times = [
            float(item["fast_seconds"])
            for item in attempts
            if float(item["fast_seconds"]) > 0.0
        ]
        reference_times = [
            float(item["reference_seconds"])
            for item in attempts
            if float(item["reference_seconds"]) > 0.0
        ]
        comparisons = [item for item in attempts if item["differences"]]
        fields: dict[str, dict[str, float | int | None]] = {}
        for field in HYBRID_COMPARISON_TOLERANCES:
            values = [
                float(item["differences"][field])
                for item in comparisons
                if field in item["differences"]
            ]
            fields[field] = {
                "count": len(values),
                "minimum": min(values) if values else None,
                "maximum": max(values) if values else None,
                "mean": statistics.fmean(values) if values else None,
                "median": statistics.median(values) if values else None,
            }
        fast_uses = strategies.get("fast_ebur128", 0)
        fallback_uses = strategies.get("fallback_loudnorm", 0)
        locked_uses = strategies.get("locked_loudnorm", 0)
        measured_attempts = fast_uses + fallback_uses + locked_uses
        return {
            "total_attempts": len(attempts),
            "initial_attempts": sum(
                item["attempt_kind"] == "initial" for item in attempts
            ),
            "retry_attempts": sum(
                item["attempt_kind"] == "retry" for item in attempts
            ),
            "selected_final_attempts": sum(
                bool(item["selected_as_final"]) for item in attempts
            ),
            "fast_qc_uses": fast_uses,
            "initial_reference_fallbacks": fallback_uses,
            "permanently_locked_reference_uses": locked_uses,
            "reused_input_measurements": strategies.get("reused_input", 0),
            "fast_qc_use_rate_percent": (
                100.0 * fast_uses / measured_attempts
                if measured_attempts
                else None
            ),
            "fallback_reasons": dict(sorted(fallback_reasons.items())),
            "ebur128_failures": sum(bool(item["error"]) for item in attempts),
            "quality_failures": sum(
                not bool(item["quality_passed"]) for item in attempts
            ),
            "retry_required_attempts": sum(
                item["retry_required"] is True for item in attempts
            ),
            "fast_timing": FastQCController._timing(fast_times),
            "reference_timing": FastQCController._timing(reference_times),
            "paired_fallback_differences": fields,
        }

    def as_dict(self) -> dict[str, object]:
        with self._lock:
            attempts = [asdict(item) for item in self._attempts]
        attempts.sort(
            key=lambda item: (str(item["label"]), int(item["attempt_index"]))
        )
        return {
            "mode": "guarded_fast_qc_with_permanent_file_fallback",
            "fast_engine": "FFmpeg ebur128 (peak=true)",
            "reference_engine": "FFmpeg loudnorm",
            "attempts": attempts,
            "summary": self._summary(attempts),
        }


__all__ = ["FastQCAttempt", "FastQCController"]
