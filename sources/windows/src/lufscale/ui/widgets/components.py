"""Widgets Qt autonomes partagés par l’interface LUFScale."""

from __future__ import annotations

import math
from typing import Any

from PySide6.QtCore import QRectF, QTimer, Qt, Signal
from PySide6.QtGui import (
    QColor,
    QDragEnterEvent,
    QDropEvent,
    QKeySequence,
    QPainter,
    QPainterPath,
    QPen,
    QRadialGradient,
)
from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QCheckBox,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QProxyStyle,
    QPushButton,
    QSizePolicy,
    QStyle,
    QStyleOptionButton,
    QStyleOptionViewItem,
    QStyledItemDelegate,
    QVBoxLayout,
    QWidget,
)

from ...i18n.loader import translate
from ..dialogs import show_application_information


class ExternalLinkButton(QPushButton):
    """Compact link-style button with an underline shown only on hover."""

    def __init__(self, text: str = "") -> None:
        super().__init__(text)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFlat(True)

    def _set_underlined(self, enabled: bool) -> None:
        link_font = self.font()
        link_font.setUnderline(enabled)
        self.setFont(link_font)

    def enterEvent(self, event: Any) -> None:
        self._set_underlined(True)
        super().enterEvent(event)

    def leaveEvent(self, event: Any) -> None:
        self._set_underlined(False)
        super().leaveEvent(event)


def framed_data_field(widget: QWidget, object_name: str) -> QFrame:
    """Place a dark data field inside a uniform two-level bezel."""
    frame = QFrame()
    frame.setObjectName(object_name)
    layout = QVBoxLayout(frame)
    layout.setContentsMargins(1, 1, 1, 1)
    layout.setSpacing(0)
    layout.addWidget(widget)
    return frame

class CpuUsageGraph(QWidget):
    def __init__(self, maximum_samples: int = 60) -> None:
        super().__init__()
        self.maximum_samples = max(2, maximum_samples)
        self.samples: list[float] = []
        self.light_theme = False
        self.setObjectName("cpuGraph")
        self.setFixedSize(150, 28)

    def set_light_theme(self, enabled: bool) -> None:
        self.light_theme = bool(enabled)
        self.update()

    def clear(self) -> None:
        self.samples.clear()
        self.update()

    def add_sample(self, value: float) -> None:
        self.samples.append(max(0.0, min(100.0, float(value))))
        if len(self.samples) > self.maximum_samples:
            del self.samples[: len(self.samples) - self.maximum_samples]
        self.update()

    def paintEvent(self, _event) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        graph_rect = self.rect().adjusted(1, 1, -1, -1)

        border_color = "#9f978d" if self.light_theme else "#566372"
        background_color = "#ddd7cf" if self.light_theme else "#151a20"
        grid_color = "#beb6ac" if self.light_theme else "#39434e"
        line_color = "#347fa4" if self.light_theme else "#35a7ff"
        painter.setPen(QPen(QColor(border_color), 1))
        painter.setBrush(QColor(background_color))
        painter.drawRoundedRect(graph_rect, 5, 5)

        grid_pen = QPen(QColor(grid_color), 1)
        grid_pen.setStyle(Qt.PenStyle.DashLine)
        painter.setPen(grid_pen)
        for fraction in (0.25, 0.5, 0.75):
            y = int(
                graph_rect.bottom() - graph_rect.height() * fraction
            )
            painter.drawLine(
                graph_rect.left() + 2,
                y,
                graph_rect.right() - 2,
                y,
            )

        if not self.samples:
            return

        left = graph_rect.left() + 2
        right = graph_rect.right() - 2
        top = graph_rect.top() + 2
        bottom = graph_rect.bottom() - 2
        usable_height = max(1, bottom - top)
        step = (
            (right - left) / max(1, self.maximum_samples - 1)
        )
        start_index = self.maximum_samples - len(self.samples)

        line_path = QPainterPath()
        for index, sample in enumerate(self.samples):
            x = left + (start_index + index) * step
            y = bottom - usable_height * sample / 100.0
            if index == 0:
                line_path.moveTo(x, y)
            else:
                line_path.lineTo(x, y)

        area_path = QPainterPath(line_path)
        area_path.lineTo(
            left + (start_index + len(self.samples) - 1) * step,
            bottom,
        )
        area_path.lineTo(left + start_index * step, bottom)
        area_path.closeSubpath()
        painter.fillPath(
            area_path,
            QColor(70, 139, 171, 52)
            if self.light_theme
            else QColor(47, 157, 244, 60),
        )
        painter.setPen(QPen(QColor(line_color), 2))
        painter.drawPath(line_path)

