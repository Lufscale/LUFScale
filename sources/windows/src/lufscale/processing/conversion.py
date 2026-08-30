"""Worker principal d'analyse et d'uniformisation audio."""

from __future__ import annotations

import csv
import math
import os
import shutil
import subprocess
import threading
import time
import uuid
from concurrent.futures import (
    FIRST_COMPLETED,
    ThreadPoolExecutor,
    wait,
)
from dataclasses import replace
from datetime import datetime
from pathlib import Path
from typing import Any

from PySide6.QtCore import QObject, Signal, Slot

from ..audio.core import (
    LOSSLESS_TARGET_CORRECTION_EXTENSIONS,
    LOUDNORM_LINEAR_SAFETY_MARGIN_DB,
    MP3_DYNAMIC_RETRY_MAX_ATTEMPTS,
    STRICT_TARGET_LUFS_TOLERANCE,
    TARGET_CORRECTION_MAX_ATTEMPTS,
    ConversionJob,
    LoudnessSettings,
    analysis_command,
    assess_quality,
    build_jobs,
    calculate_loudness_gain_db,
    conversion_command,
    dynamic_mp3_output_is_strictly_compliant,
    dynamic_mp3_true_peak_target,
    ebur128_analysis_command,
    fast_analysis_command,
    loudnorm_linear_mode_diagnostics,
    measurements_are_already_compliant,
    measurements_are_finite,
    metadata_dump_command,
    next_dynamic_mp3_true_peak_target,
    next_safe_target_correction_gain,
    parse_ebur128_measurements,
    parse_loudnorm_measurements,
    replaygain_command,
    replaygain_metadata_is_present,
    write_replaygain_container_tags,
)
from ..i18n.loader import SUPPORTED_LANGUAGES, translate
from ..persistence import AnalysisCache, ResumeManifest
from ..version import APP_VERSION
from .metrics import (
    distribute_elapsed_time_by_workload,
    format_duration,
    loudness_comparison_values,
    measurement_value,
)
from .analysis_strategy import (
    AdaptiveAnalysisController,
    normalized_analysis_method,
)
from .hybrid_analysis import qc_fast_candidate_diagnostics
from .fast_qc import FastQCController
from .process_control import ProcessControl
from .report_store import ReportStore
from .runtime import (
    adjusted_parallel_limit,
    automatic_parallel_ceiling,
    concise_ffmpeg_error,
    process_flags,
    psutil,
    sample_cpu_percent,
)


REPORT_FIELDS = [
    "source",
    "destination",
    "opération",
    "statut",
    "lufs_avant",
    "dbtp_avant",
    "gain_db",
    "lufs_apres",
    "dbtp_apres",
    "controle_qualite",
    "moteur_qc",
    "temps_secondes",
    "détail",
]

REPORT_HEADER_KEYS = {
    "source": "report_source",
    "destination": "report_destination",
    "opération": "report_operation",
    "statut": "report_status",
    "lufs_avant": "report_input_lufs",
    "dbtp_avant": "report_input_dbtp",
    "gain_db": "report_gain",
    "lufs_apres": "report_output_lufs",
    "dbtp_apres": "report_output_dbtp",
    "controle_qualite": "report_qc",
    "moteur_qc": "report_qc_engine",
    "temps_secondes": "report_seconds",
    "détail": "report_detail",
}


def qc_measurement_engine(measurements: dict[str, str] | None) -> str:
    """Return the measurement engine that supplied the reported QC values."""
    if not measurements:
        return ""
    strategy = str(measurements.get("_qc_analysis_strategy") or "")
    analysis_engine = str(measurements.get("_analysis_engine") or "")
    if strategy == "fast_ebur128" or analysis_engine == "ffmpeg_ebur128":
        return "ebur128"
    if strategy in {
        "fallback_loudnorm",
        "locked_loudnorm",
        "reference_loudnorm",
        "reused_input",
    }:
        return "loudnorm"
    # Successful quality measurements without a strategy marker come from
    # the historical loudnorm parser. This also covers copied inputs whose
    # initial loudnorm measurement is reused for QC.
    return "loudnorm"


def qc_measurement_value(measurements: dict[str, str] | None, key: str) -> str:
    """Format QC values without inventing precision absent from ebur128."""
    if not measurements or not measurements_are_finite(measurements):
        return ""
    places = 1 if qc_measurement_engine(measurements) == "ebur128" else 2
    return f"{float(measurements[key]):.{places}f}"


