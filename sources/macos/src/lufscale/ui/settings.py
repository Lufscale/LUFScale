"""Coordination des réglages de la fenêtre principale."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..i18n.loader import SUPPORTED_LANGUAGES


DEFAULT_RESUME_ENABLED = True
DEFAULT_QUALITY_CONTROL_ENABLED = True
DEFAULT_SKIP_COMPLIANT_ENABLED = True

PRESETS = {
    "library": (-16.0, -1.5, 0),
    "streaming": (-14.0, -1.0, 0),
    "dynamic": (-18.0, -2.0, 0),
}

VOLUME_TARGETS = {
    "soft": -18.0,
    "normal": -16.0,
    "loud": -14.0,
}


def load_initial_preferences(settings_store: Any) -> tuple[str, str]:
    """Charge uniquement les préférences nécessaires avant la création UI."""
    saved_language = settings_store.value("language", "en", type=str)
    language = (
        saved_language if saved_language in SUPPORTED_LANGUAGES else "en"
    )
    saved_theme = settings_store.value("theme", "dark", type=str)
    theme = saved_theme if saved_theme in {"dark", "light"} else "dark"
    return language, theme


def volume_profile_for_lufs(value: float) -> str:
    """Retourne le profil de volume correspondant à une cible LUFS."""
    return next(
        (
            key
            for key, target in VOLUME_TARGETS.items()
            if abs(value - target) < 0.01
        ),
        "custom",
    )


class SettingsController:
    """Synchronise les widgets de réglages et leur stockage persistant."""

    def __init__(self, owner: Any) -> None:
        self.owner = owner
        self._applying_preset = False
        self._applying_volume = False

    def on_volume_changed(self, index: int) -> None:
        if self._applying_volume:
            return
        target = VOLUME_TARGETS.get(
            str(self.owner.volume_combo.itemData(index))
        )
        if target is None:
            return
        self._applying_volume = True
        try:
            self.owner.lufs_spin.setValue(target)
        finally:
            self._applying_volume = False
        self.mark_preset_custom()

    def sync_volume_from_lufs(self, value: float) -> None:
        if self._applying_volume:
            return
        index = self.owner.volume_combo.findData(
            volume_profile_for_lufs(value)
        )
        if index < 0 or index == self.owner.volume_combo.currentIndex():
            return
        self._applying_volume = True
        try:
            self.owner.volume_combo.setCurrentIndex(index)
        finally:
            self._applying_volume = False

    def on_preset_changed(self, index: int) -> None:
        if self._applying_preset:
            return
        key = self.owner.preset_combo.itemData(index)
        preset = PRESETS.get(str(key))
        if preset is None:
            return
        lufs, peak, quality = preset
        self._applying_preset = True
        try:
            self.owner.lufs_spin.setValue(lufs)
            self.owner.peak_spin.setValue(peak)
            self.owner.quality_spin.setValue(quality)
        finally:
            self._applying_preset = False
        self.sync_volume_from_lufs(self.owner.lufs_spin.value())

    def mark_preset_custom(self) -> None:
        if self._applying_preset:
            return
        custom_index = self.owner.preset_combo.findData("custom")
        if custom_index >= 0:
            self._applying_preset = True
            try:
                self.owner.preset_combo.setCurrentIndex(custom_index)
            finally:
                self._applying_preset = False

    def restore(self) -> None:
        owner = self.owner
        store = owner.settings_store
        saved_output = store.value("output", "", type=str)
        if saved_output:
            owner.output_path = Path(saved_output)

        saved_preset = store.value("preset", "library", type=str)
        self._applying_preset = True
        try:
            preset_index = owner.preset_combo.findData(saved_preset)
            if preset_index < 0:
                preset_index = owner.preset_combo.findData("library")
                saved_preset = "library"
            owner.preset_combo.setCurrentIndex(preset_index)
            preset = PRESETS.get(saved_preset)
            if preset is not None:
                lufs, peak, quality = preset
                owner.lufs_spin.setValue(lufs)
                owner.peak_spin.setValue(peak)
                owner.quality_spin.setValue(quality)
            else:
                owner.lufs_spin.setValue(
                    store.value("lufs", -16.0, type=float)
                )
                owner.peak_spin.setValue(
                    store.value("peak", -1.5, type=float)
                )
                owner.quality_spin.setValue(
                    store.value("quality", 0, type=int)
                )
        finally:
            self._applying_preset = False
        self.sync_volume_from_lufs(owner.lufs_spin.value())

        saved_operation = store.value("operation", "convert", type=str)
        operation_index = owner.operation_combo.findData(saved_operation)
        owner.operation_combo.setCurrentIndex(max(operation_index, 0))
        analysis_method_index = owner.analysis_method_combo.findData(
            "historical"
        )
        owner.analysis_method_combo.setCurrentIndex(
            max(analysis_method_index, 0)
        )
        owner.parallel_spin.setValue(
            store.value("parallel", 0, type=int)
        )
        owner.overwrite_check.setChecked(
            store.value("overwrite", False, type=bool)
        )
        owner.skip_compliant_check.setChecked(
            store.value(
                "skip_compliant",
                DEFAULT_SKIP_COMPLIANT_ENABLED,
                type=bool,
            )
        )
        owner.resume_check.setChecked(
            store.value(
                "resume", DEFAULT_RESUME_ENABLED, type=bool
            )
        )
        owner.quality_check.setChecked(
            store.value(
                "quality_control",
                DEFAULT_QUALITY_CONTROL_ENABLED,
                type=bool,
            )
        )
        owner.report_check.setChecked(
            store.value("generate_report", False, type=bool)
        )
        owner.auto_start_check.setChecked(
            store.value("auto_start", False, type=bool)
        )

    def save(self) -> None:
        owner = self.owner
        store = owner.settings_store
        if owner.output_path:
            store.setValue("output", str(owner.output_path))
        store.setValue("preset", owner.preset_combo.currentData())
        store.setValue("lufs", owner.lufs_spin.value())
        store.setValue("peak", owner.peak_spin.value())
        store.setValue("quality", owner.quality_spin.value())
        store.setValue("operation", owner.operation_combo.currentData())
        store.setValue("analysis_method", "historical")
        store.setValue("parallel", owner.parallel_spin.value())
        store.setValue("overwrite", owner.overwrite_check.isChecked())
        store.setValue(
            "skip_compliant", owner.skip_compliant_check.isChecked()
        )
        store.setValue("resume", owner.resume_check.isChecked())
        store.setValue(
            "quality_control", owner.quality_check.isChecked()
        )
        store.setValue(
            "generate_report", owner.report_check.isChecked()
        )
        store.setValue("auto_start", owner.auto_start_check.isChecked())
        store.setValue("language", owner.language)
        store.setValue("theme", owner.theme)