class LeftAlignedTabStyle(QProxyStyle):
    """Keep compact tab bars against the leading edge on every platform."""

    def styleHint(
        self,
        hint: QStyle.StyleHint,
        option=None,
        widget=None,
        return_data=None,
    ) -> int:
        if hint == QStyle.StyleHint.SH_TabBar_Alignment:
            return int(Qt.AlignmentFlag.AlignLeft)
        return super().styleHint(
            hint,
            option,
            widget,
            return_data,
        )

class ElidedLabel(QLabel):
    """Compact label that preserves the beginning and end of long details."""

    def __init__(self) -> None:
        super().__init__()
        self._full_text = ""

    def set_full_text(self, text: str) -> None:
        self._full_text = text
        self.setAccessibleDescription(text)
        self._refresh_elision()

    def full_text(self) -> str:
        return self._full_text

    def _refresh_elision(self) -> None:
        available = max(0, self.contentsRect().width() - 4)
        rendered = self.fontMetrics().elidedText(
            self._full_text,
            Qt.TextElideMode.ElideMiddle,
            available,
        )
        super().setText(rendered)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self._refresh_elision()


class OptionStatusLight(QWidget):
    """Paint a genuinely circular, slightly raised option-status light."""

    def __init__(self) -> None:
        super().__init__()
        self._active = False
        self.setObjectName("optionStatusLight")
        self.setFixedSize(13, 13)
        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground,
            True,
        )
        self.setAutoFillBackground(False)
        self.setProperty("active", False)

    def set_active(self, active: bool) -> None:
        active = bool(active)
        if active == self._active:
            return
        self._active = active
        self.setProperty("active", active)
        self.update()

    def is_active(self) -> bool:
        return self._active

    def paintEvent(self, _event) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        ellipse = self.rect().adjusted(1, 1, -1, -1)
        gradient = QRadialGradient(
            self.width() * 0.34,
            self.height() * 0.27,
            self.width() * 0.72,
            self.width() * 0.29,
            self.height() * 0.20,
        )
        if self._active:
            gradient.setColorAt(0.00, QColor("#f1fff5"))
            gradient.setColorAt(0.18, QColor("#a8f4c4"))
            gradient.setColorAt(0.53, QColor("#4fd184"))
            gradient.setColorAt(0.82, QColor("#218d55"))
            gradient.setColorAt(1.00, QColor("#0d492b"))
            border = QColor("#8ce7b0")
        else:
            gradient.setColorAt(0.00, QColor("#d3dbe1"))
            gradient.setColorAt(0.20, QColor("#7b8792"))
            gradient.setColorAt(0.60, QColor("#39434c"))
            gradient.setColorAt(1.00, QColor("#171c21"))
            border = QColor("#697783")
        painter.setPen(QPen(border, 1))
        painter.setBrush(gradient)
        painter.drawEllipse(ellipse)


