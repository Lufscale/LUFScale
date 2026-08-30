"""Présentation de l'exécution et état temporel de la fenêtre principale."""

from __future__ import annotations

import html
import re
import time
from datetime import datetime, timedelta
from typing import Any, Callable

from PySide6.QtCore import QPointF, QRectF, QSizeF, QTimer
from PySide6.QtGui import (
    QBrush,
    QColor,
    QFontMetricsF,
    QPainter,
    QPyTextObject,
    QTextBlockFormat,
    QTextCharFormat,
    QTextCursor,
    QTextDocument,
    QTextFormat,
)

from ..processing.metrics import (
    format_24_hour_duration,
    format_elapsed_clock,
)
from ..processing.runtime import sample_cpu_percent
from .execution_state import ExecutionProgressState, ProcessingIssue


LOG_COLORS = {
    "success": "#62c28f",
    "compliant": "#69b8d0",
    "warning": "#e1a75b",
    "error": "#df8585",
    "resumed": "#b69ae3",
    "skipped": "#9aa7b8",
    "cancelled": "#9aa7b8",
    "info": "#c7d1dc",
}
LIGHT_LOG_COLORS = {
    "success": "#0c663d",
    "compliant": "#246b83",
    "warning": "#81500d",
    "error": "#8f3741",
    "resumed": "#68458f",
    "skipped": "#39444c",
    "cancelled": "#39444c",
    "info": "#303c45",
}
LOG_BACKGROUND_COLOR = "#12171c"
LIGHT_LOG_BACKGROUND_COLOR = "#d9d1c7"
LOG_LINE_HEIGHT_PX = 16.0
LOG_DEVANAGARI_LINE_HEIGHT_PX = 19.0
LOG_JAPANESE_LINE_HEIGHT_PX = 16.0
LOG_JAPANESE_BADGE_HEIGHT_PX = 15.0
LOG_CJK_BADGE_RAISE_PX = 2.0
LOG_CHINESE_LINE_HEIGHT_PX = 16.0
LOG_KOREAN_LINE_HEIGHT_PX = 16.0
LOG_HIGHLIGHT_GAP_PX = 1.0
LOG_LANGUAGE_LINE_HEIGHTS_PX = {
    "hi": LOG_DEVANAGARI_LINE_HEIGHT_PX,
    "ja": LOG_JAPANESE_LINE_HEIGHT_PX,
    "zh": LOG_CHINESE_LINE_HEIGHT_PX,
    "ko": LOG_KOREAN_LINE_HEIGHT_PX,
}
JAPANESE_LOG_PATTERN = re.compile(r"[\u3040-\u30ff]")
KOREAN_LOG_PATTERN = re.compile(
    r"[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]"
)
HAN_LOG_PATTERN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
DEVANAGARI_LOG_PATTERN = re.compile(r"[\u0900-\u097f\ua8e0-\ua8ff]")
LUFS_TRANSITION_PATTERN = re.compile(
    r"(?P<transition>[+\-]?\d+(?:[.,]\d+)?\s*→\s*"
    r"[+\-]?\d+(?:[.,]\d+)?\s+LUFS)"
)
JAPANESE_LUFS_OBJECT_TYPE = int(QTextFormat.ObjectTypes.UserObject) + 1
JAPANESE_LUFS_TEXT_PROPERTY = int(QTextFormat.Property.UserProperty) + 1
JAPANESE_LUFS_TEXT_COLOR_PROPERTY = int(QTextFormat.Property.UserProperty) + 2
JAPANESE_LUFS_BACKGROUND_COLOR_PROPERTY = (
    int(QTextFormat.Property.UserProperty) + 3
)
OBJECT_REPLACEMENT_CHARACTER = "\ufffc"
def log_line_height_px(message: str, language: str = "") -> float:
    """Keep one dark separator pixel without clipping bundled scripts."""
    localized_height = LOG_LANGUAGE_LINE_HEIGHTS_PX.get(language)
    if localized_height is not None:
        return localized_height
    if JAPANESE_LOG_PATTERN.search(message):
        return LOG_JAPANESE_LINE_HEIGHT_PX
    if KOREAN_LOG_PATTERN.search(message):
        return LOG_KOREAN_LINE_HEIGHT_PX
    if DEVANAGARI_LOG_PATTERN.search(message):
        return LOG_DEVANAGARI_LINE_HEIGHT_PX
    if HAN_LOG_PATTERN.search(message):
        return LOG_CHINESE_LINE_HEIGHT_PX
    return LOG_LINE_HEIGHT_PX


