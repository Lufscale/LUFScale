"""Dialogues et ressources d’interface indépendants de la fenêtre principale."""

from __future__ import annotations

import shutil
import sys
import tempfile
import uuid
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable

from PySide6.QtCore import QStandardPaths, Qt, QUrl
from PySide6.QtGui import (
    QDesktopServices,
    QFontDatabase,
    QPixmap,
)
from PySide6.QtWidgets import (
    QAbstractButton,
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFrame,
    QHeaderView,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from ..resources import (
    application_logo_path,
    application_resource_folder,
    localized_guide_path,
)
from ..version import APP_VERSION
from .help_text import format_help_text
from .issue_export import csv_export_path, write_issue_csv

FFMPEG_DOWNLOAD_URL = "https://ffmpeg.org/download.html"


def fit_dialog_button_to_text(button: QAbstractButton) -> None:
    """Give translated dialog buttons enough vertical room for every script."""
    button.ensurePolished()
    metrics = button.fontMetrics()
    text_bounds = metrics.boundingRect(button.text())
    text_height = max(
        metrics.height(),
        metrics.lineSpacing(),
        text_bounds.height(),
    )
    text_width = metrics.horizontalAdvance(button.text())
    button.setMinimumSize(
        max(58, text_width + 30),
        max(40, text_height + 20),
    )

def application_logo_pixmap(size: int) -> QPixmap:
    pixmap = QPixmap(str(application_logo_path()))
    return pixmap.scaled(
        size,
        size,
        Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.SmoothTransformation,
    )


def _translated_dialog_text(
    parent: QWidget,
    key: str,
    **values: Any,
) -> str:
    """Resolve dialog chrome in the language selected inside LUFScale."""
    translator = getattr(parent, "t", None)
    if not callable(translator):
        translator = getattr(parent.window(), "t", None)
    return translator(key, **values) if callable(translator) else key


def choose_localized_csv_path(
    parent: QWidget,
    default_path: str | Path,
    translation_owner: QWidget | None = None,
) -> Path | None:
    """Choose a CSV path in a fully app-localized, macOS-safe dialog."""
    owner = translation_owner or parent
    default = Path(default_path).expanduser()
    dialog = LocalizedCsvSaveDialog(parent, owner, default)
    if dialog.exec() != QDialog.DialogCode.Accepted:
        return None
    return dialog.selected_path()


class LocalizedCsvSaveDialog(QDialog):
    """Minimal directory browser whose complete chrome is translated by LUFScale."""

    def __init__(
        self,
        parent: QWidget,
        translation_owner: QWidget,
        default_path: Path,
    ) -> None:
        super().__init__(parent)
        self._translation_owner = translation_owner
        self._selected_path: Path | None = None
        folder = default_path.parent
        while not folder.is_dir() and folder != folder.parent:
            folder = folder.parent
        if not folder.is_dir():
            folder = Path.home()
        self._folder = folder

        self.setWindowTitle(self._t("save_issue_list_title"))
        self.setModal(True)
        self.setObjectName("localizedCsvSaveDialog")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 14, 16, 14)
        layout.setSpacing(9)

        location_row = QHBoxLayout()
        location_label = QLabel(self._t("save_dialog_location"))
        location_label.setObjectName("saveDialogLabel")
        self.location_value = QLineEdit()
        self.location_value.setObjectName("saveDialogPath")
        self.location_value.setReadOnly(True)
        self.location_value.setCursorPosition(0)
        self.parent_button = QPushButton(self._t("save_dialog_parent"))
        self.parent_button.setObjectName("saveDialogParentButton")
        fit_dialog_button_to_text(self.parent_button)
        self.parent_button.clicked.connect(self._go_to_parent)
        location_row.addWidget(location_label)
        location_row.addWidget(self.location_value, 1)
        location_row.addWidget(self.parent_button)
        layout.addLayout(location_row)

        self.folder_list = QListWidget()
        self.folder_list.setObjectName("saveDialogFolderList")
        self.folder_list.itemDoubleClicked.connect(self._enter_folder)
        layout.addWidget(self.folder_list, 1)

        filename_row = QHBoxLayout()
        filename_label = QLabel(self._t("save_dialog_filename"))
        filename_label.setObjectName("saveDialogLabel")
        self.filename_edit = QLineEdit(default_path.name)
        self.filename_edit.setObjectName("saveDialogFilename")
        filename_row.addWidget(filename_label)
        filename_row.addWidget(self.filename_edit, 1)
        layout.addLayout(filename_row)

        filetype_row = QHBoxLayout()
        filetype_label = QLabel(self._t("save_dialog_filetype"))
        filetype_label.setObjectName("saveDialogLabel")
        filetype_value = QLabel(self._t("csv_file_filter"))
        filetype_value.setObjectName("saveDialogFiletype")
        filetype_row.addWidget(filetype_label)
        filetype_row.addWidget(filetype_value, 1)
        layout.addLayout(filetype_row)

        button_row = QHBoxLayout()
        button_row.addStretch(1)
        self.save_button = QPushButton(self._t("save_dialog_save"))
        self.save_button.setObjectName("saveDialogSaveButton")
        cancel_button = QPushButton(self._t("save_dialog_cancel"))
        cancel_button.setObjectName("saveDialogCancelButton")
        for button in (self.save_button, cancel_button):
            fit_dialog_button_to_text(button)
        self.save_button.clicked.connect(self._accept_path)
        cancel_button.clicked.connect(self.reject)
        self.filename_edit.textChanged.connect(
            lambda text: self.save_button.setEnabled(bool(text.strip()))
        )
        button_row.addWidget(self.save_button)
        button_row.addWidget(cancel_button)
        layout.addLayout(button_row)

        self._refresh_folder()
        self.resize(720, 440)
        self.filename_edit.selectAll()

    def _t(self, key: str, **values: Any) -> str:
        return _translated_dialog_text(
            self._translation_owner,
            key,
            **values,
        )

    def _refresh_folder(self) -> None:
        self.location_value.setText(str(self._folder))
        self.location_value.setCursorPosition(0)
        self.folder_list.clear()
        try:
            folders = sorted(
                (
                    path
                    for path in self._folder.iterdir()
                    if path.is_dir() and not path.name.startswith(".")
                ),
                key=lambda path: path.name.casefold(),
            )
        except OSError:
            folders = []
        for folder in folders:
            item = QListWidgetItem(folder.name)
            item.setData(Qt.ItemDataRole.UserRole, str(folder))
            self.folder_list.addItem(item)
        self.parent_button.setEnabled(self._folder != self._folder.parent)

    def _go_to_parent(self) -> None:
        if self._folder != self._folder.parent:
            self._folder = self._folder.parent
            self._refresh_folder()

    def _enter_folder(self, item: QListWidgetItem) -> None:
        folder = Path(str(item.data(Qt.ItemDataRole.UserRole)))
        if folder.is_dir():
            self._folder = folder
            self._refresh_folder()

    def _accept_path(self) -> None:
        name = self.filename_edit.text().strip()
        if not name or Path(name).name != name:
            return
        path = csv_export_path(self._folder / name)
        if path.exists():
            message = QMessageBox(self)
            message.setIcon(QMessageBox.Icon.Question)
            message.setWindowTitle(self._t("save_dialog_overwrite_title"))
            message.setText(
                self._t("save_dialog_overwrite_message", file=path.name)
            )
            overwrite = message.addButton(
                self._t("save_dialog_overwrite"),
                QMessageBox.ButtonRole.AcceptRole,
            )
            cancel = message.addButton(
                self._t("save_dialog_cancel"),
                QMessageBox.ButtonRole.RejectRole,
            )
            fit_dialog_button_to_text(overwrite)
            fit_dialog_button_to_text(cancel)
            message.exec()
            if message.clickedButton() is not overwrite:
                return
        self._selected_path = path
        self.accept()

    def selected_path(self) -> Path | None:
        return self._selected_path