class LoudnessComparison(QWidget):
    """Show scrolling per-file loudness histories before and after processing."""

    def __init__(
        self,
        tolerance: float = 0.60,
        maximum_samples: int = 36,
        half_range_lu: float = 6.0,
    ) -> None:
        super().__init__()
        self.before: float | None = None
        self.after: float | None = None
        self.target = -16.0
        self.maximum_samples = max(3, int(maximum_samples))
        self.half_range_lu = max(0.1, float(half_range_lu))
        # key, source, delivered output, display target, expected output
        self.samples: list[
            tuple[str, float, float | None, float, float | None]
        ] = []
        self.state = "waiting"
        self.replaygain_display = False
        self.tolerance = max(0.0, float(tolerance))
        self.light_theme = False
        self.decimal_comma = False
        self._scroll_progress = 1.0
        self._scroll_timer = QTimer(self)
        self._scroll_timer.setInterval(30)
        self._scroll_timer.timeout.connect(self._animate_scroll)
        self.texts = {
            "before": "Before",
            "after": "After",
            "replaygain_after": "Estimated RG playback",
            "replaygain_note": "Compatible player · audio unchanged",
            "target": "Target {value} LUFS",
            "waiting": "Waiting for a processed file",
            "needs_qc": "Enable quality control to compare",
            "not_applicable": "No before/after comparison for this operation",
            "analysis_only": "No output in analysis-only mode",
            "reached": "Target reached · difference {value} LU",
            "reduced": "Difference reduced by {value} LU",
            "unchanged": "Difference unchanged",
            "increased": "Difference increased by {value} LU",
        }
        self.setObjectName("loudnessComparison")
        # Fill the comparison panel down to its normal three-pixel margin.  At
        # 221 px, equal 7 px outer/inter-card gaps leave two 100 px cards.
        self.setFixedSize(270, 221)
        self.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed,
        )

    def set_light_theme(self, enabled: bool) -> None:
        self.light_theme = bool(enabled)
        self.update()

    def set_decimal_comma(self, enabled: bool) -> None:
        self.decimal_comma = bool(enabled)
        self.update()

    def set_texts(self, **texts: str) -> None:
        for key, value in texts.items():
            if key in self.texts:
                self.texts[key] = str(value)
        self.update()

    def reset(self, target: float, state: str = "waiting") -> None:
        self._scroll_timer.stop()
        self._scroll_progress = 1.0
        self.samples.clear()
        self.before = None
        self.after = None
        self.target = float(target)
        self.replaygain_display = state == "replaygain"
        self.state = "waiting" if self.replaygain_display else str(state)
        self.update()

    def set_values(
        self,
        sample_key: str,
        before: float,
        after: float,
        target: float,
        expected: float | None = None,
    ) -> None:
        expected_value = float(target if expected is None else expected)
        values = (
            str(sample_key),
            float(before),
            float(after),
            float(target),
            expected_value,
        )
        if not all(math.isfinite(value) for value in values[1:]):
            return
        had_samples = bool(self.samples)
        matching_index: int | None = None
        for index in range(len(self.samples) - 1, -1, -1):
            pending_key, _before, pending_after, _target, _expected = (
                self.samples[index]
            )
            if pending_key == values[0]:
                matching_index = index
                break
        if matching_index is None:
            self.samples.append(values)
        else:
            # ReplayGain publishes its synchronized playback estimate as soon
            # as the source measurement finishes.  The later report confirms
            # the same keyed result after metadata/QC; replace it in place so
            # neither graph advances twice for one file.
            self.samples[matching_index] = values
        if len(self.samples) > self.maximum_samples:
            del self.samples[: len(self.samples) - self.maximum_samples]
        _, self.before, self.after, self.target, _expected = values
        self.state = "measured"
        if had_samples and matching_index is None:
            self._scroll_progress = 0.0
            self._scroll_timer.start()
        else:
            self._scroll_progress = 1.0
        self.update()

    def set_analysis_value(
        self,
        sample_key: str,
        before: float,
        target: float,
        state: str = "analysis_only",
    ) -> None:
        values = (str(sample_key), float(before), float(target))
        if not all(math.isfinite(value) for value in values[1:]):
            return
        # A queued source signal can arrive just after its completed
        # comparison signal.  In that order the full keyed sample already
        # exists and must not be followed by a duplicate pending point.
        if any(
            sample[0] == values[0] and sample[2] is not None
            for sample in self.samples
        ):
            return
        had_samples = bool(self.samples)
        self.samples.append((values[0], values[1], None, values[2], None))
        if len(self.samples) > self.maximum_samples:
            del self.samples[: len(self.samples) - self.maximum_samples]
        self.before = values[1]
        self.after = None
        self.target = values[2]
        if state == "replaygain":
            self.replaygain_display = True
            self.state = "waiting"
        else:
            self.state = str(state)
        if had_samples:
            self._scroll_progress = 0.0
            self._scroll_timer.start()
        else:
            self._scroll_progress = 1.0
        self.update()

    def _animate_scroll(self) -> None:
        # Ease each newly completed file into the rightmost slot.  The slower
        # one-slot movement mirrors the CPU trace without making old results
        # drift away when no new measurement exists.
        self._scroll_progress = min(1.0, self._scroll_progress + 0.035)
        if self._scroll_progress >= 1.0:
            self._scroll_timer.stop()
        self.update()

    def _number(self, value: float, places: int = 2) -> str:
        rendered = f"{float(value):.{places}f}"
        return rendered.replace(".", ",") if self.decimal_comma else rendered

    def _sample_x_positions(self, rect: QRectF) -> list[float]:
        if not self.samples:
            return []
        step = rect.width() / max(1, self.maximum_samples - 1)
        start_slot = self.maximum_samples - len(self.samples)
        if self._scroll_timer.isActive():
            start_slot += 1.0 - self._scroll_progress
        return [
            rect.left() + (start_slot + index) * step
            for index in range(len(self.samples))
        ]

    @staticmethod
    def _line_path(
        x_positions: list[float],
        y_positions: list[float],
    ) -> QPainterPath:
        path = QPainterPath()
        for index, (x, y) in enumerate(zip(x_positions, y_positions)):
            if index == 0:
                path.moveTo(x, y)
            else:
                path.lineTo(x, y)
        return path

    @staticmethod
    def _bounded_y(value: float, low: float, high: float, rect: QRectF) -> float:
        if high <= low:
            return rect.center().y()
        ratio = max(0.0, min(1.0, (value - low) / (high - low)))
        return rect.bottom() - ratio * rect.height()

    def _draw_trace(
        self,
        painter: QPainter,
        rect: QRectF,
        values: list[float],
        low: float,
        high: float,
        color: QColor,
        baseline: float,
        x_positions: list[float] | None = None,
        pen_style: Qt.PenStyle = Qt.PenStyle.SolidLine,
        fill_area: bool = True,
    ) -> None:
        if not values:
            return
        if x_positions is None:
            x_positions = self._sample_x_positions(rect)
        y_positions = [
            self._bounded_y(value, low, high, rect) for value in values
        ]
        painter.save()
        painter.setClipRect(rect.adjusted(-2, -2, 2, 2))
        baseline_y = self._bounded_y(baseline, low, high, rect)
        if fill_area and len(x_positions) > 1:
            area_path = QPainterPath()
            area_path.moveTo(x_positions[0], baseline_y)
            for x, y in zip(x_positions, y_positions):
                area_path.lineTo(x, y)
            area_path.lineTo(x_positions[-1], baseline_y)
            area_path.closeSubpath()
            area_color = QColor(color)
            area_color.setAlpha(48 if self.light_theme else 58)
            painter.fillPath(area_path, area_color)
        trace_pen = QPen(color, 2.0)
        trace_pen.setStyle(pen_style)
        painter.setPen(trace_pen)
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawPath(self._line_path(x_positions, y_positions))
        painter.setBrush(color)
        painter.setPen(Qt.PenStyle.NoPen)
        for index, (x, y) in enumerate(zip(x_positions, y_positions)):
            if index == len(x_positions) - 1:
                halo = QColor(color)
                halo.setAlpha(70)
                painter.setBrush(halo)
                painter.drawEllipse(QRectF(x - 4.5, y - 4.5, 9.0, 9.0))
                painter.setBrush(color)
            painter.drawEllipse(QRectF(x - 2.0, y - 2.0, 4.0, 4.0))
        painter.restore()

    def paintEvent(self, _event) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        outer = self.rect().adjusted(1, 1, -1, -1)
        if self.light_theme:
            background = "#e4ded6"
            border = "#9f978d"
            card = "#f3eee8"
            card_border = "#b5aca2"
            primary = "#28323b"
            secondary = "#667078"
            grid_color = "#cbc3ba"
            before_color = "#684489"
            success_color = "#188552"
            warning_color = "#a15b16"
        else:
            background = "#151a20"
            border = "#55616f"
            card = "#20272e"
            card_border = "#46525e"
            primary = "#e5edf4"
            secondary = "#9fb0bf"
            grid_color = "#39434e"
            before_color = "#9a72bd"
            success_color = "#75e1a6"
            warning_color = "#ffc273"

        painter.setPen(QPen(QColor(border), 1))
        painter.setBrush(QColor(background))
        painter.drawRoundedRect(outer, 6, 6)

        card_x = 7
        card_width = self.width() - 14
        # With a 221 px widget, three equal 7 px gaps leave two cards of
        # exactly 100 px: 7 + 100 + 7 + 100 + 7 = 221.  The upper margin,
        # inter-card separation and lower margin are therefore identical.
        card_gap = 7
        card_top = 7
        card_bottom_margin = 7
        card_height = max(
            50,
            (
                self.height()
                - card_top
                - card_bottom_margin
                - card_gap
            )
            // 2,
        )
        before_y = card_top
        after_y = before_y + card_height + card_gap
        for y in (before_y, after_y):
            painter.setPen(QPen(QColor(card_border), 1))
            painter.setBrush(QColor(card))
            painter.drawRoundedRect(
                card_x,
                y,
                card_width,
                card_height,
                5,
                5,
            )

        caption_font = painter.font()
        caption_font.setPointSizeF(9.4)
        caption_font.setBold(True)
        painter.setFont(caption_font)
        painter.setPen(QColor(secondary))
        before_text = (
            f"{self._number(self.before)} LUFS"
            if self.before is not None
            else "—"
        )
        after_text = (
            f"{'≈ ' if self.replaygain_display else ''}"
            f"{self._number(self.after)} LUFS"
            if self.after is not None
            else "—"
        )
        for y, label, value in (
            (before_y, self.texts["before"], before_text),
            (
                after_y,
                (
                    self.texts["replaygain_after"]
                    if self.replaygain_display
                    else self.texts["after"]
                ),
                after_text,
            ),
        ):
            split = 0.60 if y == after_y and self.replaygain_display else 0.50
            label_width = int(card_width * split)
            label_font = painter.font()
            if y == after_y and self.replaygain_display:
                label_font.setPointSizeF(8.2)
            painter.setFont(label_font)
            painter.setPen(QColor(secondary))
            painter.drawText(
                card_x + 6,
                y + 2,
                label_width - 6,
                18,
                Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
                label,
            )
            painter.setFont(caption_font)
            painter.setPen(QColor(primary))
            painter.drawText(
                card_x + label_width,
                y + 2,
                card_width - label_width - 6,
                18,
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
                value,
            )

        graph_height = max(20, card_height - 26)
        before_graph = QRectF(
            card_x + 5,
            before_y + 20,
            card_width - 10,
            graph_height,
        )
        after_graph = QRectF(
            card_x + 5,
            after_y + 20,
            card_width - 10,
            graph_height,
        )
        sample_x_positions = self._sample_x_positions(after_graph)
        after_points = [
            (x, sample[2] - sample[3])
            for x, sample in zip(sample_x_positions, self.samples)
            if sample[2] is not None
        ]
        after_x_positions = [point[0] for point in after_points]
        after_offsets = [point[1] for point in after_points]
        after_qc_offsets = [
            sample[2] - sample[4]
            for sample in self.samples
            if sample[2] is not None and sample[4] is not None
        ]
        after_color = success_color
        if (
            after_qc_offsets
            and abs(after_qc_offsets[-1]) > self.tolerance + 1e-9
        ):
            after_color = warning_color
        grid_pen = QPen(QColor(grid_color), 1)
        grid_pen.setStyle(Qt.PenStyle.DotLine)
        for graph in (before_graph, after_graph):
            painter.setPen(grid_pen)
            painter.drawLine(
                int(graph.left()),
                int(graph.top()),
                int(graph.right()),
                int(graph.top()),
            )
            painter.drawLine(
                int(graph.left()),
                int(graph.bottom()),
                int(graph.right()),
                int(graph.bottom()),
            )

        tolerance_top = self._bounded_y(
            self.tolerance,
            -self.half_range_lu,
            self.half_range_lu,
            after_graph,
        )
        tolerance_bottom = self._bounded_y(
            -self.tolerance,
            -self.half_range_lu,
            self.half_range_lu,
            after_graph,
        )
        tolerance_color = QColor(success_color)
        tolerance_color.setAlpha(26 if self.light_theme else 32)
        painter.fillRect(
            QRectF(
                after_graph.left(),
                tolerance_top,
                after_graph.width(),
                max(1.0, tolerance_bottom - tolerance_top),
            ),
            tolerance_color,
        )

        # Both graphs use the exact same fixed ±LU scale around the file target.
        # Equal vertical distances therefore represent equal loudness errors
        # before and after processing, with no automatic rescaling.
        before_target_pen = QPen(QColor(before_color), 1)
        before_target_pen.setStyle(Qt.PenStyle.DashLine)
        painter.setPen(before_target_pen)
        painter.drawLine(
            int(before_graph.left()),
            int(before_graph.center().y()),
            int(before_graph.right()),
            int(before_graph.center().y()),
        )
        after_target_pen = QPen(QColor(after_color), 1)
        after_target_pen.setStyle(Qt.PenStyle.DashLine)
        painter.setPen(after_target_pen)
        painter.drawLine(
            int(after_graph.left()),
            int(after_graph.center().y()),
            int(after_graph.right()),
            int(after_graph.center().y()),
        )
        target_y = after_graph.center().y()
        target_font = painter.font()
        target_font.setPointSizeF(8.0)
        target_font.setBold(False)
        painter.setFont(target_font)
        painter.setPen(QColor(after_color))
        target_text = self.texts["target"].format(
            value=self._number(self.target)
        )
        painter.drawText(
            int(after_graph.left() + 3),
            int(target_y - 22),
            int(after_graph.width() - 6),
            15,
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
            target_text,
        )

        def draw_after_message(key: str) -> None:
            """Use one typographic position for every inactive After state."""
            painter.setFont(target_font)
            painter.setPen(QColor(secondary))
            note_reserve = 22 if self.replaygain_display else 3
            painter.drawText(
                int(after_graph.left() + 4),
                int(after_graph.center().y() + 3),
                int(after_graph.width() - 8),
                int(
                    after_graph.bottom()
                    - after_graph.center().y()
                    - note_reserve
                ),
                Qt.AlignmentFlag.AlignCenter | Qt.TextFlag.TextWordWrap,
                self.texts[key],
            )

        if self.samples:
            before_offsets = [
                sample[1] - sample[3] for sample in self.samples
            ]
            self._draw_trace(
                painter,
                before_graph,
                before_offsets,
                -self.half_range_lu,
                self.half_range_lu,
                QColor(before_color),
                0.0,
            )

            if after_offsets:
                self._draw_trace(
                    painter,
                    after_graph,
                    after_offsets,
                    -self.half_range_lu,
                    self.half_range_lu,
                    QColor(after_color),
                    0.0,
                    after_x_positions,
                    (
                        Qt.PenStyle.DashLine
                        if self.replaygain_display
                        else Qt.PenStyle.SolidLine
                    ),
                    not self.replaygain_display,
                )
            else:
                key = self.state if self.state in self.texts else "waiting"
                draw_after_message(key)
        else:
            key = self.state if self.state in self.texts else "waiting"
            draw_after_message(key)

        if self.replaygain_display:
            note_font = painter.font()
            note_font.setPointSizeF(6.6)
            note_font.setBold(False)
            painter.setFont(note_font)
            note_color = QColor(secondary)
            note_color.setAlpha(225)
            painter.setPen(note_color)
            painter.drawText(
                int(after_graph.left() + 3),
                int(after_graph.bottom() - 20),
                int(after_graph.width() - 6),
                19,
                Qt.AlignmentFlag.AlignCenter | Qt.TextFlag.TextWordWrap,
                self.texts["replaygain_note"],
            )