def uses_cjk_lufs_badge(message: str, language: str = "") -> bool:
    """Use one fixed, baseline-aligned badge for Japanese and Chinese."""
    if language in {"ja", "zh"}:
        return True
    return bool(
        JAPANESE_LOG_PATTERN.search(message)
        or HAN_LOG_PATTERN.search(message)
    )


def log_highlight_gap_px(message: str, language: str = "") -> float:
    """Return the dark separator kept outside the painted text line."""
    del message, language
    return LOG_HIGHLIGHT_GAP_PX


def log_content_line_height_px(message: str, language: str = "") -> float:
    """Give bundled Asian fonts their full metrics before the separator."""
    line_height = log_line_height_px(message, language)
    if language in LOG_LANGUAGE_LINE_HEIGHTS_PX:
        return line_height
    if (
        JAPANESE_LOG_PATTERN.search(message)
        or KOREAN_LOG_PATTERN.search(message)
        or DEVANAGARI_LOG_PATTERN.search(message)
        or HAN_LOG_PATTERN.search(message)
    ):
        return line_height
    return max(
        1.0,
        line_height - log_highlight_gap_px(message, language),
    )


def format_wall_clock_24h(value: datetime) -> str:
    """Render a wall-clock value independently of the system locale."""
    return f"{value.hour:02d}:{value.minute:02d}"


def log_category_from_message(message: str) -> str:
    normalized = message.lstrip().upper()
    warning_prefixes = (
        "ALERTE",
        "WARNING",
        "WARNUNG",
        "AVISO",
        "WAARSCHUWING",
        "OSTRZEŻENIE",
        "ПРЕДУПРЕЖДЕНИЕ",
        "警告",
        "AVVISO",
        "चेतावनी",
    )
    error_prefixes = (
        "ERREUR",
        "ERROR",
        "FEHLER",
        "ERRORE",
        "FOUT",
        "BŁĄD",
        "ОШИБКА",
        "エラー",
        "ERRO",
        "错误",
        "त्रुटि",
    )
    if normalized.startswith(warning_prefixes):
        return "warning"
    if normalized.startswith(error_prefixes):
        return "error"
    return "info"


def format_log_message_html(message: str) -> str:
    return html.escape(message).replace("\n", "<br>")


def inverse_log_text_format(
    source_format: QTextCharFormat,
    text_color: str,
    background_color: str,
) -> QTextCharFormat:
    """Clone the adjacent native text and invert only its two colours."""
    inverse_format = QTextCharFormat(source_format)
    inverse_format.setForeground(QBrush(QColor(background_color)))
    inverse_format.setBackground(QBrush(QColor(text_color)))
    return inverse_format


def make_cjk_lufs_badge_format(
    source_format: QTextCharFormat,
    transition: str,
    text_color: str,
    background_color: str,
) -> QTextCharFormat:
    """Store a CJK LUFS badge without changing its native font."""
    inverse_format = inverse_log_text_format(
        source_format,
        text_color,
        background_color,
    )
    badge_format = QTextCharFormat(inverse_format)
    badge_format.setProperty(
        JAPANESE_LUFS_TEXT_PROPERTY,
        f" {transition} ",
    )
    badge_format.setProperty(
        JAPANESE_LUFS_TEXT_COLOR_PROPERTY,
        inverse_format.foreground().color(),
    )
    badge_format.setProperty(
        JAPANESE_LUFS_BACKGROUND_COLOR_PROPERTY,
        inverse_format.background().color(),
    )
    badge_format.clearForeground()
    badge_format.clearBackground()
    badge_format.setObjectType(JAPANESE_LUFS_OBJECT_TYPE)
    badge_format.setVerticalAlignment(
        QTextCharFormat.VerticalAlignment.AlignMiddle
    )
    return badge_format


