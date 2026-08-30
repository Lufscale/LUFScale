from __future__ import annotations

from dataclasses import dataclass

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
)

from ..widgets import DropArea, NavigablePathField, framed_data_field
from ._bindings import COMPACT_WORKSPACE_HEIGHT, PanelBindings


@dataclass(frozen=True, slots=True)
class SourcesPanel(PanelBindings):
    sources_panel: QFrame
    drop_area: DropArea
    add_folder_button: QPushButton
    add_files_button: QPushButton
    paste_button: QPushButton
    remove_button: QPushButton
    clear_button: QPushButton
    source_audio_count_label: QLabel
    source_list: QListWidget
    source_field_frame: QFrame
    destination_title: QLabel
    output_label: NavigablePathField
    output_button: QPushButton
    open_output_button: QPushButton

    @classmethod
    def create(cls, language: str) -> "SourcesPanel":
        sources_panel = QFrame()
        sources_panel.setObjectName("panel")
        sources_panel.setProperty("role", "sources")
        sources_panel.setSizePolicy(
            QSizePolicy.Policy.Ignored,
            QSizePolicy.Policy.Fixed,
        )
        sources_panel.setFixedHeight(COMPACT_WORKSPACE_HEIGHT)
        sources_layout = QVBoxLayout(sources_panel)
        sources_layout.setContentsMargins(9, 7, 9, 8)
        sources_layout.setSpacing(4)

        drop_area = DropArea(language)
        sources_layout.addWidget(drop_area)

        source_actions = QVBoxLayout()
        source_actions.setContentsMargins(0, 0, 0, 0)
        source_actions.setSpacing(4)
        add_actions_row = QHBoxLayout()
        add_actions_row.setSpacing(5)
        edit_actions_row = QHBoxLayout()
        edit_actions_row.setSpacing(5)
        add_folder_button = QPushButton()
        add_files_button = QPushButton()
        paste_button = QPushButton()
        remove_button = QPushButton()
        clear_button = QPushButton()
        source_audio_count_label = QLabel()
        source_audio_count_label.setObjectName("sourceAudioCount")
        source_audio_count_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )
        source_audio_count_label.setFixedHeight(30)
        source_audio_count_label.setMinimumWidth(128)
        for button in (add_folder_button, add_files_button, paste_button):
            button.setObjectName("secondaryButton")
        for button in (remove_button, clear_button):
            button.setObjectName("quietButton")
        for button in (
            add_folder_button,
            add_files_button,
            paste_button,
            remove_button,
            clear_button,
        ):
            button.setProperty("compact", True)
            button.setFixedHeight(30)
        add_actions_row.addWidget(add_folder_button, 1)
        add_actions_row.addWidget(add_files_button, 1)
        edit_actions_row.addWidget(source_audio_count_label, 2)
        edit_actions_row.addWidget(paste_button, 1)
        edit_actions_row.addWidget(remove_button, 1)
        edit_actions_row.addWidget(clear_button, 1)
        source_actions.addLayout(add_actions_row)
        source_actions.addLayout(edit_actions_row)
        sources_layout.addLayout(source_actions)

        source_list = QListWidget()
        source_list.setObjectName("sourceList")
        source_list.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )
        source_list.setSelectionMode(
            QAbstractItemView.SelectionMode.ExtendedSelection
        )
        source_list.setAlternatingRowColors(True)
        # A language-independent minimum keeps Japanese, Chinese and Hindi
        # from increasing the entire upper workspace through font metrics.
        source_list.setMinimumHeight(98)
        source_list.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        source_list.setVerticalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel
        )
        source_field_frame = framed_data_field(
            source_list,
            "sourceFieldFrame",
        )
        source_field_frame.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )
        sources_layout.addWidget(source_field_frame, 1)

        destination_frame = QFrame()
        destination_frame.setObjectName("compactDestination")
        destination_layout = QGridLayout(destination_frame)
        destination_layout.setContentsMargins(7, 5, 7, 6)
        destination_layout.setHorizontalSpacing(6)
        destination_layout.setVerticalSpacing(4)
        destination_title = QLabel()
        destination_title.setObjectName("panelTitle")
        output_label = NavigablePathField()
        output_label.setObjectName("pathLabel")
        output_label.setFrame(True)
        output_label.setFixedHeight(30)
        output_label.setSizePolicy(
            QSizePolicy.Policy.Ignored,
            QSizePolicy.Policy.Preferred,
        )
        output_button = QPushButton()
        output_button.setObjectName("primaryOutlineButton")
        open_output_button = QPushButton()
        open_output_button.setObjectName("primaryOutlineButton")
        for button in (output_button, open_output_button):
            button.setProperty("compact", True)
            button.setFixedHeight(30)
        destination_layout.addWidget(destination_title, 0, 0)
        destination_layout.addWidget(output_label, 0, 1)
        destination_layout.addWidget(open_output_button, 0, 2)
        destination_layout.addWidget(output_button, 0, 3)
        destination_layout.setColumnStretch(1, 1)
        sources_layout.addWidget(destination_frame)

        return cls(
            sources_panel=sources_panel,
            drop_area=drop_area,
            add_folder_button=add_folder_button,
            add_files_button=add_files_button,
            paste_button=paste_button,
            remove_button=remove_button,
            clear_button=clear_button,
            source_audio_count_label=source_audio_count_label,
            source_list=source_list,
            source_field_frame=source_field_frame,
            destination_title=destination_title,
            output_label=output_label,
            output_button=output_button,
            open_output_button=open_output_button,
        )
