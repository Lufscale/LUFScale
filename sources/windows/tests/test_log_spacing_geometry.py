from __future__ import annotations

import ast
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).parents[1]
EXECUTION_PATH = PROJECT_ROOT / "src/lufscale/ui/execution.py"
OVERLAY_PATH = PROJECT_ROOT / "src/lufscale/ui/widgets/processing_log.py"


def numeric_constants(source: str) -> dict[str, float]:
    tree = ast.parse(source)
    values: dict[str, float] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            continue
        if isinstance(node.value, ast.Constant) and isinstance(
            node.value.value,
            (int, float),
        ):
            values[target.id] = float(node.value.value)
    return values


class UniversalLogSpacingGeometryTests(unittest.TestCase):
    def test_every_lufs_range_is_native_inverse_text(self) -> None:
        source = EXECUTION_PATH.read_text(encoding="utf-8")
        values = numeric_constants(source)
        self.assertEqual(values["LOG_HIGHLIGHT_GAP_PX"], 1.0)
        self.assertEqual(values["LOG_DEVANAGARI_WINDOWS_11_GAP_PX"], 3.0)
        self.assertEqual(values["WINDOWS_11_MINIMUM_BUILD"], 22000.0)
        self.assertEqual(values["LOG_TEXT_FONT_SIZE_PX"], 12.0)
        self.assertEqual(values["LOG_TEXT_FONT_WEIGHT"], 400.0)
        self.assertEqual(values["LOG_SCRIPT_FONT_SIZE_PX"], 11.0)
        self.assertEqual(values["LOG_SCRIPT_FONT_WEIGHT"], 600.0)
        self.assertEqual(values["LOG_LINE_HEIGHT_PX"], 16.0)
        self.assertEqual(values["LOG_JAPANESE_LINE_HEIGHT_PX"], 17.0)
        self.assertNotIn("LOG_JAPANESE_LUFS_LINE_HEIGHT_PX", source)
        for marker in (
            "def inverse_log_text_format(",
            "source_format: QTextCharFormat,",
            "inverse_format = QTextCharFormat(source_format)",
            "if transition_match is None:",
            'LOG_TEXT_FONT_FAMILY = "DejaVu Sans"',
            "inverse_format.setForeground(QBrush(QColor(background_color)))",
            "inverse_format.setBackground(QBrush(QColor(text_color)))",
            "surrounding_format = cursor.charFormat()",
            'f" {transition} ",',
            "inverse_log_text_format(",
            "surrounding_format,",
            'if self.owner.language == "hi" and is_windows_11_or_newer():',
            "transition_format.clearBackground()",
            "transition_format.setFontStyleStrategy(",
            "CONTROLLED_LOG_HIGHLIGHT_HEIGHT_PROPERTY",
            "QFont.StyleStrategy.NoFontMerging",
        ):
            self.assertIn(marker, source)
        self.assertEqual(
            source.count("QFont.StyleStrategy.NoFontMerging"),
            1,
        )
        windows_11_hindi_branch = source.split(
            'if self.owner.language == "hi" and is_windows_11_or_newer():',
            1,
        )[1].split("cursor.insertText(", 1)[0]
        self.assertIn(
            "transition_format.fontStyleStrategy()",
            windows_11_hindi_branch,
        )
        for font_mutator in (
            "setFontFamilies",
            "setFontFamily",
            "setFontPixelSize",
            "setFontPointSize",
            "setFontWeight",
        ):
            self.assertNotIn(font_mutator, windows_11_hindi_branch)
        self.assertNotIn(
            'if self.owner.language != "ja" or transition_match is None:',
            source,
        )
        inverse_function = source.split("def inverse_log_text_format", 1)[1].split(
            "def log_content_line_height_px", 1
        )[0]
        self.assertNotIn("setFont", inverse_function)
        self.assertNotIn("QFont", inverse_function)
        self.assertNotIn("LOG_BADGE_FONT_", source)
        self.assertNotIn("LOG_BADGE_SUBPIXEL_WEIGHT_OFFSET_PX", source)
        for bitmap_marker in (
            "QImage",
            "QPainter",
            "QTextImageFormat",
            "cursor.insertImage(",
            "ImageResource",
            "devicePixelRatioF()",
            "make_lufs_badge_image",
        ):
            self.assertNotIn(bitmap_marker, source)

    def test_windows_11_hindi_highlight_has_fixed_viewport_geometry(self) -> None:
        overlay = OVERLAY_PATH.read_text(encoding="utf-8")
        results = (
            PROJECT_ROOT / "src/lufscale/ui/panels/results.py"
        ).read_text(encoding="utf-8")
        for marker in (
            "class ProcessingLogTextEdit(QTextEdit):",
            "super().paintEvent(event)",
            "self._paint_controlled_highlights(event.rect())",
            "natural_cursor_rect.center().y() - fixed_height / 2.0",
            "painter.fillRect(highlight_rect, fill_color)",
            "painter.drawText(",
            "QFontMetricsF(font, self.viewport())",
        ):
            self.assertIn(marker, overlay)
        self.assertIn("log_box = ProcessingLogTextEdit()", results)
        for bitmap_marker in (
            "QImage",
            "QPixmap",
            "QTextImageFormat",
            "drawPixmap",
            "drawImage",
        ):
            self.assertNotIn(bitmap_marker, overlay)

    def test_separator_is_a_real_block_margin_outside_native_text(self) -> None:
        source = EXECUTION_PATH.read_text(encoding="utf-8")
        self.assertNotIn("def log_line_bottom_margin_px", source)
        for marker in (
            "def log_content_line_height_px(",
            "def is_windows_11_or_newer() -> bool:",
            "sys.getwindowsversion().build >= WINDOWS_11_MINIMUM_BUILD",
            "def log_highlight_gap_px(",
            'uses_devanagari = language == "hi" or DEVANAGARI_LOG_PATTERN.search(message)',
            "return LOG_DEVANAGARI_WINDOWS_11_GAP_PX",
            "log_highlight_gap_px(message, language)",
            "log_highlight_gap_px(message, self.owner.language)",
            "log_content_line_height_px(message, self.owner.language)",
            "QTextBlockFormat.LineHeightTypes.FixedHeight.value",
        ):
            self.assertIn(marker, source)


if __name__ == "__main__":
    unittest.main()