class CjkLufsBadgeTextObject(QPyTextObject):
    """Paint a sharp 15 px CJK badge with the adjacent native font."""

    def intrinsicSize(
        self,
        document: QTextDocument,
        position: int,
        text_format: QTextFormat,
    ) -> QSizeF:
        del document, position
        char_format = text_format.toCharFormat()
        label = str(text_format.property(JAPANESE_LUFS_TEXT_PROPERTY))
        width = max(
            1.0,
            QFontMetricsF(char_format.font()).horizontalAdvance(label),
        )
        return QSizeF(width, LOG_JAPANESE_BADGE_HEIGHT_PX)

    def drawObject(
        self,
        painter: QPainter,
        rectangle: QRectF,
        document: QTextDocument,
        position: int,
        text_format: QTextFormat,
    ) -> None:
        del document, position
        char_format = text_format.toCharFormat()
        label = str(text_format.property(JAPANESE_LUFS_TEXT_PROPERTY))
        text_color = QColor(
            text_format.property(JAPANESE_LUFS_TEXT_COLOR_PROPERTY)
        )
        background_color = QColor(
            text_format.property(JAPANESE_LUFS_BACKGROUND_COLOR_PROPERTY)
        )
        metrics = QFontMetricsF(char_format.font())
        paint_rectangle = QRectF(rectangle)
        paint_rectangle.translate(0.0, -LOG_CJK_BADGE_RAISE_PX)
        baseline = (
            paint_rectangle.top()
            + (paint_rectangle.height() - metrics.height()) / 2.0
            + metrics.ascent()
        )
        painter.save()
        painter.fillRect(paint_rectangle, background_color)
        painter.setFont(char_format.font())
        painter.setPen(text_color)
        painter.drawText(QPointF(paint_rectangle.left(), baseline), label)
        painter.restore()


def format_log_text_fragment_html(
    text: str,
    color: str,
) -> str:
    safe_fragment = html.escape(text).replace("\n", "<br>")
    return f'<span style="color:{color}; font-weight:400;">{safe_fragment}</span>'


