from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from ..widgets import (
    OptionHelpButton,
    OptionStatusLight,
    PersistentCheckBox,
    ProfessionalComboBox,
    StepControl,
)
from ._bindings import COMPACT_WORKSPACE_HEIGHT, PanelBindings


class StatusTabWidget(QWidget):
    """Draw tabs and their pane as one continuous, platform-neutral outline."""

    currentChanged = Signal(int)
    HEADER_HEIGHT = 30

    def __init__(self) -> None:
        super().__init__()
        self._light_theme = False
        self._status_widget: QWidget | None = None
        self._stack = QStackedWidget(self)
        self._stack.setObjectName("settingsStack")
        self._tab_buttons: list[QPushButton] = []
        self._current_index = -1
        self.setAutoFillBackground(False)

    def addTab(self, page: QWidget, text: str) -> int:
        index = self._stack.addWidget(page)
        button = QPushButton(text, self)
        button.setObjectName("settingsTabButton")
        button.setCheckable(True)
        button.setFlat(True)
        button.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        button.clicked.connect(
            lambda _checked=False, tab_index=index: self.setCurrentIndex(
                tab_index
            )
        )
        self._tab_buttons.append(button)
        if self._current_index < 0:
            self.setCurrentIndex(0)
        self._refresh_geometry()
        return index

    def count(self) -> int:
        return len(self._tab_buttons)

    def currentIndex(self) -> int:
        return self._current_index

    def setCurrentIndex(self, index: int) -> None:
        if not 0 <= index < self.count():
            return
        changed = index != self._current_index
        self._current_index = index
        self._stack.setCurrentIndex(index)
        for tab_index, button in enumerate(self._tab_buttons):
            button.setChecked(tab_index == index)
        self._apply_tab_text_colors()
        self.update()
        if changed:
            self.currentChanged.emit(index)

    def setTabText(self, index: int, text: str) -> None:
        if not 0 <= index < self.count():
            return
        button = self._tab_buttons[index]
        button.setText(text)
        button.setAccessibleName(text)
        self._refresh_geometry()

    def set_light_theme(self, enabled: bool) -> None:
        self._light_theme = bool(enabled)
        self._apply_tab_text_colors()
        self.update()

    def _apply_tab_text_colors(self) -> None:
        selected_color = "#28323b" if self._light_theme else "#f0f4f7"
        normal_color = "#596a76" if self._light_theme else "#aebac7"
        for index, button in enumerate(self._tab_buttons):
            color = (
                selected_color if index == self._current_index else normal_color
            )
            button.setStyleSheet(
                "background: transparent; border: none; padding: 0; "
                f"color: {color}; font-size: 12px; font-weight: 600;"
            )

    def set_status_widget(self, widget: QWidget) -> None:
        if self._status_widget is not None:
            self._status_widget.hide()
        self._status_widget = widget
        widget.setParent(self)
        widget.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed,
        )
        widget.show()
        self.refresh_status_widget()

    def _tab_strip_right(self) -> int:
        if not self._tab_buttons:
            return 0
        return max(button.geometry().right() for button in self._tab_buttons)

    def refresh_status_widget(self) -> None:
        self._refresh_tab_geometry()
        if self._status_widget is None:
            return
        layout = self._status_widget.layout()
        if layout is not None:
            layout.activate()
            requested_width = layout.sizeHint().width()
        else:
            requested_width = self._status_widget.sizeHint().width()
        left_limit = self._tab_strip_right() + 9
        # The final acronym follows the same ten-pixel right inset as the Audio
        # controls.  The full header height lets each lamp-and-label cell use
        # equal breathing room above and below.
        right_edge = max(left_limit, self.width() - 10)
        status_width = min(
            max(0, right_edge - left_limit),
            max(0, requested_width),
        )
        self._status_widget.setGeometry(
            right_edge - status_width,
            0,
            status_width,
            self.HEADER_HEIGHT,
        )
        self._status_widget.raise_()

    def _refresh_tab_geometry(self) -> None:
        x = 0
        for button in self._tab_buttons:
            width = max(
                104,
                min(
                    150,
                    button.fontMetrics().horizontalAdvance(button.text()) + 32,
                ),
            )
            button.setGeometry(x, 0, width, self.HEADER_HEIGHT)
            # Adjacent tabs share one boundary pixel instead of painting two
            # platform-dependent vertical strokes next to each other.
            x += width - 1
            button.raise_()

    def _refresh_geometry(self) -> None:
        self._refresh_tab_geometry()
        self._stack.setGeometry(
            1,
            self.HEADER_HEIGHT,
            max(0, self.width() - 2),
            max(0, self.height() - self.HEADER_HEIGHT - 1),
        )
        self.refresh_status_widget()
        self.update()

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self._refresh_geometry()

    def paintEvent(self, _event) -> None:
        if self.count() <= 0 or self._current_index < 0:
            return
        right = self.width() - 1
        bottom = self.height() - 1
        pane_top = self.HEADER_HEIGHT - 1
        if right <= 0 or bottom <= pane_top:
            return

        if self._light_theme:
            pane_color = QColor("#e4ded6")
            inactive_color = QColor("#d7d0c7")
            inactive_border = QColor("#9f978d")
            outline = QColor("#8f867b")
        else:
            pane_color = QColor("#242b32")
            inactive_color = QColor("#20262c")
            inactive_border = QColor("#46525e")
            # Match the neutral outer frame and recessed inner edge used by
            # the processing journal.
            outline = QColor("#5b6975")
        outline_width = 1.7
        # A stroke centred on x=0 loses half its width to the widget clip.
        # Keep the complete outer stroke inside the paint area so the left and
        # right sides have exactly the same weight and contrast.
        outline_inset = outline_width / 2.0

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        pane_fill = QPainterPath()
        pane_fill.addRoundedRect(
            0,
            pane_top,
            right,
            bottom - pane_top,
            6.0,
            6.0,
        )
        painter.fillPath(pane_fill, pane_color)

        # Paint every tab surface first, then every border segment exactly
        # once.  In particular, a boundary shared by two tabs has one owner;
        # this avoids the doubled strokes visible with the former loop plus
        # active-tab repaint.
        corner_radius = 5.0
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        for index, button in enumerate(self._tab_buttons):
            rect = button.geometry()
            selected = index == self._current_index
            # Use the same inset for the selected tab's rounded outer corner
            # and its vertical side.  Previously the curve started at x=0
            # while the complete one-pixel side had to be painted at x=1,
            # producing the visible one-pixel step beside Audio.
            tab_inset = outline_inset if selected else 0.5
            top_left = float(rect.left()) + tab_inset
            top_right = float(rect.right()) - tab_inset
            fill_path = QPainterPath()
            fill_path.moveTo(rect.left() + 1, pane_top)
            fill_path.lineTo(rect.left() + 1, corner_radius)
            fill_path.quadTo(
                rect.left() + 1,
                1,
                rect.left() + corner_radius,
                1,
            )
            fill_path.lineTo(rect.right() - corner_radius, 1)
            fill_path.quadTo(
                rect.right() - 1,
                1,
                rect.right() - 1,
                corner_radius,
            )
            fill_path.lineTo(rect.right() - 1, pane_top)
            fill_path.closeSubpath()
            painter.fillPath(
                fill_path,
                pane_color if selected else inactive_color,
            )

            painter.setPen(
                QPen(
                    outline if selected else inactive_border,
                    outline_width if selected else 1.0,
                )
            )
            top_path = QPainterPath()
            if selected:
                # The two selected-tab sides and its rounded top are one
                # continuous path.  They use the same fractional axis as the
                # pane outline below, eliminating the one-pixel step beside
                # Audio and the protruding joint beside Options.
                top_path.moveTo(
                    top_left,
                    pane_top + outline_inset,
                )
                top_path.lineTo(top_left, corner_radius)
            else:
                top_path.moveTo(top_left, corner_radius)
            top_path.quadTo(
                top_left,
                tab_inset,
                top_left + corner_radius,
                tab_inset,
            )
            top_path.lineTo(top_right - corner_radius, tab_inset)
            top_path.quadTo(
                top_right,
                tab_inset,
                top_right,
                corner_radius,
            )
            if selected:
                top_path.lineTo(
                    top_right,
                    pane_top + outline_inset,
                )
            painter.drawPath(top_path)

        active = self._tab_buttons[self._current_index].geometry()
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        for boundary_index in range(self.count() + 1):
            if boundary_index == 0:
                x = self._tab_buttons[0].geometry().left()
                touches_active = self._current_index == 0
            elif boundary_index == self.count():
                x = self._tab_buttons[-1].geometry().right()
                touches_active = self._current_index == self.count() - 1
            else:
                x = self._tab_buttons[boundary_index - 1].geometry().right()
                touches_active = self._current_index in {
                    boundary_index - 1,
                    boundary_index,
                }
            # The active boundaries already belong to the continuous path
            # drawn above.  Repainting either one here caused the doubled or
            # protruding vertical segments reported on macOS.
            if touches_active:
                continue
            # The far side of the inactive tab remains a real part of that
            # tab.  Omitting the two outer boundaries made Options lose its
            # right side when Audio was active, and Audio lose its left side
            # when Options was active.
            if boundary_index == 0:
                side_x = float(x) + outline_inset
            elif boundary_index == self.count():
                side_x = float(x) - outline_inset
            else:
                side_x = float(x)
            painter.setPen(QPen(inactive_border, 1.0))
            side_path = QPainterPath()
            side_path.moveTo(side_x, corner_radius)
            side_path.lineTo(side_x, pane_top + outline_inset)
            painter.drawPath(side_path)

        # One owner paints every segment exactly once: the selected tab has no
        # lower edge, while the neutral pane outline resumes on either side.
        # The selected tab remains connected to its pane.  The outline uses
        # the same neutral frame plus recessed inner edge as the journal.
        def pane_outline_path(
            inset: float,
            radius: float,
        ) -> QPainterPath:
            left = inset
            top = pane_top + inset
            edge_right = right - inset
            edge_bottom = bottom - inset
            active_left = max(
                left,
                float(active.left()) + outline_inset,
            )
            active_right = min(
                edge_right,
                float(active.right()) - outline_inset,
            )
            path = QPainterPath()
            if active_left > left:
                path.moveTo(active_left, top)
                path.lineTo(left + radius, top)
                path.quadTo(left, top, left, top + radius)
            else:
                path.moveTo(left, top)
            path.lineTo(left, edge_bottom - radius)
            path.quadTo(left, edge_bottom, left + radius, edge_bottom)
            path.lineTo(edge_right - radius, edge_bottom)
            path.quadTo(
                edge_right,
                edge_bottom,
                edge_right,
                edge_bottom - radius,
            )
            if active_right < edge_right:
                path.lineTo(edge_right, top + radius)
                path.quadTo(
                    edge_right,
                    top,
                    edge_right - radius,
                    top,
                )
                path.lineTo(active_right, top)
            else:
                path.lineTo(edge_right, top)
            return path

        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setPen(QPen(outline, outline_width))
        painter.drawPath(pane_outline_path(outline_inset, 6.0))


