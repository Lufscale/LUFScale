"""Préparation des requêtes de conversion depuis l'interface."""

from __future__ import annotations

from typing import Any

from PySide6.QtWidgets import QMessageBox

from ..audio.core import LoudnessSettings, validate_output
from ..processing.conversion_request import ConversionRequest


class ConversionRequestController:
    """Valide l'action et capture un instantané cohérent des réglages."""

    def __init__(self, owner: Any) -> None:
        self.owner = owner

    def prepare(self) -> ConversionRequest | None:
        """Retourne une requête prête à démarrer, ou ``None`` si elle échoue."""
        owner = self.owner
        if owner.worker_coordinator.busy:
            return None

        if owner.output_path is None:
            # Destination selection belongs exclusively to the dedicated
            # Choose button.  Starting a conversion must never open a file
            # chooser as a side effect.  Keep the primary action available
            # after adding sources, but explain the missing prerequisite.
            QMessageBox.information(
                owner,
                owner.t("choose_output"),
                owner.t("destination_required_start"),
            )
            return None
        output = owner.output_path

        ffmpeg = owner.startup_coordinator.resolve_ffmpeg()
        if ffmpeg is None:
            return None

        error = validate_output(owner.source_paths, output, owner.language)
        if error:
            QMessageBox.warning(owner, owner.t("invalid_location"), error)
            return None

        owner._save_settings()
        owner.execution_presenter.reset_for_run()

        request = ConversionRequest(
            ffmpeg=ffmpeg,
            inputs=tuple(owner.source_paths),
            output=output,
            settings=LoudnessSettings(
                integrated_lufs=owner.lufs_spin.value(),
                true_peak=owner.peak_spin.value(),
                quality=owner.quality_spin.value(),
            ),
            overwrite=owner.overwrite_check.isChecked(),
            operation=str(owner.operation_combo.currentData()),
            max_parallel=owner.parallel_spin.value(),
            resume_enabled=owner.resume_check.isChecked(),
            quality_control=owner.quality_check.isChecked(),
            generate_report=owner.report_check.isChecked(),
            language=owner.language,
            skip_compliant=owner.skip_compliant_check.isChecked(),
            analysis_method="hybrid",
        )
        owner._reset_loudness_comparison(
            request.settings.integrated_lufs,
            request.loudness_comparison_state,
        )
        return request


__all__ = ["ConversionRequestController"]
