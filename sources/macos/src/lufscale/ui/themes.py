"""Feuilles de style sombre et claire de l’interface Qt."""

from __future__ import annotations

import re


STYLE_SHEET = """
QWidget {
    color: #e6edf4;
    font-family: "SF Pro Text", "Helvetica Neue", "Segoe UI",
        "Noto Sans Devanagari", "Noto Sans SC", "Noto Sans JP", sans-serif;
    font-size: 13px;
}
QMainWindow {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #252b32,
        stop: 0.18 #20262c,
        stop: 1 #171c21
    );
}
QScrollArea#mainScroll {
    border: none;
    background: transparent;
}
QWidget#mainContent {
    background: transparent;
}
QFrame#panel {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #343b43,
        stop: 0.08 #30373f,
        stop: 1 #252b32
    );
    border: 1px solid #4c5865;
    border-top-color: #5b6774;
    border-bottom-color: #14191e;
    border-radius: 8px;
}
QFrame#panel QLabel,
QFrame#panel QCheckBox {
    background: transparent;
}
QFrame#panel[role="settings"] {
    /* A single neutral stroke avoids the asymmetric bevel that was much more
       visible above the option lamps in the dark theme than in the light one. */
    border: 1px solid #4c5865;
}
QFrame#panel[role="loudnessComparison"] {
    /* Its box already shares the journal's lower coordinate.  A neutral
       bottom stroke makes that common edge visible instead of hiding it in
       the former near-black bevel. */
    border-bottom-color: #4c5865;
}
QFrame#compactDestination {
    background: #20272e;
    border: 1px solid #3f4a55;
    border-radius: 7px;
}
QFrame#compactDestination QLabel {
    background: transparent;
}
QFrame#compactDestination QLineEdit#pathLabel {
    color: #dce5ed;
    background: #12171c;
    border: 1px solid #566574;
    border-radius: 5px;
    padding: 3px 7px;
    selection-color: #ffffff;
    selection-background-color: #245f88;
}
QFrame#compactDestination QLineEdit#pathLabel:hover {
    border-color: #68a9d3;
}
QFrame#compactDestination QLineEdit#pathLabel:focus {
    border: 2px solid #3da9ef;
    padding: 2px 6px;
}
QLabel#header {
    font-size: 27px;
    font-weight: 700;
    color: #f2f6fa;
}
QLabel#headerTagline {
    font-size: 13.5px;
    font-weight: 700;
    color: #f2f6fa;
}
QLabel#author {
    font-size: 11px;
    font-weight: 700;
    color: #f2f6fa;
}
QLabel#description {
    color: #aab6c3;
    background: #19242d;
    border: 1px solid #3d596d;
    border-radius: 6px;
    padding: 5px 9px;
    font-size: 13px;
}
QPushButton#versionButton:enabled {
    color: #e8eef4;
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #3c4752,
        stop: 1 #29313a
    );
    border: 1px solid #5e6c7b;
    border-bottom-color: #171d22;
    border-radius: 6px;
    padding: 4px 8px;
    font-size: 12px;
    font-weight: 600;
}
QPushButton#versionButton:enabled:hover {
    color: #ffffff;
    background: #3b5368;
    border-color: #65b7f0;
}
QFrame#dropArea {
    border: 2px dashed #4e91bd;
    border-radius: 10px;
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #252d35,
        stop: 1 #1d242b
    );
}
QFrame#dropArea[dragActive="true"] {
    border-color: #40b5ff;
    background: #23384a;
}
QFrame#dropArea QLabel {
    background: transparent;
}
QLabel#dropTitle {
    font-size: 17px;
    font-weight: 600;
    color: #7cc8ff;
}
QLabel#dropSubtitle {
    color: #9dabb9;
    font-size: 12px;
}
QLabel#cpuTitle, QLabel#cpuValue, QLabel#elapsedTime, QLabel#etaTime,
QLabel#activityStatus {
    color: #aebac7;
    font-weight: 600;
    font-size: 12px;
}
QLabel#activityStatus {
    background: transparent;
    border: none;
    padding: 0;
}
QWidget#optionContainer {
    background: transparent;
}
QWidget#stackedOption {
    background: transparent;
}
QWidget#optionContainer QLabel,
QFrame#panel QCheckBox {
    font-size: 12px;
}
QWidget#settingsTabs {
    background: transparent;
}
QFrame#settingsOutline {
    background: #242b32;
    border: none;
}
QStackedWidget#settingsStack {
    background: transparent;
    border: none;
}
QWidget#settingsPage {
    background: transparent;
    border: none;
}
QWidget#optionStatusWidget,
QWidget#optionStatusIndicator {
    background: transparent;
}
QLabel#optionStatusLight {
    background: qradialgradient(
        cx: 0.34, cy: 0.26, radius: 0.84,
        fx: 0.30, fy: 0.20,
        stop: 0 #aab5bf,
        stop: 0.18 #66727d,
        stop: 0.62 #303943,
        stop: 1 #151a20
    );
    border: 1px solid #667584;
    border-top-color: #a1acb6;
    border-bottom-color: #10151a;
    border-radius: 7px;
}
QLabel#optionStatusLight[active="true"] {
    background: qradialgradient(
        cx: 0.34, cy: 0.24, radius: 0.86,
        fx: 0.29, fy: 0.18,
        stop: 0 #e7fff0,
        stop: 0.16 #a8f4c4,
        stop: 0.48 #54d58a,
        stop: 0.78 #23945a,
        stop: 1 #0e4b2d
    );
    border: 1px solid #9af2bd;
    border-top-color: #e4ffed;
    border-bottom-color: #17683f;
}
QLabel#optionStatusAcronym {
    color: #82909d;
    background: transparent;
    border: none;
    font-size: 8.5px;
    font-weight: 700;
    padding: 0;
}
QLabel#optionRowAcronym {
    color: #9fd5fb;
    background: #263744;
    border: 1px solid #4d87ad;
    border-radius: 5px;
    font-size: 9px;
    font-weight: 700;
    padding: 1px 4px;
}
QWidget#optionStatusIndicator:hover QLabel#optionStatusAcronym {
    color: #dce8f2;
}
QFrame[role="sources"] QPushButton[compact="true"] {
    font-size: 12px;
    font-weight: 600;
}
QLabel#panelTitle {
    font-size: 13px;
    font-weight: 650;
    color: #dce5ee;
}
QLabel#pathLabel {
    color: #d2dce6;
    background: #171c21;
    border: 1px solid #434e59;
    border-top-color: #11161a;
    border-radius: 6px;
    padding: 6px 9px;
}
QPushButton {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #46515c,
        stop: 0.12 #3c4650,
        stop: 1 #2b333b
    );
    color: #e8eef4;
    border: 1px solid #5a6673;
    border-top-color: #6b7784;
    border-bottom-color: #161b20;
    border-radius: 6px;
    padding: 7px 12px;
    font-weight: 550;
}
QPushButton:hover {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #53606d,
        stop: 1 #35414b
    );
    border-color: #6daed8;
}
QPushButton:pressed {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #252c33,
        stop: 1 #3a454f
    );
    padding-top: 8px;
    padding-bottom: 6px;
}
QPushButton[compact="true"] {
    min-height: 24px;
    padding: 3px 8px;
}
QPushButton[compact="true"]:pressed {
    padding-top: 4px;
    padding-bottom: 2px;
}
QPushButton#secondaryButton:enabled,
QPushButton#quietButton:enabled,
QPushButton#primaryOutlineButton:enabled,
QPushButton#utilityButton:enabled {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #424d58,
        stop: 1 #2c343c
    );
    color: #e8eef4;
    border-color: #566574;
    font-weight: 600;
}
QPushButton#secondaryButton:enabled:hover,
QPushButton#quietButton:enabled:hover,
QPushButton#primaryOutlineButton:enabled:hover,
QPushButton#utilityButton:enabled:hover {
    background: #3a5367;
    border-color: #63b5eb;
}
QPushButton#primaryButton:enabled {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #42b5ff,
        stop: 0.12 #2f9df4,
        stop: 1 #176dad
    );
    color: #e8eef4;
    border: 1px solid #58bdff;
    border-bottom-color: #0c3d61;
    font-weight: 650;
    padding-left: 22px;
    padding-right: 22px;
}
QPushButton#primaryButton:enabled:hover {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #62c3ff,
        stop: 1 #2289d2
    );
    border-color: #86d2ff;
}
QPushButton#primaryButton:enabled:pressed {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #155f94,
        stop: 1 #2b91d7
    );
}
QPushButton#dangerButton:enabled {
    background: #38282a;
    color: #e8eef4;
    border-color: #6f494d;
}
QPushButton#dangerButton:enabled:hover {
    background: #4a2e31;
    border-color: #a86066;
}
QListWidget, QTextEdit {
    background: #12171c;
    color: #dce5ed;
    border: 1px solid #414c57;
    border-top-color: #0c1014;
    border-radius: 7px;
    selection-background-color: #245f88;
    selection-color: #ffffff;
}
QFrame#sourceFieldFrame,
QFrame#logFieldFrame {
    background: #242d34;
    border: 1px solid #4c5b66;
    border-radius: 8px;
    padding: 1px;
}
QListWidget#sourceList {
    padding: 3px;
    alternate-background-color: #171d23;
    border: 1px solid #1b242b;
    border-radius: 6px;
}
QTextEdit#logBox {
    padding: 5px;
    font-family: "SF Mono", "Menlo", "Monaco", monospace;
    font-size: 12px;
    border: 1px solid #1b242b;
    border-radius: 6px;
}
QListWidget#sourceList:focus,
QTextEdit#logBox:focus {
    border-color: #517b91;
}
QTextEdit {
    font-weight: 400;
}
QScrollBar:vertical {
    background: #1a2026;
    width: 16px;
    margin: 2px;
    border: 1px solid #303943;
    border-radius: 7px;
}
QScrollBar::handle:vertical {
    background: #667584;
    min-height: 32px;
    border: 2px solid #1a2026;
    border-radius: 5px;
}
QScrollBar::handle:vertical:hover {
    background: #8091a2;
}
QScrollBar::handle:vertical:pressed {
    background: #3f9bd5;
}
QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0;
    background: transparent;
    border: none;
}
QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background: transparent;
}
QScrollBar:horizontal {
    background: #1a2026;
    height: 16px;
    margin: 2px;
    border: 1px solid #303943;
    border-radius: 7px;
}
QScrollBar::handle:horizontal {
    background: #667584;
    min-width: 32px;
    border: 2px solid #1a2026;
    border-radius: 5px;
}
QScrollBar::handle:horizontal:hover {
    background: #8091a2;
}
QScrollBar::handle:horizontal:pressed {
    background: #3f9bd5;
}
QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {
    width: 0;
    background: transparent;
    border: none;
}
QScrollBar::add-page:horizontal,
QScrollBar::sub-page:horizontal {
    background: transparent;
}
QAbstractScrollArea::corner {
    background: #1a2026;
    border: none;
}
QProgressBar {
    border: 1px solid #475360;
    border-top-color: #11161a;
    border-radius: 6px;
    background: #151a20;
    text-align: center;
    min-height: 24px;
    color: #e6edf4;
    font-weight: 600;
}
QProgressBar::chunk {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #48b9ff,
        stop: 0.18 #2f9df4,
        stop: 1 #176cae
    );
    border-radius: 5px;
}
QComboBox, QDoubleSpinBox, QSpinBox {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #242b32,
        stop: 1 #181e24
    );
    color: #e8eef4;
    border: 1px solid #56626e;
    border-top-color: #10151a;
    border-radius: 6px;
    min-height: 22px;
    padding: 3px 8px;
    selection-background-color: #286d9c;
    selection-color: #ffffff;
}
QComboBox:hover, QDoubleSpinBox:hover, QSpinBox:hover {
    border-color: #6d8da5;
}
QComboBox:focus, QDoubleSpinBox:focus, QSpinBox:focus {
    border: 1px solid #3da9ef;
    background: #1d2730;
}
QComboBox {
    padding-right: 34px;
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 28px;
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #3b4651,
        stop: 1 #28313a
    );
    border-left: 1px solid #53606d;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
}
QComboBox::drop-down:hover {
    background: #3c596e;
    border-left-color: #6fbcea;
}
QComboBox::down-arrow {
    width: 0;
    height: 0;
}
QWidget#stepControl {
    background: transparent;
}
QPushButton#stepButton:enabled {
    padding: 0;
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #46515c,
        stop: 1 #2a323a
    );
    color: #e8eef4;
    border: 1px solid #5a6876;
    border-bottom-color: #151a1f;
    border-radius: 6px;
    font-size: 16px;
    font-weight: 700;
}
QPushButton#stepButton:enabled:hover {
    background: #405769;
    border-color: #68b5e5;
}
QPushButton#stepButton:enabled:pressed {
    background: #24313b;
}
QPushButton#stepButton:disabled {
    padding: 0;
    background: #2c333a;
    color: #8793a0;
    border: 1px solid #46515c;
    border-bottom-color: #1b2025;
    border-radius: 6px;
    font-size: 16px;
    font-weight: 700;
}
QPushButton#helpButton:enabled {
    min-width: 22px;
    max-width: 22px;
    min-height: 22px;
    max-height: 22px;
    padding: 0;
    background: #263c4d;
    color: #8bd2ff;
    border: 1px solid #4e8bb2;
    border-radius: 11px;
    font-size: 12px;
    font-weight: 750;
}
QPushButton#helpButton:enabled:hover {
    background: #315872;
    color: #ffffff;
    border-color: #6cc5ff;
}
QPushButton#helpButton:enabled:pressed {
    background: #1c3445;
}
QComboBox QAbstractItemView {
    background: #20262c;
    color: #e5ecf3;
    border: 1px solid #596674;
    selection-background-color: #286d9c;
    selection-color: #ffffff;
    padding: 4px;
}
QCheckBox {
    min-height: 20px;
    spacing: 6px;
}
QCheckBox::indicator:unchecked {
    width: 15px;
    height: 15px;
    background: #171c21;
    border: 1px solid #788797;
    border-radius: 4px;
}
QCheckBox::indicator:unchecked:hover {
    background: #22313c;
    border: 2px solid #45aeef;
}
QCheckBox::indicator:unchecked:disabled {
    background: #242a30;
    border: 1px solid #53606c;
}
QCheckBox::indicator:checked {
    width: 15px;
    height: 15px;
    background: #2f9df4;
    border: 1px solid #72c7ff;
    border-radius: 4px;
}
QCheckBox::indicator:checked:!active {
    background: #397eae;
    border-color: #6f93ad;
}
QCheckBox::indicator:checked:disabled {
    background: #5d7289;
    border-color: #71869b;
}
QCheckBox:disabled {
    color: #87939f;
}
QStatusBar {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #262d34,
        stop: 1 #1a2026
    );
    color: #9eabb8;
    border-top: 1px solid #3d4752;
    padding-left: 8px;
    font-size: 12px;
}
QStatusBar::item {
    border: none;
}
QPushButton#websiteLink {
    color: #9eabb8;
    background: transparent;
    border: 1px solid transparent;
    border-radius: 3px;
    padding: 0 3px;
    margin: 0;
    min-width: 0;
    min-height: 0;
    font-size: 12px;
    font-weight: 400;
}
QPushButton#websiteLink:hover {
    color: #9eabb8;
    background: transparent;
}
QPushButton#websiteLink:pressed {
    color: #9eabb8;
    background: transparent;
}
QPushButton#websiteLink:focus {
    border-color: #9eabb8;
}
QMessageBox,
QDialog#applicationInfoDialog,
QDialog#completionSummaryDialog,
QDialog#issueListDialog {
    background-color: #303840;
    color: #f2f6fa;
    font-family: "Segoe UI", "Inter", "Noto Sans Devanagari",
        "Noto Sans SC", "Noto Sans JP", sans-serif;
    font-size: 13px;
    font-weight: 400;
}
QMessageBox,
QDialog#applicationInfoDialog {
    min-width: 380px;
}
QDialog#completionSummaryDialog {
    min-width: 220px;
}
QMessageBox QLabel,
QDialog#applicationInfoDialog QLabel#applicationInfoText,
QDialog#applicationInfoDialog QTextEdit#applicationInfoText,
QDialog#completionSummaryDialog QLabel#completionSummaryText {
    color: #f2f6fa;
    background-color: transparent;
    border: none;
    font-family: "Segoe UI", "Inter", "Noto Sans Devanagari",
        "Noto Sans SC", "Noto Sans JP", sans-serif;
    font-size: 13px;
    font-weight: 400;
    padding: 12px 8px 6px 8px;
}
QDialog#completionSummaryDialog QLabel#completionSummaryText {
    padding: 0;
    margin: 0;
}
QDialog#applicationInfoDialog QLabel#applicationInfoIcon,
QDialog#completionSummaryDialog QLabel#completionSummaryIcon {
    background-color: transparent;
    padding: 0;
}
QDialog#issueListDialog QTreeWidget#issueListTable {
    color: #dce5ed;
    background: #12171c;
    alternate-background-color: #171d23;
    border: 1px solid #414c57;
    selection-color: #ffffff;
    selection-background-color: #245f88;
}
QDialog#issueListDialog QTreeWidget#issueListTable::item {
    color: #dce5ed;
    background: transparent;
    min-height: 20px;
}
QDialog#issueListDialog QTreeWidget#issueListTable::item:selected {
    color: #ffffff;
    background: #245f88;
}
QDialog#issueListDialog QHeaderView::section {
    color: #e6edf4;
    background: #242a30;
    border: none;
    border-right: 1px solid #414c57;
    border-bottom: 1px solid #414c57;
    padding: 4px;
    font-weight: 600;
}
QMessageBox QPushButton:enabled,
QDialog#applicationInfoDialog QPushButton:enabled,
QDialog#completionSummaryDialog QPushButton:enabled,
QDialog#issueListDialog QPushButton:enabled {
    color: #e8eef4;
    background: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #4b5661,
        stop: 1 #353e47
    );
    border: 1px solid #697887;
    border-bottom-color: #222a31;
    min-width: 58px;
    min-height: 22px;
    padding: 7px 14px;
    font-family: "SF Pro Text", "Helvetica Neue", "Segoe UI", "Inter",
        "Noto Sans Devanagari", "Noto Sans SC", "Noto Sans JP",
        sans-serif;
    font-size: 13px;
    font-weight: 600;
}
QMessageBox QPushButton:enabled:hover,
QDialog#applicationInfoDialog QPushButton:enabled:hover,
QDialog#completionSummaryDialog QPushButton:enabled:hover,
QDialog#issueListDialog QPushButton:enabled:hover {
    background: #52606d;
    border-color: #7e90a1;
}
QMessageBox QPushButton:enabled:pressed,
QDialog#applicationInfoDialog QPushButton:enabled:pressed,
QDialog#completionSummaryDialog QPushButton:enabled:pressed,
QDialog#issueListDialog QPushButton:enabled:pressed {
    background: #293139;
    border-color: #1c2329;
}
QPushButton:disabled {
    color: #6f7a85;
    background: #242a30;
    border-color: #353d45;
}
"""


