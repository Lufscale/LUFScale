from __future__ import annotations

from dataclasses import dataclass

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout

from ...i18n.loader import LANGUAGES
from ...version import APP_AUTHOR, APP_NAME
from ..dialogs import application_logo_pixmap
from ..widgets import ProfessionalComboBox
from ._bindings import PanelBindings


@dataclass(frozen=True, slots=True)
class HeaderPanel(PanelBindings):
    header_row: QHBoxLayout
    header_logo_label: QLabel
    header_label: QLabel
    tagline_label: QLabel
    version_button: QPushButton
    author_label: QLabel
    theme_button: QPushButton
    guide_button: QPushButton
    language_combo: ProfessionalComboBox

    @classmethod
    def create(cls, language: str) -> "HeaderPanel":
        header_row = QHBoxLayout()
        header_row.setSpacing(8)

        header_logo_label = QLabel()
        header_logo_label.setObjectName("headerLogo")
        header_logo_label.setFixedSize(48, 48)
        header_logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_logo_label.setAccessibleName(APP_NAME)
        header_logo_label.setPixmap(application_logo_pixmap(40))
        header_row.addWidget(
            header_logo_label,
            0,
            Qt.AlignmentFlag.AlignVCenter,
        )

        title_block = QVBoxLayout()
        title_block.setContentsMargins(0, 0, 0, 0)
        title_block.setSpacing(0)
        header_label = QLabel()
        header_label.setObjectName("header")
        header_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom
        )
        tagline_label = QLabel()
        tagline_label.setObjectName("headerTagline")
        tagline_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom
        )
        version_button = QPushButton()
        version_button.setObjectName("versionButton")

        title_row = QHBoxLayout()
        title_row.setContentsMargins(0, 0, 0, 0)
        title_row.setSpacing(12)
        title_row.setAlignment(Qt.AlignmentFlag.AlignBottom)
        title_row.addWidget(
            header_label,
            0,
            Qt.AlignmentFlag.AlignBottom,
        )
        title_row.addWidget(
            version_button,
            0,
            Qt.AlignmentFlag.AlignBottom,
        )
        title_row.addWidget(
            tagline_label,
            0,
            Qt.AlignmentFlag.AlignBottom,
        )
        title_row.addStretch(1)

        author_label = QLabel(APP_AUTHOR)
        author_label.setObjectName("author")
        subtitle_row = QHBoxLayout()
        # The logo pixmap has a small internal lower inset.  Lift the author
        # signature by three pixels so its baseline meets the visible bottom
        # of the logo instead of the lower edge of the 48 px label.
        subtitle_row.setContentsMargins(0, 0, 0, 3)
        subtitle_row.setSpacing(12)
        subtitle_row.addWidget(author_label)
        subtitle_row.addStretch(1)
        title_block.addLayout(title_row)
        title_block.addLayout(subtitle_row)
        header_row.addLayout(title_block, 1)
        header_row.addStretch(1)

        theme_button = QPushButton()
        theme_button.setObjectName("utilityButton")
        guide_button = QPushButton()
        guide_button.setObjectName("utilityButton")
        language_combo = ProfessionalComboBox()
        language_combo.setObjectName("languageCombo")
        for code, label in LANGUAGES:
            language_combo.addItem(label, code)
        longest_language_width = max(
            language_combo.fontMetrics().horizontalAdvance(label)
            for _code, label in LANGUAGES
        )
        language_combo_width = longest_language_width + 76
        language_combo.setFixedWidth(language_combo_width)
        language_combo.view().setMinimumWidth(language_combo_width)
        language_combo.view().setTextElideMode(Qt.TextElideMode.ElideNone)
        language_index = language_combo.findData(language)
        language_combo.setCurrentIndex(max(language_index, 0))

        header_row.addWidget(theme_button)
        header_row.addWidget(guide_button)
        header_row.addWidget(language_combo)

        return cls(
            header_row=header_row,
            header_logo_label=header_logo_label,
            header_label=header_label,
            tagline_label=tagline_label,
            version_button=version_button,
            author_label=author_label,
            theme_button=theme_button,
            guide_button=guide_button,
            language_combo=language_combo,
        )