@lru_cache(maxsize=1)
def register_bundled_interface_fonts() -> tuple[int, ...]:
    font_folder = application_resource_folder() / "assets" / "fonts"
    font_ids = []
    for file_name in (
        "NotoSansDevanagari-Regular.ttf",
        "NotoSansDevanagari-Bold.ttf",
        "NotoSansJP-Regular.ttf",
        "NotoSansJP-Bold.ttf",
        "NotoSansSC-Regular.ttf",
        "NotoSansSC-Bold.ttf",
        "NotoSansKR-Regular.ttf",
        "NotoSansKR-Bold.ttf",
    ):
        font_id = QFontDatabase.addApplicationFont(
            str(font_folder / file_name)
        )
        if font_id >= 0:
            font_ids.append(font_id)
    return tuple(font_ids)

def prepare_cached_guide(
    language: str,
    resource_root: Path | None = None,
    cache_root: Path | None = None,
) -> Path:
    source = localized_guide_path(language, resource_root)
    if cache_root is None:
        standard_cache = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.CacheLocation
        )
        cache_root = (
            Path(standard_cache)
            if standard_cache
            else Path(tempfile.gettempdir()) / "LUFScale"
        )
    destination = (
        Path(cache_root)
        / "guides"
        / APP_VERSION
        / source.name
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(
        f".{destination.name}.{uuid.uuid4().hex}.tmp"
    )
    try:
        shutil.copy2(source, temporary)
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)
    return destination