class StepControl(QWidget):
    def __init__(self, spin_box: QAbstractSpinBox) -> None:
        super().__init__()
        self.setObjectName("stepControl")
        self.setMinimumHeight(30)
        self.spin_box = spin_box
        self.spin_box.setMinimumHeight(30)
        self.spin_box.setButtonSymbols(
            QAbstractSpinBox.ButtonSymbols.NoButtons
        )

        self.decrease_button = QPushButton("−")
        self.decrease_button.setObjectName("stepButton")
        self.increase_button = QPushButton("+")
        self.increase_button.setObjectName("stepButton")
        for button in (self.decrease_button, self.increase_button):
            button.setFixedWidth(30)
            button.setFixedHeight(30)
            button.setAutoRepeat(True)
            button.setAutoRepeatDelay(400)
            button.setAutoRepeatInterval(90)

        self.decrease_button.clicked.connect(
            lambda: self._step_value(self.spin_box.stepDown)
        )
        self.increase_button.clicked.connect(
            lambda: self._step_value(self.spin_box.stepUp)
        )

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)
        layout.addWidget(self.spin_box, 1)
        layout.addWidget(self.decrease_button)
        layout.addWidget(self.increase_button)

    def _clear_editor_selection(self) -> None:
        """Keep the new numeric value readable after a −/+ click."""
        editor = self.spin_box.lineEdit()
        if editor is None:
            return
        editor.deselect()
        editor.setCursorPosition(len(editor.text()))

    def _step_value(self, step) -> None:
        step()
        self._clear_editor_selection()
        # Some native styles update the editor once more after the clicked
        # signal. Clear that deferred selection as well.
        QTimer.singleShot(0, self._clear_editor_selection)

    def set_button_accessibility(
        self,
        decrease: str,
        increase: str,
    ) -> None:
        self.decrease_button.setAccessibleName(decrease)
        self.increase_button.setAccessibleName(increase)

