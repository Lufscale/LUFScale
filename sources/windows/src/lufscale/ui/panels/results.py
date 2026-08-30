from __future__ import annotations

from dataclasses import dataclass

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from ..widgets import (
    LoudnessComparison,
    OptionHelpButton,
    ProcessingLogTextEdit,
    framed_data_field,
)
from ._bindings import PanelBindings


@dataclass(frozen=True, slots=True)
class ResultsPanel(PanelBindings):
    results_row: QHBoxLayout
    log_title_label: QLabel
    warnings_button: QPushButton
    errors_button: QPushButton
    log_help_button: OptionHelpButton
    log_box: ProcessingLogTextEdit
    log_field_frame: QFrame
    loudness_comparison_frame: QFrame
    loudness_comparison_title: QLabel
    loudness_comparison_help_button: OptionHelpButton
    loudness_comparison: LoudnessComparison

    @classmethod
    def create(cls, metrics_row: QGridLayout) -> "ResultsPanel":
        results_row = QHBoxLayout()
        results_row.setSpacing(8)
        log_column = QVBoxLayout()
        log_column.setContentsMargins(0, 0, 0, 0)
        log_column.setSpacing(0)
        # Keep the timing and activity metrics above the journal while the
        # comparison panel starts immediately below the action buttons. This
        # lets the right-hand panel use the same full lower-area height without
        # changing the journal's established order.
        log_column.addLayout(metrics_row)
        # Preserve the established gap below the metrics while allowing the
        # journal header itself to meet the frame with no second gap.
        log_column.addSpacing(3)
        log_header_widget = QWidget()
        log_header_widget.setObjectName("resultsHeader")
        log_header_widget.setFixedHeight(32)
        log_header = QHBoxLayout(log_header_widget)
        log_header.setContentsMargins(0, 0, 0, 0)
        # Spacing is explicit below: this keeps Warning and Error at their
        # established coordinates while giving Help a safe right inset.
        log_header.setSpacing(0)
        log_title_label = QLabel()
        log_title_label.setObjectName("panelTitle")
        log_title_label.setFixedHeight(24)
        warnings_button = QPushButton()
        warnings_button.setObjectName("warningListButton")
        warnings_button.setProperty("compact", True)
        warnings_button.setFixedHeight(24)
        warnings_button.setEnabled(False)
        errors_button = QPushButton()
        errors_button.setObjectName("errorListButton")
        errors_button.setProperty("compact", True)
        errors_button.setFixedHeight(24)
        errors_button.setEnabled(False)
        log_help_button = OptionHelpButton()
        # Warning/Error buttons are 24 px high while the circular help button
        # is 22 px high. Keep the Help slot geometry that provides the visual
        # rise and right clearance needed by the antialiased circular border.
        log_help_slot = QWidget()
        log_help_slot.setObjectName("logHelpSlot")
        log_help_slot.setFixedSize(28, 28)
        log_help_slot_layout = QVBoxLayout(log_help_slot)
        # The six-pixel bottom margin raises the 22 px circle by four pixels
        # compared with the former 24 px slot. The matching right margin keeps
        # the full outline visible. Its dimensions remain unchanged from
        # 2.0.16 so Help keeps the approved X and Y position.
        log_help_slot_layout.setContentsMargins(0, 0, 6, 6)
        log_help_slot_layout.setSpacing(0)
        log_help_slot_layout.addWidget(log_help_button)
        # Bottom alignment moves the title and all three controls down by four
        # pixels. With no layout gap below this row, the issue buttons meet the
        # frame and the title centre sits 12 px above it - the same geometry as
        # the Settings title above the Audio tab.
        log_header.addWidget(
            log_title_label, 0, Qt.AlignmentFlag.AlignBottom
        )
        log_header.addStretch(1)
        log_header.addWidget(
            warnings_button, 0, Qt.AlignmentFlag.AlignBottom
        )
        log_header.addSpacing(6)
        log_header.addWidget(
            errors_button, 0, Qt.AlignmentFlag.AlignBottom
        )
        # Keep the same six-pixel rhythm on both sides of Error. Because Help
        # and its right-hand slot stay fixed, this explicit gap moves Warning
        # and Error six pixels left without changing Help's X or Y position.
        log_header.addSpacing(6)
        log_header.addWidget(
            log_help_slot, 0, Qt.AlignmentFlag.AlignBottom
        )
        log_column.addWidget(log_header_widget)
        log_box = ProcessingLogTextEdit()
        log_box.setObjectName("logBox")
        log_box.setReadOnly(True)
        log_box.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Ignored,
        )
        log_box.setMinimumHeight(110)
        log_box.document().setMaximumBlockCount(5000)
        log_field_frame = framed_data_field(log_box, "logFieldFrame")
        log_field_frame.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )
        # At the minimum/startup layout, the complete metrics-plus-log column
        # and the complete loudness-history panel share the same height. The
        # log remains vertically elastic afterwards, while the graph keeps its
        # fixed size.
        log_field_frame.setMinimumHeight(172)
        log_column.addWidget(log_field_frame, 1)
        results_row.addLayout(log_column, 1)

        comparison_column = QVBoxLayout()
        comparison_column.setContentsMargins(0, 0, 0, 0)
        comparison_column.setSpacing(0)

        loudness_comparison_frame = QFrame()
        loudness_comparison_frame.setObjectName("panel")
        loudness_comparison_frame.setProperty(
            "role",
            "loudnessComparison",
        )
        loudness_comparison_frame.setFixedWidth(286)
        # Keep the upper edge fixed.  The panel and journal now share the same
        # lower geometry; the role-specific neutral bottom stroke in themes.py
        # makes that common coordinate equally visible on both frames.
        loudness_comparison_frame.setFixedHeight(258)
        loudness_comparison_frame.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed,
        )
        comparison_layout = QVBoxLayout(loudness_comparison_frame)
        comparison_layout.setContentsMargins(8, 3, 8, 3)
        comparison_layout.setSpacing(0)
        comparison_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        comparison_header_widget = QWidget()
        comparison_header_widget.setObjectName("resultsHeader")
        comparison_header_widget.setFixedHeight(29)
        comparison_header = QHBoxLayout(comparison_header_widget)
        comparison_header.setContentsMargins(0, 0, 0, 0)
        comparison_header.setSpacing(0)
        loudness_comparison_title = QLabel()
        loudness_comparison_title.setObjectName("panelTitle")
        loudness_comparison_title.setFixedHeight(24)
        loudness_comparison_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        loudness_comparison_help_button = OptionHelpButton()
        comparison_header.addSpacing(22)
        comparison_header.addWidget(loudness_comparison_title, 1)
        comparison_header.addWidget(loudness_comparison_help_button)
        comparison_layout.addWidget(comparison_header_widget)
        comparison_layout.addSpacing(2)

        loudness_comparison = LoudnessComparison()
        comparison_layout.addWidget(
            loudness_comparison,
            0,
            Qt.AlignmentFlag.AlignHCenter,
        )
        comparison_column.addWidget(
            loudness_comparison_frame,
            0,
            Qt.AlignmentFlag.AlignTop,
        )
        # Additional window height belongs to the processing journal.  The
        # comparison panel remains directly below the action buttons instead
        # of following the lower edge of the resized window.
        comparison_column.setAlignment(Qt.AlignmentFlag.AlignTop)
        results_row.addLayout(comparison_column, 0)

        return cls(
            results_row=results_row,
            log_title_label=log_title_label,
            warnings_button=warnings_button,
            errors_button=errors_button,
            log_help_button=log_help_button,
            log_box=log_box,
            log_field_frame=log_field_frame,
            loudness_comparison_frame=loudness_comparison_frame,
            loudness_comparison_title=loudness_comparison_title,
            loudness_comparison_help_button=loudness_comparison_help_button,
            loudness_comparison=loudness_comparison,
        )
