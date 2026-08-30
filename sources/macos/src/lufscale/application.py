from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

from PySide6.QtCore import (
    QSettings,
    QTimer,
    Qt,
    QUrl,
    Slot,
)
from PySide6.QtGui import (
    QCloseEvent,
    QDesktopServices,
    QFont,
    QIcon,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLayout,
    QMainWindow,
    QMessageBox,
    QScrollArea,
    QSizePolicy,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from .i18n.loader import (
    SUPPORTED_LANGUAGES,
    translate,
)
from .ui.themes import LIGHT_STYLE_SHEET, STYLE_SHEET
from .ui.help_catalog import compose_help_text
from .ui.dialogs import (
    prepare_cached_guide,
    register_bundled_interface_fonts,
    show_application_information,
    show_issue_list,
)
from .ui.execution import (
    ExecutionPresenter,
)
from .ui.settings import (
    DEFAULT_QUALITY_CONTROL_ENABLED,
    DEFAULT_RESUME_ENABLED,
    DEFAULT_SKIP_COMPLIANT_ENABLED,
    PRESETS,
    VOLUME_TARGETS,
    SettingsController,
    load_initial_preferences,
)
from .ui.source_management import SourceController
from .ui.startup import StartupCoordinator
from .ui.completion import CompletionController
from .ui.conversion_request import ConversionRequestController
from .ui.shutdown import ShutdownCoordinator
from .ui.workers import WorkerCoordinator
from .ui.panels import (
    HeaderPanel,
    ProgressPanel,
    ResultsPanel,
    SettingsPanel,
    SourcesPanel,
)
from .ui.widgets import (
    ExternalLinkButton,
    OptionHelpButton,
    ProfessionalComboBox,
)
from .processing.conversion import ConversionWorker
from .processing.ffmpeg import find_ffmpeg
from .processing.metrics import (
    DECIMAL_COMMA_LANGUAGES,
)
from .resources import (
    application_logo_path,
    localized_guide_path,
)
from .version import (
    APP_AUTHOR,
    APP_DISPLAY_VERSION,
    APP_LICENSE,
    APP_LICENSE_URL,
    APP_NAME,
    APP_VERSION,
    APP_WEBSITE_URL,
)

try:
    import psutil
except ImportError:
    psutil = None


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        register_bundled_interface_fonts()
        self.settings_store = QSettings(APP_NAME, APP_NAME)
        self.language, self.theme = load_initial_preferences(self.settings_store)
        self.setWindowTitle(f"{self.t('app_name')} {APP_DISPLAY_VERSION}")
        screen = QApplication.primaryScreen()
        if screen is None:
            self.resize(1180, 700)
        else:
            available = screen.availableGeometry()
            self.resize(
                min(1180, max(760, available.width() - 12)),
                min(700, max(540, available.height() - 12)),
            )
        self.setMinimumSize(760, 540)

        self.startup_coordinator = StartupCoordinator(self)
        self.source_controller = SourceController(self, find_ffmpeg)
        self.settings_controller = SettingsController(self)
        self.worker_coordinator = WorkerCoordinator(self)
        self.shutdown_coordinator = ShutdownCoordinator(self)
        self.conversion_request_controller = ConversionRequestController(self)
        self.completion_controller = CompletionController(self)
        self.execution_presenter = ExecutionPresenter(self)
        # Aliases conservés pour les extensions qui pilotent les minuteries.
        self.cpu_timer = self.execution_presenter.cpu_timer
        self.elapsed_timer = self.execution_presenter.elapsed_timer

        self._build_ui()
        self._restore_settings()
        self._retranslate_ui()
        self._refresh_source_list()
        self._refresh_controls()
        QTimer.singleShot(0, self._fit_initial_window_to_content)

    def t(self, key: str, **values: Any) -> str:
        return translate(self.language, key, **values)

    @property
    def worker(self) -> ConversionWorker | None:
        """Relais historique vers le worker de conversion actif."""
        return self.worker_coordinator.worker

    @worker.setter
    def worker(self, value: ConversionWorker | None) -> None:
        self.worker_coordinator.worker = value

    @property
    def worker_thread(self) -> Any:
        """Relais historique vers le thread de conversion actif."""
        return self.worker_coordinator.worker_thread

    @worker_thread.setter
    def worker_thread(self, value: Any) -> None:
        self.worker_coordinator.worker_thread = value

    @property
    def close_after_cancel(self) -> bool:
        """Relais historique vers la fermeture différée."""
        return self.shutdown_coordinator.close_after_cancel

    @close_after_cancel.setter
    def close_after_cancel(self, value: bool) -> None:
        self.shutdown_coordinator.close_after_cancel = value

    @property
    def source_paths(self) -> list[Path]:
        """Expose l'état des sources aux anciens appels de MainWindow."""
        return self.source_controller.state.paths

    @source_paths.setter
    def source_paths(self, paths: list[Path]) -> None:
        self.source_controller.state.paths = paths

    @property
    def output_path(self) -> Path | None:
        """Expose la destination aux anciens appels de MainWindow."""
        return self.source_controller.state.output_path

    @output_path.setter
    def output_path(self, path: Path | None) -> None:
        self.source_controller.state.output_path = path

    def _fit_initial_window_to_content(self) -> None:
        screen = self.screen() or QApplication.primaryScreen()
        if screen is None:
            return
        available = screen.availableGeometry()
        maximum_width = max(760, available.width() - 12)
        maximum_height = max(540, available.height() - 12)
        # Translation-dependent size hints must not enlarge the window.  The
        # two upper panels have a shared fixed budget for all bundled scripts.
        # Remove only the surplus initially assigned to the elastic log so its
        # lower edge matches the fixed loudness graph. The explicit row bottom
        # gap remains between both panels and the status bar.  Future user
        # resizes still flow exclusively into the log.
        desired_width = min(maximum_width, self.width())
        results_surplus = max(
            0,
            self.results_row.geometry().height()
            - self.loudness_comparison_frame.height(),
        )
        desired_height = min(
            maximum_height,
            max(self.minimumHeight(), self.height() - results_surplus),
        )
        self.resize(desired_width, desired_height)
        self.move(
            available.x() + max(0, (available.width() - desired_width) // 2),
            available.y() + max(0, (available.height() - desired_height) // 2),
        )

    def _fit_audio_label_column(self) -> None:
        """Reserve enough room for every translated Audio-row label."""
        help_width = max(
            help_button.sizeHint().width()
            for _container, _label, help_button in self._audio_label_rows
        )
        label_width = max(
            label.fontMetrics().horizontalAdvance(label.text())
            for _container, label, _help_button in self._audio_label_rows
        )
        column_width = label_width + help_width + 11
        self.audio_options_layout.setColumnMinimumWidth(1, column_width)
        for container, _label, _help_button in self._audio_label_rows:
            container.setMinimumWidth(column_width)

    def _set_option_help(
        self,
        button: OptionHelpButton,
        title: str,
        text: str,
    ) -> None:
        button.set_help(
            title,
            text,
            self.t("show_option_help", option=title),
        )

    def _help_text(self, dialog: str) -> str:
        """Return the localized help using the shared section catalogue."""
        return compose_help_text(self.t, dialog)

    def _build_ui(self) -> None:
        self.scroll_area = QScrollArea()
        self.scroll_area.setObjectName("mainScroll")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        self.main_content = QWidget()
        self.main_content.setObjectName("mainContent")
        self.main_content.setSizePolicy(
            QSizePolicy.Policy.Ignored,
            QSizePolicy.Policy.Ignored,
        )
        self.scroll_area.setWidget(self.main_content)
        self.setCentralWidget(self.scroll_area)

        main = QVBoxLayout(self.main_content)
        main.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        main.setContentsMargins(14, 0, 14, 0)
        main.setSpacing(0)

        header_panel = HeaderPanel.create(self.language)
        header_panel.bind_to(self)
        self.version_button.clicked.connect(self.show_application_features)
        self.theme_button.clicked.connect(self._toggle_theme)
        self.guide_button.clicked.connect(self.open_language_guide)
        main.addLayout(self.header_row)
        main.addSpacing(3)

        workspace_row = QHBoxLayout()
        workspace_row.setContentsMargins(0, 0, 0, 0)
        workspace_row.setSpacing(8)

        sources_panel = SourcesPanel.create(self.language)
        sources_panel.bind_to(self)
        self.drop_area.paths_dropped.connect(self.add_paths)
        self.add_folder_button.clicked.connect(self.choose_source_folder)
        self.add_files_button.clicked.connect(self.choose_source_files)
        self.paste_button.clicked.connect(self.paste_paths)
        self.remove_button.clicked.connect(self.remove_selected_sources)
        self.clear_button.clicked.connect(self.clear_sources)
        self.source_list.itemSelectionChanged.connect(self._refresh_controls)
        self.output_button.clicked.connect(self.choose_output_folder)
        self.open_output_button.clicked.connect(self.open_output_folder)

        settings_panel = SettingsPanel.create(
            presets=PRESETS,
            volume_targets=VOLUME_TARGETS,
            cpu_count=max(1, os.cpu_count() or 1),
            resume_enabled=DEFAULT_RESUME_ENABLED,
            quality_control_enabled=DEFAULT_QUALITY_CONTROL_ENABLED,
            skip_compliant_enabled=DEFAULT_SKIP_COMPLIANT_ENABLED,
        )
        settings_panel.bind_to(self)
        workspace_row.addWidget(self.sources_panel, 1)
        workspace_row.addWidget(self.options_frame, 1)
        # The settings/source block keeps its compact height.  Additional
        # window height belongs to the results row so the log grows while the
        # loudness graph remains fixed.
        main.addLayout(workspace_row, 0)
        # Lower the processing row by one pixel; together with its internal
        # inset this centres the action buttons between Settings and Results.
        main.addSpacing(4)

        self.preset_combo.currentIndexChanged.connect(self._on_preset_changed)
        self.lufs_spin.valueChanged.connect(lambda _value: self._mark_preset_custom())
        self.lufs_spin.valueChanged.connect(self._sync_volume_from_lufs)
        self.peak_spin.valueChanged.connect(lambda _value: self._mark_preset_custom())
        self.quality_spin.valueChanged.connect(
            lambda _value: self._mark_preset_custom()
        )
        self.operation_combo.currentIndexChanged.connect(self._on_operation_changed)
        self.volume_combo.currentIndexChanged.connect(self._on_volume_changed)
        self.language_combo.currentIndexChanged.connect(self._on_language_changed)

        progress_panel = ProgressPanel.create()
        progress_panel.bind_to(self)
        self.start_button.clicked.connect(self.start_conversion)
        self.pause_button.clicked.connect(self.toggle_conversion_pause)
        self.cancel_button.clicked.connect(self.cancel_conversion)
        main.addLayout(self.progress_block)
        # Leave the lowered action buttons clearly detached from the results
        # while retaining the compact rhythm of the page.
        main.addSpacing(5)

        results_panel = ResultsPanel.create(self.metrics_row)
        results_panel.bind_to(self)
        self.warnings_button.clicked.connect(
            lambda _checked=False: self.show_processing_issues("warning")
        )
        self.errors_button.clicked.connect(
            lambda _checked=False: self.show_processing_issues("error")
        )
        main.addLayout(self.results_row, 1)
        # Keep the result frames visually separate from the status bar.  This
        # fixed gap never participates in the results-row stretch, so the
        # the comparison panel stays fixed while only the log grows.
        main.addSpacing(6)
        self.loudness_comparison.reset(self.lufs_spin.value())
        self.lufs_spin.valueChanged.connect(self._on_loudness_target_changed)

        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.setFixedHeight(18)
        status_bar.setContentsMargins(8, 0, 5, 0)
        status_bar.showMessage(self._source_safety_status_text())

        self.website_link = ExternalLinkButton(APP_WEBSITE_URL)
        self.website_link.setObjectName("websiteLink")
        self.website_link.setFixedHeight(16)
        self.website_link.setAccessibleName(APP_WEBSITE_URL)
        self.website_link.clicked.connect(self.open_official_website)
        status_bar.addPermanentWidget(self.website_link)
        self._apply_theme()

    def _set_combo_text(self, combo: QComboBox, data: str, key: str) -> None:
        index = combo.findData(data)
        if index >= 0:
            combo.setItemText(index, self.t(key))

    def _source_safety_status_text(self) -> str:
        # QStatusBar paints temporary text with a native six-pixel inset.
        # Two non-breaking spaces align the first visible letter with the
        # fourteen-pixel content margin used by the processing log.
        return f"\N{NO-BREAK SPACE}\N{NO-BREAK SPACE}{self.t('source_safety')}"

    def _fit_progress_action_buttons(self) -> None:
        """Keep translated action labels complete before the first resize."""
        for button, padding, minimum in (
            (self.start_button, 48, 118),
            (self.cancel_button, 34, 88),
        ):
            text_width = button.fontMetrics().horizontalAdvance(button.text())
            button.setMinimumWidth(max(minimum, text_width + padding))
        pause_width = max(
            self.pause_button.fontMetrics().horizontalAdvance(self.t(key))
            for key in ("pause", "resume_processing")
        )
        self.pause_button.setFixedWidth(max(88, pause_width + 34))

    def _fit_author_signature(self) -> None:
        """Track the author name across exactly the application-title width."""
        target_width = self.header_label.fontMetrics().horizontalAdvance(
            self.header_label.text()
        )
        author_font = self.author_label.font()
        author_font.setLetterSpacing(
            QFont.SpacingType.AbsoluteSpacing,
            0.0,
        )
        self.author_label.setFont(author_font)
        natural_width = self.author_label.fontMetrics().horizontalAdvance(APP_AUTHOR)
        gaps = max(1, len(APP_AUTHOR) - 1)
        letter_spacing = max(
            0.0,
            (target_width - natural_width) / gaps,
        )
        author_font.setLetterSpacing(
            QFont.SpacingType.AbsoluteSpacing,
            letter_spacing,
        )
        self.author_label.setFont(author_font)
        self.author_label.setFixedWidth(target_width)

    def _retranslate_ui(self) -> None:
        self.setWindowTitle(f"{self.t('app_name')} {APP_DISPLAY_VERSION}")
        self.header_label.setText(self.t("app_name"))
        self._fit_author_signature()
        self.tagline_label.setText(self.t("tagline"))
        self.version_button.setText(self.t("version_label", version=APP_VERSION))
        self.version_button.setAccessibleName(
            self.t("version_label", version=APP_VERSION)
        )
        self.version_button.setAccessibleDescription(self.t("help_title"))
        theme_text_key = "switch_to_light" if self.theme == "dark" else "switch_to_dark"
        self.theme_button.setText(self.t(theme_text_key))
        self.theme_button.setAccessibleName(self.t(theme_text_key))
        self.theme_button.setAccessibleDescription(self.t("theme_accessible"))
        self.language_combo.setAccessibleName(self.t("language"))
        self.language_combo.setAccessibleDescription(self.t("language_tooltip"))
        self.guide_button.setText(self.t("help_button"))
        self.guide_button.setAccessibleName(self.t("help_button"))
        self.guide_button.setAccessibleDescription(self.t("guide_help_tooltip"))
        self.website_link.setToolTip(self.t("official_website_tooltip"))
        self.website_link.setAccessibleDescription(
            self.t("official_website_tooltip")
        )
        self.drop_area.set_language(self.language)

        self.add_folder_button.setText(self.t("add_folders"))
        self.add_files_button.setText(self.t("add_mp3"))
        self.paste_button.setText(self.t("paste"))
        self.remove_button.setText(self.t("remove_selection"))
        selection_description = self.t("source_selection_tooltip")
        self.remove_button.setAccessibleDescription(selection_description)
        self.source_list.setAccessibleDescription(selection_description)
        self.clear_button.setText(self.t("remove_all"))
        self.destination_title.setText(self.t("destination"))
        self.output_button.setText(self.t("choose"))
        self.open_output_button.setText(self.t("show_finder"))
        path_help = self.t("destination_path_tooltip")
        self.output_label.setAccessibleName(self.t("destination"))
        self.output_label.setAccessibleDescription(path_help)

        self.options_title.setText(self.t("settings"))
        self.settings_tabs.setTabText(0, self.t("audio_tab"))
        self.settings_tabs.setTabText(1, self.t("options_tab"))
        self.settings_tabs.refresh_status_widget()
        self.preset_label.setText(self.t("preset"))
        self._set_combo_text(self.preset_combo, "library", "preset_library")
        self._set_combo_text(self.preset_combo, "streaming", "preset_streaming")
        self._set_combo_text(self.preset_combo, "dynamic", "preset_dynamic")
        self._set_combo_text(self.preset_combo, "custom", "custom")
        self.preset_combo.setAccessibleDescription(self.t("preset_tooltip"))
        self._set_option_help(
            self.preset_help,
            self.t("preset"),
            self._help_text("preset"),
        )

        self.operation_label.setText(self.t("operation"))
        self._set_combo_text(self.operation_combo, "convert", "operation_convert")
        self._set_combo_text(self.operation_combo, "replaygain", "operation_replaygain")
        self._set_combo_text(self.operation_combo, "analyze", "operation_analyze")
        self.operation_combo.setAccessibleDescription(self.t("operation_tooltip"))
        self._set_option_help(
            self.operation_help,
            self.t("operation"),
            self._help_text("operation"),
        )

        self.analysis_method_label.setText(self.t("analysis_method"))
        self._set_combo_text(
            self.analysis_method_combo,
            "historical",
            "analysis_method_historical",
        )
        self.analysis_method_combo.setAccessibleDescription(
            self.t("analysis_method_tooltip")
        )
        self._set_option_help(
            self.analysis_method_help,
            self.t("analysis_method"),
            self._help_text("analysis_method"),
        )

        self.volume_label.setText(self.t("volume"))
        self._set_combo_text(self.volume_combo, "soft", "volume_soft")
        self._set_combo_text(self.volume_combo, "normal", "volume_normal")
        self._set_combo_text(self.volume_combo, "loud", "volume_loud")
        self._set_combo_text(self.volume_combo, "custom", "custom")
        self.volume_combo.setAccessibleDescription(self.t("volume_tooltip"))
        self._set_option_help(
            self.volume_help,
            self.t("volume"),
            self._help_text("volume"),
        )
        self.target_label.setText(self.t("target"))
        self.lufs_spin.setAccessibleDescription(self.t("target_tooltip"))
        self._set_option_help(
            self.target_help,
            self.t("target"),
            self._help_text("target"),
        )
        self.peak_label.setText(self.t("peak"))
        self.peak_spin.setAccessibleDescription(self.t("peak_tooltip"))
        self._set_option_help(
            self.peak_help,
            self.t("peak"),
            self._help_text("peak"),
        )
        self.quality_label.setText(self.t("quality"))
        self.quality_spin.setAccessibleDescription(self.t("quality_tooltip"))
        self._set_option_help(
            self.quality_help,
            self.t("quality"),
            self._help_text("quality"),
        )
        decrease_tooltip = self.t("decrease_value")
        increase_tooltip = self.t("increase_value")
        for control in (
            self.lufs_control,
            self.peak_control,
            self.quality_control,
            self.parallel_control,
        ):
            control.set_button_accessibility(decrease_tooltip, increase_tooltip)
        self.parallel_label.setText(self.t("parallel"))
        self.parallel_spin.setSpecialValueText(self.t("parallel_auto"))
        self.parallel_spin.setAccessibleDescription(self.t("parallel_tooltip"))
        self._set_option_help(
            self.parallel_help,
            self.t("parallel"),
            self._help_text("parallel"),
        )
        self._fit_audio_label_column()
        self.overwrite_check.setText(self.t("overwrite"))
        self.overwrite_check.setAccessibleDescription(self.t("overwrite_tooltip"))
        self._set_option_help(
            self.overwrite_help,
            self.t("overwrite"),
            self._help_text("overwrite"),
        )
        self.skip_compliant_check.setText(self.t("skip_compliant"))
        self.skip_compliant_check.setAccessibleDescription(
            self.t("skip_compliant_tooltip")
        )
        self._set_option_help(
            self.skip_compliant_help,
            self.t("skip_compliant"),
            self._help_text("skip_compliant"),
        )
        self.resume_check.setText(self.t("resume"))
        self.resume_check.setAccessibleDescription(self.t("resume_tooltip"))
        self._set_option_help(
            self.resume_help,
            self.t("resume"),
            self._help_text("resume"),
        )
        self.quality_check.setText(self.t("quality_control"))
        self.quality_check.setAccessibleDescription(self.t("quality_control_tooltip"))
        self._set_option_help(
            self.quality_control_help,
            self.t("quality_control"),
            self._help_text("quality_control"),
        )
        self.report_check.setText(self.t("create_report"))
        self.report_check.setAccessibleDescription(self.t("report_tooltip"))
        self._set_option_help(
            self.report_help,
            self.t("create_report"),
            self._help_text("report"),
        )
        self.auto_start_check.setText(self.t("auto_start"))
        self.auto_start_check.setAccessibleDescription(self.t("auto_start_tooltip"))
        self._set_option_help(
            self.auto_start_help,
            self.t("auto_start"),
            self._help_text("auto_start"),
        )
        for key, title, description, acronym_key in (
            (
                "overwrite",
                self.t("overwrite"),
                self.t("overwrite_tooltip"),
                "option_status_overwrite",
            ),
            (
                "skip_compliant",
                self.t("skip_compliant"),
                self.t("skip_compliant_tooltip"),
                "option_status_skip_compliant",
            ),
            (
                "resume",
                self.t("resume"),
                self.t("resume_tooltip"),
                "option_status_resume",
            ),
            (
                "quality_control",
                self.t("quality_control"),
                self.t("quality_control_tooltip"),
                "option_status_quality_control",
            ),
            (
                "create_report",
                self.t("create_report"),
                self.t("report_tooltip"),
                "option_status_report",
            ),
            (
                "auto_start",
                self.t("auto_start"),
                self.t("auto_start_tooltip"),
                "option_status_auto_start",
            ),
        ):
            indicator_cell = self.option_status_cells[key]
            acronym_label = self.option_status_acronyms[key]
            acronym = self.t(acronym_key)
            acronym_label.setText(acronym)
            acronym_width = acronym_label.fontMetrics().horizontalAdvance(acronym)
            indicator_cell.setFixedWidth(max(18, acronym_width + 2))
            row_acronym_label = self.option_row_acronyms[key]
            row_acronym_label.setText(acronym)
            # The compact lights summarize state; Help remains available in
            # the Options rows. Keep accessibility metadata without showing
            # hover descriptions over the cell, circle, or acronym.
            indicator_cell.setToolTip("")
            indicator_cell.setAccessibleName(title)
            indicator_light = self.option_status_lights[key]
            indicator_light.setToolTip("")
            indicator_light.setAccessibleName(title)
            indicator_light.setAccessibleDescription(description)
            acronym_label.setToolTip("")
            acronym_label.setAccessibleName(title)
            acronym_label.setAccessibleDescription(description)
            row_acronym_label.setToolTip(title)
            row_acronym_label.setAccessibleName(title)
        self._fit_option_row_acronyms()
        status_layout = self.option_status_widget.layout()
        if isinstance(status_layout, QHBoxLayout):
            sample_label = next(iter(self.option_status_acronyms.values()))
            # Keep three typographic spaces between consecutive labels.  The
            # actual pixel width follows the active interface font, so the
            # gap remains consistent across all twelve languages.
            status_layout.setSpacing(
                max(8, 3 * sample_label.fontMetrics().horizontalAdvance(" "))
            )
        self.settings_tabs.refresh_status_widget()
        self.cpu_title_label.setText(self.t("cpu_usage"))
        cpu_tooltip = self.t("cpu_tooltip")
        self.cpu_title_label.setAccessibleDescription(cpu_tooltip)
        self.cpu_graph.setAccessibleDescription(cpu_tooltip)
        self.cpu_value_label.setAccessibleDescription(cpu_tooltip)
        if psutil is None:
            self.cpu_value_label.setText("")
        self.loudness_comparison_title.setText(self.t("loudness_comparison_title"))
        self._fit_loudness_comparison_title()
        comparison_tooltip = self.t("loudness_comparison_tooltip")
        self.loudness_comparison_frame.setAccessibleDescription(comparison_tooltip)
        self.loudness_comparison.setAccessibleDescription(comparison_tooltip)
        self._set_option_help(
            self.loudness_comparison_help_button,
            self.t("loudness_comparison_title"),
            self._help_text("loudness_comparison"),
        )
        self.loudness_comparison.set_decimal_comma(
            self.language in DECIMAL_COMMA_LANGUAGES
        )
        self.loudness_comparison.set_texts(
            before=self.t("loudness_comparison_before"),
            after=self.t("loudness_comparison_after"),
            replaygain_after=self.t("loudness_comparison_replaygain_after"),
            replaygain_note=self.t("loudness_comparison_replaygain_note"),
            target=self.t("loudness_comparison_target", value="{value}"),
            waiting=self.t("loudness_comparison_waiting"),
            needs_qc=self.t("loudness_comparison_needs_qc"),
            not_applicable=self.t("loudness_comparison_no_after"),
            analysis_only=self.t("loudness_comparison_no_after"),
            reached=self.t("loudness_comparison_reached", value="{value}"),
            reduced=self.t("loudness_comparison_reduced", value="{value}"),
            unchanged=self.t("loudness_comparison_unchanged"),
            increased=self.t("loudness_comparison_increased", value="{value}"),
        )
        self._set_elapsed_display(self.execution_presenter.elapsed_seconds)
        self._refresh_eta_display()
        self._refresh_activity_display()
        self.pause_button.setText(
            self.t(
                "resume_processing"
                if self.execution_presenter.conversion_paused
                else "pause"
            )
        )
        self.cancel_button.setText(self.t("cancel"))
        self._fit_progress_action_buttons()
        self.log_title_label.setText(self.t("log_title"))
        self._refresh_issue_buttons()
        self.log_box.setPlaceholderText(self.t("log_placeholder"))
        log_help_text = self._help_text("log")
        self.log_box.setAccessibleDescription(log_help_text)
        self._set_option_help(
            self.log_help_button,
            self.t("log_title"),
            log_help_text,
        )
        if self.worker_thread is None:
            self.statusBar().showMessage(self._source_safety_status_text())

    @Slot(int)
    def _on_language_changed(self, index: int) -> None:
        language = str(self.language_combo.itemData(index))
        if language not in SUPPORTED_LANGUAGES or language == self.language:
            return
        self.language = language
        self._retranslate_ui()
        self._refresh_source_list()
        self._refresh_controls()
        self._save_settings()

    @Slot(int)
    def _on_volume_changed(self, index: int) -> None:
        self.settings_controller.on_volume_changed(index)

    @Slot(float)
    def _sync_volume_from_lufs(self, value: float) -> None:
        self.settings_controller.sync_volume_from_lufs(value)

    @Slot(int)
    def _on_preset_changed(self, index: int) -> None:
        self.settings_controller.on_preset_changed(index)

    @Slot()
    def _mark_preset_custom(self, *_args) -> None:
        self.settings_controller.mark_preset_custom()

    def _restore_settings(self) -> None:
        self.settings_controller.restore()

    def _save_settings(self) -> None:
        self.settings_controller.save()

    def _apply_theme(self) -> None:
        is_light = self.theme == "light"
        self.setStyleSheet(LIGHT_STYLE_SHEET if is_light else STYLE_SHEET)
        self.settings_tabs.set_light_theme(is_light)
        self.cpu_graph.set_light_theme(is_light)
        self.loudness_comparison.set_light_theme(is_light)
        for combo in self.findChildren(ProfessionalComboBox):
            combo.set_light_theme(is_light)
        if hasattr(self, "log_box"):
            self._rerender_log_entries()

    @Slot()
    def _toggle_theme(self) -> None:
        self.theme = "light" if self.theme == "dark" else "dark"
        self._apply_theme()
        self._retranslate_ui()
        self._save_settings()

    def _refresh_source_list(self) -> None:
        self.source_controller.refresh_source_list()

    def _refresh_controls(self) -> None:
        self.source_controller.refresh_controls()
        self._refresh_issue_buttons()

    def _refresh_issue_buttons(self) -> None:
        """Expose retained issues only in a paused or terminal state."""
        if not hasattr(self, "warnings_button"):
            return
        running = self.worker_thread is not None
        can_inspect = not running or self.execution_presenter.conversion_paused
        for category, button, text_key, accessibility_key in (
            (
                "warning",
                self.warnings_button,
                "warnings_button",
                "warnings_button_tooltip",
            ),
            (
                "error",
                self.errors_button,
                "errors_button",
                "errors_button_tooltip",
            ),
        ):
            count = len(self.execution_presenter.issues(category))
            button.setText(self.t(text_key, count=count))
            # Keep the explanation available to assistive technologies, but
            # do not display it as a hover tooltip on these direct actions.
            button.setToolTip("")
            button.setAccessibleName(self.t(text_key, count=count))
            button.setAccessibleDescription(self.t(accessibility_key))
            button.setEnabled(bool(count) and can_inspect)

    @Slot(str, str, str)
    def append_processing_issue(
        self,
        category: str,
        source: str,
        detail: str,
    ) -> None:
        self.execution_presenter.add_issue(category, source, detail)

    def show_processing_issues(self, category: str) -> None:
        entries = self.execution_presenter.issues(category)
        if not entries:
            return
        if (
            self.worker_thread is not None
            and not self.execution_presenter.conversion_paused
        ):
            return
        is_warning = category == "warning"
        show_issue_list(
            self,
            self.t("warnings_dialog_title" if is_warning else "errors_dialog_title"),
            entries,
            "warnings" if is_warning else "errors",
        )

    @Slot(list)
    def add_paths(self, raw_paths: list[str]) -> None:
        self.source_controller.add_paths(raw_paths)

    def choose_source_folder(self) -> None:
        self.source_controller.choose_source_folder()

    def choose_source_files(self) -> None:
        self.source_controller.choose_source_files()

    def paste_paths(self) -> None:
        self.source_controller.paste_paths()

    def remove_selected_sources(self) -> None:
        self.source_controller.remove_selected_sources()

    def clear_sources(self) -> None:
        self.source_controller.clear_sources()

    def choose_output_folder(self) -> bool:
        return self.source_controller.choose_output_folder()

    def open_output_folder(self) -> None:
        self.source_controller.open_output_folder()

    @Slot()
    def open_language_guide(self) -> None:
        embedded_guide = localized_guide_path(self.language)
        if not embedded_guide.is_file():
            QMessageBox.warning(
                self,
                self.t("guide_missing_title"),
                self.t("guide_missing_message", path=embedded_guide),
            )
            return
        try:
            guide_path = prepare_cached_guide(self.language)
        except OSError:
            QMessageBox.warning(
                self,
                self.t("guide_missing_title"),
                self.t("guide_open_error", path=embedded_guide),
            )
            return
        if not QDesktopServices.openUrl(QUrl.fromLocalFile(str(guide_path))):
            QMessageBox.warning(
                self,
                self.t("guide_missing_title"),
                self.t("guide_open_error", path=guide_path),
            )

    @Slot()
    def show_application_features(self) -> None:
        details = (
            f"{self.t('description')}\n\n"
            f"{self.t('help_overview')}\n\n"
            f"{self.t('version_changes_title', version=APP_DISPLAY_VERSION)}\n"
            f"{self.t('version_changes')}\n\n"
            f"{self.t('official_website')}\n{APP_WEBSITE_URL}\n\n"
            f"{APP_LICENSE}\n{APP_LICENSE_URL}"
        )
        show_application_information(
            self,
            (f"{self.t('app_name')} {APP_DISPLAY_VERSION} — {self.t('help_title')}"),
            details,
        )

    @Slot()
    def open_official_website(self) -> None:
        QDesktopServices.openUrl(QUrl(APP_WEBSITE_URL))

    @Slot()
    def show_loudness_comparison_help(self) -> None:
        show_application_information(
            self,
            self.t("loudness_comparison_title"),
            self._help_text("loudness_comparison"),
        )

    def _start_cpu_monitoring(self) -> None:
        self.execution_presenter.start_cpu_monitoring(psutil is not None)

    @Slot()
    def _update_cpu_usage(self) -> None:
        self.execution_presenter.update_cpu_usage()

    def _stop_cpu_monitoring(self) -> None:
        self.execution_presenter.stop_cpu_monitoring()

    @Slot(str)
    def append_log_message(self, message: str) -> None:
        self.execution_presenter.append_log_message(message)

    @Slot(str, str)
    def append_colored_log(self, category: str, message: str) -> None:
        self.execution_presenter.append_colored_log(category, message)

    def _append_colored_log(
        self,
        category: str,
        message: str,
        *,
        count_activity: bool,
    ) -> None:
        self.execution_presenter._append_colored_log(
            category,
            message,
            count_activity=count_activity,
        )

    def _active_log_palette(self) -> dict[str, str]:
        return self.execution_presenter._active_log_palette()

    def _render_log_entry(self, category: str, message: str) -> None:
        self.execution_presenter._render_log_entry(category, message)

    def _rerender_log_entries(self) -> None:
        self.execution_presenter.rerender_log_entries()

    def _reset_loudness_comparison(
        self,
        target: float,
        comparison_state: str = "waiting",
    ) -> None:
        self.loudness_comparison.reset(target, comparison_state)

    def _fit_loudness_comparison_title(self) -> None:
        """Keep long translated titles clear of the Help button."""
        available_width = self.loudness_comparison_frame.width() - 64
        for pixel_size in range(13, 8, -1):
            self.loudness_comparison_title.setStyleSheet(f"font-size: {pixel_size}px;")
            if (
                self.loudness_comparison_title.fontMetrics().horizontalAdvance(
                    self.loudness_comparison_title.text()
                )
                <= available_width
            ):
                break

    def _fit_option_row_acronyms(self) -> None:
        """Give every localized Options badge one unclipped common width."""
        labels = tuple(self.option_row_acronyms.values())
        if not labels:
            return
        # Eight pixels of stylesheet padding, two border pixels and a small
        # native-font reserve are included in addition to the measured text.
        width = max(
            54,
            max(
                label.fontMetrics().horizontalAdvance(label.text()) + 16
                for label in labels
            ),
        )
        for label in labels:
            label.setFixedWidth(width)

    @Slot(float)
    def _on_loudness_target_changed(self, target: float) -> None:
        self._reset_loudness_comparison(
            target,
            self._selected_loudness_comparison_state(),
        )

    def _selected_loudness_comparison_state(self) -> str:
        operation = str(self.operation_combo.currentData() or "convert")
        if operation == "analyze":
            return "analysis_only"
        if operation == "replaygain":
            return "replaygain"
        if operation == "convert" and not self.quality_check.isChecked():
            return "needs_qc"
        return "waiting"

    @Slot(int)
    def _on_operation_changed(self, _index: int) -> None:
        self._refresh_controls()
        if self.worker_thread is None:
            self._reset_loudness_comparison(
                self.lufs_spin.value(),
                self._selected_loudness_comparison_state(),
            )

    @Slot(str, float, float, float, float)
    def on_loudness_comparison(
        self,
        sample_key: str,
        before: float,
        after: float,
        target: float,
        expected: float,
    ) -> None:
        self.loudness_comparison.set_values(
            sample_key,
            before,
            after,
            target,
            expected,
        )

    @Slot(str, float, float)
    def on_loudness_analysis(
        self,
        sample_key: str,
        before: float,
        target: float,
    ) -> None:
        self.loudness_comparison.set_analysis_value(
            sample_key,
            before,
            target,
            (
                "replaygain"
                if self.operation_combo.currentData() == "replaygain"
                else "analysis_only"
            ),
        )

    def _set_elapsed_display(self, seconds: float) -> None:
        self.execution_presenter.set_elapsed_display(seconds)

    def _current_paused_duration(self) -> float:
        state = self.execution_presenter.state
        return state.current_paused_duration(self.execution_presenter._clock())

    def _active_conversion_elapsed(self) -> float:
        state = self.execution_presenter.state
        return state.active_conversion_elapsed(self.execution_presenter._clock())

    def _set_activity(self, key: str, **values: Any) -> None:
        self.execution_presenter.set_activity(key, **values)

    def _hide_activity(self) -> None:
        self.execution_presenter.hide_activity()

    def _set_activity_counters(
        self,
        current: int | None = None,
        total: int | None = None,
    ) -> None:
        self.execution_presenter.set_activity_counters(current, total)

    def _refresh_activity_display(self) -> None:
        self.execution_presenter.refresh_activity_display()

    def _refresh_eta_display(self) -> None:
        self.execution_presenter.refresh_eta_display()

    def _update_eta_estimate(self) -> None:
        self.execution_presenter.update_eta_estimate()

    def _start_elapsed_monitoring(self) -> None:
        self.execution_presenter.start_elapsed_monitoring()

    @Slot()
    def _update_elapsed_time(self) -> None:
        self.execution_presenter.update_elapsed_time()

    def _stop_elapsed_monitoring(self, final_elapsed: float | None = None) -> None:
        self.execution_presenter.stop_elapsed_monitoring(final_elapsed)

    @Slot()
    def start_conversion(self) -> None:
        request = self.conversion_request_controller.prepare()
        if request is not None:
            self.worker_coordinator.start_conversion(**request.worker_parameters())

    @Slot(int)
    def on_scan_finished(self, total: int) -> None:
        self.execution_presenter.scan_finished(total)

    @Slot(int, int, int)
    def on_estimate_calibration_started(
        self,
        completed: int,
        total: int,
        parallel_jobs: int,
    ) -> None:
        self.execution_presenter.estimate_calibration_started(
            completed,
            total,
            parallel_jobs,
        )

    @Slot(int, int, str)
    def on_progress(self, current: int, total: int, _label: str) -> None:
        self.execution_presenter.progress(current, total)

    @Slot()
    def toggle_conversion_pause(self) -> None:
        self.worker_coordinator.toggle_conversion_pause()

    @Slot()
    def cancel_conversion(self) -> None:
        self.worker_coordinator.cancel_conversion()

    @Slot(int, int, int, int, int, bool, float, str)
    def on_finished(
        self,
        success: int,
        failed: int,
        skipped: int,
        warnings: int,
        compliant: int,
        cancelled: bool,
        elapsed: float,
        report_path: str,
    ) -> None:
        self.completion_controller.conversion_finished(
            success=success,
            failed=failed,
            skipped=skipped,
            warnings=warnings,
            compliant=compliant,
            cancelled=cancelled,
            elapsed=elapsed,
            report_path=report_path,
        )

    @Slot()
    def on_thread_finished(self) -> None:
        self.worker_coordinator.conversion_thread_finished()

    def closeEvent(self, event: QCloseEvent) -> None:
        self.shutdown_coordinator.request_close(event)


def main() -> int:
    app = QApplication(sys.argv)
    app.setOrganizationName(APP_NAME)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setWindowIcon(QIcon(str(application_logo_path())))
    window = MainWindow()
    window.show()

    window.startup_coordinator.schedule_ffmpeg_check()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