class ApplicationInfoDialog(QDialog):
    def __init__(
        self,
        parent: QWidget,
        title: str,
        text: str,
    ) -> None:
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setModal(True)
        self.setObjectName("applicationInfoDialog")

        screen = parent.screen() or QApplication.primaryScreen()
        if screen is None:
            dialog_width = 840
            maximum_height = 720
        else:
            available = screen.availableGeometry()
            dialog_width = min(
                840,
                max(520, available.width() - 80),
            )
            maximum_height = max(300, available.height() - 64)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 20, 24, 18)
        layout.setSpacing(14)

        icon_label = QLabel()
        icon_label.setObjectName("applicationInfoIcon")
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setFixedSize(58, 58)
        icon_label.setPixmap(application_logo_pixmap(58))
        layout.addWidget(
            icon_label,
            0,
            Qt.AlignmentFlag.AlignHCenter,
        )

        # QTextEdit owns both the wrapped document and its scroll bars.  This
        # avoids the QLabel/QScrollArea height disagreement that clipped the
        # final line on macOS in French and several fallback-font scripts.
        text_view = QTextEdit()
        text_view.setObjectName("applicationInfoText")
        text_view.setReadOnly(True)
        text_view.setAcceptRichText(False)
        text_view.setPlainText(format_help_text(text))
        text_view.setFrameShape(QFrame.Shape.NoFrame)
        text_view.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        text_view.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        text_view.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        text_view.setStyleSheet(
            "QTextEdit#applicationInfoText {"
            "background: transparent; border: none; padding: 0px;"
            "}"
        )
        # Paragraph spacing is expressed as plain blank lines by the shared
        # formatter.  Keeping the QTextDocument untouched here makes the one
        # dialog used by both Version and every question-mark button robust on
        # the native macOS Qt build as well as on the packaged fallback fonts.
        text_width = max(320, dialog_width - 48)
        text_view.setFixedWidth(text_width)
        text_view.document().setDocumentMargin(8.0)
        # Measure against a deliberately narrower line than the final
        # viewport.  This absorbs native macOS scrollbar metrics and Cyrillic,
        # CJK or Devanagari fallback differences before deciding whether a
        # vertical scrollbar is actually necessary.
        text_view.document().setTextWidth(text_width - 42)
        text_view.ensurePolished()
        line_height = text_view.fontMetrics().lineSpacing()
        measured_text_height = int(
            text_view.document().documentLayout().documentSize().height()
        )
        # Five complete lines remain inside the document viewport. Native
        # macOS fallback fonts (notably Cyrillic, CJK and Devanagari) can
        # report a smaller document height before the dialog is finally laid
        # out.  The reserve prevents the final paragraph from being hidden.
        text_height = measured_text_height + (5 * line_height) + 16

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
        )
        buttons.setObjectName("applicationInfoButtons")
        ok_button = buttons.button(QDialogButtonBox.StandardButton.Ok)
        ok_button.setText(_translated_dialog_text(parent, "dialog_ok"))
        fit_dialog_button_to_text(ok_button)
        buttons.setMinimumHeight(ok_button.minimumHeight())
        buttons.accepted.connect(self.accept)

        margins = layout.contentsMargins()
        fixed_content_height = (
            margins.top()
            + margins.bottom()
            + 58
            + buttons.sizeHint().height()
            + (layout.spacing() * 2)
            + 10
        )
        maximum_text_height = max(
            line_height * 4,
            maximum_height - fixed_content_height,
        )
        visible_text_height = min(text_height, maximum_text_height)

        # Keep a scrollbar available after the native widget has polished its
        # real font metrics.  A fixed viewport and a fixed dialog previously
        # made the last Russian lines unreachable on some macOS systems.
        text_view.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        text_view.setMinimumHeight(min(visible_text_height, line_height * 8))
        text_view.setMaximumHeight(maximum_text_height)
        text_view.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )
        layout.addWidget(text_view, 1)
        layout.addWidget(buttons)

        dialog_height = min(
            maximum_height,
            max(230, fixed_content_height + visible_text_height),
        )
        self.resize(dialog_width, dialog_height)
        self.setMinimumSize(dialog_width, min(dialog_height, 300))
        self.setMaximumSize(dialog_width, maximum_height)