class PersistentCheckBox(QCheckBox):
    def paintEvent(self, event) -> None:
        super().paintEvent(event)
        if not self.isChecked():
            return

        option = QStyleOptionButton()
        self.initStyleOption(option)
        indicator = self.style().subElementRect(
            QStyle.SubElement.SE_CheckBoxIndicator,
            option,
            self,
        ).adjusted(0, 0, -1, -1)

        if not self.isEnabled():
            fill = QColor("#5d7289")
        elif self.window().isActiveWindow():
            fill = QColor("#2f9df4")
        else:
            fill = QColor("#397eae")

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(QPen(QColor("#7f93a7"), 1))
        painter.setBrush(fill)
        painter.drawRoundedRect(indicator, 4, 4)

        left = indicator.left()
        top = indicator.top()
        width = indicator.width()
        height = indicator.height()
        painter.setPen(
            QPen(
                QColor("#ffffff"),
                2,
                Qt.PenStyle.SolidLine,
                Qt.PenCapStyle.RoundCap,
                Qt.PenJoinStyle.RoundJoin,
            )
        )
        painter.drawLine(
            left + int(width * 0.22),
            top + int(height * 0.54),
            left + int(width * 0.43),
            top + int(height * 0.75),
        )
        painter.drawLine(
            left + int(width * 0.43),
            top + int(height * 0.75),
            left + int(width * 0.80),
            top + int(height * 0.28),
        )

