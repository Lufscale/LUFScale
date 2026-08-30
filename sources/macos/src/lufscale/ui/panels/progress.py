from __future__ import annotations

from dataclasses import dataclass

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from ..widgets import CpuUsageGraph
from ._bindings import PanelBindings


@dataclass(frozen=True, slots=True)
class ProgressPanel(PanelBindings):
    progress_block: QVBoxLayout
    metrics_row: QGridLayout
    progress_bar: QProgressBar
    cpu_title_label: QLabel
    cpu_graph: CpuUsageGraph
    cpu_value_label: QLabel
    start_button: QPushButton
    pause_button: QPushButton
    cancel_button: QPushButton
    elapsed_label: QLabel
    eta_label: QLabel
    activity_labels: dict[str, QLabel]

    @classmethod
    def create(cls) -> "ProgressPanel":
        progress_block = QVBoxLayout()
        progress_block.setContentsMargins(0, 0, 0, 0)
        progress_block.setSpacing(1)
        progress_row = QHBoxLayout()
        progress_row.setContentsMargins(0, 0, 0, 0)
        progress_row.setSpacing(6)

        progress_bar = QProgressBar()
        progress_bar.setRange(0, 100)
        progress_bar.setValue(0)
        cpu_title_label = QLabel()
        cpu_title_label.setObjectName("cpuTitle")
        cpu_graph = CpuUsageGraph()
        cpu_value_label = QLabel("")
        cpu_value_label.setObjectName("cpuValue")
        cpu_value_label.setFixedWidth(42)
        cpu_value_label.setContentsMargins(3, 0, 0, 0)
        cpu_value_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )
        start_button = QPushButton()
        start_button.setObjectName("primaryButton")
        pause_button = QPushButton()
        pause_button.setObjectName("secondaryButton")
        pause_button.setEnabled(False)
        cancel_button = QPushButton()
        cancel_button.setObjectName("dangerButton")
        cancel_button.setEnabled(False)

        # The fallback fonts used by Japanese, Chinese and Hindi report
        # slightly taller size hints on macOS.  A shared compact action height
        # keeps this row, and therefore the entire main window, independent of
        # the selected language while retaining ample glyph room.
        for button in (start_button, pause_button, cancel_button):
            button.setProperty("compact", True)
            button.setFixedHeight(32)

        action_buttons = {start_button, pause_button, cancel_button}
        for widget, stretch in (
            (progress_bar, 1),
            (cpu_title_label, 0),
            (cpu_graph, 0),
            (cpu_value_label, 0),
            (start_button, 0),
            (pause_button, 0),
            (cancel_button, 0),
        ):
            if widget in action_buttons:
                # The CPU graph is shorter than the action buttons.  A
                # three-pixel top inset gives both their upper edges the same
                # visual distance from the Settings panel.
                wrapper = QWidget()
                wrapper.setFixedHeight(35)
                wrapper_layout = QVBoxLayout(wrapper)
                wrapper_layout.setContentsMargins(0, 3, 0, 0)
                wrapper_layout.setSpacing(0)
                wrapper_layout.addWidget(widget)
                progress_row.addWidget(
                    wrapper,
                    stretch,
                    Qt.AlignmentFlag.AlignVCenter,
                )
            else:
                progress_row.addWidget(
                    widget,
                    stretch,
                    Qt.AlignmentFlag.AlignVCenter,
                )
        progress_block.addLayout(progress_row)

        metrics_row = QGridLayout()
        elapsed_label = QLabel()
        elapsed_label.setObjectName("elapsedTime")
        elapsed_label.setFixedHeight(20)
        elapsed_label.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed,
        )
        eta_label = QLabel()
        eta_label.setObjectName("etaTime")
        eta_label.setFixedHeight(20)
        eta_label.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed,
        )
        activity_labels: dict[str, QLabel] = {}
        activity_positions = (
            ("activity_files", 0, 1),
            ("activity_skipped", 1, 1),
            ("activity_successes", 0, 2),
            ("activity_errors", 1, 2),
            ("activity_warnings", 0, 3),
            ("activity_compliant", 1, 3),
        )
        for key, row, column in activity_positions:
            label = QLabel()
            label.setObjectName("activityStatus")
            label.setFixedHeight(20)
            label.setSizePolicy(
                QSizePolicy.Policy.Preferred,
                QSizePolicy.Policy.Preferred,
            )
            label.setWordWrap(False)
            label.setAlignment(
                Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
            )
            label.setVisible(False)
            activity_labels[key] = label
            metrics_row.addWidget(label, row, column)
        metrics_row.setContentsMargins(0, 0, 0, 0)
        metrics_row.setHorizontalSpacing(20)
        metrics_row.setVerticalSpacing(2)
        metrics_row.setRowMinimumHeight(0, 20)
        metrics_row.setRowMinimumHeight(1, 20)
        metrics_row.addWidget(elapsed_label, 0, 0)
        metrics_row.addWidget(eta_label, 1, 0)
        for column in range(4):
            metrics_row.setColumnStretch(column, 0)
        metrics_row.setColumnStretch(4, 1)

        return cls(
            progress_block=progress_block,
            metrics_row=metrics_row,
            progress_bar=progress_bar,
            cpu_title_label=cpu_title_label,
            cpu_graph=cpu_graph,
            cpu_value_label=cpu_value_label,
            start_button=start_button,
            pause_button=pause_button,
            cancel_button=cancel_button,
            elapsed_label=elapsed_label,
            eta_label=eta_label,
            activity_labels=activity_labels,
        )
