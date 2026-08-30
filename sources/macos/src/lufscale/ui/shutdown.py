"""Coordination de la fermeture de l'application LUFScale."""

from __future__ import annotations

from typing import Any, Callable

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMessageBox

from .dialogs import show_application_information


class ShutdownCoordinator:
    """Décide si la fenêtre peut se fermer ou doit attendre un worker."""

    def __init__(
        self,
        owner: Any,
        *,
        information_dialog: Callable[[Any, str, str], None] = (
            show_application_information
        ),
        question_dialog: Callable[..., Any] | None = None,
        schedule_close: Callable[[int, Callable[[], None]], Any] | None = None,
        yes_button: Any | None = None,
        no_button: Any | None = None,
    ) -> None:
        self.owner = owner
        self.information_dialog = information_dialog
        self.question_dialog = question_dialog
        self.schedule_close = schedule_close
        self.yes_button = yes_button
        self.no_button = no_button
        self.close_after_cancel = False

    def request_close(self, event: Any) -> bool:
        """Accepte, refuse ou diffère une demande de fermeture."""
        owner = self.owner
        workers = owner.worker_coordinator
        if workers.conversion_running:
            yes_button = (
                self.yes_button
                if self.yes_button is not None
                else QMessageBox.StandardButton.Yes
            )
            no_button = (
                self.no_button
                if self.no_button is not None
                else QMessageBox.StandardButton.No
            )
            question_dialog = self.question_dialog or QMessageBox.question
            answer = question_dialog(
                owner,
                owner.t("processing_in_progress"),
                owner.t("close_question"),
                yes_button | no_button,
                no_button,
            )
            if answer == yes_button:
                self.close_after_cancel = True
                owner.cancel_conversion()
            event.ignore()
            return False

        owner._save_settings()
        event.accept()
        return True

    def conversion_thread_finished(self) -> bool:
        """Termine une fermeture différée après le nettoyage du worker."""
        if not self.close_after_cancel:
            return False
        self.close_after_cancel = False
        schedule_close = self.schedule_close or QTimer.singleShot
        schedule_close(0, self.owner.close)
        return True


__all__ = ["ShutdownCoordinator"]
