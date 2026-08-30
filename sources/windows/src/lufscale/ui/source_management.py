"""Présentation Qt des sources et de la destination de traitement."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

from PySide6.QtCore import QTimer, Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QListWidgetItem,
    QMessageBox,
)

from .source_state import SourceSelectionState, paths_from_clipboard


MAX_VISIBLE_SOURCE_PATHS = 2000


class SourceController:
    """Relie l'état des chemins aux widgets de la fenêtre principale."""

    def __init__(
        self,
        owner: Any,
        ffmpeg_locator: Callable[[], str | None],
    ) -> None:
        self.owner = owner
        self.state = SourceSelectionState()
        self.ffmpeg_locator = ffmpeg_locator

    def refresh_source_list(self) -> None:
        self.owner.source_list.clear()
        visible_paths = self.state.paths[:MAX_VISIBLE_SOURCE_PATHS]
        for path in visible_paths:
            self.owner.source_list.addItem(str(path))
        hidden_count = len(self.state.paths) - len(visible_paths)
        if hidden_count > 0:
            summary_item = QListWidgetItem(
                self.owner.t("source_list_more", count=hidden_count)
            )
            summary_item.setFlags(Qt.ItemFlag.NoItemFlags)
            self.owner.source_list.addItem(summary_item)
        audio_count = self.state.audio_file_count()
        count_text = self.owner.t(
            "source_audio_count", count=audio_count
        )
        self.owner.source_audio_count_label.setText(count_text)
        self.owner.source_audio_count_label.setAccessibleDescription(
            count_text
        )

    def refresh_controls(self) -> None:
        owner = self.owner
        conversion_running = owner.worker_thread is not None
        busy = conversion_running
        has_sources = bool(self.state.paths)
        has_source_selection = bool(owner.source_list.selectedItems())
        has_output = self.state.output_path is not None
        output_text = (
            str(self.state.output_path)
            if self.state.output_path
            else owner.t("no_folder")
        )
        if owner.output_label.text() != output_text:
            owner.output_label.setText(output_text)
            owner.output_label.setCursorPosition(0)
            owner.output_label.deselect()
        path_help = owner.t("destination_path_tooltip")
        if has_output:
            owner.output_label.setAccessibleDescription(
                f"{path_help}\n\n{output_text}"
            )
        else:
            owner.output_label.setAccessibleDescription(path_help)
        owner.start_button.setEnabled(
            not busy
            and has_sources
        )
        operation = str(owner.operation_combo.currentData())
        owner.start_button.setText(
            {
                "convert": owner.t("convert"),
                "replaygain": owner.t("add_replaygain"),
                "analyze": owner.t("analyze"),
            }.get(operation, owner.t("start"))
        )
        owner.pause_button.setEnabled(conversion_running)
        owner.pause_button.setText(
            owner.t(
                "resume_processing"
                if owner.execution_presenter.conversion_paused
                else "pause"
            )
        )
        owner.cancel_button.setEnabled(conversion_running)
        # La destination doit rester accessible pendant le traitement.
        owner.open_output_button.setEnabled(has_output)
        for widget in (
            owner.add_folder_button,
            owner.add_files_button,
            owner.paste_button,
            owner.output_button,
            owner.preset_combo,
            owner.volume_combo,
            owner.lufs_control,
            owner.peak_control,
            owner.quality_control,
            owner.operation_combo,
            owner.analysis_method_combo,
            owner.parallel_control,
            owner.overwrite_check,
            owner.skip_compliant_check,
            owner.resume_check,
            owner.quality_check,
            owner.report_check,
            owner.auto_start_check,
            owner.language_combo,
            owner.drop_area,
        ):
            widget.setEnabled(not busy)
        owner.quality_control.setEnabled(
            not busy and operation == "convert"
        )
        owner.overwrite_check.setEnabled(
            not busy and operation != "analyze"
        )
        owner.skip_compliant_check.setEnabled(
            not busy and operation == "convert"
        )
        owner.resume_check.setEnabled(
            not busy and operation != "analyze"
        )
        owner.quality_check.setEnabled(
            not busy and operation != "analyze"
        )
        owner.remove_button.setEnabled(
            not busy and has_source_selection
        )
        owner.clear_button.setEnabled(not busy and has_sources)
        owner._fit_progress_action_buttons()

    def add_paths(self, raw_paths: list[str]) -> None:
        owner = self.owner
        if owner.worker_thread is not None:
            return
        accepted = self.state.add_paths(raw_paths)
        self.refresh_source_list()
        self.refresh_controls()

        if accepted <= 0:
            owner.statusBar().showMessage(owner.t("no_new_source"), 5000)
            return

        if (
            owner.auto_start_check.isChecked()
            and self.state.output_path is not None
        ):
            QTimer.singleShot(200, owner.start_conversion)

    def choose_source_folder(self) -> None:
        folder = QFileDialog.getExistingDirectory(
            self.owner, self.owner.t("add_source_folder")
        )
        if folder:
            self.add_paths([folder])

    def choose_source_files(self) -> None:
        files, _ = QFileDialog.getOpenFileNames(
            self.owner,
            self.owner.t("add_source_files"),
            "",
            self.owner.t("mp3_filter"),
        )
        if files:
            self.add_paths(files)

    def paste_paths(self) -> None:
        paths = paths_from_clipboard(QApplication.clipboard().mimeData())
        if paths:
            self.add_paths(paths)
            return
        QMessageBox.information(
            self.owner,
            self.owner.t("clipboard"),
            self.owner.t("clipboard_empty"),
        )

    def remove_selected_sources(self) -> None:
        selected_rows = {
            self.owner.source_list.row(item)
            for item in self.owner.source_list.selectedItems()
            if self.owner.source_list.row(item) < MAX_VISIBLE_SOURCE_PATHS
        }
        self.state.remove_rows(selected_rows)
        self.refresh_source_list()
        self.refresh_controls()

    def clear_sources(self) -> None:
        self.state.clear()
        self.refresh_source_list()
        self.refresh_controls()

    def choose_output_folder(self) -> bool:
        start_folder = (
            str(self.state.output_path) if self.state.output_path else ""
        )
        folder = QFileDialog.getExistingDirectory(
            self.owner, self.owner.t("choose_output"), start_folder
        )
        if not folder:
            return False
        self.state.output_path = Path(folder).expanduser().resolve()
        self.owner._save_settings()
        self.refresh_controls()
        return True

    def open_output_folder(self) -> None:
        if not self.state.output_path:
            return
        try:
            self.state.output_path.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            QMessageBox.warning(
                self.owner,
                self.owner.t("folder_unavailable"),
                self.owner.t("open_output_error", error=exc),
            )
            return
        QDesktopServices.openUrl(
            QUrl.fromLocalFile(str(self.state.output_path))
        )
