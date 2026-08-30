"""Coordination Qt de la disponibilité de FFmpeg au démarrage et à l'usage."""

from __future__ import annotations

from typing import Any, Callable

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMessageBox

from ..processing.ffmpeg import ffmpeg_capability_error, find_ffmpeg
from .dialogs import show_ffmpeg_setup_dialog


class StartupCoordinator:
    """Présente les diagnostics FFmpeg sans les mêler à ``MainWindow``."""

    def __init__(
        self,
        owner: Any,
        locator: Callable[[], str | None] = find_ffmpeg,
        capability_checker: Callable[[str, str], str | None] = (
            ffmpeg_capability_error
        ),
    ) -> None:
        self.owner = owner
        self.locator = locator
        self.capability_checker = capability_checker

    def resolve_ffmpeg(self, *, startup: bool = False) -> str | None:
        """Valide FFmpeg et présente le dialogue adapté au contexte."""
        ffmpeg = self.locator()
        if ffmpeg is None:
            show_ffmpeg_setup_dialog(self.owner)
            return None

        capability_error = self.capability_checker(
            ffmpeg,
            self.owner.language,
        )
        if not capability_error:
            return ffmpeg

        if startup:
            show_ffmpeg_setup_dialog(
                self.owner,
                capability_error,
                "ffmpeg_incompatible",
            )
        else:
            QMessageBox.critical(
                self.owner,
                self.owner.t("ffmpeg_incompatible"),
                capability_error,
            )
        return None

    def check_ffmpeg_at_startup(self) -> None:
        self.resolve_ffmpeg(startup=True)

    def schedule_ffmpeg_check(self, delay_ms: int = 250) -> None:
        QTimer.singleShot(delay_ms, self.check_ffmpeg_at_startup)


def check_ffmpeg_at_startup(window: Any) -> None:
    """Relais historique conservé pour les anciens imports."""
    StartupCoordinator(window).check_ffmpeg_at_startup()


__all__ = ["StartupCoordinator", "check_ffmpeg_at_startup"]