class ProfessionalComboBox(QComboBox):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._light_theme = False

    def set_light_theme(self, enabled: bool) -> None:
        self._light_theme = bool(enabled)
        self.update()

    def paintEvent(self, event) -> None:
        super().paintEvent(event)
        center_x = self.width() - 14
        center_y = self.height() // 2
        if self._light_theme:
            color = "#35576f" if self.isEnabled() else "#8a8f92"
        else:
            color = "#b8c7d8" if self.isEnabled() else "#667381"

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(
            QPen(
                QColor(color),
                2,
                Qt.PenStyle.SolidLine,
                Qt.PenCapStyle.RoundCap,
                Qt.PenJoinStyle.RoundJoin,
            )
        )
        painter.drawLine(
            center_x - 4,
            center_y - 2,
            center_x,
            center_y + 2,
        )
        painter.drawLine(
            center_x,
            center_y + 2,
            center_x + 4,
            center_y - 2,
        )


class _CurrentLanguageCheckDelegate(QStyledItemDelegate):
    """Draw a bare check beside the active language in the popup only."""

    CHECK_COLUMN_WIDTH = 22

    def __init__(self, combo: QComboBox) -> None:
        super().__init__(combo)
        self._combo = combo

    def paint(self, painter, option, index) -> None:
        # Keep the native item rendering and its full-row selection colour,
        # while reserving a stable column for the check on Windows 10 and 11.
        if option.state & QStyle.StateFlag.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())

        item_option = QStyleOptionViewItem(option)
        item_option.rect = option.rect.adjusted(
            self.CHECK_COLUMN_WIDTH,
            0,
            0,
            0,
        )
        super().paint(painter, item_option, index)

        if index.row() != self._combo.currentIndex():
            return

        if option.state & QStyle.StateFlag.State_Selected:
            check_color = option.palette.highlightedText().color()
        else:
            check_color = option.palette.text().color()

        left = option.rect.left() + 5
        center_y = option.rect.center().y()
        painter.save()
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(
            QPen(
                check_color,
                2,
                Qt.PenStyle.SolidLine,
                Qt.PenCapStyle.RoundCap,
                Qt.PenJoinStyle.RoundJoin,
            )
        )
        painter.drawLine(left, center_y, left + 4, center_y + 4)
        painter.drawLine(left + 4, center_y + 4, left + 12, center_y - 5)
        painter.restore()