def _option_label() -> tuple[QWidget, QLabel, OptionHelpButton]:
    container = QWidget()
    container.setObjectName("optionContainer")
    label = QLabel()
    help_button = OptionHelpButton()
    layout = QHBoxLayout(container)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(6)
    label.setAlignment(
        Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
    )
    label.setSizePolicy(
        QSizePolicy.Policy.Expanding,
        QSizePolicy.Policy.Preferred,
    )
    layout.addWidget(label, 1)
    layout.addWidget(help_button)
    return container, label, help_button


def _option_checkbox(
    checkbox: QCheckBox,
) -> tuple[QWidget, OptionHelpButton, QLabel]:
    container = QWidget()
    container.setObjectName("optionContainer")
    help_button = OptionHelpButton()
    layout = QHBoxLayout(container)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)
    acronym_label = QLabel()
    acronym_label.setObjectName("optionRowAcronym")
    acronym_label.setAlignment(
        Qt.AlignmentFlag.AlignCenter
    )
    # The final common width is fitted after translation from the active
    # font metrics.  This initial minimum keeps the untranslated startup
    # layout stable without clipping accented or non-Latin abbreviations.
    acronym_label.setMinimumWidth(54)
    layout.addWidget(acronym_label)
    layout.addSpacing(8)
    layout.addWidget(checkbox)
    # Preserve a visible gap between long translated option text and Help.
    layout.addSpacing(12)
    layout.addWidget(help_button)
    layout.addStretch(1)
    return container, help_button, acronym_label


