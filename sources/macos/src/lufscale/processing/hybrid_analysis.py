"""Conservative boundaries shared by the guarded MP3 QC cascade."""

from __future__ import annotations

import math
from typing import Mapping


HYBRID_COMPARISON_TOLERANCES = {
    "input_i": 0.15,
    "input_tp": 0.15,
}
HYBRID_QC_LUFS_TOLERANCE = 0.60
HYBRID_QC_PEAK_TOLERANCE = 0.25
HYBRID_QC_LOUDNESS_BOUNDARY_GUARD_LU = 0.15
HYBRID_QC_TRUE_PEAK_SAFE_MARGIN_DB = 0.25


def compare_measurements(
    fast: Mapping[str, str],
    reference: Mapping[str, str],
    tolerances: Mapping[str, float] = HYBRID_COMPARISON_TOLERANCES,
) -> tuple[bool, dict[str, float]]:
    """Compare every QC-driving field for fallback diagnostics."""
    differences: dict[str, float] = {}
    accepted = True
    for field, tolerance in tolerances.items():
        try:
            difference = abs(float(fast[field]) - float(reference[field]))
        except (KeyError, TypeError, ValueError):
            accepted = False
            continue
        if not math.isfinite(difference):
            accepted = False
            continue
        differences[field] = difference
        if difference - max(0.0, float(tolerance)) > 1e-9:
            accepted = False
    if len(differences) != len(tolerances):
        accepted = False
    return accepted, differences


def qc_fast_candidate_diagnostics(
    measurements: Mapping[str, str],
    input_measurements: Mapping[str, str],
    *,
    expected_lufs: float,
    true_peak_limit: float,
    preserve_audio: bool,
    dynamic_mp3_path: bool,
    copied_compliant: bool,
) -> dict[str, float | str | bool | None]:
    """Authorize only a result safely inside both QC pass boundaries.

    The dynamic-MP3 flag is intentionally not a blanket exclusion.  A fast
    measurement may certify a dynamic output only when no retry can be needed
    according to the stricter inner region.  Copies reuse their already known
    input measurement and therefore never enter this cascade.
    """
    diagnostics: dict[str, float | str | bool | None] = {
        "eligible": False,
        "reason": "invalid_fast_measurements",
        "expected_lufs": float(expected_lufs),
        "loudness_error_lu": None,
        "loudness_boundary_margin_lu": None,
        "true_peak_margin_db": None,
        "preserved_peak_error_db": None,
    }
    _ = dynamic_mp3_path
    if copied_compliant:
        diagnostics["reason"] = "byte_copy_reuses_input_measurement"
        return diagnostics
    try:
        fast_lufs = float(measurements["input_i"])
        fast_peak = float(measurements["input_tp"])
    except (KeyError, TypeError, ValueError):
        return diagnostics
    if not math.isfinite(fast_lufs) or not math.isfinite(fast_peak):
        return diagnostics

    if preserve_audio:
        try:
            input_lufs = float(input_measurements["input_i"])
            input_peak = float(input_measurements["input_tp"])
        except (KeyError, TypeError, ValueError):
            diagnostics["reason"] = "invalid_reference_input"
            return diagnostics
        if not math.isfinite(input_lufs) or not math.isfinite(input_peak):
            diagnostics["reason"] = "invalid_reference_input"
            return diagnostics
        loudness_error = abs(fast_lufs - input_lufs)
        peak_error = abs(fast_peak - input_peak)
        loudness_margin = HYBRID_QC_LUFS_TOLERANCE - loudness_error
        peak_margin = HYBRID_QC_PEAK_TOLERANCE - peak_error
        loudness_safe = (
            loudness_margin >= HYBRID_QC_LOUDNESS_BOUNDARY_GUARD_LU
        )
        peak_safe = peak_margin >= HYBRID_QC_LOUDNESS_BOUNDARY_GUARD_LU
        diagnostics.update(
            {
                "loudness_error_lu": loudness_error,
                "loudness_boundary_margin_lu": loudness_margin,
                "true_peak_margin_db": peak_margin,
                "preserved_peak_error_db": peak_error,
            }
        )
    else:
        loudness_error = abs(fast_lufs - float(expected_lufs))
        loudness_margin = HYBRID_QC_LUFS_TOLERANCE - loudness_error
        peak_margin = float(true_peak_limit) - fast_peak
        loudness_safe = (
            loudness_margin >= HYBRID_QC_LOUDNESS_BOUNDARY_GUARD_LU
        )
        peak_safe = peak_margin >= HYBRID_QC_TRUE_PEAK_SAFE_MARGIN_DB
        diagnostics.update(
            {
                "loudness_error_lu": loudness_error,
                "loudness_boundary_margin_lu": loudness_margin,
                "true_peak_margin_db": peak_margin,
            }
        )

    if loudness_safe and peak_safe:
        diagnostics.update({"eligible": True, "reason": "eligible"})
    elif not loudness_safe and not peak_safe:
        diagnostics["reason"] = "loudness_and_true_peak_boundaries"
    elif not loudness_safe:
        diagnostics["reason"] = "loudness_boundary"
    else:
        diagnostics["reason"] = "true_peak_boundary"
    return diagnostics


__all__ = [
    "HYBRID_COMPARISON_TOLERANCES",
    "HYBRID_QC_LOUDNESS_BOUNDARY_GUARD_LU",
    "HYBRID_QC_LUFS_TOLERANCE",
    "HYBRID_QC_PEAK_TOLERANCE",
    "HYBRID_QC_TRUE_PEAK_SAFE_MARGIN_DB",
    "compare_measurements",
    "qc_fast_candidate_diagnostics",
]
