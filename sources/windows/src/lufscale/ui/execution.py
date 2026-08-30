"""Présentation de l'exécution et état temporel de la fenêtre principale."""

from __future__ import annotations

import html
import re
import sys
import time
from datetime import datetime, timedelta
from typing import Any, Callable

from PySide6.QtCore import QTimer
from PySide6.QtGui import (
    QBrush,
    QColor,
    QFont,
    QTextBlockFormat,
    QTextCharFormat,
    QTextCursor,
)

from ..processing.metrics import (
    format_24_hour_duration,
    format_elapsed_clock,
)
from ..processing.runtime import sample_cpu_percent
from .execution_state import ExecutionProgressState, ProcessingIssue
from .widgets.processing_log import (
    CONTROLLED_LOG_HIGHLIGHT_FILL_PROPERTY,
    CONTROLLED_LOG_HIGHLIGHT_HEIGHT_PROPERTY,
    CONTROLLED_LOG_HIGHLIGHT_PROPERTY,
    CONTROLLED_LOG_HIGHLIGHT_TEXT_PROPERTY,
)


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
LOG_TEXT_FONT_FAMILY = "DejaVu Sans"
LOG_TEXT_FONT_SIZE_PX = 12
LOG_TEXT_FONT_WEIGHT = 400
LOG_LINE_HEIGHT_PX = 16.0
# Keep the separator outside the text line. LUFS transitions are native text,
# not bitmap badges, so Windows uses exactly the same glyph renderer as it does
# for the text immediately before and after the highlighted range.
LOG_SCRIPT_FONT_SIZE_PX = 11
LOG_SCRIPT_FONT_WEIGHT = 600
LOG_KOREAN_LINE_HEIGHT_PX = 17.0
LOG_CHINESE_LINE_HEIGHT_PX = 19.0
LOG_HIGHLIGHT_GAP_PX = 1.0
LOG_JAPANESE_LINE_HEIGHT_PX = 17.0
LOG_DEVANAGARI_LINE_HEIGHT_PX = 20.0
LOG_DEVANAGARI_WINDOWS_11_GAP_PX = 3.0
WINDOWS_11_MINIMUM_BUILD = 22000
LOG_LANGUAGE_LINE_HEIGHTS_PX = {
    "ko": LOG_KOREAN_LINE_HEIGHT_PX,
    "zh": LOG_CHINESE_LINE_HEIGHT_PX,
    "ja": LOG_JAPANESE_LINE_HEIGHT_PX,
    "hi": LOG_DEVANAGARI_LINE_HEIGHT_PX,
}
JAPANESE_LOG_PATTERN = re.compile(r"[\u3040-\u30ff]")
KOREAN_LOG_PATTERN = re.compile(
    r"[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]"
)
HAN_LOG_PATTERN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
DEVANAGARI_LOG_PATTERN = re.compile(r"[\u0900-\u097f\ua8e0-\ua8ff]")
JAPANESE_LOG_RUN_PATTERN = re.compile(
    r"[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff]+"
)
KOREAN_LOG_RUN_PATTERN = re.compile(
    r"[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]+"
)
LOG_SCRIPT_RUN_FORMATS = {
    "ja": (JAPANESE_LOG_RUN_PATTERN, "Noto Sans JP Thin"),
    "ko": (KOREAN_LOG_RUN_PATTERN, "Noto Sans KR Thin"),
}
LUFS_TRANSITION_PATTERN = re.compile(
    r"(?P<transition>[+\-]?\d+(?:[.,]\d+)?\s*→\s*"
    r"[+\-]?\d+(?:[.,]\d+)?\s+LUFS)"
)


def log_line_height_px(message: str, language: str = "") -> float:
    """Match the one-pixel French highlight gap in every bundled script."""
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


def is_windows_11_or_newer() -> bool:
    """Identify the Windows text engine that expands Devanagari descenders."""
    if sys.platform != "win32" or not hasattr(sys, "getwindowsversion"):
        return False
    try:
        return sys.getwindowsversion().build >= WINDOWS_11_MINIMUM_BUILD
    except (AttributeError, TypeError, ValueError):
        return False


def log_highlight_gap_px(message: str, language: str = "") -> float:
    """Keep the native Hindi highlight clear of the following line on Win11."""
    uses_devanagari = language == "hi" or DEVANAGARI_LOG_PATTERN.search(message)
    if uses_devanagari and is_windows_11_or_newer():
        return LOG_DEVANAGARI_WINDOWS_11_GAP_PX
    return LOG_HIGHLIGHT_GAP_PX


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


def format_log_message_html(
    message: str,
    language: str = "",
) -> str:
    safe_message = compact_script_runs_html(html.escape(message), language)
    return safe_message.replace("\n", "<br>")


def compact_script_runs_html(safe_message: str, language: str) -> str:
    """Keep Japanese and Korean glyphs compact but clearly legible."""
    script_format = LOG_SCRIPT_RUN_FORMATS.get(language)
    if script_format is None:
        return safe_message
    pattern, font_family = script_format
    return pattern.sub(
        lambda match: (
            f'<span style="font-family:\'{font_family}\'; '
            f'font-size:{LOG_SCRIPT_FONT_SIZE_PX}px; '
            f'font-weight:{LOG_SCRIPT_FONT_WEIGHT};">'
            f"{match.group(0)}</span>"
        ),
        safe_message,
    )


