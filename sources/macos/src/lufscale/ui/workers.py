"""Orchestration Qt du worker de conversion."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

from PySide6.QtCore import QThread

from ..audio.core import LoudnessSettings
from ..processing.conversion import ConversionWorker


class WorkerCoordinator:
    """Possède les threads Qt sans absorber les décisions de ``MainWindow``."""

    def __init__(
        self,
        owner: Any,
        *,
        thread_factory: Callable[[Any], Any] = QThread,
        conversion_worker_factory: Callable[..., Any] = ConversionWorker,
    ) -> None:
        self.owner = owner
        self.thread_factory = thread_factory
        self.conversion_worker_factory = conversion_worker_factory
        self.worker: ConversionWorker | None = None
        self.worker_thread: QThread | None = None

    @property
    def conversion_running(self) -> bool:
        return self.worker_thread is not None

    @property
    def busy(self) -> bool:
        return self.conversion_running

    def start_conversion(
        self,
        *,
        ffmpeg: str,
        inputs: list[Path],
        output: Path,
        settings: LoudnessSettings,
        overwrite: bool,
        operation: str,
        max_parallel: int,
        resume_enabled: bool,
        quality_control: bool,
        generate_report: bool,
        language: str,
        skip_compliant: bool,
        analysis_method: str = "historical",
    ) -> bool:
        """Crée, connecte et démarre le worker de traitement."""
        if self.busy:
            return False

        thread = self.thread_factory(self.owner)
        worker = self.conversion_worker_factory(
            ffmpeg,
            inputs,
            output,
            settings,
            overwrite,
            operation,
            max_parallel,
            resume_enabled,
            quality_control,
            generate_report,
            language,
            skip_compliant,
            analysis_method,
        )
        worker.moveToThread(thread)
        thread.started.connect(worker.run)
        worker.scan_finished.connect(self.owner.on_scan_finished)
        worker.estimate_calibration_started.connect(
            self.owner.on_estimate_calibration_started
        )
        worker.progress.connect(self.owner.on_progress)
        worker.loudness_comparison.connect(
            self.owner.on_loudness_comparison
        )
        worker.loudness_analysis.connect(self.owner.on_loudness_analysis)
        worker.log.connect(self.owner.append_log_message)
        worker.log_entry.connect(self.owner.append_colored_log)
        worker.issue_entry.connect(self.owner.append_processing_issue)
        worker.finished.connect(self.owner.on_finished)
        worker.finished.connect(thread.quit)
        thread.finished.connect(self.owner.on_thread_finished)
        thread.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)

        self.worker = worker
        self.worker_thread = thread
        self.owner._start_elapsed_monitoring()
        self.owner._start_cpu_monitoring()
        self.owner._refresh_controls()
        thread.start()
        return True

    def toggle_conversion_pause(self) -> bool:
        """Transmet pause ou reprise et synchronise sa présentation."""
        if self.worker is None or self.worker_thread is None:
            return False
        presenter = self.owner.execution_presenter
        if presenter.conversion_paused:
            if not self.worker.request_resume():
                return False
            presenter.resume()
            self.owner.append_log_message(self.owner.t("processing_resumed"))
        else:
            if not self.worker.request_pause():
                return False
            presenter.pause()
            self.owner.append_log_message(self.owner.t("processing_paused"))
        self.owner._refresh_controls()
        return True

    def cancel_conversion(self) -> bool:
        """Demande une annulation non bloquante au worker actif."""
        if self.worker is None:
            return False
        self.owner.cancel_button.setEnabled(False)
        self.owner.execution_presenter.cancel_pause()
        self.owner.pause_button.setEnabled(False)
        self.owner._refresh_issue_buttons()
        self.worker.request_cancel()
        return True

    def conversion_thread_finished(self) -> None:
        """Nettoie l'état d'exécution après la fin du thread principal."""
        self.owner._stop_cpu_monitoring()
        self.owner._stop_elapsed_monitoring()
        self.worker = None
        self.worker_thread = None
        self.owner.execution_presenter.reset_pause()
        self.owner._refresh_controls()
        self.owner.shutdown_coordinator.conversion_thread_finished()


__all__ = ["WorkerCoordinator"]