class ConversionWorker(QObject):
    scan_finished = Signal(int)
    estimate_calibration_started = Signal(int, int, int)
    progress = Signal(int, int, str)
    loudness_comparison = Signal(str, float, float, float, float)
    loudness_analysis = Signal(str, float, float)
    log = Signal(str)
    log_entry = Signal(str, str)
    issue_entry = Signal(str, str, str)
    finished = Signal(int, int, int, int, int, bool, float, str)

    def __init__(
        self,
        ffmpeg: str,
        inputs: list[Path],
        output: Path,
        settings: LoudnessSettings,
        overwrite: bool,
        operation: str,
        max_parallel: int,
        resume_enabled: bool,
        quality_control: bool,
        generate_report: bool = True,
        language: str = "fr",
        skip_compliant: bool = True,
        analysis_method: str = "historical",
    ) -> None:
        super().__init__()
        self.ffmpeg = ffmpeg
        self.inputs = inputs
        self.output = output
        self.settings = settings
        self.overwrite = overwrite
        self.operation = (
            operation
            if operation in {"convert", "replaygain", "analyze"}
            else "convert"
        )
        self.auto_parallel = max_parallel <= 0
        self.max_parallel = (
            automatic_parallel_ceiling() if self.auto_parallel else max(1, max_parallel)
        )
        self.resume_enabled = resume_enabled
        self.quality_control = quality_control
        self.generate_report = generate_report
        self.skip_compliant = bool(skip_compliant)
        self.analysis_method = normalized_analysis_method(analysis_method)
        self.language = language if language in SUPPORTED_LANGUAGES else "fr"
        self._process_control = ProcessControl(lambda: self.t("processing_cancelled"))
        # Alias conservés pour les intégrations historiques et le pipeline.
        self._cancel_event = self._process_control.cancel_event
        self._pause_event = self._process_control.pause_event
        self._pause_condition = self._process_control.pause_condition
        self._process_lock = self._process_control.process_lock
        self._current_processes = self._process_control.current_processes
        self._manifest: ResumeManifest | None = None
        self._analysis_cache: AnalysisCache | None = None
        self._metrics_lock = threading.Lock()
        self._analysis_cache_hits = 0
        self._fast_analysis_count = 0
        self._full_analysis_count = 0
        self._fast_probe_seconds = 0.0
        self._full_fallback_seconds = 0.0
        self._historical_analysis_count = 0
        self._historical_analysis_seconds = 0.0
        self._adaptive = AdaptiveAnalysisController()
        self._adaptive_disable_logged = False
        self._hybrid = FastQCController()

    def t(self, key: str, **values: Any) -> str:
        return translate(self.language, key, **values)

    def _active_elapsed_since(self, started_at: float) -> float:
        return self._process_control.active_elapsed_since(started_at)

    @staticmethod
    def _set_process_paused(process: subprocess.Popen[str], paused: bool) -> None:
        ProcessControl.set_process_paused(process, paused)

    def _wait_if_paused(self) -> None:
        self._process_control.wait_if_paused()

    def _analysis_configuration(self) -> dict[str, Any]:
        return {
            # Fast linear measurements must never be mistaken for historical
            # dynamic-pass cache entries shared by older application builds.
            "schema": 6,
            # The guarded QC build keeps the exact historical loudnorm input
            # analysis and may therefore reuse its compatible cache.
            "analysis_method": (
                "historical"
                if self.analysis_method == "hybrid"
                else self.analysis_method
            ),
            "integrated_lufs": self.settings.integrated_lufs,
            "loudness_range": self.settings.loudness_range,
            "true_peak": self.settings.true_peak,
        }

    def _cached_measurements(self, sources: list[Path]) -> dict[str, str] | None:
        if self._analysis_cache is None:
            return None
        result = self._analysis_cache.measurements(
            sources, self._analysis_configuration()
        )
        if result is not None:
            result["_cached_analysis_strategy"] = str(
                result.get("_analysis_strategy") or ""
            )
            result["_analysis_strategy"] = "cache"
            result["_fast_probe_seconds"] = "0"
            result["_full_fallback_seconds"] = "0"
            with self._metrics_lock:
                self._analysis_cache_hits += 1
        return result

    def _store_measurements(
        self, sources: list[Path], measurements: dict[str, str]
    ) -> None:
        if self._analysis_cache is None:
            return
        try:
            self._analysis_cache.store(
                sources,
                self._analysis_configuration(),
                measurements,
            )
        except OSError:
            pass

    def _pool_results(
        self,
        items: list[Any],
        task,
        thread_name_prefix: str,
    ):
        if not items:
            return
        with ThreadPoolExecutor(
            max_workers=self.max_parallel,
            thread_name_prefix=thread_name_prefix,
        ) as executor:
            pending = iter(items)
            current_limit = (
                self.max_parallel
                if not self.auto_parallel or psutil is None
                else min(4, self.max_parallel)
            )
            active: dict[Any, Any] = {}

            if self.auto_parallel and psutil is not None:
                sample_cpu_percent()

            def fill_slots() -> None:
                while len(active) < current_limit and not self._cancel_event.is_set():
                    try:
                        item = next(pending)
                    except StopIteration:
                        return
                    active[executor.submit(task, item)] = item

            fill_slots()
            while active:
                completed_futures, _ = wait(
                    set(active),
                    timeout=1.0,
                    return_when=FIRST_COMPLETED,
                )
                if self.auto_parallel and psutil is not None:
                    cpu = sample_cpu_percent()
                    if cpu is not None:
                        adjusted = adjusted_parallel_limit(
                            current_limit,
                            self.max_parallel,
                            cpu,
                        )
                        if adjusted != current_limit:
                            current_limit = adjusted
                            self.log.emit(
                                self.t(
                                    "parallel_adjusted",
                                    active=current_limit,
                                    cpu=cpu,
                                )
                            )

                for future in completed_futures:
                    item = active.pop(future)
                    yield future, item
                if self._pause_event.is_set():
                    try:
                        self._wait_if_paused()
                    except InterruptedError:
                        # Pause -> Cancel is a normal end condition for the
                        # pool coordinator.  Letting this exception escape
                        # from the generator bypasses ``run()``'s normal
                        # finalization, so ``finished`` is never emitted and
                        # the Qt thread keeps the interface locked forever.
                        # Running tasks have already received cancellation
                        # through ProcessControl; queued tasks are cancelled
                        # here before the executor is closed.
                        for future in active:
                            future.cancel()
                        return
                fill_slots()

    def _set_status(self, report: dict[str, Any], code: str) -> None:
        report["_status_code"] = code
        report["statut"] = self.t(f"status_{code}")

    def request_cancel(self) -> None:
        self._process_control.request_cancel()

    def request_pause(self) -> bool:
        return self._process_control.request_pause()

    def request_resume(self) -> bool:
        return self._process_control.request_resume()

    def _run_process(
        self, command: list[str], *, capture_stdout: bool = False
    ) -> tuple[int, str, str]:
        self._wait_if_paused()

        # ``command`` is an argument list produced by the audio command
        # builders; no shell is involved and file paths remain single values.
        process = subprocess.Popen(  # noqa: S603
            command,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE if capture_stdout else subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            creationflags=process_flags(),
        )
        registered_while_active = self._process_control.register_process(process)
        try:
            stdout, stderr = process.communicate()
            if not registered_while_active or self._cancel_event.is_set():
                raise InterruptedError(self.t("processing_cancelled"))
            return process.returncode, stdout or "", stderr
        finally:
            self._process_control.unregister_process(process)

    def _temporary_path(self, job: ConversionJob) -> Path:
        return job.destination.with_name(
            f".{job.destination.stem}.{uuid.uuid4().hex}.tmp"
            f"{job.destination.suffix.lower()}"
        )

    @staticmethod
    def _dynamic_mp3_output_score(
        settings: LoudnessSettings,
        measurements: dict[str, str],
    ) -> tuple[float, float, float, float, float]:
        """Rank candidates while treating the true-peak ceiling as absolute."""
        if not measurements_are_finite(measurements):
            return (1.0, 1.0, math.inf, math.inf, math.inf)
        try:
            loudness = float(measurements["input_i"])
            true_peak = float(measurements["input_tp"])
        except (KeyError, TypeError, ValueError):
            return (1.0, 1.0, math.inf, math.inf, math.inf)
        loudness_error = abs(loudness - settings.integrated_lufs)
        peak_excess = max(0.0, true_peak - settings.true_peak)
        loudness_excess = max(
            0.0,
            loudness_error - STRICT_TARGET_LUFS_TOLERANCE,
        )
        return (
            float(peak_excess > 0.0),
            float(loudness_excess > 0.0),
            peak_excess,
            loudness_excess,
            loudness_error,
        )

    def _retry_dynamic_mp3_output(
        self,
        job: ConversionJob,
        temporary: Path,
        input_measurements: dict[str, str],
        initial_output_measurements: dict[str, str],
        initial_internal_target: float,
        applied_gain_db: float | None,
        report: dict[str, Any],
    ) -> dict[str, str]:
        """Retry only non-compliant dynamic MP3 outputs with measured feedback."""
        best_output = initial_output_measurements
        best_target = float(initial_internal_target)
        best_score = self._dynamic_mp3_output_score(self.settings, best_output)
        feedback_output = initial_output_measurements
        feedback_target = float(initial_internal_target)
        seen_targets = {round(feedback_target, 6)}
        attempted_targets: list[str] = []
        selected_attempt = 0
        retry_error = ""
        retry_started = time.perf_counter()

        report["_dynamic_mp3_initial_internal_true_peak_dbtp"] = (
            f"{initial_internal_target:.9f}"
        )
        report["_dynamic_mp3_initial_output_lufs"] = measurement_value(
            initial_output_measurements, "input_i"
        )
        report["_dynamic_mp3_initial_output_dbtp"] = measurement_value(
            initial_output_measurements, "input_tp"
        )

        try:
            for attempt in range(1, MP3_DYNAMIC_RETRY_MAX_ATTEMPTS + 1):
                if dynamic_mp3_output_is_strictly_compliant(
                    self.settings, feedback_output
                ):
                    break
                next_target = next_dynamic_mp3_true_peak_target(
                    self.settings,
                    feedback_output,
                    feedback_target,
                )
                if next_target is None:
                    break
                target_key = round(next_target, 6)
                if target_key in seen_targets:
                    break
                seen_targets.add(target_key)
                attempted_targets.append(f"{next_target:.9f}")

                retry_output = self._temporary_path(job)
                retry_settings = replace(
                    self.settings,
                    true_peak=next_target,
                )
                try:
                    conversion = conversion_command(
                        self.ffmpeg,
                        job.source,
                        retry_output,
                        retry_settings,
                        input_measurements,
                    )
                    return_code, _, stderr = self._run_process(conversion)
                    if return_code != 0:
                        raise RuntimeError(concise_ffmpeg_error(stderr, self.language))

                    retry_output_measurements = self._analyze_path_for_quality(
                        job,
                        retry_output,
                        input_measurements,
                        attempt_index=attempt,
                        attempt_kind="retry",
                        internal_true_peak_target=next_target,
                        applied_gain_db=applied_gain_db,
                        preserve_audio=False,
                        copied_compliant=False,
                        force_reference=bool(report.get("_fast_qc_reference_locked")),
                        report=report,
                    )
                    retry_score = self._dynamic_mp3_output_score(
                        self.settings, retry_output_measurements
                    )
                    if retry_score < best_score:
                        os.replace(retry_output, temporary)
                        best_output = retry_output_measurements
                        best_target = next_target
                        best_score = retry_score
                        selected_attempt = attempt

                    feedback_output = retry_output_measurements
                    feedback_target = next_target
                except InterruptedError:
                    raise
                except Exception as exc:
                    retry_error = str(exc)
                    break
                finally:
                    try:
                        retry_output.unlink(missing_ok=True)
                    except OSError:
                        pass
        finally:
            report["_dynamic_mp3_retry_seconds"] = time.perf_counter() - retry_started

        applied_margin = max(0.0, self.settings.true_peak - best_target)
        report["_internal_true_peak_dbtp"] = f"{best_target:.9f}"
        report["_dynamic_mp3_peak_margin_db"] = f"{applied_margin:.9f}"
        report["_dynamic_mp3_peak_margin_applied"] = bool(applied_margin > 0.0)
        report["_dynamic_mp3_retry_count"] = len(attempted_targets)
        report["_dynamic_mp3_retry_targets_dbtp"] = attempted_targets
        report["_dynamic_mp3_retry_selected_attempt"] = selected_attempt
        report["_dynamic_mp3_retry_used"] = bool(selected_attempt)
        report["_dynamic_mp3_strict_compliance"] = (
            dynamic_mp3_output_is_strictly_compliant(self.settings, best_output)
        )
        report["_dynamic_mp3_retry_error"] = retry_error
        report["_hybrid_qc_selected_attempt"] = selected_attempt
        self._hybrid.mark_selected_attempt(self._relative_label(job), selected_attempt)
        return best_output

    def _retry_lossless_output_toward_target(
        self,
        job: ConversionJob,
        temporary: Path,
        input_measurements: dict[str, str],
        initial_output_measurements: dict[str, str],
        report: dict[str, Any],
    ) -> dict[str, str]:
        """Use measured peak headroom for a lossless, source-based retry."""
        best_output = initial_output_measurements
        best_score = self._dynamic_mp3_output_score(self.settings, best_output)
        feedback_output = initial_output_measurements
        current_post_gain = 0.0
        attempted_gains: list[str] = []
        selected_attempt = 0
        retry_error = ""
        retry_started = time.perf_counter()

        try:
            for attempt in range(1, TARGET_CORRECTION_MAX_ATTEMPTS + 1):
                next_gain = next_safe_target_correction_gain(
                    self.settings,
                    feedback_output,
                    current_post_gain,
                )
                if next_gain is None:
                    break
                attempted_gains.append(f"{next_gain:.6f}")
                retry_output = self._temporary_path(job)
                try:
                    conversion = conversion_command(
                        self.ffmpeg,
                        job.source,
                        retry_output,
                        self.settings,
                        input_measurements,
                        post_gain_db=next_gain,
                    )
                    return_code, _, stderr = self._run_process(conversion)
                    if return_code != 0:
                        raise RuntimeError(concise_ffmpeg_error(stderr, self.language))
                    retry_measurements = self._analyze_path_for_quality(
                        job,
                        retry_output,
                        input_measurements,
                        attempt_index=attempt,
                        attempt_kind="lossless_target_correction",
                        internal_true_peak_target=self.settings.true_peak,
                        applied_gain_db=None,
                        preserve_audio=False,
                        copied_compliant=False,
                        force_reference=True,
                        report=report,
                    )
                    retry_score = self._dynamic_mp3_output_score(
                        self.settings, retry_measurements
                    )
                    if retry_score < best_score:
                        os.replace(retry_output, temporary)
                        best_output = retry_measurements
                        best_score = retry_score
                        selected_attempt = attempt
                    feedback_output = retry_measurements
                    current_post_gain = next_gain
                except InterruptedError:
                    raise
                except Exception as exc:
                    retry_error = str(exc)
                    break
                finally:
                    try:
                        retry_output.unlink(missing_ok=True)
                    except OSError:
                        pass
        finally:
            report["_lossless_target_correction_seconds"] = (
                time.perf_counter() - retry_started
            )

        report["_lossless_target_correction_attempts"] = len(attempted_gains)
        report["_lossless_target_correction_gains_db"] = attempted_gains
        report["_lossless_target_correction_selected_attempt"] = selected_attempt
        report["_lossless_target_correction_used"] = bool(selected_attempt)
        report["_lossless_target_correction_error"] = retry_error
        return best_output

    def _configuration(self) -> dict[str, Any]:
        return {
            "application_version": APP_VERSION,
            "operation": self.operation,
            "integrated_lufs": self.settings.integrated_lufs,
            "loudness_range": self.settings.loudness_range,
            "true_peak": self.settings.true_peak,
            "quality": self.settings.quality,
            "quality_control": self.quality_control,
            "skip_compliant": self.skip_compliant,
            "analysis_method": self.analysis_method,
        }

    def _relative_label(self, job: ConversionJob) -> str:
        return str(job.destination.relative_to(self.output))

    def _measure_command(self, command: list[str]) -> dict[str, str]:
        return_code, _, stderr = self._run_process(command)
        if self._cancel_event.is_set():
            raise InterruptedError(self.t("processing_cancelled"))
        if return_code != 0:
            raise RuntimeError(concise_ffmpeg_error(stderr, self.language))
        return parse_loudnorm_measurements(stderr, self.language)

    def _measure_ebur128_command(self, command: list[str]) -> dict[str, str]:
        return_code, _, stderr = self._run_process(command)
        if self._cancel_event.is_set():
            raise InterruptedError(self.t("processing_cancelled"))
        if return_code != 0:
            raise RuntimeError(concise_ffmpeg_error(stderr, self.language))
        return parse_ebur128_measurements(stderr, self.language)

    def _analyze_with_safe_fallback(
        self,
        fast_command: list[str],
        full_command: list[str],
        *,
        adaptive: bool = False,
    ) -> dict[str, str]:
        fast_started = time.perf_counter()
        fast_measurements: dict[str, str] | None = None
        try:
            fast_measurements = self._measure_command(fast_command)
        except InterruptedError:
            raise
        except Exception:
            # A bundled FFmpeg that rejects the optimized graph remains fully
            # supported through the historical command below.
            fast_measurements = None
        fast_elapsed = time.perf_counter() - fast_started

        diagnostics = (
            loudnorm_linear_mode_diagnostics(self.settings, fast_measurements)
            if fast_measurements is not None
            else {
                "eligible": False,
                "reason": "probe_error",
                "gain_db": None,
                "predicted_true_peak_dbtp": None,
                "true_peak_margin_db": None,
                "lra_margin_lu": None,
                "safety_margin_db": LOUDNORM_LINEAR_SAFETY_MARGIN_DB,
            }
        )

        if fast_measurements is not None and bool(diagnostics["eligible"]):
            # The probe's reported offset describes its deliberately
            # unmodified output, not a historical dynamic first pass.  FFmpeg
            # ignores this value in the verified linear path; zero is the
            # safest value if a future build changes that behavior.
            fast_measurements["target_offset"] = "0.00"
            fast_measurements["_analysis_strategy"] = (
                "adaptive_fast_linear" if adaptive else "fast_linear"
            )
            fast_measurements["_fast_probe_seconds"] = f"{fast_elapsed:.9f}"
            fast_measurements["_full_fallback_seconds"] = "0"
            fast_measurements["_historical_analysis_seconds"] = "0"
            self._copy_linear_diagnostics(
                fast_measurements,
                diagnostics,
                fallback_reason="",
            )
            with self._metrics_lock:
                self._fast_analysis_count += 1
                self._fast_probe_seconds += fast_elapsed
            if adaptive:
                self._observe_adaptive(
                    fast_success=True,
                    probe_seconds=fast_elapsed,
                )
            return fast_measurements

        full_started = time.perf_counter()
        measurements = self._measure_command(full_command)
        full_elapsed = time.perf_counter() - full_started
        measurements["_analysis_strategy"] = (
            "adaptive_full_fallback" if adaptive else "full_fallback"
        )
        measurements["_fast_probe_seconds"] = f"{fast_elapsed:.9f}"
        measurements["_full_fallback_seconds"] = f"{full_elapsed:.9f}"
        measurements["_historical_analysis_seconds"] = "0"
        self._copy_linear_diagnostics(
            measurements,
            diagnostics,
            fallback_reason=str(diagnostics["reason"]),
        )
        with self._metrics_lock:
            self._full_analysis_count += 1
            self._fast_probe_seconds += fast_elapsed
            self._full_fallback_seconds += full_elapsed
        if adaptive:
            self._observe_adaptive(
                fast_success=False,
                probe_seconds=fast_elapsed,
                full_seconds=full_elapsed,
            )
        return measurements

    @staticmethod
    def _copy_linear_diagnostics(
        measurements: dict[str, str],
        diagnostics: dict[str, Any],
        *,
        fallback_reason: str,
    ) -> None:
        measurements["_fast_fallback_reason"] = fallback_reason
        measurements["_linear_eligibility_reason"] = str(
            diagnostics.get("reason") or ""
        )
        for name in (
            "gain_db",
            "predicted_true_peak_dbtp",
            "true_peak_margin_db",
            "lra_margin_lu",
            "safety_margin_db",
        ):
            value = diagnostics.get(name)
            measurements[f"_linear_{name}"] = (
                "" if value is None else f"{float(value):.9f}"
            )

    def _observe_adaptive(
        self,
        *,
        fast_success: bool,
        probe_seconds: float,
        full_seconds: float = 0.0,
    ) -> None:
        snapshot = self._adaptive.observe(
            fast_success=fast_success,
            probe_seconds=probe_seconds,
            full_seconds=full_seconds,
        )
        should_log = False
        if snapshot.decision == "disabled_unprofitable":
            with self._metrics_lock:
                if not self._adaptive_disable_logged:
                    self._adaptive_disable_logged = True
                    should_log = True
        if should_log:
            self.log.emit(
                self.t(
                    "adaptive_disabled_log",
                    sample=snapshot.sample_size,
                    successes=snapshot.fast_successes,
                    percent=(snapshot.estimated_savings_ratio or 0.0) * 100.0,
                )
            )

    def _analyze_historical_command(
        self,
        command: list[str],
        *,
        strategy: str = "historical",
        fallback_reason: str = "",
    ) -> dict[str, str]:
        started = time.perf_counter()
        measurements = self._measure_command(command)
        elapsed = time.perf_counter() - started
        diagnostics = loudnorm_linear_mode_diagnostics(self.settings, measurements)
        measurements["_analysis_strategy"] = strategy
        measurements["_fast_probe_seconds"] = "0"
        measurements["_full_fallback_seconds"] = "0"
        measurements["_historical_analysis_seconds"] = f"{elapsed:.9f}"
        self._copy_linear_diagnostics(
            measurements,
            diagnostics,
            fallback_reason=fallback_reason,
        )
        with self._metrics_lock:
            self._historical_analysis_count += 1
            self._historical_analysis_seconds += elapsed
        return measurements

    def _analyze_commands(
        self,
        fast_command: list[str],
        full_command: list[str],
        *,
        hybrid_command: list[str] | None = None,
        label: str = "",
    ) -> dict[str, str]:
        if self.analysis_method == "historical":
            return self._analyze_historical_command(full_command)
        if self.analysis_method == "hybrid":
            # The guarded experiment changes only MP3 output QC.  Input
            # measurements remain on the stable loudnorm command.
            return self._analyze_historical_command(
                full_command,
                strategy="hybrid_qc_fast_historical_input",
            )
        if self.analysis_method == "adaptive":
            if not self._adaptive.should_probe():
                return self._analyze_historical_command(
                    full_command,
                    strategy="adaptive_historical",
                    fallback_reason="adaptive_disabled_unprofitable",
                )
            return self._analyze_with_safe_fallback(
                fast_command,
                full_command,
                adaptive=True,
            )
        return self._analyze_with_safe_fallback(fast_command, full_command)

    def _analyze_path(self, source: Path) -> dict[str, str]:
        return self._analyze_commands(
            fast_analysis_command(self.ffmpeg, source, self.settings),
            analysis_command(self.ffmpeg, source, self.settings),
        )

    def _analyze_path_full(self, source: Path) -> dict[str, str]:
        """Run the historical full measurement used for final quality control."""
        return self._measure_command(
            analysis_command(self.ffmpeg, source, self.settings)
        )

    def _analyze_path_for_quality(
        self,
        job: ConversionJob,
        source: Path,
        input_measurements: dict[str, str],
        *,
        attempt_index: int,
        attempt_kind: str,
        internal_true_peak_target: float | None,
        applied_gain_db: float | None,
        preserve_audio: bool,
        copied_compliant: bool,
        force_reference: bool,
        report: dict[str, Any],
    ) -> dict[str, str]:
        """Measure one QC attempt with a guarded, permanent fallback.

        The fast engine can only certify a result that lies inside the strict
        inner pass region.  It never authorizes a retry or a warning.  Once a
        file reaches loudnorm, all later retries bypass ebur128.
        """
        label = self._relative_label(job)
        permanent_before = bool(force_reference)
        dynamic_mp3_path = bool(report["_dynamic_mp3_path"])

        def quality_and_retry(
            measurements: dict[str, str],
        ) -> tuple[bool, bool | None]:
            quality = assess_quality(
                self.settings,
                input_measurements,
                measurements,
                applied_gain_db=applied_gain_db,
                preserve_audio=preserve_audio or copied_compliant,
                language=self.language,
            )
            retry_required = (
                not dynamic_mp3_output_is_strictly_compliant(
                    self.settings, measurements
                )
                if dynamic_mp3_path
                else None
            )
            return quality.passed, retry_required

        def reference_measurement(strategy: str) -> dict[str, str]:
            reference_started = time.perf_counter()
            measurements = self._analyze_path_full(source)
            reference_elapsed = time.perf_counter() - reference_started
            measurements["_qc_fast_seconds"] = "0"
            measurements["_qc_reference_seconds"] = f"{reference_elapsed:.9f}"
            measurements["_qc_analysis_strategy"] = strategy
            return measurements

        if self.analysis_method != "hybrid" or source.suffix.lower() != ".mp3":
            return reference_measurement("reference_loudnorm")

        report["_fast_qc_attempts"] = int(report.get("_fast_qc_attempts") or 0) + 1
        if copied_compliant:
            measurements = dict(input_measurements)
            measurements["_qc_fast_seconds"] = "0"
            measurements["_qc_reference_seconds"] = "0"
            measurements["_qc_analysis_strategy"] = "reused_input"
            quality_passed, retry_required = quality_and_retry(measurements)
            self._hybrid.record(
                label=label,
                attempt_index=attempt_index,
                attempt_kind=attempt_kind,
                strategy="reused_input",
                permanent_reference_before=False,
                permanent_reference_after=False,
                fast=None,
                reference=None,
                fast_seconds=0.0,
                reference_seconds=0.0,
                candidate_eligible=False,
                fallback_reason="byte_copy_reuses_input_measurement",
                quality_passed=quality_passed,
                retry_required=retry_required,
            )
            report["_fast_qc_last_strategy"] = "reused_input"
            return measurements

        if permanent_before:
            measurements = reference_measurement("locked_loudnorm")
            quality_passed, retry_required = quality_and_retry(measurements)
            self._hybrid.record(
                label=label,
                attempt_index=attempt_index,
                attempt_kind=attempt_kind,
                strategy="locked_loudnorm",
                permanent_reference_before=True,
                permanent_reference_after=True,
                fast=None,
                reference=measurements,
                fast_seconds=0.0,
                reference_seconds=float(measurements["_qc_reference_seconds"]),
                candidate_eligible=False,
                fallback_reason="permanent_file_fallback",
                quality_passed=quality_passed,
                retry_required=retry_required,
            )
            report["_fast_qc_locked_reference_uses"] = (
                int(report.get("_fast_qc_locked_reference_uses") or 0) + 1
            )
            report["_fast_qc_last_strategy"] = "locked_loudnorm"
            return measurements

        fast_measurements: dict[str, str] | None = None
        fast_error = ""
        fast_started = time.perf_counter()
        try:
            fast_measurements = self._measure_ebur128_command(
                ebur128_analysis_command(self.ffmpeg, source)
            )
        except InterruptedError:
            raise
        except Exception as exc:
            fast_error = str(exc) or "ebur128_error"
        fast_elapsed = time.perf_counter() - fast_started

        expected_lufs = (
            float(input_measurements["input_i"])
            if preserve_audio
            else (
                float(self.settings.integrated_lufs)
                if applied_gain_db is None
                else float(input_measurements["input_i"]) + float(applied_gain_db)
            )
        )
        candidate = (
            qc_fast_candidate_diagnostics(
                fast_measurements,
                input_measurements,
                expected_lufs=expected_lufs,
                true_peak_limit=self.settings.true_peak,
                preserve_audio=preserve_audio,
                dynamic_mp3_path=dynamic_mp3_path,
                copied_compliant=False,
            )
            if fast_measurements is not None
            else {"eligible": False, "reason": "ebur128_error"}
        )
        if fast_measurements is not None and bool(candidate["eligible"]):
            fast_measurements["_qc_fast_seconds"] = f"{fast_elapsed:.9f}"
            fast_measurements["_qc_reference_seconds"] = "0"
            fast_measurements["_qc_analysis_strategy"] = "fast_ebur128"
            quality_passed, retry_required = quality_and_retry(fast_measurements)
            self._hybrid.record(
                label=label,
                attempt_index=attempt_index,
                attempt_kind=attempt_kind,
                strategy="fast_ebur128",
                permanent_reference_before=False,
                permanent_reference_after=False,
                fast=fast_measurements,
                reference=None,
                fast_seconds=fast_elapsed,
                reference_seconds=0.0,
                candidate_eligible=True,
                fallback_reason="",
                quality_passed=quality_passed,
                retry_required=retry_required,
            )
            report["_fast_qc_uses"] = int(report.get("_fast_qc_uses") or 0) + 1
            report["_fast_qc_last_strategy"] = "fast_ebur128"
            return fast_measurements

        measurements = reference_measurement("fallback_loudnorm")
        quality_passed, retry_required = quality_and_retry(measurements)
        fallback_reason = str(candidate.get("reason") or "guard_rejected")
        self._hybrid.record(
            label=label,
            attempt_index=attempt_index,
            attempt_kind=attempt_kind,
            strategy="fallback_loudnorm",
            permanent_reference_before=False,
            permanent_reference_after=True,
            fast=fast_measurements,
            reference=measurements,
            fast_seconds=fast_elapsed,
            reference_seconds=float(measurements["_qc_reference_seconds"]),
            candidate_eligible=False,
            fallback_reason=fallback_reason,
            quality_passed=quality_passed,
            retry_required=retry_required,
            error=fast_error,
        )
        report["_fast_qc_reference_locked"] = True
        report["_fast_qc_initial_fallbacks"] = (
            int(report.get("_fast_qc_initial_fallbacks") or 0) + 1
        )
        report["_fast_qc_fallback_reason"] = fallback_reason
        report["_fast_qc_error"] = fast_error
        report["_fast_qc_last_strategy"] = "fallback_loudnorm"
        return measurements

    def _analyze_job(
        self, job: ConversionJob
    ) -> tuple[ConversionJob, dict[str, str] | None, str, float]:
        started = time.perf_counter()
        try:
            # Analyze-only is an explicit measurement request.  Always invoke
            # FFmpeg so a previous Normalize/ReplayGain run cannot silently
            # repopulate the graph from the persistent cache.
            measurements = (
                None
                if self.operation == "analyze"
                else self._cached_measurements([job.source])
            )
            if measurements is None:
                measurements = self._analyze_path(job.source)
                self._store_measurements([job.source], measurements)
            return job, measurements, "", time.perf_counter() - started
        except InterruptedError:
            return (
                job,
                None,
                self.t("status_cancelled"),
                time.perf_counter() - started,
            )
        except Exception as exc:
            return job, None, str(exc), time.perf_counter() - started

    def _report_base(self, job: ConversionJob) -> dict[str, Any]:
        operation_labels = {
            "convert": self.t("operation_convert_label"),
            "replaygain": self.t("operation_replaygain_label"),
            "analyze": self.t("operation_analyze_label"),
        }
        return {
            "source": str(job.source),
            "destination": (
                "" if self.operation == "analyze" else str(job.destination)
            ),
            "opération": operation_labels[self.operation],
            "statut": "",
            "_status_code": "",
            "_qc_warning": False,
            "_qc_status_code": "",
            "_qc_detail": "",
            "_copied_compliant": False,
            "_analysis_seconds": 0.0,
            "_analysis_strategy": "",
            "_fast_probe_seconds": 0.0,
            "_full_fallback_seconds": 0.0,
            "_historical_analysis_seconds": 0.0,
            "_fast_fallback_reason": "",
            "_linear_eligibility_reason": "",
            "_input_lra": "",
            "_input_thresh": "",
            "_target_offset": "",
            "_linear_gain_db": "",
            "_linear_predicted_true_peak_dbtp": "",
            "_linear_true_peak_margin_db": "",
            "_linear_lra_margin_lu": "",
            "_linear_safety_margin_db": "",
            "_source_duration_seconds": 0.0,
            "_conversion_seconds": 0.0,
            "_quality_seconds": 0.0,
            "_qc_analysis_strategy": "",
            "_fast_qc_attempts": 0,
            "_fast_qc_uses": 0,
            "_fast_qc_initial_fallbacks": 0,
            "_fast_qc_locked_reference_uses": 0,
            "_fast_qc_reference_locked": False,
            "_fast_qc_fallback_reason": "",
            "_fast_qc_error": "",
            "_fast_qc_last_strategy": "",
            "_hybrid_qc_selected_attempt": 0,
            "_dynamic_mp3_path": False,
            "_dynamic_mp3_peak_margin_applied": False,
            "_requested_true_peak_dbtp": f"{self.settings.true_peak:.9f}",
            "_internal_true_peak_dbtp": f"{self.settings.true_peak:.9f}",
            "_dynamic_mp3_peak_margin_db": "0.000000000",
            "_dynamic_mp3_initial_internal_true_peak_dbtp": "",
            "_dynamic_mp3_initial_output_lufs": "",
            "_dynamic_mp3_initial_output_dbtp": "",
            "_dynamic_mp3_retry_count": 0,
            "_dynamic_mp3_retry_targets_dbtp": [],
            "_dynamic_mp3_retry_selected_attempt": 0,
            "_dynamic_mp3_retry_used": False,
            "_dynamic_mp3_retry_seconds": 0.0,
            "_dynamic_mp3_strict_compliance": None,
            "_dynamic_mp3_retry_error": "",
            "_lossless_target_correction_attempts": 0,
            "_lossless_target_correction_gains_db": [],
            "_lossless_target_correction_selected_attempt": 0,
            "_lossless_target_correction_used": False,
            "_lossless_target_correction_seconds": 0.0,
            "_lossless_target_correction_error": "",
            "lufs_avant": "",
            "dbtp_avant": "",
            "gain_db": "",
            "lufs_apres": "",
            "dbtp_apres": "",
            "controle_qualite": "",
            "moteur_qc": "",
            "temps_secondes": "0.00",
            "détail": "",
        }

    @staticmethod
    def _copy_analysis_diagnostics(
        report: dict[str, Any],
        measurements: dict[str, str],
    ) -> None:
        report["_analysis_strategy"] = str(measurements.get("_analysis_strategy") or "")
        report["_fast_probe_seconds"] = float(
            measurements.get("_fast_probe_seconds") or 0.0
        )
        report["_full_fallback_seconds"] = float(
            measurements.get("_full_fallback_seconds") or 0.0
        )
        report["_historical_analysis_seconds"] = float(
            measurements.get("_historical_analysis_seconds") or 0.0
        )
        report["_fast_fallback_reason"] = str(
            measurements.get("_fast_fallback_reason") or ""
        )
        report["_linear_eligibility_reason"] = str(
            measurements.get("_linear_eligibility_reason") or ""
        )
        report["_input_lra"] = str(measurements.get("input_lra") or "")
        report["_input_thresh"] = str(measurements.get("input_thresh") or "")
        report["_target_offset"] = str(measurements.get("target_offset") or "")
        for name in (
            "gain_db",
            "predicted_true_peak_dbtp",
            "true_peak_margin_db",
            "lra_margin_lu",
            "safety_margin_db",
        ):
            report[f"_linear_{name}"] = str(measurements.get(f"_linear_{name}") or "")
        report["_source_duration_seconds"] = float(
            measurements.get("_input_duration_seconds") or 0.0
        )

    def _error_report(
        self,
        job: ConversionJob,
        detail: str,
        elapsed: float = 0.0,
    ) -> dict[str, Any]:
        report = self._report_base(job)
        self._set_status(report, "error")
        report.update(
            {
                "temps_secondes": f"{elapsed:.2f}",
                "_analysis_seconds": elapsed,
                "détail": detail,
            }
        )
        return report

    def _analysis_report(
        self,
        job: ConversionJob,
        input_measurements: dict[str, str],
        elapsed: float,
    ) -> dict[str, Any]:
        report = self._report_base(job)
        self._copy_analysis_diagnostics(report, input_measurements)
        self._set_status(report, "analyzed")
        report["lufs_avant"] = measurement_value(input_measurements, "input_i")
        report["dbtp_avant"] = measurement_value(input_measurements, "input_tp")
        report["temps_secondes"] = f"{elapsed:.2f}"
        report["_analysis_seconds"] = elapsed
        # Analyze-only has no delivered output and therefore no output QC.
        # The predicted values remain available in the CSV report, but the log
        # must not label the source measurement as a successful quality check.
        report["controle_qualite"] = self.t("not_performed")
        report["_qc_status_code"] = "not_performed"

        if not measurements_are_finite(input_measurements):
            report["détail"] = self.t("silent_unmeasurable")
            return report

        gain_db = calculate_loudness_gain_db(
            self.settings, input_measurements, self.language
        )
        report["gain_db"] = f"{gain_db:.2f}"
        predicted_lufs = self.settings.integrated_lufs
        predicted_peak = min(
            float(input_measurements["input_tp"]) + gain_db,
            self.settings.true_peak,
        )
        report["lufs_apres"] = f"{predicted_lufs:.2f}"
        report["dbtp_apres"] = f"{predicted_peak:.2f}"
        report["détail"] = self.t("estimated_result")
        return report

    def _cleanup_stale_temporaries(self, job: ConversionJob) -> None:
        patterns = (f".{job.destination.stem}.*.tmp{job.destination.suffix.lower()}",)
        for pattern in patterns:
            for temporary in job.destination.parent.glob(pattern):
                try:
                    temporary.unlink()
                except OSError:
                    pass

    def _copy_source_to(self, source: Path, destination: Path) -> None:
        self._wait_if_paused()
        shutil.copy2(source, destination)

    def _process_job(
        self,
        job: ConversionJob,
        input_measurements: dict[str, str],
        analysis_elapsed: float,
        configuration: dict[str, Any],
    ) -> dict[str, Any]:
        started = time.perf_counter()
        report = self._report_base(job)
        self._copy_analysis_diagnostics(report, input_measurements)
        report["_analysis_seconds"] = analysis_elapsed
        report["lufs_avant"] = measurement_value(input_measurements, "input_i")
        report["dbtp_avant"] = measurement_value(input_measurements, "input_tp")
        temporary = self._temporary_path(job)
        applied_gain: float | None = None
        detail = ""

        try:
            self._wait_if_paused()

            job.destination.parent.mkdir(parents=True, exist_ok=True)
            self._cleanup_stale_temporaries(job)
            finite_input = measurements_are_finite(input_measurements)
            copied_compliant = bool(
                self.operation == "convert"
                and self.skip_compliant
                and measurements_are_already_compliant(
                    self.settings,
                    input_measurements,
                )
            )

            if copied_compliant:
                self._copy_source_to(job.source, temporary)
                applied_gain = 0.0
                report["gain_db"] = "0.00"
                report["lufs_apres"] = measurement_value(input_measurements, "input_i")
                report["dbtp_apres"] = measurement_value(input_measurements, "input_tp")
                report["_copied_compliant"] = True
                detail = self.t("already_compliant_copy")
            elif self.operation == "replaygain" and finite_input:
                track_gain = calculate_loudness_gain_db(
                    self.settings, input_measurements, self.language
                )
                report["gain_db"] = f"{track_gain:.2f}"
                return_code, _, stderr = self._run_process(
                    replaygain_command(
                        self.ffmpeg,
                        job.source,
                        temporary,
                        track_gain,
                        float(input_measurements["input_tp"]),
                    )
                )
                if return_code != 0:
                    raise RuntimeError(concise_ffmpeg_error(stderr, self.language))
                write_replaygain_container_tags(
                    temporary,
                    track_gain,
                    float(input_measurements["input_tp"]),
                )
                detail = self.t("audio_copy_replaygain")
            elif self.operation == "replaygain":
                self._copy_source_to(job.source, temporary)
                detail = self.t("silent_copy_no_replaygain")
            elif not finite_input:
                self._copy_source_to(job.source, temporary)
                detail = self.t("silent_copy")
            else:
                report["gain_db"] = (
                    f"{calculate_loudness_gain_db(self.settings, input_measurements, self.language):.2f}"
                )
                conversion_settings = self.settings
                internal_true_peak = dynamic_mp3_true_peak_target(
                    job.destination,
                    self.settings,
                    input_measurements,
                )
                if internal_true_peak is not None:
                    applied_margin = max(
                        0.0,
                        self.settings.true_peak - internal_true_peak,
                    )
                    report["_dynamic_mp3_path"] = True
                    report["_dynamic_mp3_peak_margin_applied"] = bool(
                        applied_margin > 0.0
                    )
                    report["_internal_true_peak_dbtp"] = f"{internal_true_peak:.9f}"
                    report["_dynamic_mp3_peak_margin_db"] = f"{applied_margin:.9f}"
                    conversion_settings = replace(
                        self.settings,
                        true_peak=internal_true_peak,
                    )
                conversion = conversion_command(
                    self.ffmpeg,
                    job.source,
                    temporary,
                    conversion_settings,
                    input_measurements,
                )
                return_code, _, stderr = self._run_process(conversion)
                if return_code != 0:
                    raise RuntimeError(concise_ffmpeg_error(stderr, self.language))
                detail = self.t("track_two_pass")

            self._wait_if_paused()

            report["_conversion_seconds"] = time.perf_counter() - started
            quality_started = time.perf_counter()
            quality_warning = ""
            if self.quality_control:
                try:
                    output_measurements = (
                        input_measurements
                        if (
                            copied_compliant
                            and not (
                                self.analysis_method == "hybrid"
                                and temporary.suffix.lower() == ".mp3"
                            )
                        )
                        else self._analyze_path_for_quality(
                            job,
                            temporary,
                            input_measurements,
                            attempt_index=0,
                            attempt_kind="initial",
                            internal_true_peak_target=(
                                float(report["_internal_true_peak_dbtp"])
                            ),
                            applied_gain_db=applied_gain,
                            preserve_audio=(self.operation == "replaygain"),
                            copied_compliant=copied_compliant,
                            force_reference=False,
                            report=report,
                        )
                    )
                    report["_qc_analysis_strategy"] = str(
                        output_measurements.get("_qc_analysis_strategy") or ""
                    )
                    try:
                        initial_internal_target = float(
                            report["_internal_true_peak_dbtp"]
                        )
                    except (TypeError, ValueError):
                        initial_internal_target = self.settings.true_peak
                    if report["_dynamic_mp3_path"]:
                        output_measurements = self._retry_dynamic_mp3_output(
                            job,
                            temporary,
                            input_measurements,
                            output_measurements,
                            initial_internal_target,
                            applied_gain,
                            report,
                        )
                    elif (
                        self.operation == "convert"
                        and not copied_compliant
                        and temporary.suffix.lower()
                        in LOSSLESS_TARGET_CORRECTION_EXTENSIONS
                    ):
                        output_measurements = self._retry_lossless_output_toward_target(
                            job,
                            temporary,
                            input_measurements,
                            output_measurements,
                            report,
                        )
                        report["_hybrid_qc_selected_attempt"] = 0
                        self._hybrid.mark_selected_attempt(self._relative_label(job), 0)
                    else:
                        report["_hybrid_qc_selected_attempt"] = 0
                        self._hybrid.mark_selected_attempt(self._relative_label(job), 0)
                    report["moteur_qc"] = qc_measurement_engine(output_measurements)
                    report["lufs_apres"] = qc_measurement_value(
                        output_measurements, "input_i"
                    )
                    report["dbtp_apres"] = qc_measurement_value(
                        output_measurements, "input_tp"
                    )
                    quality = assess_quality(
                        self.settings,
                        input_measurements,
                        output_measurements,
                        applied_gain_db=applied_gain,
                        preserve_audio=(
                            self.operation == "replaygain" or copied_compliant
                        ),
                        language=self.language,
                    )
                    if (
                        self.operation == "replaygain"
                        and finite_input
                        and quality.passed
                    ):
                        return_code, metadata, stderr = self._run_process(
                            metadata_dump_command(self.ffmpeg, temporary),
                            capture_stdout=True,
                        )
                        if return_code != 0:
                            quality_warning = concise_ffmpeg_error(
                                stderr, self.language
                            )
                        elif not replaygain_metadata_is_present(metadata):
                            quality_warning = self.t("replaygain_tags_missing")

                    if not quality.passed:
                        quality_warning = (
                            f"{quality_warning} ; {quality.message}"
                            if quality_warning
                            else quality.message
                        )
                    report["_qc_warning"] = bool(quality_warning)
                    report["_qc_status_code"] = "warning" if quality_warning else "ok"
                    report["_qc_detail"] = quality_warning
                    report["controle_qualite"] = (
                        self.t("qc_ok")
                        if not quality_warning
                        else self.t("qc_warning", detail=quality_warning)
                    )
                except InterruptedError:
                    raise
                except Exception as exc:
                    report["_qc_warning"] = True
                    report["_qc_status_code"] = "impossible"
                    report["_qc_detail"] = str(exc)
                    report["controle_qualite"] = self.t("qc_impossible", error=exc)
            else:
                # A disabled QC pass still records the actual delivered
                # loudness for the processing log.  This is deliberately a
                # measurement-only pass: it never assesses compliance,
                # raises a QC warning, updates the meter, or retries an MP3.
                if self.operation != "analyze":
                    try:
                        output_measurements = (
                            input_measurements
                            if copied_compliant or self.operation == "replaygain"
                            else self._analyze_path_full(temporary)
                        )
                        report["lufs_apres"] = measurement_value(
                            output_measurements, "input_i"
                        )
                        report["dbtp_apres"] = measurement_value(
                            output_measurements, "input_tp"
                        )
                    except InterruptedError:
                        raise
                    except Exception as exc:
                        report["_output_measurement_error"] = str(exc)
                report["_qc_status_code"] = "not_performed"
                report["controle_qualite"] = self.t("not_performed")
            post_measurement_seconds = time.perf_counter() - quality_started
            if self.quality_control:
                report["_quality_seconds"] = post_measurement_seconds
            elif self.operation != "analyze":
                # The measurement-only pass belongs to analysis time; the
                # summary must not claim that QC ran when it was disabled.
                report["_analysis_seconds"] = (
                    float(report.get("_analysis_seconds") or 0.0)
                    + post_measurement_seconds
                )
                report["_quality_seconds"] = 0.0

            self._wait_if_paused()
            os.replace(temporary, job.destination)
            self._set_status(report, "ok")
            report["détail"] = detail
            report["temps_secondes"] = (
                f"{analysis_elapsed + time.perf_counter() - started:.2f}"
            )
            if self._manifest is not None:
                try:
                    self._manifest.mark_completed(job, configuration, report)
                except OSError as exc:
                    report["détail"] += self.t("resume_not_saved", error=exc)
            return report

        except InterruptedError:
            if not report["_conversion_seconds"]:
                report["_conversion_seconds"] = time.perf_counter() - started
            self._set_status(report, "cancelled")
            report["détail"] = self.t("interrupted")
            report["temps_secondes"] = (
                f"{analysis_elapsed + time.perf_counter() - started:.2f}"
            )
            return report
        except Exception as exc:
            if not report["_conversion_seconds"]:
                report["_conversion_seconds"] = time.perf_counter() - started
            self._set_status(report, "error")
            report["détail"] = str(exc)
            report["temps_secondes"] = (
                f"{analysis_elapsed + time.perf_counter() - started:.2f}"
            )
            return report
        finally:
            try:
                temporary.unlink(missing_ok=True)
            except OSError:
                pass

    def _emit_loudness_comparison(self, report: dict[str, Any]) -> None:
        """Emit measured before/after data from the worker thread."""
        if not self.quality_control and self.operation != "replaygain":
            return
        values = loudness_comparison_values(
            report,
            self.settings.integrated_lufs,
            self.operation,
        )
        if values is not None:
            self.loudness_comparison.emit(
                str(report.get("source") or ""),
                *values,
            )

    def _emit_source_loudness(
        self,
        measurements: dict[str, str] | None,
        sample_key: str,
    ) -> None:
        """Publish one finite source measurement to the Before history."""
        try:
            before = float((measurements or {}).get("input_i") or "")
        except (TypeError, ValueError):
            return
        if math.isfinite(before):
            self.loudness_analysis.emit(
                str(sample_key),
                before,
                self.settings.integrated_lufs,
            )

    def _emit_replaygain_estimate(
        self,
        measurements: dict[str, str] | None,
        sample_key: str,
    ) -> None:
        """Publish synchronized source and compatible-player estimates.

        ReplayGain's displayed playback loudness is known as soon as the
        source measurement is complete: it is the source loudness plus the
        exact Track gain that will be written.  Waiting for the copied file's
        metadata/QC pass made the lower graph trail the upper graph whenever
        several files were processed concurrently.
        """
        try:
            before = float((measurements or {}).get("input_i") or "")
            gain = calculate_loudness_gain_db(
                self.settings,
                measurements or {},
                self.language,
            )
            target = float(self.settings.integrated_lufs)
            estimated_playback = before + float(gain)
        except (KeyError, TypeError, ValueError):
            return
        if all(
            math.isfinite(value)
            for value in (before, estimated_playback, target)
        ):
            self.loudness_comparison.emit(
                str(sample_key),
                before,
                estimated_playback,
                target,
                target,
            )

    def _analyze_and_process_job(
        self,
        job: ConversionJob,
        configuration: dict[str, Any],
    ) -> dict[str, Any]:
        analyzed_job, measurements, error, analysis_elapsed = self._analyze_job(job)
        if self._cancel_event.is_set():
            report = self._report_base(analyzed_job)
            self._set_status(report, "cancelled")
            report["_analysis_seconds"] = analysis_elapsed
            report["temps_secondes"] = f"{analysis_elapsed:.2f}"
            report["détail"] = self.t("interrupted")
            return report
        if error or measurements is None:
            return self._error_report(
                analyzed_job,
                self.t(
                    "analysis_impossible",
                    error=error or self.t("measurement_unavailable"),
                ),
                analysis_elapsed,
            )
        if self.operation == "replaygain":
            # Both graphs derive from this one source measurement.  Publish
            # them atomically so concurrent metadata/QC work cannot leave the
            # compatible-player graph one or more files behind.
            self._emit_replaygain_estimate(
                measurements,
                str(analyzed_job.source),
            )
        return self._process_job(
            analyzed_job,
            measurements,
            analysis_elapsed,
            configuration,
        )

    def _write_report(self, reports: ReportStore) -> str:
        if not reports:
            return ""
        self.output.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        report_name = f"{self.t('report_filename_prefix')}_{timestamp}.csv"
        path = self.output / report_name
        with path.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(
                [self.t(REPORT_HEADER_KEYS[field]) for field in REPORT_FIELDS]
            )
            for report in reports.sorted_by_source():
                writer.writerow([report.get(field, "") for field in REPORT_FIELDS])
        return str(path)

    def _log_report(self, report: dict[str, Any]) -> None:
        label = Path(str(report["source"])).name
        elapsed = format_duration(
            float(report.get("temps_secondes") or 0), self.language
        )
        status_code = str(report.get("_status_code") or "")
        status = (
            self.t(f"status_{status_code}")
            if status_code
            else str(report.get("statut") or "")
        )
        before = report.get("lufs_avant")
        after = report.get("lufs_apres")
        if (
            before
            and self.operation == "replaygain"
            and not bool(report.get("_copied_compliant"))
        ):
            gain = report.get("gain_db") or "0.00"
            target = f"{self.settings.integrated_lufs:.2f}"
            levels = f" — {self.t('replaygain_levels_log', before=before, gain=gain, target=target)}"
        elif before and after and self.operation != "analyze":
            levels = f" — {before} → {after} LUFS"
        elif not self.quality_control and self.operation != "analyze":
            levels = f" — {self.t('output_lufs_unavailable')}"
        elif before:
            levels = f" — {self.t('input_lufs_log', value=before)}"
        else:
            levels = ""
        qc_status_code = str(report.get("_qc_status_code") or "")
        qc_detail = str(report.get("_qc_detail") or "")
        if status_code in {"skipped", "cancelled", "error"}:
            # No output analysis ran for these terminal states.  In
            # particular, an existing destination is skipped before FFmpeg is
            # started and must never inherit a successful QC badge.
            quality = ""
        elif self.operation == "analyze":
            # A source measurement is complete, but no output exists to pass
            # or fail the quality-control step.
            quality = ""
        elif qc_status_code == "ok":
            if self.operation == "replaygain":
                quality = self.t("replaygain_qc_ok")
            else:
                quality = self.t("qc_ok")
        elif qc_status_code == "warning":
            quality = (
                self.t("qc_warning", detail=qc_detail)
                if qc_detail
                else self.t("status_warning")
            )
        elif qc_status_code == "impossible":
            quality = self.t("qc_impossible", error=qc_detail)
        elif qc_status_code == "not_performed":
            quality = self.t("not_performed")
        elif bool(report.get("_qc_warning")):
            # Old resume records did not store a canonical QC code.  Do not
            # reuse their possibly foreign-language badge.
            quality = self.t("status_warning")
        elif status_code == "ok":
            quality = self.t("qc_ok" if self.quality_control else "not_performed")
        else:
            quality = ""
        quality_text = self.t("qc_log", quality=quality) if quality else ""
        copied_compliant = bool(report.get("_copied_compliant"))
        compliant_text = (
            f" — {self.t('already_compliant_log')}" if copied_compliant else ""
        )
        if copied_compliant:
            category = "warning" if bool(report.get("_qc_warning")) else "compliant"
            line_start = f"{self.t('already_compliant_badge')} — {label}"
        elif status_code in {"ok", "analyzed"}:
            category = "warning" if bool(report.get("_qc_warning")) else "success"
            # Successful file lines no longer repeat a SUCCESS badge.  Their
            # color already carries the outcome, leaving the filename as the
            # useful visual anchor.  Exceptional states keep an explicit
            # badge because it adds information.
            line_start = label
        elif status_code == "resumed":
            category = "resumed"
            line_start = f"{status} — {label}"
        elif status_code == "skipped":
            category = "skipped"
            line_start = f"{status} — {label}"
        elif status_code == "cancelled":
            category = "cancelled"
            line_start = f"{status} — {label}"
        else:
            category = "error"
            line_start = f"{status} — {label}"
        self.log_entry.emit(
            category,
            f"{line_start} — {elapsed}{levels}{quality_text}{compliant_text}",
        )
        detail = str(report.get("détail") or "")
        if category in {"warning", "error"}:
            issue_detail = (
                quality
                if category == "warning" and quality
                else detail or quality or status
            )
            self.issue_entry.emit(
                category,
                str(report.get("source") or ""),
                issue_detail,
            )
        if detail and report.get("_status_code") in {"error", "cancelled"}:
            self.log_entry.emit(category, f"  {detail}")

    @Slot()
    def run(self) -> None:
        """Run one batch and always release the Qt thread on failure.

        Qt does not convert an exception escaping a slot into the worker's
        normal ``finished`` signal.  Without this boundary the coordinator
        keeps the controls locked forever because the QThread remains active.
        """
        started = time.perf_counter()
        try:
            self._run_batch()
        except Exception as exc:
            cancelled = self._cancel_event.is_set()
            detail = self.t("internal_error", error=exc)
            self.log.emit(detail)
            if not cancelled:
                self.issue_entry.emit("error", str(self.output), detail)
            self.finished.emit(
                0,
                0 if cancelled else 1,
                0,
                0,
                0,
                cancelled,
                self._active_elapsed_since(started),
                "",
            )

    def _run_batch(self) -> None:
        run_started = time.perf_counter()
        success = 0
        failed = 0
        skipped = 0
        warnings = 0
        compliant = 0
        report_path = ""

        try:
            self._wait_if_paused()
            self.log.emit(self.t("recursive_scan"))
            jobs = build_jobs(self.inputs, self.output, self.language)
            self._wait_if_paused()
        except InterruptedError:
            self.log.emit(self.t("processing_cancelled"))
            self.finished.emit(
                0,
                0,
                0,
                0,
                0,
                True,
                self._active_elapsed_since(run_started),
                "",
            )
            return
        except Exception as exc:
            self.log.emit(self.t("scan_error", error=exc))
            issue_source = str(self.inputs[0]) if self.inputs else str(self.output)
            self.issue_entry.emit("error", issue_source, str(exc))
            self.finished.emit(
                0, 1, 0, 0, 0, False, self._active_elapsed_since(run_started), ""
            )
            return

        total = len(jobs)
        self.scan_finished.emit(total)
        if not jobs:
            self.log.emit(self.t("no_mp3"))
            self.finished.emit(
                0, 0, 0, 0, 0, False, self._active_elapsed_since(run_started), ""
            )
            return

        try:
            self.output.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            self.log.emit(self.t("destination_error", error=exc))
            self.issue_entry.emit("error", str(self.output), str(exc))
            self.finished.emit(
                0,
                1,
                0,
                0,
                0,
                False,
                self._active_elapsed_since(run_started),
                "",
            )
            return
        reports = ReportStore()
        self._analysis_cache = AnalysisCache(
            self.output / ".normaliseur_mp3_analyses.json"
        )
        configuration = self._configuration()
        if self.resume_enabled and self.operation != "analyze":
            self._manifest = ResumeManifest(
                self.output / ".normaliseur_mp3_reprise.json"
            )

        operation_key = {
            "convert": "convert_operation",
            "replaygain": "replaygain_operation",
            "analyze": "operation_analyze_label",
        }[self.operation]
        parallel_description = (
            self.t(
                "parallel_auto_log",
                maximum=self.max_parallel,
            )
            if self.auto_parallel
            else str(self.max_parallel)
        )
        self.log.emit(
            self.t(
                "files_found",
                total=total,
                operation=self.t(operation_key),
                parallel=parallel_description,
            )
        )
        pending: list[ConversionJob] = []
        completed = 0
        for job in jobs:
            if self._manifest is not None and not self.overwrite:
                previous = self._manifest.completed_report(job, configuration)
                if previous is not None:
                    report = self._report_base(job)
                    report.update(previous)
                    # Resuming is a manifest lookup, not a new quality-control
                    # pass.  Never inherit the former QC verdict in the current
                    # log or CSV row.
                    report["controle_qualite"] = ""
                    report["moteur_qc"] = ""
                    report["_qc_status_code"] = "not_performed"
                    report["_qc_warning"] = False
                    report["_qc_detail"] = ""
                    report["_analysis_seconds"] = 0.0
                    report["_conversion_seconds"] = 0.0
                    report["_quality_seconds"] = 0.0
                    localized_base = self._report_base(job)
                    report["opération"] = localized_base["opération"]
                    self._set_status(report, "resumed")
                    report["temps_secondes"] = "0.00"
                    report["détail"] = self.t("already_completed")
                    reports.append(report)
                    skipped += 1
                    completed += 1
                    self._log_report(report)
                    self.progress.emit(
                        completed,
                        total,
                        job.source.name,
                    )
                    continue

            if (
                self.operation != "analyze"
                and job.destination.exists()
                and not self.overwrite
            ):
                report = self._report_base(job)
                self._set_status(report, "skipped")
                report["détail"] = self.t("file_exists")
                reports.append(report)
                skipped += 1
                completed += 1
                self._log_report(report)
                self.progress.emit(
                    completed,
                    total,
                    job.source.name,
                )
                continue
            pending.append(job)

        initial_parallel_jobs = (
            min(4, self.max_parallel) if self.auto_parallel else self.max_parallel
        )
        self.estimate_calibration_started.emit(
            completed,
            total,
            max(1, min(len(pending), initial_parallel_jobs)),
        )

        if pending and self.operation != "analyze" and not self._cancel_event.is_set():
            self.log.emit(self.t("pipeline_enabled"))

            def pipeline_task(job: ConversionJob) -> dict[str, Any]:
                return self._analyze_and_process_job(job, configuration)

            for future, job in self._pool_results(
                pending,
                pipeline_task,
                "pipeline-piste",
            ):
                try:
                    report = future.result()
                except Exception as exc:
                    report = self._error_report(
                        job, self.t("internal_error", error=exc)
                    )
                reports.append(report)
                status_code = str(report.get("_status_code") or "")
                if status_code == "ok":
                    success += 1
                    if bool(report.get("_qc_warning")):
                        warnings += 1
                elif status_code == "error":
                    failed += 1
                elif status_code == "cancelled":
                    continue
                completed += 1
                if status_code == "ok":
                    self._emit_loudness_comparison(report)
                self._log_report(report)
                self.progress.emit(
                    completed,
                    total,
                    Path(str(report["source"])).name,
                )
            pending = []

        if pending and not self._cancel_event.is_set():
            self.log.emit(self.t("pre_measurement"))
            for future, _submitted_job in self._pool_results(
                pending,
                self._analyze_job,
                "analyse-mp3",
            ):
                job, result, error, elapsed = future.result()
                if self._cancel_event.is_set():
                    continue
                if error or result is None:
                    report = self._error_report(
                        job,
                        self.t(
                            "analysis_impossible",
                            error=error,
                        ),
                        elapsed,
                    )
                    reports.append(report)
                    failed += 1
                    completed += 1
                    self._log_report(report)
                    self.progress.emit(
                        completed,
                        total,
                        job.source.name,
                    )
                else:
                    self._emit_source_loudness(result, str(job.source))
                    report = self._analysis_report(job, result, elapsed)
                    reports.append(report)
                    success += 1
                    completed += 1
                    self._log_report(report)
                    self.progress.emit(
                        completed,
                        total,
                        job.source.name,
                    )

        try:
            self._wait_if_paused()
        except InterruptedError:
            pass

        finalization_started = time.perf_counter()
        self.log.emit(self.t("finalizing"))
        processing_elapsed = self._active_elapsed_since(run_started)
        csv_report_path = ""
        if self.generate_report and not self._cancel_event.is_set():
            try:
                csv_report_path = self._write_report(reports)
                report_path = csv_report_path
                if csv_report_path:
                    self.log.emit(self.t("report_log", path=csv_report_path))
            except OSError as exc:
                warnings += 1
                self.log.emit(self.t("report_error", error=exc))
                self.issue_entry.emit(
                    "warning",
                    str(self.output),
                    self.t("report_error", error=exc),
                )
        if self._analysis_cache_hits:
            self.log.emit(
                self.t(
                    "analysis_cache_summary",
                    hits=self._analysis_cache_hits,
                )
            )
        (
            analysis_total,
            conversion_total,
            quality_total,
        ) = reports.workload_totals
        compliant = reports.compliant_count
        (
            analysis_elapsed,
            conversion_elapsed,
            quality_elapsed,
        ) = distribute_elapsed_time_by_workload(
            processing_elapsed,
            analysis_total,
            conversion_total,
            quality_total,
        )
        if analysis_total + conversion_total + quality_total > 0.0:
            self.log.emit(
                self.t(
                    "phase_summary",
                    analysis=format_duration(analysis_elapsed, self.language),
                    conversion=format_duration(conversion_elapsed, self.language),
                    quality=format_duration(quality_elapsed, self.language),
                )
            )
        self._flush_persistence()
        self.log.emit(
            self.t(
                "finalization_completed",
                duration=format_duration(
                    time.perf_counter() - finalization_started,
                    self.language,
                ),
            )
        )

        elapsed_total = self._active_elapsed_since(run_started)
        self.log.emit(
            self.t(
                "total_time",
                duration=format_duration(elapsed_total, self.language),
            )
        )
        reports.close()
        self.finished.emit(
            success,
            failed,
            skipped,
            warnings,
            compliant,
            self._cancel_event.is_set(),
            elapsed_total,
            report_path,
        )

    def _flush_persistence(self) -> None:
        """Compact only checkpoints changed during the current run."""
        for store in (self._analysis_cache, self._manifest):
            if store is None:
                continue
            try:
                store.flush()
            except OSError:
                # Journal entries remain replayable if compaction itself
                # cannot replace the snapshot.
                pass


__all__ = ["ConversionWorker"]