class CompletionSummaryDialog(QDialog):
    """Compact summary that never clips long translated final lines."""

    def __init__(
        self,
        parent: QWidget,
        title: str,
        text: str,
    ) -> None:
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setModal(True)
        self.setObjectName("completionSummaryDialog")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 14, 16, 12)
        layout.setSpacing(9)

        icon_label = QLabel()
        icon_label.setObjectName("completionSummaryIcon")
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setFixedSize(50, 50)
        icon_label.setPixmap(application_logo_pixmap(50))
        layout.addWidget(
            icon_label,
            0,
            Qt.AlignmentFlag.AlignHCenter,
        )

        text_label = QLabel(text)
        text_label.setObjectName("completionSummaryText")
        text_label.setTextFormat(Qt.TextFormat.PlainText)
        text_label.setWordWrap(True)
        text_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        text_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        text_label.setAutoFillBackground(False)
        text_label.setContentsMargins(0, 0, 0, 0)
        text_label.ensurePolished()
        longest_line_width = max(
            (
                text_label.fontMetrics().horizontalAdvance(line)
                for line in text.splitlines()
            ),
            default=0,
        )
        screen = parent.screen() or QApplication.primaryScreen()
        available_width = (
            screen.availableGeometry().width() if screen is not None else 640
        )
        dialog_width = min(
            max(240, longest_line_width + 32),
            min(340, max(240, available_width - 80)),
        )
        # Reserve the native vertical-scrollbar width even when it is not
        # currently visible, so enabling it can never hide the last glyphs.
        text_width = dialog_width - 52
        text_label.setFixedWidth(text_width)
        line_height = text_label.fontMetrics().lineSpacing()
        text_bounds = text_label.fontMetrics().boundingRect(
            0,
            0,
            text_width,
            10000,
            int(Qt.TextFlag.TextWordWrap),
            text,
        )
        measured_text_height = max(
            text_label.sizeHint().height(),
            text_label.heightForWidth(text_width),
            text_bounds.height() + 4,
            line_height * max(1, len(text.splitlines())) + 8,
        )
        # Keep two full typographic lines as a safety margin.  Native macOS
        # font fallback can report a smaller bounding box for Japanese,
        # Chinese and Devanagari than the glyphs finally painted by Qt.
        text_height = measured_text_height + (2 * line_height)
        text_label.setFixedHeight(text_height)

        screen_height = (
            screen.availableGeometry().height() if screen is not None else 720
        )
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
        )
        buttons.setObjectName("completionSummaryButtons")
        ok_button = buttons.button(QDialogButtonBox.StandardButton.Ok)
        ok_button.setText(_translated_dialog_text(parent, "dialog_ok"))
        fit_dialog_button_to_text(ok_button)
        buttons.setMinimumHeight(ok_button.minimumHeight())
        buttons.accepted.connect(self.accept)

        margins = layout.contentsMargins()
        fixed_content_height = (
            margins.top()
            + margins.bottom()
            + 50
            + buttons.sizeHint().height()
            + (layout.spacing() * 2)
        )
        maximum_dialog_height = max(260, screen_height - 40)
        maximum_text_height = max(
            line_height * 4,
            maximum_dialog_height - fixed_content_height,
        )
        visible_text_height = min(text_height, maximum_text_height)

        text_scroll = QScrollArea()
        text_scroll.setObjectName("completionSummaryScroll")
        text_scroll.setFrameShape(QFrame.Shape.NoFrame)
        text_scroll.setAutoFillBackground(False)
        text_scroll.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground,
            True,
        )
        text_scroll.viewport().setAutoFillBackground(False)
        text_scroll.viewport().setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground,
            True,
        )
        text_scroll.setStyleSheet(
            "QScrollArea#completionSummaryScroll {"
            "background: transparent; border: none;"
            "}"
            "QScrollArea#completionSummaryScroll QWidget {"
            "background: transparent;"
            "}"
        )
        text_scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        text_scroll.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        text_scroll.setWidget(text_label)
        text_scroll.setWidgetResizable(False)
        text_scroll.setFixedSize(dialog_width - 32, visible_text_height)
        layout.addWidget(text_scroll)

        layout.addWidget(buttons)

        dialog_height = fixed_content_height + visible_text_height + 6
        self.setFixedSize(dialog_width, dialog_height)


