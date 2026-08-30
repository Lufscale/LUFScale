"""Thread-safe decisions for LUFScale analysis strategies."""

from __future__ import annotations

import threading
from dataclasses import asdict, dataclass


ANALYSIS_METHODS = frozenset({"historical", "fast", "adaptive", "hybrid"})
DEFAULT_ANALYSIS_METHOD = "historical"


def normalized_analysis_method(value: object) -> str:
    """Return a supported analysis method without accepting silent variants."""
    method = str(value or "").strip().lower()
    return method if method in ANALYSIS_METHODS else DEFAULT_ANALYSIS_METHOD


@dataclass(frozen=True, slots=True)
class AdaptiveAnalysisSnapshot:
    """Machine-readable state of the adaptive profitability decision."""

    sample_size: int
    fast_successes: int
    fallbacks: int
    probe_seconds: float
    fallback_probe_seconds: float
    fallback_full_seconds: float
    estimated_baseline_seconds: float | None
    estimated_strategy_seconds: float | None
    estimated_savings_seconds: float | None
    estimated_savings_ratio: float | None
    full_to_probe_ratio: float | None
    decision: str
    probes_enabled: bool


class AdaptiveAnalysisController:
    """Stop fast probes when measured costs predict no useful speed gain.

    Successful probes do not have a historical measurement to compare with.
    Their missing full-analysis cost is estimated from the observed ratio
    between full and probe durations on fallback files.  The estimate is
    weighted by probe duration, which tracks source duration on one system.
    """

    def __init__(
        self,
        *,
        minimum_sample_size: int = 12,
        minimum_fallbacks: int = 3,
        required_savings_ratio: float = 0.05,
    ) -> None:
        self.minimum_sample_size = max(1, int(minimum_sample_size))
        self.minimum_fallbacks = max(1, int(minimum_fallbacks))
        self.required_savings_ratio = max(
            0.0, float(required_savings_ratio)
        )
        self._lock = threading.Lock()
        self._sample_size = 0
        self._fast_successes = 0
        self._fallbacks = 0
        self._probe_seconds = 0.0
        self._fallback_probe_seconds = 0.0
        self._fallback_full_seconds = 0.0
        self._decision = "sampling"
        self._probes_enabled = True

    def should_probe(self) -> bool:
        with self._lock:
            return self._probes_enabled

    def observe(
        self,
        *,
        fast_success: bool,
        probe_seconds: float,
        full_seconds: float = 0.0,
    ) -> AdaptiveAnalysisSnapshot:
        """Record one completed probe and update the shared decision."""
        probe = max(0.0, float(probe_seconds))
        full = max(0.0, float(full_seconds))
        with self._lock:
            self._sample_size += 1
            self._probe_seconds += probe
            if fast_success:
                self._fast_successes += 1
            else:
                self._fallbacks += 1
                self._fallback_probe_seconds += probe
                self._fallback_full_seconds += full
            self._update_decision_locked()
            return self._snapshot_locked()

    def snapshot(self) -> AdaptiveAnalysisSnapshot:
        with self._lock:
            return self._snapshot_locked()

    def as_dict(self) -> dict[str, object]:
        return asdict(self.snapshot())

    def _estimate_locked(
        self,
    ) -> tuple[float, float, float, float, float] | None:
        if self._fallback_probe_seconds <= 0.0:
            return None
        ratio = self._fallback_full_seconds / self._fallback_probe_seconds
        successful_probe_seconds = (
            self._probe_seconds - self._fallback_probe_seconds
        )
        estimated_success_full = successful_probe_seconds * ratio
        baseline = self._fallback_full_seconds + estimated_success_full
        strategy = self._fallback_full_seconds + self._probe_seconds
        savings = baseline - strategy
        savings_ratio = savings / baseline if baseline > 0.0 else 0.0
        return ratio, baseline, strategy, savings, savings_ratio

    def _update_decision_locked(self) -> None:
        if not self._probes_enabled:
            return
        if self._sample_size < self.minimum_sample_size:
            return
        if self._fallbacks < self.minimum_fallbacks:
            self._decision = "sampling_insufficient_fallbacks"
            return
        estimate = self._estimate_locked()
        if estimate is None:
            self._decision = "sampling_insufficient_timing"
            return
        savings_ratio = estimate[-1]
        if savings_ratio >= self.required_savings_ratio:
            self._decision = "continue_profitable"
            return
        self._decision = "disabled_unprofitable"
        self._probes_enabled = False

    def _snapshot_locked(self) -> AdaptiveAnalysisSnapshot:
        estimate = self._estimate_locked()
        if estimate is None:
            ratio = baseline = strategy = savings = savings_ratio = None
        else:
            ratio, baseline, strategy, savings, savings_ratio = estimate
        return AdaptiveAnalysisSnapshot(
            sample_size=self._sample_size,
            fast_successes=self._fast_successes,
            fallbacks=self._fallbacks,
            probe_seconds=self._probe_seconds,
            fallback_probe_seconds=self._fallback_probe_seconds,
            fallback_full_seconds=self._fallback_full_seconds,
            estimated_baseline_seconds=baseline,
            estimated_strategy_seconds=strategy,
            estimated_savings_seconds=savings,
            estimated_savings_ratio=savings_ratio,
            full_to_probe_ratio=ratio,
            decision=self._decision,
            probes_enabled=self._probes_enabled,
        )


__all__ = [
    "ANALYSIS_METHODS",
    "DEFAULT_ANALYSIS_METHOD",
    "AdaptiveAnalysisController",
    "AdaptiveAnalysisSnapshot",
    "normalized_analysis_method",
]