def _option_status_indicator(
    acronym: str,
) -> tuple[QWidget, OptionStatusLight, QLabel]:
    """Create one compact light used to mirror an Options checkbox."""
    container = QWidget()
    container.setObjectName("optionStatusIndicator")
    layout = QVBoxLayout(container)
    # The 13 px lamp, one-pixel gap and 12 px label occupy 26 px.  Symmetric
    # two-pixel margins therefore centre the complete indicator in the 30 px
    # tab header and keep the text clear of the pane separator.
    layout.setContentsMargins(0, 2, 0, 2)
    layout.setSpacing(1)

    light = OptionStatusLight()

    acronym_label = QLabel(acronym)
    acronym_label.setObjectName("optionStatusAcronym")
    acronym_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    acronym_label.setFixedHeight(12)

    layout.addWidget(
        light,
        0,
        Qt.AlignmentFlag.AlignHCenter,
    )
    layout.addWidget(acronym_label)
    return container, light, acronym_label


def _bind_option_status_light(
    checkbox: QCheckBox,
    light: OptionStatusLight,
) -> None:
    """Keep a status light in lockstep with its source checkbox."""
    def sync(active: bool) -> None:
        light.set_active(active)

    checkbox.toggled.connect(sync)
    sync(checkbox.isChecked())