class ExecutionPresenter:
    """Relie l'état d'exécution aux widgets, sans piloter les workers."""

    def __init__(
        self,
        owner: Any,
        *,
        clock: Callable[[], float] = time.perf_counter,
        wall_clock: Callable[[], datetime] = datetime.now,
    ) -> None:
        self.owner = owner
        self.state = ExecutionProgressState()
        self._clock = clock
        self._wall_clock = wall_clock
        self._cjk_lufs_handler: CjkLufsBadgeTextObject | None = None
        self._cjk_lufs_handler_attempted = False
        self.cpu_timer = QTimer(owner)
        self.cpu_timer.setInterval(1000)
        self.cpu_timer.timeout.connect(self.update_cpu_usage)
        self.elapsed_timer = QTimer(owner)
        self.elapsed_timer.setInterval(1000)
        self.elapsed_timer.timeout.connect(self.update_elapsed_time)

    @property
    def conversion_paused(self) -> bool:
        return self.state.conversion_paused

    @property
    def elapsed_seconds(self) -> float:
        return self.state.elapsed_seconds

    @property
    def eta_total(self) -> int:
        return self.state.eta_total

    def start_cpu_monitoring(self, available: bool = True) -> None:
        self.owner.cpu_graph.clear()
        self.owner.cpu_value_label.setText("")
        if not available:
            return
        sample_cpu_percent()
        self.cpu_timer.start()

    def update_cpu_usage(self) -> None:
        value = sample_cpu_percent()
        if value is None:
            self.cpu_timer.stop()
            self.owner.cpu_value_label.setText("")
            return
        self.owner.cpu_graph.add_sample(value)
        self.owner.cpu_value_label.setText(f"{value:.0f} %")

    def stop_cpu_monitoring(self) -> None:
        self.cpu_timer.stop()

    def reset_for_run(self) -> None:
        self.owner.log_box.clear()
        self.state.reset_for_run()
        self.owner._refresh_issue_buttons()
        self.owner.progress_bar.setRange(0, 0)
        self.set_activity_counters(0, 0)

    def append_log_message(self, message: str) -> None:
        self._append_colored_log(
            log_category_from_message(message),
            message,
            count_activity=False,
        )

    def append_colored_log(self, category: str, message: str) -> None:
        self._append_colored_log(
            category,
            message,
            count_activity=True,
        )

    def add_issue(
        self,
        category: str,
        source: str,
        detail: str,
    ) -> ProcessingIssue | None:
        issue = self.state.add_issue(category, source, detail)
        if issue is not None:
            self.owner._refresh_issue_buttons()
        return issue

    def issues(self, category: str) -> tuple[ProcessingIssue, ...]:
        return tuple(self.state.issues.get(category, ()))

    def _append_colored_log(
        self,
        category: str,
        message: str,
        *,
        count_activity: bool,
    ) -> None:
        if count_activity and not message.startswith("  "):
            self.state.count_activity(category, message)
            self.set_activity_counters()
        self.state.log_entries.append((category, message))
        self._render_log_entry(category, message)

    def _active_log_palette(self) -> dict[str, str]:
        return (
            LIGHT_LOG_COLORS
            if self.owner.theme == "light"
            else LOG_COLORS
        )

    def _active_log_background_color(self) -> str:
        return (
            LIGHT_LOG_BACKGROUND_COLOR
            if self.owner.theme == "light"
            else LOG_BACKGROUND_COLOR
        )

    def _ensure_cjk_lufs_handler(self) -> bool:
        """Register the supported Qt 6.8 interface lazily and safely."""
        if self._cjk_lufs_handler is not None:
            return True
        if self._cjk_lufs_handler_attempted:
            return False
        self._cjk_lufs_handler_attempted = True
        try:
            handler = CjkLufsBadgeTextObject(self.owner.log_box)
            layout = self.owner.log_box.document().documentLayout()
            layout.registerHandler(JAPANESE_LUFS_OBJECT_TYPE, handler)
        except (AttributeError, RuntimeError, TypeError):
            return False
        self._cjk_lufs_handler = handler
        return True

    def _insert_log_message(
        self,
        cursor: QTextCursor,
        message: str,
        color: str,
    ) -> None:
        """Insert a line whose LUFS range is native inverse-colour text."""
        transition_match = LUFS_TRANSITION_PATTERN.search(message)
        if transition_match is None:
            cursor.insertHtml(
                f'<span style="color:{color}; font-weight:400;">'
                f"{format_log_message_html(message)}</span>"
            )
            return

        cursor.insertHtml(
            format_log_text_fragment_html(
                message[:transition_match.start()],
                color,
            )
        )
        transition = transition_match.group("transition")
        background_color = self._active_log_background_color()
        surrounding_format = cursor.charFormat()
        if (
            uses_cjk_lufs_badge(message, self.owner.language)
            and self._ensure_cjk_lufs_handler()
        ):
            cursor.insertText(
                OBJECT_REPLACEMENT_CHARACTER,
                make_cjk_lufs_badge_format(
                    surrounding_format,
                    transition,
                    color,
                    background_color,
                ),
            )
        else:
            cursor.insertText(
                f" {transition} ",
                inverse_log_text_format(
                    surrounding_format,
                    color,
                    background_color,
                ),
            )
        cursor.insertHtml(
            format_log_text_fragment_html(
                message[transition_match.end():],
                color,
            )
        )

    def _render_log_entry(self, category: str, message: str) -> None:
        palette = self._active_log_palette()
        color = palette.get(category, palette["info"])
        cursor = self.owner.log_box.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        block_format = QTextBlockFormat()
        block_format.setTopMargin(0.0)
        if uses_cjk_lufs_badge(message, self.owner.language):
            block_format.setBottomMargin(0.0)
            block_format.setLineHeight(
                log_line_height_px(message, self.owner.language),
                QTextBlockFormat.LineHeightTypes.FixedHeight.value,
            )
        else:
            block_format.setBottomMargin(
                log_highlight_gap_px(message, self.owner.language)
            )
            block_format.setLineHeight(
                log_content_line_height_px(message, self.owner.language),
                QTextBlockFormat.LineHeightTypes.FixedHeight.value,
            )
        if not cursor.atStart():
            cursor.insertBlock(block_format)
        self._insert_log_message(cursor, message, color)
        cursor.setBlockFormat(block_format)
        self.owner.log_box.setTextCursor(cursor)
        self.owner.log_box.ensureCursorVisible()

    def rerender_log_entries(self) -> None:
        if not self.state.log_entries:
            return
        scroll_bar = self.owner.log_box.verticalScrollBar()
        previous_value = scroll_bar.value()
        was_at_end = previous_value >= scroll_bar.maximum() - 2
        entries = tuple(self.state.log_entries)
        self.owner.log_box.clear()
        for category, message in entries:
            self._render_log_entry(category, message)
        scroll_bar.setValue(
            scroll_bar.maximum() if was_at_end else previous_value
        )

    def set_elapsed_display(self, seconds: float) -> None:
        self.state.elapsed_seconds = max(0.0, seconds)
        self.owner.elapsed_label.setText(
            self.owner.t(
                "elapsed_time",
                duration=format_elapsed_clock(self.state.elapsed_seconds),
            )
        )

    def set_activity(self, key: str, **values: Any) -> None:
        self.state.activity_visible = True
        self.state.activity_key = key
        self.state.activity_values = dict(values)
        self.refresh_activity_display()

    def hide_activity(self) -> None:
        self.state.activity_visible = False
        for label in self.owner.activity_labels.values():
            label.clear()
            label.setVisible(False)

    def set_activity_counters(
        self,
        current: int | None = None,
        total: int | None = None,
    ) -> None:
        del current
        state = self.state
        self.set_activity(
            "activity_progress",
            total=max(0, state.eta_total if total is None else total),
            success=state.activity_success,
            warnings=state.activity_warnings,
            failed=state.activity_failed,
            skipped=state.activity_skipped,
            compliant=state.activity_compliant,
        )

    def refresh_activity_display(self) -> None:
        state = self.state
        if not state.activity_visible:
            for label in self.owner.activity_labels.values():
                label.clear()
                label.setVisible(False)
            return
        values = state.activity_values
        counts = {
            "activity_files": int(values.get("total", 0)),
            "activity_successes": int(values.get("success", 0)),
            "activity_warnings": int(values.get("warnings", 0)),
            "activity_errors": int(values.get("failed", 0)),
            "activity_skipped": int(values.get("skipped", 0)),
            "activity_compliant": int(values.get("compliant", 0)),
        }
        full_text = self.owner.t(state.activity_key, **values)
        for key, count in counts.items():
            label = self.owner.activity_labels[key]
            label.setText(self.owner.t(key, count=count))
            label.setAccessibleDescription(full_text)
            label.setVisible(True)

    def refresh_eta_display(self) -> None:
        state = self.state
        if state.eta_state == "complete":
            self.owner.eta_label.setText(
                self.owner.t(
                    "total_time",
                    duration=format_24_hour_duration(
                        state.elapsed_seconds
                    ),
                )
            )
        elif (
            state.eta_state == "estimate"
            and state.estimated_total_seconds is not None
        ):
            remaining_seconds = max(
                0.0,
                state.estimated_total_seconds - state.elapsed_seconds,
            )
            current_time = self._wall_clock()
            finish = current_time + timedelta(seconds=remaining_seconds)
            duration = format_24_hour_duration(
                state.estimated_total_seconds
            )
            finish_time = format_wall_clock_24h(finish)
            finish_day_offset = (finish.date() - current_time.date()).days
            if finish_day_offset > 0:
                self.owner.eta_label.setText(
                    self.owner.t(
                        "estimated_total_time_with_day_finish",
                        duration=duration,
                        time=finish_time,
                        days=finish_day_offset,
                    )
                )
            else:
                self.owner.eta_label.setText(
                    self.owner.t(
                        "estimated_total_time_with_finish",
                        duration=duration,
                        time=finish_time,
                    )
                )
        elif state.eta_state == "calculating":
            self.owner.eta_label.setText(
                self.owner.t("estimated_total_calculating")
            )
        else:
            self.owner.eta_label.setText(
                self.owner.t("estimated_total_unavailable")
            )

    def update_eta_estimate(self) -> None:
        self.state.update_eta_estimate(self._clock())
        self.refresh_eta_display()

    def start_elapsed_monitoring(self) -> None:
        self.state.start_elapsed_monitoring(self._clock())
        self.set_elapsed_display(0.0)
        self.refresh_eta_display()
        self.elapsed_timer.start()

    def update_elapsed_time(self) -> None:
        if self.state.conversion_started_at is None:
            return
        now = self._clock()
        self.set_elapsed_display(
            self.state.active_conversion_elapsed(now)
        )
        self.state.update_eta_estimate(now)
        self.refresh_eta_display()

    def stop_elapsed_monitoring(
        self,
        final_elapsed: float | None = None,
    ) -> None:
        self.elapsed_timer.stop()
        elapsed = self.state.stop_elapsed_monitoring(
            self._clock(),
            final_elapsed,
        )
        self.set_elapsed_display(elapsed)

    def scan_finished(self, total: int) -> None:
        self.owner.progress_bar.setFormat("%p%")
        self.owner.progress_bar.setRange(0, max(total, 1))
        self.owner.progress_bar.setValue(0)
        self.state.scan_finished(total)
        self.set_activity_counters(0, self.state.eta_total)
        self.refresh_eta_display()

    def estimate_calibration_started(
        self,
        completed: int,
        total: int,
        parallel_jobs: int,
    ) -> None:
        self.state.estimate_calibration_started(
            completed,
            total,
            parallel_jobs,
            self._clock(),
        )
        self.refresh_eta_display()

    def progress(self, current: int, total: int) -> None:
        self.owner.progress_bar.setFormat("%p%")
        self.owner.progress_bar.setRange(0, max(total, 1))
        self.owner.progress_bar.setValue(current)
        self.state.progress(current, total)
        self.set_activity_counters(current, total)
        self.update_eta_estimate()

    def pause(self) -> None:
        elapsed = self.state.pause(self._clock())
        self.set_elapsed_display(elapsed)
        self.elapsed_timer.stop()

    def resume(self) -> None:
        self.state.resume(self._clock())
        self.elapsed_timer.start()

    def cancel_pause(self) -> None:
        self.state.resume(self._clock())

    def finish(
        self,
        *,
        success: int,
        failed: int,
        skipped: int,
        warnings: int,
        compliant: int,
        cancelled: bool,
        elapsed: float,
    ) -> None:
        self.stop_cpu_monitoring()
        self.stop_elapsed_monitoring(elapsed)
        self.state.finish(
            success=success,
            failed=failed,
            skipped=skipped,
            warnings=warnings,
            compliant=compliant,
            cancelled=cancelled,
        )
        self.refresh_eta_display()
        # Keep the final counters visible until reset_for_run() initializes
        # the next batch.  This also makes completion and cancellation states
        # inspectable after the worker thread has been cleaned up.
        final_total = max(
            self.state.eta_total,
            success + failed + skipped,
        )
        self.set_activity_counters(total=final_total)

    def reset_pause(self) -> None:
        self.state.conversion_paused = False
        self.state.conversion_pause_started_at = None


__all__ = [
    "CjkLufsBadgeTextObject",
    "ExecutionPresenter",
    "ExecutionProgressState",
    "ProcessingIssue",
    "LIGHT_LOG_COLORS",
    "LIGHT_LOG_BACKGROUND_COLOR",
    "LOG_BACKGROUND_COLOR",
    "LOG_COLORS",
    "format_log_message_html",
    "format_wall_clock_24h",
    "inverse_log_text_format",
    "log_category_from_message",
    "log_content_line_height_px",
    "log_highlight_gap_px",
    "log_line_height_px",
    "make_cjk_lufs_badge_format",
    "uses_cjk_lufs_badge",
]