class IssueListDialog(QDialog):
    """Independent, exportable view of retained warnings or errors."""

    def __init__(
        self,
        parent: QWidget,
        title: str,
        entries: Iterable[Any],
        export_kind: str,
    ) -> None:
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setModal(True)
        self.setObjectName("issueListDialog")
        self._parent_window = parent
        self._entries = tuple(entries)
        self._export_kind = export_kind

        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 14, 14, 12)
        layout.setSpacing(10)

        self.issue_table = QTreeWidget()
        self.issue_table.setObjectName("issueListTable")
        self.issue_table.setColumnCount(3)
        self.issue_table.setHeaderLabels(
            (
                _translated_dialog_text(parent, "issue_file_column"),
                _translated_dialog_text(parent, "issue_path_column"),
                _translated_dialog_text(parent, "issue_detail_column"),
            )
        )
        self.issue_table.setRootIsDecorated(False)
        self.issue_table.setUniformRowHeights(True)
        self.issue_table.setAlternatingRowColors(True)
        for entry in self._entries:
            values = (
                str(getattr(entry, "filename", "")),
                str(getattr(entry, "path", "")),
                str(getattr(entry, "detail", "")),
            )
            item = QTreeWidgetItem(values)
            for column, value in enumerate(values):
                item.setToolTip(column, value)
            self.issue_table.addTopLevelItem(item)
        header = self.issue_table.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.issue_table, 1)

        button_row = QHBoxLayout()
        save_button = QPushButton(
            _translated_dialog_text(parent, "save_issue_list")
        )
        save_button.setObjectName("saveIssueListButton")
        close_button = QPushButton(
            _translated_dialog_text(parent, "close_button")
        )
        close_button.setObjectName("closeIssueListButton")
        for button in (save_button, close_button):
            fit_dialog_button_to_text(button)
        save_button.clicked.connect(self._save_entries)
        close_button.clicked.connect(self.accept)
        button_row.addWidget(save_button)
        button_row.addStretch(1)
        button_row.addWidget(close_button)
        layout.addLayout(button_row)

        screen = parent.screen() or QApplication.primaryScreen()
        if screen is None:
            self.resize(840, 420)
        else:
            available = screen.availableGeometry()
            self.resize(
                min(840, max(620, available.width() - 80)),
                min(420, max(300, available.height() - 100)),
            )

    def _default_export_path(self) -> Path:
        output_path = getattr(self._parent_window, "output_path", None)
        if output_path:
            folder = Path(output_path)
        else:
            documents = QStandardPaths.writableLocation(
                QStandardPaths.StandardLocation.DocumentsLocation
            )
            folder = Path(documents) if documents else Path.home()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return folder / f"LUFScale_{self._export_kind}_{timestamp}.csv"

    def _save_entries(self) -> None:
        parent = self._parent_window
        filename = choose_localized_csv_path(
            self,
            self._default_export_path(),
            parent,
        )
        if not filename:
            return
        path = csv_export_path(filename)
        headers = (
            _translated_dialog_text(parent, "issue_file_column"),
            _translated_dialog_text(parent, "issue_path_column"),
            _translated_dialog_text(parent, "issue_detail_column"),
        )
        try:
            write_issue_csv(
                path,
                headers,
                (
                    (
                        getattr(entry, "filename", ""),
                        getattr(entry, "path", ""),
                        getattr(entry, "detail", ""),
                    )
                    for entry in self._entries
                ),
            )
        except OSError as exc:
            QMessageBox.warning(
                self,
                _translated_dialog_text(parent, "save_issue_list_error_title"),
                _translated_dialog_text(
                    parent, "save_issue_list_error", error=exc
                ),
            )


