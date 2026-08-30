"""Single source of truth for every question-mark help dialog."""

from __future__ import annotations

from collections.abc import Callable


# Every dialog is assembled from the same ordered sections in all languages.
# Keeping this catalogue outside application.py prevents a translated dialog
# from silently losing a paragraph when the interface evolves.
HELP_DIALOG_SECTIONS: dict[str, tuple[str, ...]] = {
    "preset": ("preset_tooltip",),
    "operation": (
        "operation_help_text",
        "replaygain_usefulness_text",
        "replaygain_qc_help_text",
        "analyze_only_fresh_help_text",
    ),
    "analysis_method": ("analysis_method_tooltip",),
    "volume": ("volume_tooltip",),
    "target": ("target_tooltip",),
    "peak": ("peak_tooltip",),
    "quality": ("quality_tooltip",),
    "parallel": ("parallel_tooltip",),
    "overwrite": ("overwrite_tooltip",),
    "skip_compliant": ("skip_compliant_tooltip",),
    "resume": ("resume_tooltip",),
    "quality_control": ("quality_control_tooltip",),
    "report": ("report_tooltip",),
    "auto_start": ("auto_start_tooltip",),
    "loudness_comparison": (
        "loudness_comparison_help_text",
        "analysis_progress_help_text",
    ),
    "log": (
        "log_help_text",
        "replaygain_log_help_text",
        "analysis_progress_help_text",
    ),
}

HELP_CONTENT_KEYS = frozenset(
    key
    for sections in HELP_DIALOG_SECTIONS.values()
    for key in sections
)


def compose_help_text(
    translate: Callable[[str], str],
    dialog: str,
) -> str:
    """Build one help dialog from its language-independent section list."""
    return "\n\n".join(translate(key) for key in HELP_DIALOG_SECTIONS[dialog])


__all__ = ["HELP_CONTENT_KEYS", "HELP_DIALOG_SECTIONS", "compose_help_text"]
