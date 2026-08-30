"""Présentation des résultats terminaux des traitements de LUFScale."""

from __future__ import annotations

from typing import Any, Callable

from PySide6.QtWidgets import QMessageBox

from ..processing.metrics import format_duration
from .dialogs import show_application_information, show_completion_summary


class CompletionController:
    """Coordonne les résumés, journaux et dialogues de fin d'exécution."""

    def __init__(
        self,
        owner: Any,
        *,
        information_dialog: Callable[[Any, str, str], None] = (
            show_application_information
        ),
        completion_dialog: Callable[[Any, str, str], None] | None = None,
        critical_dialog: Callable[[Any, str, str], Any] | None = None,
    ) -> None:
        self.owner = owner
        self.information_dialog = information_dialog
        self.completion_dialog = completion_dialog or (
            show_completion_summary
            if information_dialog is show_application_information
            else information_dialog
        )
        self.critical_dialog = critical_dialog or QMessageBox.critical

    def conversion_finished(
        self,
        *,
        success: int,
        failed: int,
        skipped: int,
        warnings: int,
        compliant: int,
        cancelled: bool,
        elapsed: float,
        report_path: str,
    ) -> None:
        """Présente le bilan final d'une conversion ou d'une analyse."""
        owner = self.owner
        owner.execution_presenter.finish(
            success=success,
            failed=failed,
            skipped=skipped,
            warnings=warnings,
            compliant=compliant,
            cancelled=cancelled,
            elapsed=elapsed,
        )
        duration = format_duration(elapsed, owner.language)
        values = {
            "files": max(
                int(getattr(owner.execution_presenter, "eta_total", 0)),
                success + failed + skipped,
            ),
            "success": success,
            "failed": failed,
            "skipped": skipped,
            "warnings": warnings,
            "compliant": compliant,
            "duration": duration,
        }
        summary = owner.t(
            "cancelled_summary" if cancelled else "completed_summary",
            **values,
        )
        owner.append_log_message(summary)
        if report_path:
            owner.append_log_message(
                owner.t("report_path", path=report_path)
            )
        owner.statusBar().showMessage(owner._source_safety_status_text())

        if cancelled:
            return

        dialog_summary = owner.t("completed_dialog_summary", **values)
        self.completion_dialog(
            owner,
            owner.t(
                "completed_with_errors"
                if failed or warnings
                else "processing_completed"
            ),
            dialog_summary,
        )


__all__ = ["CompletionController"]
