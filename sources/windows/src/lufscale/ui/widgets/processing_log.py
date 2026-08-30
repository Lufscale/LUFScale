"""Journal de traitement avec surlignages à géométrie contrôlée."""

from __future__ import annotations

from PySide6.QtCore import QPoint, QPointF, QRectF
from PySide6.QtGui import QColor, QFontMetricsF, QPainter, QTextCursor, QTextFormat
from PySide6.QtWidgets import QTextEdit


_USER_PROPERTY_BASE = QTextFormat.Property.UserProperty.value + 211200
CONTROLLED_LOG_HIGHLIGHT_PROPERTY = _USER_PROPERTY_BASE
CONTROLLED_LOG_HIGHLIGHT_FILL_PROPERTY = _USER_PROPERTY_BASE + 1
CONTROLLED_LOG_HIGHLIGHT_TEXT_PROPERTY = _USER_PROPERTY_BASE + 2
CONTROLLED_LOG_HIGHLIGHT_HEIGHT_PROPERTY = _USER_PROPERTY_BASE + 3


class ProcessingLogTextEdit(QTextEdit):
    """Paint selected native-text ranges without platform font-box overflow."""

    def paintEvent(self, event) -> None:
        super().paintEvent(event)
        self._paint_controlled_highlights(event.rect())

    def _paint_controlled_highlights(self, dirty_rect) -> None:
        document = self.document()
        selection = self.textCursor()
        if selection.hasSelection():
            selection_start = min(selection.position(), selection.anchor())
            selection_end = max(selection.position(), selection.anchor())
        else:
            selection_start = selection_end = -1

        painter = QPainter(self.viewport())
        painter.setClipRect(dirty_rect)
        try:
            top_cursor = self.cursorForPosition(
                QPoint(0, max(0, dirty_rect.top()))
            )
            bottom_cursor = self.cursorForPosition(
                QPoint(
                    max(0, self.viewport().width() - 1),
                    min(self.viewport().height() - 1, dirty_rect.bottom()),
                )
            )
            block = top_cursor.block()
            final_block_position = bottom_cursor.block().position()
            while block.isValid():
                layout = block.layout()
                if layout is None or layout.lineCount() == 0:
                    block = block.next()
                    continue

                iterator = block.begin()
                while not iterator.atEnd():
                    fragment = iterator.fragment()
                    iterator += 1
                    if not fragment.isValid():
                        continue
                    text_format = fragment.charFormat()
                    if not bool(
                        text_format.property(
                            CONTROLLED_LOG_HIGHLIGHT_PROPERTY
                        )
                    ):
                        continue

                    fragment_start = fragment.position()
                    fragment_end = fragment_start + fragment.length()
                    if (
                        selection_start >= 0
                        and selection_start < fragment_end
                        and fragment_start < selection_end
                    ):
                        # Let Qt show its normal selection colours so copying
                        # the native document text remains clear and complete.
                        continue

                    self._paint_fragment_highlight(
                        painter,
                        block,
                        layout,
                        fragment,
                        text_format,
                        dirty_rect,
                    )
                if block.position() >= final_block_position:
                    break
                block = block.next()
        finally:
            painter.end()

    def _paint_fragment_highlight(
        self,
        painter: QPainter,
        block,
        layout,
        fragment,
        text_format,
        dirty_rect,
    ) -> None:
        relative_start = fragment.position() - block.position()
        relative_end = relative_start + fragment.length()
        block_text = block.text()
        fixed_height = float(
            text_format.property(CONTROLLED_LOG_HIGHLIGHT_HEIGHT_PROPERTY)
        )
        fill_color = QColor(
            text_format.property(CONTROLLED_LOG_HIGHLIGHT_FILL_PROPERTY)
        )
        text_color = QColor(
            text_format.property(CONTROLLED_LOG_HIGHLIGHT_TEXT_PROPERTY)
        )

        first_line = layout.lineAt(0)
        block_cursor = QTextCursor(block)
        block_cursor_rect = self.cursorRect(block_cursor)
        layout_origin_x = (
            block_cursor_rect.left()
            - first_line.cursorToX(first_line.textStart())[0]
        )

        font = text_format.font()
        metrics = QFontMetricsF(font, self.viewport())
        painter.setFont(font)
        painter.setPen(text_color)

        for line_index in range(layout.lineCount()):
            line = layout.lineAt(line_index)
            line_start = line.textStart()
            line_end = line_start + line.textLength()
            segment_start = max(relative_start, line_start)
            segment_end = min(relative_end, line_end)
            if segment_start >= segment_end:
                continue

            absolute_segment_start = block.position() + segment_start
            segment_cursor = QTextCursor(self.document())
            segment_cursor.setPosition(absolute_segment_start)
            natural_cursor_rect = self.cursorRect(segment_cursor)
            top = natural_cursor_rect.center().y() - fixed_height / 2.0
            left = layout_origin_x + line.cursorToX(segment_start)[0]
            right = layout_origin_x + line.cursorToX(segment_end)[0]
            highlight_rect = QRectF(
                min(left, right),
                top,
                abs(right - left),
                fixed_height,
            )
            if not highlight_rect.intersects(QRectF(dirty_rect)):
                continue

            painter.fillRect(highlight_rect, fill_color)
            baseline = (
                highlight_rect.top()
                + (highlight_rect.height() - metrics.height()) / 2.0
                + metrics.ascent()
            )
            segment_text = block_text[segment_start:segment_end]
            painter.drawText(
                QPointF(highlight_rect.left(), baseline),
                segment_text,
            )


__all__ = [
    "CONTROLLED_LOG_HIGHLIGHT_FILL_PROPERTY",
    "CONTROLLED_LOG_HIGHLIGHT_HEIGHT_PROPERTY",
    "CONTROLLED_LOG_HIGHLIGHT_PROPERTY",
    "CONTROLLED_LOG_HIGHLIGHT_TEXT_PROPERTY",
    "ProcessingLogTextEdit",
]
