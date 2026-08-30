"""État testable du suivi d'une conversion, sans dépendance à Qt."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..processing.metrics import (
    estimate_calibration_is_ready,
    estimate_remaining_seconds,
    refresh_estimated_total_duration_seconds,
)


ETA_REFRESH_COMPLETED_ITEMS = 5
ETA_REFRESH_ACTIVE_SECONDS = 10.0


@dataclass(frozen=True, slots=True)
class ProcessingIssue:
    """One per-file warning or error retained for later inspection."""

    category: str
    filename: str
    path: str
    detail: str


@dataclass(slots=True)
class ExecutionProgressState:
    """État temporel, estimation et compteurs d'une conversion."""

    conversion_started_at: float | None = None
    conversion_paused: bool = False
    conversion_pause_started_at: float | None = None
    conversion_paused_seconds: float = 0.0
    elapsed_seconds: float = 0.0
    eta_started_at: float | None = None
    eta_current: int = 0
    eta_total: int = 0
    eta_baseline_completed: int = 0
    eta_parallel_jobs: int = 1
    eta_pause_baseline: float = 0.0
    estimated_total_seconds: float | None = None
    eta_last_estimate_completed: int = 0
    eta_last_estimate_elapsed: float = 0.0
    eta_state: str = "unavailable"
    activity_visible: bool = False
    activity_key: str = "activity_progress"
    activity_values: dict[str, Any] = field(default_factory=dict)
    activity_success: int = 0
    activity_warnings: int = 0
    activity_failed: int = 0
    activity_skipped: int = 0
    activity_compliant: int = 0
    log_entries: deque[tuple[str, str]] = field(
        default_factory=lambda: deque(maxlen=5000)
    )
    issues: dict[str, list[ProcessingIssue]] = field(
        default_factory=lambda: {"warning": [], "error": []}
    )

    def reset_for_run(self) -> None:
        self.activity_success = 0
        self.activity_warnings = 0
        self.activity_failed = 0
        self.activity_skipped = 0
        self.activity_compliant = 0
        self.eta_current = 0
        self.eta_total = 0
        self.log_entries.clear()
        self.issues["warning"].clear()
        self.issues["error"].clear()

    def add_issue(
        self,
        category: str,
        source: str,
        detail: str,
    ) -> ProcessingIssue | None:
        """Retain a structured issue without parsing the visible log."""
        if category not in self.issues:
            return None
        source_path = Path(source).expanduser()
        issue = ProcessingIssue(
            category=category,
            filename=source_path.name or str(source_path),
            path=str(source_path.parent),
            detail=str(detail).strip(),
        )
        self.issues[category].append(issue)
        return issue

    def count_activity(self, category: str, message: str) -> None:
        if message.startswith("  "):
            return
        if category == "success":
            self.activity_success += 1
        elif category == "compliant":
            self.activity_success += 1
            self.activity_compliant += 1
        elif category == "warning":
            self.activity_success += 1
            self.activity_warnings += 1
        elif category == "error":
            self.activity_failed += 1
        elif category in {"resumed", "skipped"}:
            self.activity_skipped += 1

    def current_paused_duration(self, now: float) -> float:
        paused = self.conversion_paused_seconds
        if self.conversion_pause_started_at is not None:
            paused += now - self.conversion_pause_started_at
        return paused

    def active_conversion_elapsed(self, now: float) -> float:
        if self.conversion_started_at is None:
            return self.elapsed_seconds
        return max(
            0.0,
            now
            - self.conversion_started_at
            - self.current_paused_duration(now),
        )

    def start_elapsed_monitoring(self, now: float) -> None:
        self.conversion_started_at = now
        self.conversion_paused = False
        self.conversion_pause_started_at = None
        self.conversion_paused_seconds = 0.0
        self.elapsed_seconds = 0.0
        self.eta_started_at = None
        self.eta_current = 0
        self.eta_total = 0
        self.eta_baseline_completed = 0
        self.eta_parallel_jobs = 1
        self.eta_pause_baseline = 0.0
        self.estimated_total_seconds = None
        self.eta_last_estimate_completed = 0
        self.eta_last_estimate_elapsed = 0.0
        self.eta_state = "calculating"

    def pause(self, now: float) -> float:
        self.elapsed_seconds = self.active_conversion_elapsed(now)
        self.conversion_pause_started_at = now
        self.conversion_paused = True
        return self.elapsed_seconds

    def resume(self, now: float) -> None:
        if self.conversion_pause_started_at is not None:
            self.conversion_paused_seconds += (
                now - self.conversion_pause_started_at
            )
        self.conversion_pause_started_at = None
        self.conversion_paused = False

    def stop_elapsed_monitoring(
        self,
        now: float,
        final_elapsed: float | None = None,
    ) -> float:
        if final_elapsed is None:
            final_elapsed = self.active_conversion_elapsed(now)
        if self.conversion_pause_started_at is not None:
            self.conversion_paused_seconds += (
                now - self.conversion_pause_started_at
            )
            self.conversion_pause_started_at = None
        self.conversion_paused = False
        self.conversion_started_at = None
        self.elapsed_seconds = max(0.0, final_elapsed)
        return self.elapsed_seconds

    def scan_finished(self, total: int) -> None:
        self.eta_started_at = None
        self.eta_current = 0
        self.eta_total = max(total, 0)
        self.eta_baseline_completed = 0
        self.eta_parallel_jobs = 1
        self.estimated_total_seconds = None
        self.eta_last_estimate_completed = 0
        self.eta_last_estimate_elapsed = 0.0
        self.eta_state = "calculating" if total > 0 else "unavailable"

    def estimate_calibration_started(
        self,
        completed: int,
        total: int,
        parallel_jobs: int,
        now: float,
    ) -> None:
        self.eta_started_at = now
        self.eta_current = max(0, completed)
        self.eta_total = max(0, total)
        self.eta_baseline_completed = self.eta_current
        self.eta_parallel_jobs = max(1, parallel_jobs)
        self.eta_pause_baseline = self.current_paused_duration(now)
        self.estimated_total_seconds = None
        self.eta_last_estimate_completed = self.eta_current
        self.eta_last_estimate_elapsed = 0.0
        self.eta_state = (
            "calculating"
            if self.eta_total > self.eta_baseline_completed
            else "complete"
        )

    def progress(self, current: int, total: int) -> None:
        self.eta_current = max(0, current)
        self.eta_total = max(0, total)

    def update_eta_estimate(self, now: float) -> None:
        if (
            self.eta_state in {"unavailable", "complete"}
            or self.eta_started_at is None
            or self.eta_total <= 0
        ):
            return
        if self.eta_current >= self.eta_total:
            self.estimated_total_seconds = None
            self.eta_state = "complete"
            return
        elapsed = max(
            0.0,
            now
            - self.eta_started_at
            - max(
                0.0,
                self.current_paused_duration(now)
                - self.eta_pause_baseline,
            ),
        )
        effective_completed = (
            self.eta_current - self.eta_baseline_completed
        )
        effective_total = self.eta_total - self.eta_baseline_completed
        if not estimate_calibration_is_ready(
            elapsed,
            effective_completed,
            effective_total,
            self.eta_parallel_jobs,
        ):
            self.eta_state = "calculating"
            return
        elapsed_since_start = self.active_conversion_elapsed(now)
        if self.estimated_total_seconds is not None:
            completed_since_refresh = (
                self.eta_current - self.eta_last_estimate_completed
            )
            active_seconds_since_refresh = max(
                0.0,
                elapsed_since_start - self.eta_last_estimate_elapsed,
            )
            if (
                completed_since_refresh < ETA_REFRESH_COMPLETED_ITEMS
                and active_seconds_since_refresh
                < ETA_REFRESH_ACTIVE_SECONDS
            ):
                self.eta_state = "estimate"
                return
        raw_estimate = estimate_remaining_seconds(
            elapsed,
            effective_completed,
            effective_total,
        )
        if raw_estimate is None:
            self.eta_state = "calculating"
            return
        self.estimated_total_seconds = (
            refresh_estimated_total_duration_seconds(
                self.estimated_total_seconds,
                elapsed_since_start,
                raw_estimate,
            )
        )
        self.eta_last_estimate_completed = self.eta_current
        self.eta_last_estimate_elapsed = elapsed_since_start
        self.eta_state = (
            "estimate"
            if self.estimated_total_seconds is not None
            else "calculating"
        )

    def finish(
        self,
        *,
        success: int,
        failed: int,
        skipped: int,
        warnings: int,
        compliant: int,
        cancelled: bool,
    ) -> None:
        self.eta_state = "unavailable" if cancelled else "complete"
        self.estimated_total_seconds = None
        self.activity_success = max(0, success)
        self.activity_warnings = max(0, warnings)
        self.activity_failed = max(0, failed)
        self.activity_skipped = max(0, skipped)
        self.activity_compliant = max(0, compliant)


__all__ = ["ExecutionProgressState", "ProcessingIssue"]