def inverse_log_text_format(
    source_format: QTextCharFormat,
    text_color: str,
    background_color: str,
) -> QTextCharFormat:
    """Clone the adjacent native format and invert only its two colours."""
    inverse_format = QTextCharFormat(source_format)
    inverse_format.setForeground(QBrush(QColor(background_color)))
    inverse_format.setBackground(QBrush(QColor(text_color)))
    return inverse_format


def log_content_line_height_px(message: str, language: str = "") -> float:
    """Reserve the last pixel of each block outside its text layout."""
    return max(
        1.0,
        log_line_height_px(message, language)
        - log_highlight_gap_px(message, language),
    )


def format_log_text_fragment_html(
    text: str,
    color: str,
    language: str,
) -> str:
    """Escape and style a plain-text fragment around an inline LUFS badge."""
    safe_fragment = compact_script_runs_html(html.escape(text), language)
    return (
        f'<span style="color:{color}; '
        f'font-family:\'{LOG_TEXT_FONT_FAMILY}\'; '
        f'font-size:{LOG_TEXT_FONT_SIZE_PX}px; '
        f'font-weight:{LOG_TEXT_FONT_WEIGHT};">'
        f'{safe_fragment.replace(chr(10), "<br>")}</span>'
    )


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

    def _insert_log_message(
        self,
        cursor: QTextCursor,
        message: str,
        color: str,
    ) -> None:
        """Insert a line whose LUFS range is native inverse-colour text."""
        transition_match = LUFS_TRANSITION_PATTERN.search(message)
        if transition_match is None:
            safe_message = format_log_message_html(
                message,
                self.owner.language,
            )
            cursor.insertHtml(
                f'<span style="color:{color}; '
                f'font-family:\'{LOG_TEXT_FONT_FAMILY}\'; '
                f'font-size:{LOG_TEXT_FONT_SIZE_PX}px; '
                f'font-weight:{LOG_TEXT_FONT_WEIGHT};">'
                f"{safe_message}</span>"
            )
            return

        cursor.insertHtml(
            format_log_text_fragment_html(
                message[:transition_match.start()],
                color,
                self.owner.language,
            )
        )
        transition = transition_match.group("transition")
        background_color = self._active_log_background_color()
        surrounding_format = cursor.charFormat()
        if self.owner.language == "hi" and is_windows_11_or_newer():
            # DirectWrite does not clip QTextCharFormat backgrounds to the
            # fixed paragraph height when a Windows 11 Devanagari fallback run
            # expands its ascent/descent. Keep native document text, but mark
            # this Latin-only range for a fixed, centered viewport overlay.
            transition_format = QTextCharFormat(surrounding_format)
            transition_format.setForeground(
                QBrush(QColor(background_color))
            )
            transition_format.clearBackground()
            transition_format.setFontStyleStrategy(
                transition_format.fontStyleStrategy()
                | QFont.StyleStrategy.NoFontMerging
            )
            transition_format.setProperty(
                CONTROLLED_LOG_HIGHLIGHT_PROPERTY,
                True,
            )
            transition_format.setProperty(
                CONTROLLED_LOG_HIGHLIGHT_FILL_PROPERTY,
                QColor(color),
            )
            transition_format.setProperty(
                CONTROLLED_LOG_HIGHLIGHT_TEXT_PROPERTY,
                QColor(background_color),
            )
            transition_format.setProperty(
                CONTROLLED_LOG_HIGHLIGHT_HEIGHT_PROPERTY,
                log_content_line_height_px(message, self.owner.language),
            )
        else:
            transition_format = inverse_log_text_format(
                surrounding_format,
                color,
                background_color,
            )
        cursor.insertText(
            f" {transition} ",
            transition_format,
        )
        cursor.insertHtml(
            format_log_text_fragment_html(
                message[transition_match.end():],
                color,
                self.owner.language,
            )
        )

    def _render_log_entry(self, category: str, message: str) -> None:
        palette = self._active_log_palette()
        color = palette.get(category, palette["info"])
        # QTextBlockFormat.setLineHeight() expects the integer value of the
        # PySide enum. Reapply the format after insertHtml(), because an HTML
        # fragment inserted into the document's initial empty block can reset
        # that block's line-height properties.
        cursor = self.owner.log_box.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        block_format = QTextBlockFormat()
        block_format.setTopMargin(0.0)
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
    "ExecutionPresenter",
    "ExecutionProgressState",
    "ProcessingIssue",
    "LIGHT_LOG_COLORS",
    "LIGHT_LOG_BACKGROUND_COLOR",
    "LOG_BACKGROUND_COLOR",
    "LOG_COLORS",
    "format_log_message_html",
    "format_wall_clock_24h",
    "log_category_from_message",
    "log_content_line_height_px",
    "log_line_height_px",
]