_LIGHT_THEME_COLORS = {
    "#e6edf4": "#303436",
    "#f2f6fa": "#24282a",
    "#252b32": "#ded8d0",
    "#20262c": "#d6d0c8",
    "#181e24": "#ebe6df",
    "#1d2730": "#eee9e2",
    "#171c21": "#cec7bd",
    "#343b43": "#e9e4dc",
    "#30373f": "#e2dcd4",
    "#4c5865": "#a69d92",
    "#5b6774": "#b8afa4",
    "#14191e": "#91887e",
    "#20272e": "#e3ddd5",
    "#3f4a55": "#aaa095",
    "#aab6c3": "#615f5a",
    "#b9dcfa": "#1d5f89",
    "#3c4752": "#e5dfd7",
    "#29313a": "#d9d2c9",
    "#5e6c7b": "#a69c90",
    "#171d22": "#91877c",
    "#3b5368": "#d8e7eb",
    "#65b7f0": "#3d96cc",
    "#252d35": "#e6e0d8",
    "#1d242b": "#dcd5cc",
    "#4e91bd": "#4a9aca",
    "#23384a": "#dceef9",
    "#7cc8ff": "#176d9f",
    "#9dabb9": "#68655f",
    "#aebac7": "#5b5954",
    "#9fd5fb": "#17658f",
    "#19242d": "#e7f3fa",
    "#3d596d": "#9cc1d6",
    "#242b32": "#e4ded6",
    "#46525e": "#aaa095",
    "#d9efff": "#174f73",
    "#2d353d": "#e8e2da",
    "#dce5ee": "#33373a",
    "#d2dce6": "#3b3e3f",
    "#434e59": "#a69c90",
    "#11161a": "#90867a",
    "#46515c": "#e8e2da",
    "#3c4650": "#ded7ce",
    "#2b333b": "#d2cbc1",
    "#2a323a": "#d9d2c8",
    "#e8eef4": "#303436",
    "#5a6673": "#a49a8e",
    "#6b7784": "#bbb1a5",
    "#161b20": "#8f8579",
    "#53606d": "#d6cfc5",
    "#56626e": "#a39a8f",
    "#6d8da5": "#6f9db8",
    "#3da9ef": "#258cc7",
    "#3c596e": "#d7eaf4",
    "#35414b": "#d4dde4",
    "#6daed8": "#3d96cc",
    "#252c33": "#c9c1b7",
    "#3a454f": "#e7e1d9",
    "#424d58": "#e5dfd7",
    "#2c343c": "#d8d1c7",
    "#d8e2eb": "#3a3e40",
    "#566371": "#a49a8f",
    "#3b4b58": "#dcebf4",
    "#68a9d3": "#3b91c4",
    "#343d46": "#e3ddd5",
    "#272e35": "#d7d0c6",
    "#aeb9c5": "#65625d",
    "#384550": "#ddd8d0",
    "#f0f5fa": "#2d3335",
    "#607a90": "#719cb8",
    "#344a5d": "#e1eef6",
    "#263744": "#cfe1ec",
    "#81caff": "#146d9f",
    "#4d87ad": "#6da6c8",
    "#315269": "#d4e9f5",
    "#c7e4fa": "#235b7e",
    "#566574": "#9cabb7",
    "#3a5367": "#d7eaf5",
    "#63b5eb": "#3692ca",
    "#6f7a85": "#62615d",
    "#242a30": "#ddd7cf",
    "#353d45": "#b7aea3",
    "#38282a": "#faeeee",
    "#e0a1a1": "#9b454b",
    "#6f494d": "#c99094",
    "#4a2e31": "#f4dfe0",
    "#a86066": "#b9696f",
    "#12171c": "#d9d1c7",
    "#dce5ed": "#303638",
    "#414c57": "#9e958a",
    "#0c1014": "#8f8579",
    "#245f88": "#8cc8ed",
    "#242d34": "#ddd7cf",
    "#4c5b66": "#a39a8f",
    "#1b242b": "#b7aea3",
    "#171d23": "#e7e1d9",
    "#517b91": "#478fb8",
    "#1a2026": "#d5cec4",
    "#303943": "#afa69b",
    "#667584": "#988f84",
    "#151a20": "#ddd7cf",
    "#10151a": "#aaa095",
    "#222a31": "#bdb5aa",
    "#3b4651": "#e6e0d8",
    "#28313a": "#d7d0c7",
    "#d9e9f6": "#273a49",
    "#5a6876": "#a5b2bd",
    "#151a1f": "#8e9aa4",
    "#405769": "#d7e8f2",
    "#68b5e5": "#3c95c9",
    "#24313b": "#ccd8df",
    "#687581": "#8b99a4",
    "#343c44": "#bac4cc",
    "#263c4d": "#e1eff7",
    "#8bd2ff": "#176d9e",
    "#4e8bb2": "#76a9c7",
    "#315872": "#d3e9f5",
    "#1c3445": "#c7dce8",
    "#e5ecf3": "#26343e",
    "#596674": "#a5b2bd",
    "#286d9c": "#8dc8eb",
    "#788797": "#929faa",
    "#22313c": "#e4edf2",
    "#45aeef": "#258bc6",
    "#53606c": "#a6b2bc",
    "#397eae": "#3a94c8",
    "#6f93ad": "#7ba4be",
    "#5d7289": "#9eb0bf",
    "#71869b": "#9cafbe",
    "#87939f": "#596167",
    "#262d34": "#ddd6ce",
    "#9eabb8": "#615f5a",
    "#3d4752": "#aaa195",
    "#5f9fc8": "#3b7fa7",
    "#303840": "#e7e1da",
    "#4b5661": "#e9e4dc",
    "#353e47": "#dcd5cc",
    "#697887": "#a69d92",
    "#52606d": "#e2dcd4",
    "#7e90a1": "#978e83",
    "#1c2329": "#9f968b",
}


def build_light_style_sheet(style_sheet: str) -> str:
    return re.sub(
        r"#[0-9a-fA-F]{6}",
        lambda match: _LIGHT_THEME_COLORS.get(
            match.group(0).lower(),
            match.group(0),
        ),
        style_sheet,
    )


LIGHT_STYLE_SHEET = build_light_style_sheet(STYLE_SHEET) + """
QPushButton#stepButton:disabled {
    background: #c9c2b8;
    color: #626b72;
    border: 1px solid #a79e94;
    border-bottom-color: #8f877e;
    border-radius: 6px;
}
QLabel#optionStatusAcronym {
    color: #34434d;
}
QWidget#optionStatusIndicator:hover QLabel#optionStatusAcronym {
    color: #174f73;
}
QLabel#optionRowAcronym {
    color: #174f73;
    background: #d7eaf4;
    border-color: #6da6c8;
}
"""