@dataclass(frozen=True, slots=True)
class SettingsPanel(PanelBindings):
    options_frame: QFrame
    options_title: QLabel
    settings_outline: QFrame
    settings_tabs: StatusTabWidget
    audio_settings_tab: QWidget
    workflow_settings_tab: QWidget
    audio_options_layout: QGridLayout
    preset_label: QLabel
    preset_help: OptionHelpButton
    preset_combo: ProfessionalComboBox
    operation_label: QLabel
    operation_help: OptionHelpButton
    operation_combo: ProfessionalComboBox
    analysis_method_label: QLabel
    analysis_method_help: OptionHelpButton
    analysis_method_combo: ProfessionalComboBox
    volume_label: QLabel
    volume_help: OptionHelpButton
    volume_combo: ProfessionalComboBox
    target_label: QLabel
    target_help: OptionHelpButton
    lufs_spin: QDoubleSpinBox
    lufs_control: StepControl
    peak_label: QLabel
    peak_help: OptionHelpButton
    peak_spin: QDoubleSpinBox
    peak_control: StepControl
    quality_label: QLabel
    quality_help: OptionHelpButton
    quality_spin: QSpinBox
    quality_control: StepControl
    parallel_label: QLabel
    parallel_help: OptionHelpButton
    parallel_spin: QSpinBox
    parallel_control: StepControl
    _audio_label_rows: tuple[tuple[QWidget, QLabel, OptionHelpButton], ...]
    overwrite_check: PersistentCheckBox
    overwrite_help: OptionHelpButton
    skip_compliant_check: PersistentCheckBox
    skip_compliant_help: OptionHelpButton
    resume_check: PersistentCheckBox
    resume_help: OptionHelpButton
    quality_check: PersistentCheckBox
    quality_control_help: OptionHelpButton
    report_check: PersistentCheckBox
    report_help: OptionHelpButton
    auto_start_check: PersistentCheckBox
    auto_start_help: OptionHelpButton
    option_status_widget: QWidget
    option_status_cells: dict[str, QWidget]
    option_status_lights: dict[str, OptionStatusLight]
    option_status_acronyms: dict[str, QLabel]
    option_row_acronyms: dict[str, QLabel]

    @classmethod
    def create(
        cls,
        *,
        presets: Mapping[str, tuple[float, float, int]],
        volume_targets: Mapping[str, float],
        cpu_count: int,
        resume_enabled: bool,
        quality_control_enabled: bool,
        skip_compliant_enabled: bool,
    ) -> "SettingsPanel":
        options_frame = QFrame()
        options_frame.setObjectName("panel")
        options_frame.setProperty("role", "settings")
        options_frame.setSizePolicy(
            QSizePolicy.Policy.Ignored,
            QSizePolicy.Policy.Fixed,
        )
        options_frame.setFixedHeight(COMPACT_WORKSPACE_HEIGHT)
        options_panel_layout = QVBoxLayout(options_frame)
        # A fixed title cell and tab-bar height keep the first control at the
        # same y-coordinate for Latin, CJK and Devanagari font metrics.
        options_panel_layout.setContentsMargins(10, 4, 10, 8)
        options_panel_layout.setSpacing(0)
        options_title = QLabel()
        options_title.setObjectName("panelTitle")
        options_title.setFixedHeight(20)
        options_title.setAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
        )
        options_panel_layout.addWidget(options_title)
        options_panel_layout.addSpacing(2)

        settings_tabs = StatusTabWidget()
        settings_tabs.setObjectName("settingsTabs")
        # The stable interface exposes only the validated historical analysis
        # path, so the former experimental-method row no longer consumes room.
        # A fixed compact tab height keeps taller CJK/Devanagari font metrics
        # from increasing the whole main page and creating a scrollbar.
        settings_tabs.setSizePolicy(
            QSizePolicy.Policy.Ignored,
            QSizePolicy.Policy.Expanding,
        )

        audio_settings_tab = QWidget()
        workflow_settings_tab = QWidget()
        for tab in (audio_settings_tab, workflow_settings_tab):
            tab.setObjectName("settingsPage")
            tab.setSizePolicy(
                QSizePolicy.Policy.Ignored,
                QSizePolicy.Policy.Preferred,
            )
        settings_tabs.addTab(audio_settings_tab, "")
        settings_tabs.addTab(workflow_settings_tab, "")
        # The tab widget paints the only outline and opens it under the active
        # tab. The wrapper only reserves a stable compact height.
        settings_outline = QFrame()
        settings_outline.setObjectName("settingsOutline")
        settings_outline.setFixedHeight(286)
        settings_outline.setSizePolicy(
            QSizePolicy.Policy.Ignored,
            QSizePolicy.Policy.Fixed,
        )
        settings_outline_layout = QVBoxLayout(settings_outline)
        settings_outline_layout.setContentsMargins(1, 1, 1, 1)
        settings_outline_layout.setSpacing(0)
        settings_outline_layout.addWidget(settings_tabs)
        options_panel_layout.addWidget(settings_outline, 1)

        audio_options_layout = QGridLayout()
        audio_options_layout.setContentsMargins(10, 7, 10, 8)
        audio_options_layout.setHorizontalSpacing(8)
        # Two visible pixels separate the 30 px controls without making the
        # settings panel taller than the normal startup viewport.
        audio_options_layout.setVerticalSpacing(2)
        audio_options_layout.setColumnStretch(2, 1)
        for row in range(7):
            audio_options_layout.setRowMinimumHeight(row, 30)
            audio_options_layout.setRowStretch(row, 0)
        # All surplus height belongs below the controls.  Without this final
        # stretch row QGridLayout spreads it between the seven audio rows,
        # which makes their spacing change when the main window is enlarged.
        audio_options_layout.setRowStretch(7, 1)
        audio_options_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        audio_settings_tab.setLayout(audio_options_layout)

        preset_label_widget, preset_label, preset_help = _option_label()
        audio_options_layout.addWidget(preset_label_widget, 0, 1)
        preset_combo = ProfessionalComboBox()
        for key in presets:
            preset_combo.addItem("", key)
        preset_combo.addItem("", "custom")
        audio_options_layout.addWidget(preset_combo, 0, 2, 1, 3)

        operation_label_widget, operation_label, operation_help = (
            _option_label()
        )
        audio_options_layout.addWidget(operation_label_widget, 1, 1)
        operation_combo = ProfessionalComboBox()
        operation_combo.addItem("", "convert")
        operation_combo.addItem("", "replaygain")
        operation_combo.addItem("", "analyze")
        audio_options_layout.addWidget(operation_combo, 1, 2, 1, 3)

        analysis_method_label_widget, analysis_method_label, analysis_method_help = (
            _option_label()
        )
        analysis_method_combo = ProfessionalComboBox()
        analysis_method_combo.addItem("", "historical")
        analysis_method_combo.setCurrentIndex(0)
        analysis_method_label_widget.setParent(audio_settings_tab)
        analysis_method_label_widget.setVisible(False)
        analysis_method_combo.setParent(audio_settings_tab)
        analysis_method_combo.setVisible(False)

        volume_label_widget, volume_label, volume_help = _option_label()
        volume_combo = ProfessionalComboBox()
        for key in volume_targets:
            volume_combo.addItem("", key)
        volume_combo.addItem("", "custom")

        for combo in (
            preset_combo,
            operation_combo,
            volume_combo,
        ):
            combo.setMinimumHeight(30)
            combo.setSizeAdjustPolicy(
                QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon
            )
            combo.setMinimumContentsLength(6)

        target_label_widget, target_label, target_help = _option_label()
        lufs_spin = QDoubleSpinBox()
        lufs_spin.setRange(-30.0, -5.0)
        lufs_spin.setDecimals(1)
        lufs_spin.setSingleStep(0.5)
        lufs_spin.setSuffix(" LUFS")
        lufs_spin.setValue(-16.0)
        lufs_control = StepControl(lufs_spin)

        peak_label_widget, peak_label, peak_help = _option_label()
        peak_spin = QDoubleSpinBox()
        peak_spin.setRange(-9.0, 0.0)
        peak_spin.setDecimals(1)
        peak_spin.setSingleStep(0.5)
        peak_spin.setSuffix(" dBTP")
        peak_spin.setValue(-1.5)
        peak_control = StepControl(peak_spin)

        quality_label_widget, quality_label, quality_help = _option_label()
        quality_spin = QSpinBox()
        quality_spin.setRange(0, 9)
        quality_spin.setValue(0)
        quality_control = StepControl(quality_spin)

        parallel_label_widget, parallel_label, parallel_help = _option_label()
        parallel_spin = QSpinBox()
        parallel_spin.setRange(0, min(16, max(1, cpu_count)))
        parallel_spin.setValue(0)
        parallel_control = StepControl(parallel_spin)

        audio_label_rows = (
            (preset_label_widget, preset_label, preset_help),
            (operation_label_widget, operation_label, operation_help),
            (volume_label_widget, volume_label, volume_help),
            (target_label_widget, target_label, target_help),
            (peak_label_widget, peak_label, peak_help),
            (quality_label_widget, quality_label, quality_help),
            (parallel_label_widget, parallel_label, parallel_help),
        )

        for row, label_widget, control in (
            (2, volume_label_widget, volume_combo),
            (3, target_label_widget, lufs_control),
            (4, peak_label_widget, peak_control),
            (5, quality_label_widget, quality_control),
            (6, parallel_label_widget, parallel_control),
        ):
            audio_options_layout.addWidget(label_widget, row, 1)
            audio_options_layout.addWidget(control, row, 2, 1, 3)

        overwrite_check = PersistentCheckBox()
        skip_compliant_check = PersistentCheckBox()
        skip_compliant_check.setChecked(skip_compliant_enabled)
        resume_check = PersistentCheckBox()
        resume_check.setChecked(resume_enabled)
        quality_check = PersistentCheckBox()
        quality_check.setChecked(quality_control_enabled)
        report_check = PersistentCheckBox()
        report_check.setChecked(False)
        auto_start_check = PersistentCheckBox()
        auto_start_check.setChecked(False)

        status_specs = (
            ("overwrite", "", overwrite_check),
            ("skip_compliant", "", skip_compliant_check),
            ("resume", "", resume_check),
            ("quality_control", "", quality_check),
            ("create_report", "", report_check),
            ("auto_start", "", auto_start_check),
        )
        option_status_widget = QWidget()
        option_status_widget.setObjectName("optionStatusWidget")
        option_status_layout = QHBoxLayout(option_status_widget)
        option_status_layout.setContentsMargins(0, 0, 0, 0)
        option_status_layout.setSpacing(6)
        option_status_cells: dict[str, QWidget] = {}
        option_status_lights: dict[str, OptionStatusLight] = {}
        option_status_acronyms: dict[str, QLabel] = {}
        for key, acronym, checkbox in status_specs:
            cell, light, acronym_label = _option_status_indicator(acronym)
            option_status_layout.addWidget(cell)
            option_status_cells[key] = cell
            option_status_lights[key] = light
            option_status_acronyms[key] = acronym_label
            _bind_option_status_light(checkbox, light)
        settings_tabs.set_status_widget(option_status_widget)

        overwrite_widget, overwrite_help, overwrite_acronym = _option_checkbox(
            overwrite_check
        )
        skip_compliant_widget, skip_compliant_help, skip_compliant_acronym = _option_checkbox(
            skip_compliant_check
        )
        resume_widget, resume_help, resume_acronym = _option_checkbox(
            resume_check
        )
        quality_widget, quality_control_help, quality_acronym = _option_checkbox(
            quality_check
        )
        report_widget, report_help, report_acronym = _option_checkbox(
            report_check
        )
        auto_start_widget, auto_start_help, auto_start_acronym = _option_checkbox(
            auto_start_check
        )
        option_row_acronyms = {
            "overwrite": overwrite_acronym,
            "skip_compliant": skip_compliant_acronym,
            "resume": resume_acronym,
            "quality_control": quality_acronym,
            "create_report": report_acronym,
            "auto_start": auto_start_acronym,
        }

        workflow_layout = QVBoxLayout(workflow_settings_tab)
        workflow_layout.setContentsMargins(10, 8, 10, 8)
        workflow_layout.setSpacing(5)
        for option_widget in (
            overwrite_widget,
            skip_compliant_widget,
            resume_widget,
            quality_widget,
            report_widget,
            auto_start_widget,
        ):
            option_widget.setSizePolicy(
                QSizePolicy.Policy.Ignored,
                QSizePolicy.Policy.Preferred,
            )
            workflow_layout.addWidget(option_widget)
        workflow_layout.addStretch(1)

        return cls(
            options_frame=options_frame,
            options_title=options_title,
            settings_outline=settings_outline,
            settings_tabs=settings_tabs,
            audio_settings_tab=audio_settings_tab,
            workflow_settings_tab=workflow_settings_tab,
            audio_options_layout=audio_options_layout,
            preset_label=preset_label,
            preset_help=preset_help,
            preset_combo=preset_combo,
            operation_label=operation_label,
            operation_help=operation_help,
            operation_combo=operation_combo,
            analysis_method_label=analysis_method_label,
            analysis_method_help=analysis_method_help,
            analysis_method_combo=analysis_method_combo,
            volume_label=volume_label,
            volume_help=volume_help,
            volume_combo=volume_combo,
            target_label=target_label,
            target_help=target_help,
            lufs_spin=lufs_spin,
            lufs_control=lufs_control,
            peak_label=peak_label,
            peak_help=peak_help,
            peak_spin=peak_spin,
            peak_control=peak_control,
            quality_label=quality_label,
            quality_help=quality_help,
            quality_spin=quality_spin,
            quality_control=quality_control,
            parallel_label=parallel_label,
            parallel_help=parallel_help,
            parallel_spin=parallel_spin,
            parallel_control=parallel_control,
            _audio_label_rows=audio_label_rows,
            overwrite_check=overwrite_check,
            overwrite_help=overwrite_help,
            skip_compliant_check=skip_compliant_check,
            skip_compliant_help=skip_compliant_help,
            resume_check=resume_check,
            resume_help=resume_help,
            quality_check=quality_check,
            quality_control_help=quality_control_help,
            report_check=report_check,
            report_help=report_help,
            auto_start_check=auto_start_check,
            auto_start_help=auto_start_help,
            option_status_widget=option_status_widget,
            option_status_cells=option_status_cells,
            option_status_lights=option_status_lights,
            option_status_acronyms=option_status_acronyms,
            option_row_acronyms=option_row_acronyms,
        )