class LanguageComboBox(ProfessionalComboBox):
    """Language selector with an active-item marker in its popup list."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._current_language_delegate = _CurrentLanguageCheckDelegate(self)
        self.view().setItemDelegate(self._current_language_delegate)
        self.currentIndexChanged.connect(self._refresh_current_language_check)

    def _refresh_current_language_check(self, _index: int) -> None:
        self.view().viewport().update()

class OptionHelpButton(QPushButton):
    def __init__(self) -> None:
        super().__init__("?")
        self.setObjectName("helpButton")
        self.setFixedSize(22, 22)
        self.help_title = ""
        self.help_text = ""
        self.clicked.connect(self._show_help)

    def set_help(
        self,
        title: str,
        text: str,
        accessible_name: str,
    ) -> None:
        self.help_title = title
        self.help_text = text
        self.setAccessibleName(accessible_name)
        self.setAccessibleDescription(text)

    def _show_help(self) -> None:
        if not self.help_text:
            return
        show_application_information(
            self,
            self.help_title,
            self.help_text,
        )

class NavigablePathField(QLineEdit):
    """Immutable path field that keeps a visible navigation cursor."""

    def __init__(self) -> None:
        super().__init__()
        self._protected_text = ""
        # Qt intentionally hides the caret of a read-only QLineEdit. Editing
        # is therefore blocked by the event handlers below instead.
        self.setReadOnly(False)
        self.setAcceptDrops(False)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setCursor(Qt.CursorShape.IBeamCursor)
        self.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.setClearButtonEnabled(False)
        self.textEdited.connect(self._restore_protected_text)

    def setText(self, text: str) -> None:
        self._protected_text = text
        super().setText(text)

    def _restore_protected_text(self, _edited_text: str) -> None:
        cursor_position = self.cursorPosition()
        super().setText(self._protected_text)
        self.setCursorPosition(
            min(cursor_position, len(self._protected_text))
        )

    def _navigation_step(self) -> int:
        character_width = max(
            1,
            self.fontMetrics().averageCharWidth(),
        )
        return max(1, self.width() // character_width // 2)

    def move_cursor_by(self, direction: int) -> None:
        if not self.text():
            return
        self.setFocus(Qt.FocusReason.ShortcutFocusReason)
        position = self.cursorPosition()
        step = self._navigation_step()
        self.setCursorPosition(
            max(0, min(len(self.text()), position + direction * step))
        )

    def mousePressEvent(self, event: Any) -> None:
        self.setFocus(Qt.FocusReason.MouseFocusReason)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: Any) -> None:
        if event.button() == Qt.MouseButton.MiddleButton:
            event.ignore()
            return
        super().mouseReleaseEvent(event)

    def keyPressEvent(self, event: Any) -> None:
        if event.matches(QKeySequence.StandardKey.Copy) or event.matches(
            QKeySequence.StandardKey.SelectAll
        ):
            super().keyPressEvent(event)
            return
        if event.key() in {
            Qt.Key.Key_Left,
            Qt.Key.Key_Right,
            Qt.Key.Key_Home,
            Qt.Key.Key_End,
        }:
            super().keyPressEvent(event)
            return
        event.ignore()

    def inputMethodEvent(self, event: Any) -> None:
        event.ignore()

    def dragEnterEvent(self, event: Any) -> None:
        event.ignore()

    def dropEvent(self, event: Any) -> None:
        event.ignore()

    def contextMenuEvent(self, event: Any) -> None:
        # Qt's standard read-only menu keeps Copy and Select All available but
        # disables every mutating action. Restore the visible caret afterward.
        cursor_position = self.cursorPosition()
        self.setReadOnly(True)
        try:
            super().contextMenuEvent(event)
        finally:
            self.setReadOnly(False)
            self.setCursorPosition(cursor_position)

    def focusOutEvent(self, event: Any) -> None:
        if self.text() != self._protected_text:
            super().setText(self._protected_text)
        super().focusOutEvent(event)

    def wheelEvent(self, event: Any) -> None:
        delta = event.angleDelta().x() or event.angleDelta().y()
        if not delta or not self.text():
            super().wheelEvent(event)
            return
        self.move_cursor_by(-1 if delta > 0 else 1)
        event.accept()

class DropArea(QFrame):
    paths_dropped = Signal(list)

    def __init__(self, language: str = "fr") -> None:
        super().__init__()
        self.setAcceptDrops(True)
        self.setObjectName("dropArea")
        self.setFixedHeight(64)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setSpacing(1)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.title = QLabel()
        self.title.setObjectName("dropTitle")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setMinimumHeight(25)
        self.subtitle = QLabel()
        self.subtitle.setObjectName("dropSubtitle")
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle.setMinimumHeight(18)
        layout.addWidget(self.title)
        layout.addWidget(self.subtitle)
        self.set_language(language)

    def set_language(self, language: str) -> None:
        self.title.setText(translate(language, "drop_title"))
        self.subtitle.setText(translate(language, "drop_subtitle"))

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.setProperty("dragActive", True)
            self.style().unpolish(self)
            self.style().polish(self)
        else:
            event.ignore()

    def dragLeaveEvent(self, event) -> None:
        self.setProperty("dragActive", False)
        self.style().unpolish(self)
        self.style().polish(self)
        super().dragLeaveEvent(event)

    def dropEvent(self, event: QDropEvent) -> None:
        self.setProperty("dragActive", False)
        self.style().unpolish(self)
        self.style().polish(self)
        paths = [
            url.toLocalFile()
            for url in event.mimeData().urls()
            if url.isLocalFile()
        ]
        if paths:
            self.paths_dropped.emit(paths)
            event.acceptProposedAction()