def show_issue_list(
    parent: QWidget,
    title: str,
    entries: Iterable[Any],
    export_kind: str,
) -> None:
    IssueListDialog(parent, title, entries, export_kind).exec()

def show_application_information(
    parent: QWidget,
    title: str,
    text: str,
) -> None:
    dialog = ApplicationInfoDialog(parent, title, text)
    dialog.setObjectName("applicationInfoDialog")
    dialog.exec()


def show_completion_summary(
    parent: QWidget,
    title: str,
    text: str,
) -> None:
    dialog = CompletionSummaryDialog(parent, title, text)
    dialog.exec()

def show_ffmpeg_setup_dialog(
    parent: QWidget,
    detail: str | None = None,
    title_key: str = "ffmpeg_missing",
) -> None:
    dialog = QMessageBox(parent)
    dialog.setIcon(QMessageBox.Icon.Warning)
    dialog.setWindowTitle(parent.t(title_key))
    dialog.setText(detail or parent.t("interface_ffmpeg_message"))
    download_button = None
    # The 2.1.12 application bundle contains its own verified engine.  A
    # missing engine therefore means the application bundle is incomplete;
    # offering a separate FFmpeg download would contradict the autonomous
    # distribution model.  The button remains useful when running the source
    # tree directly.
    if not getattr(sys, "frozen", False):
        download_button = dialog.addButton(
            parent.t("ffmpeg_download_button"),
            QMessageBox.ButtonRole.ActionRole,
        )
    ok_button = dialog.addButton(QMessageBox.StandardButton.Ok)
    ok_button.setText(_translated_dialog_text(parent, "dialog_ok"))
    fit_dialog_button_to_text(ok_button)
    dialog.exec()
    if download_button is not None and dialog.clickedButton() is download_button:
        QDesktopServices.openUrl(QUrl(FFMPEG_DOWNLOAD_URL))
