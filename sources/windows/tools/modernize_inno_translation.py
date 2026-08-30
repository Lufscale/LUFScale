#!/usr/bin/env python3
"""Build a complete current Inno translation from a verified legacy file."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re


CURRENT_LANG_OPTIONS = (
    "LanguageName",
    "LanguageID",
    "LanguageCodePage",
    "DialogFontName",
    "DialogFontSize",
    "DialogFontBaseScaleWidth",
    "DialogFontBaseScaleHeight",
    "WelcomeFontName",
    "WelcomeFontSize",
    "RightToLeft",
)
PLACEHOLDER_PATTERN = re.compile(r"%\d+|%n|\[[^\]]+\]")


def read_sections(path: Path) -> dict[str, dict[str, str]]:
    """Read the assignment sections used by Inno message files."""
    sections: dict[str, dict[str, str]] = {}
    section = ""
    for line_number, raw_line in enumerate(
        path.read_text(encoding="utf-8-sig").splitlines(),
        start=1,
    ):
        line = raw_line.strip()
        if not line or line.startswith(";"):
            continue
        if line.startswith("[") and line.endswith("]"):
            section = line[1:-1]
            sections.setdefault(section, {})
            continue
        if not section or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        entries = sections.setdefault(section, {})
        if key in entries:
            raise ValueError(f"Duplicate {section} key {key!r} at {path}:{line_number}")
        entries[key] = value
    return sections


def placeholder_counts(value: str) -> Counter[str]:
    return Counter(PLACEHOLDER_PATTERN.findall(value))


def merge_current_section(
    section: str,
    reference: dict[str, str],
    legacy: dict[str, str],
    supplement: dict[str, str],
) -> dict[str, str]:
    unknown_supplements = sorted(set(supplement) - set(reference))
    if unknown_supplements:
        raise ValueError(
            f"Unrecognized {section} supplement keys: {', '.join(unknown_supplements)}"
        )

    merged: dict[str, str] = {}
    missing: list[str] = []
    for key, reference_value in reference.items():
        if key in supplement:
            translated_value = supplement[key]
        elif key in legacy:
            translated_value = legacy[key]
        else:
            missing.append(key)
            continue
        if placeholder_counts(translated_value) != placeholder_counts(reference_value):
            raise ValueError(
                f"Placeholder mismatch for {section}.{key}: "
                f"expected {dict(placeholder_counts(reference_value))}, "
                f"found {dict(placeholder_counts(translated_value))}"
            )
        merged[key] = translated_value
    if missing:
        raise ValueError(
            f"Missing current {section} translations: {', '.join(missing)}"
        )
    return merged


def build_translation(
    reference_path: Path,
    legacy_path: Path,
    supplement_path: Path,
    output_path: Path,
    language: str,
    version: str,
) -> None:
    reference = read_sections(reference_path)
    legacy = read_sections(legacy_path)
    supplement = read_sections(supplement_path)

    lang_options = legacy.get("LangOptions", {})
    required_options = ("LanguageName", "LanguageID", "LanguageCodePage")
    missing_options = [key for key in required_options if key not in lang_options]
    if missing_options:
        raise ValueError(f"Missing language options: {', '.join(missing_options)}")

    merged_sections: dict[str, dict[str, str]] = {}
    for section in ("Messages", "CustomMessages"):
        merged_sections[section] = merge_current_section(
            section,
            reference.get(section, {}),
            legacy.get(section, {}),
            supplement.get(section, {}),
        )

    lines = [
        f"; LUFScale-maintained Inno Setup {version} {language} messages",
        "; Built from the pinned official Inno translation and its current Default.isl.",
        "; Obsolete directives and message names are intentionally excluded.",
        "",
        "[LangOptions]",
    ]
    for key in CURRENT_LANG_OPTIONS:
        if key in lang_options:
            lines.append(f"{key}={lang_options[key]}")
    for section in ("Messages", "CustomMessages"):
        lines.extend(("", f"[{section}]"))
        lines.extend(f"{key}={value}" for key, value in merged_sections[section].items())

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", type=Path, required=True)
    parser.add_argument("--legacy", type=Path, required=True)
    parser.add_argument("--supplement", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--language", required=True)
    parser.add_argument("--version", required=True)
    args = parser.parse_args()
    build_translation(
        args.reference,
        args.legacy,
        args.supplement,
        args.output,
        args.language,
        args.version,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
