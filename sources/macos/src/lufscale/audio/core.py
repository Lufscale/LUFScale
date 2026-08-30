from __future__ import annotations

import json
import math
import os
import re
import struct
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

from ..i18n.translations import EXTRA_CORE_TEXTS

for _localized_core_texts in EXTRA_CORE_TEXTS.values():
    _localized_core_texts.pop("album_unmeasurable", None)
    _localized_core_texts.pop("empty_album", None)


CORE_TEXTS = {
    "fr": {
        "no_inputs": "Ajoutez au moins un dossier ou un fichier audio compatible.",
        "output_inside_source": (
            "Le dossier de sortie ne peut pas être placé dans un dossier source. "
            "Choisissez un emplacement extérieur aux dossiers déposés."
        ),
        "output_recreates_source": (
            "Ce dossier de sortie recréerait les fichiers directement dans la "
            "source. Choisissez un autre emplacement."
        ),
        "output_contains_source": (
            "Le dossier de sortie sélectionné contient déjà le fichier source. "
            "Choisissez un autre emplacement."
        ),
        "no_measurements": ("FFmpeg n’a renvoyé aucune mesure de sonie exploitable."),
        "incomplete_measurements": "Mesures FFmpeg incomplètes : {fields}",
        "loudness_unmeasurable": "La sonie n’est pas mesurable.",
        "output_not_silent": "La sortie n’est plus silencieuse.",
        "output_unmeasurable": "La sortie n’a pas de sonie mesurable.",
        "silent_preserved": "Audio silencieux conservé.",
        "loudness_changed": "sonie modifiée de {value:+.2f} LU",
        "peak_changed": "crête modifiée de {value:+.2f} dB",
        "unexpected_loudness": ("{actual:.2f} LUFS au lieu de {expected:.2f}"),
        "peak_above_limit": ("crête {value:.2f} dBTP au-dessus de la limite"),
        "measurements_ok": "Mesures conformes.",
    },
    "en": {
        "no_inputs": "Add at least one folder or supported audio file.",
        "output_inside_source": (
            "The output folder cannot be inside a source folder. "
            "Choose a location outside the dropped folders."
        ),
        "output_recreates_source": (
            "This output folder would recreate files directly in the source. "
            "Choose another location."
        ),
        "output_contains_source": (
            "The selected output folder already contains the source file. "
            "Choose another location."
        ),
        "no_measurements": ("FFmpeg did not return usable loudness measurements."),
        "incomplete_measurements": "Incomplete FFmpeg measurements: {fields}",
        "loudness_unmeasurable": "The loudness cannot be measured.",
        "output_not_silent": "The output is no longer silent.",
        "output_unmeasurable": "The output has no measurable loudness.",
        "silent_preserved": "Silent audio preserved.",
        "loudness_changed": "loudness changed by {value:+.2f} LU",
        "peak_changed": "peak changed by {value:+.2f} dB",
        "unexpected_loudness": ("{actual:.2f} LUFS instead of {expected:.2f}"),
        "peak_above_limit": ("peak {value:.2f} dBTP exceeds the limit"),
        "measurements_ok": "Measurements are compliant.",
    },
}


SUPPORTED_AUDIO_EXTENSIONS = frozenset(
    {".mp3", ".flac", ".wav", ".aif", ".aiff", ".m4a", ".ogg", ".opus"}
)

# The 1.22.16 corpus diagnostic measured up to +0.82 dB of true-peak growth
# after libmp3lame. Version 1.22.17 therefore introduced a 1.00 dB initial
# reserve; measured feedback below handles codec outliers and low loudness.
MP3_DYNAMIC_TRUE_PEAK_MARGIN_DB = 1.0
MP3_DYNAMIC_RETRY_MAX_ATTEMPTS = 3
MP3_DYNAMIC_RETRY_GUARD_DB = 0.05
MP3_DYNAMIC_RETRY_MIN_STEP_DB = 0.01
LOUDNORM_MIN_TRUE_PEAK_DBTP = -9.0
LOUDNORM_LINEAR_SAFETY_MARGIN_DB = 0.05
LOSSLESS_TARGET_CORRECTION_EXTENSIONS = frozenset({".flac", ".wav", ".aif", ".aiff"})
TARGET_CORRECTION_MAX_ATTEMPTS = 2
TARGET_CORRECTION_GUARD_DB = 0.05
TARGET_CORRECTION_MIN_STEP_DB = 0.05
# This stricter inner target controls corrective retries and candidate ranking.
# It is intentionally narrower than the final user-facing QC warning limit.
STRICT_TARGET_LUFS_TOLERANCE = 0.50
# A source is copied without normalization only when it is already very close
# to the requested value.  This threshold is intentionally stricter than the
# final quality-control allowance: -14.39 LUFS must not be treated as an
# unchanged -14.00 LUFS source merely because encoder output has a wider QC
# tolerance.
ALREADY_COMPLIANT_LUFS_TOLERANCE = 0.10
# The correction engines still try to reach the historical ±0.50 LU target.
# The final QC warning boundary is slightly wider so values displayed as
# -14.51 or -14.55 LUFS are treated as acceptable rounding/codec variance,
# while the exact measured value remains visible in the log and reports.
QUALITY_CONTROL_LUFS_TOLERANCE = 0.60
QUALITY_CONTROL_TRUE_PEAK_TOLERANCE_DB = 0.25

# Encoders required by the formats that LUFScale advertises. PCM encoders are
# included explicitly so a custom/minimal FFmpeg build fails at startup with a
# useful message instead of halfway through a batch.
REQUIRED_AUDIO_ENCODERS = (
    "libmp3lame",
    "flac",
    "pcm_s16le",
    "pcm_s16be",
    "pcm_s24le",
    "pcm_s24be",
    "pcm_s32le",
    "pcm_s32be",
    "pcm_f32le",
    "aac",
    "libvorbis",
    "libopus",
)


def is_supported_audio_file(path: Path | str) -> bool:
    return Path(path).suffix.lower() in SUPPORTED_AUDIO_EXTENSIONS


def core_text(language: str, key: str, **values: Any) -> str:
    if language in EXTRA_CORE_TEXTS:
        template = EXTRA_CORE_TEXTS[language].get(key, CORE_TEXTS["en"][key])
    else:
        selected = language if language in CORE_TEXTS else "en"
        template = CORE_TEXTS[selected][key]
    return template.format(**values)


@dataclass(frozen=True)
class LoudnessSettings:
    integrated_lufs: float = -16.0
    loudness_range: float = 11.0
    true_peak: float = -1.5
    quality: int = 0


@dataclass(frozen=True)
class ConversionJob:
    source: Path
    destination: Path


@dataclass(frozen=True)
class QualityResult:
    passed: bool
    message: str


def _path_key(path: Path) -> str:
    return os.path.normcase(str(path.resolve()))


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def canonicalize_inputs(items: Iterable[Path | str]) -> list[Path]:
    """Return existing, unique folders and audio files without duplicates."""
    unique: list[Path] = []
    seen: set[str] = set()

    for raw_item in items:
        item = Path(raw_item).expanduser().resolve()
        if not item.exists():
            continue
        if item.is_file() and not is_supported_audio_file(item):
            continue
        key = _path_key(item)
        if key not in seen:
            seen.add(key)
            unique.append(item)

    selected_directories = [item for item in unique if item.is_dir()]
    result: list[Path] = []

    for item in unique:
        nested_in_another_root = any(
            directory != item and is_relative_to(item, directory)
            for directory in selected_directories
        )
        if not nested_in_another_root:
            result.append(item)

    return result


def validate_output(
    inputs: Sequence[Path], output_root: Path, language: str = "fr"
) -> str | None:
    output = output_root.expanduser().resolve()
    if not inputs:
        return core_text(language, "no_inputs")

    for source in inputs:
        source = source.resolve()
        if source.is_dir() and is_relative_to(output, source):
            return core_text(language, "output_inside_source")
        if source.is_dir() and (output / source.name).resolve() == source:
            return core_text(language, "output_recreates_source")
        if source.is_file() and (output / source.name).resolve() == source:
            return core_text(language, "output_contains_source")
    return None


def _unique_name(name: str, used: set[str]) -> str:
    candidate = name
    counter = 2
    while os.path.normcase(candidate) in used:
        candidate = f"{name}__{counter}"
        counter += 1
    used.add(os.path.normcase(candidate))
    return candidate


def _unique_file_name(name: str, used: set[str]) -> str:
    """Return a unique file name while preserving its real extension.

    Appending the collision counter to the complete name created outputs such
    as ``song.mp3__2``.  FFmpeg then interpreted ``.mp3__2`` as the output
    format and rejected the second standalone file.  The counter belongs in
    the stem so every destination remains a supported audio path.
    """
    path = Path(name)
    candidate = name
    counter = 2
    while os.path.normcase(candidate) in used:
        candidate = f"{path.stem}__{counter}{path.suffix}"
        counter += 1
    used.add(os.path.normcase(candidate))
    return candidate


def iter_audio_files(folder: Path) -> Iterable[Path]:
    for current_root, directory_names, file_names in os.walk(folder, followlinks=False):
        directory_names.sort(key=str.casefold)
        file_names.sort(key=str.casefold)
        current = Path(current_root)
        for file_name in file_names:
            if is_supported_audio_file(file_name):
                yield current / file_name


def iter_mp3_files(folder: Path) -> Iterable[Path]:
    """Backward-compatible alias retained for integrations using the old API."""
    yield from iter_audio_files(folder)


def build_jobs(
    inputs: Sequence[Path | str],
    output_root: Path | str,
    language: str = "fr",
) -> list[ConversionJob]:
    roots = canonicalize_inputs(inputs)
    output = Path(output_root).expanduser().resolve()
    error = validate_output(roots, output, language)
    if error:
        raise ValueError(error)

    jobs: list[ConversionJob] = []
    used_root_names: set[str] = set()
    used_file_names: set[str] = set()

    for source_root in roots:
        if source_root.is_dir():
            destination_name = _unique_name(source_root.name, used_root_names)
            destination_root = output / destination_name
            for source in iter_audio_files(source_root):
                relative = source.relative_to(source_root)
                jobs.append(ConversionJob(source, destination_root / relative))
        else:
            destination_name = _unique_file_name(
                source_root.name,
                used_file_names,
            )
            jobs.append(ConversionJob(source_root, output / destination_name))

    return jobs


def loudnorm_analysis_filter(settings: LoudnessSettings) -> str:
    return (
        f"loudnorm=I={settings.integrated_lufs:g}"
        f":LRA={settings.loudness_range:g}"
        f":TP={settings.true_peak:g}:print_format=json"
    )


def ebur128_analysis_filter() -> str:
    """Return the lightweight EBU R128 scanner with true-peak measurement."""
    return "ebur128=peak=true"


def loudnorm_fast_analysis_filter(settings: LoudnessSettings) -> str:
    """Measure at 192 kHz while bypassing loudnorm's dynamic limiter.

    The synthetic measured values deliberately select loudnorm's linear path
    with zero gain.  The filter therefore reports the input EBU R128 values
    without normalizing the discarded output.  Callers must use the result
    only when :func:`loudnorm_linear_mode_is_available` returns true; the
    dynamic second pass needs the target offset produced by a full analysis.
    """
    return (
        "aresample=192000,"
        f"loudnorm=I={settings.integrated_lufs:g}"
        f":LRA={settings.loudness_range:g}"
        f":TP={settings.true_peak:g}"
        f":measured_I={settings.integrated_lufs:g}"
        ":measured_LRA=1:measured_TP=-99:measured_thresh=-60"
        ":offset=0:linear=true:print_format=json"
    )


def parse_loudnorm_measurements(stderr: str, language: str = "fr") -> dict[str, str]:
    blocks = re.findall(r'\{\s*"input_i".*?\}', stderr, flags=re.DOTALL)
    if not blocks:
        raise ValueError(core_text(language, "no_measurements"))

    measurements = json.loads(blocks[-1])
    required = {
        "input_i",
        "input_tp",
        "input_lra",
        "input_thresh",
        "target_offset",
    }
    missing = required.difference(measurements)
    if missing:
        raise ValueError(
            core_text(
                language,
                "incomplete_measurements",
                fields=", ".join(sorted(missing)),
            )
        )
    result = {key: str(value) for key, value in measurements.items()}
    duration = re.search(
        r"Duration:\s*(?P<hours>\d+):(?P<minutes>\d{2}):"
        r"(?P<seconds>\d{2}(?:\.\d+)?)",
        stderr,
    )
    if duration is not None:
        duration_seconds = (
            int(duration.group("hours")) * 3600
            + int(duration.group("minutes")) * 60
            + float(duration.group("seconds"))
        )
        result["_input_duration_seconds"] = f"{duration_seconds:.6f}"
    # The loudnorm filter internally works at 192 kHz to calculate true peaks.
    # Preserve the first input stream properties so the conversion pass can
    # return lossless files to their original sample rate and PCM depth.
    stream = re.search(
        r"Audio:\s*(?P<codec>[A-Za-z0-9_]+).*?,\s*"
        r"(?P<sample_rate>\d+)\s*Hz(?P<tail>[^\r\n]*)",
        stderr,
    )
    if stream is not None:
        codec = stream.group("codec")
        tail = stream.group("tail")
        result["_input_codec"] = codec
        result["_input_sample_rate"] = stream.group("sample_rate")
        sample_format = re.search(
            r",\s*(?P<format>u8|s16p?|s32p?|s64p?|fltp?|dblp?)"
            r"(?:\s|,|\(|$)",
            tail,
        )
        if sample_format is not None:
            result["_input_sample_format"] = sample_format.group("format")
        explicit_depth = re.search(r"\((?P<bits>\d+)\s*bit\)", tail)
        codec_depth = re.match(r"pcm_[suf](?P<bits>\d+)", codec)
        if explicit_depth is not None:
            result["_input_bit_depth"] = explicit_depth.group("bits")
        elif codec_depth is not None:
            result["_input_bit_depth"] = codec_depth.group("bits")
        elif sample_format is not None and sample_format.group("format") in {
            "s16",
            "s16p",
        }:
            result["_input_bit_depth"] = "16"
    return result


def parse_ebur128_measurements(stderr: str, language: str = "fr") -> dict[str, str]:
    """Parse the final FFmpeg ``ebur128`` summary as loudnorm-compatible data.

    ``ebur128`` reports one threshold for integrated loudness and another for
    loudness range.  The former is the value compatible with loudnorm's
    ``input_thresh`` field.  ``target_offset`` is deliberately zero because
    callers may use this result only for a guarded linear second pass.
    """
    summaries = re.findall(
        r"Summary:\s*"
        r"Integrated loudness:\s*"
        r"I:\s*(?P<input_i>[-+]?\S+)\s*LUFS\s*"
        r"Threshold:\s*(?P<input_thresh>[-+]?\S+)\s*LUFS\s*"
        r"Loudness range:\s*"
        r"LRA:\s*(?P<input_lra>[-+]?\S+)\s*LU\s*"
        r"Threshold:\s*[-+]?\S+\s*LUFS\s*"
        r"LRA low:\s*[-+]?\S+\s*LUFS\s*"
        r"LRA high:\s*[-+]?\S+\s*LUFS\s*"
        r"True peak:\s*"
        r"Peak:\s*(?P<input_tp>[-+]?\S+)\s*dBFS",
        stderr,
        flags=re.DOTALL,
    )
    if not summaries:
        raise ValueError(core_text(language, "no_measurements"))

    values = summaries[-1]
    result = {
        "input_i": values[0],
        "input_thresh": values[1],
        "input_lra": values[2],
        "input_tp": values[3],
        "target_offset": "0.00",
        "_analysis_engine": "ffmpeg_ebur128",
    }
    duration = re.search(
        r"Duration:\s*(?P<hours>\d+):(?P<minutes>\d{2}):"
        r"(?P<seconds>\d{2}(?:\.\d+)?)",
        stderr,
    )
    if duration is not None:
        duration_seconds = (
            int(duration.group("hours")) * 3600
            + int(duration.group("minutes")) * 60
            + float(duration.group("seconds"))
        )
        result["_input_duration_seconds"] = f"{duration_seconds:.6f}"
    stream = re.search(
        r"Audio:\s*(?P<codec>[A-Za-z0-9_]+).*?,\s*"
        r"(?P<sample_rate>\d+)\s*Hz(?P<tail>[^\r\n]*)",
        stderr,
    )
    if stream is not None:
        codec = stream.group("codec")
        tail = stream.group("tail")
        result["_input_codec"] = codec
        result["_input_sample_rate"] = stream.group("sample_rate")
        sample_format = re.search(
            r",\s*(?P<format>u8|s16p?|s32p?|s64p?|fltp?|dblp?)"
            r"(?:\s|,|\(|$)",
            tail,
        )
        if sample_format is not None:
            result["_input_sample_format"] = sample_format.group("format")
        explicit_depth = re.search(r"\((?P<bits>\d+)\s*bit\)", tail)
        codec_depth = re.match(r"pcm_[suf](?P<bits>\d+)", codec)
        if explicit_depth is not None:
            result["_input_bit_depth"] = explicit_depth.group("bits")
        elif codec_depth is not None:
            result["_input_bit_depth"] = codec_depth.group("bits")
        elif sample_format is not None and sample_format.group("format") in {
            "s16",
            "s16p",
        }:
            result["_input_bit_depth"] = "16"
    return result


def measurements_are_finite(measurements: dict[str, str]) -> bool:
    keys = ("input_i", "input_tp", "input_lra", "input_thresh", "target_offset")
    try:
        return all(math.isfinite(float(measurements[key])) for key in keys)
    except (KeyError, TypeError, ValueError):
        return False


def loudnorm_linear_mode_is_available(
    settings: LoudnessSettings,
    measurements: dict[str, str],
    *,
    safety_margin_db: float = LOUDNORM_LINEAR_SAFETY_MARGIN_DB,
) -> bool:
    """Mirror FFmpeg's second-pass linear-mode gate conservatively.

    FFmpeg uses zero/default values as sentinels for missing measurements.
    A small peak and LRA margin sends borderline rounded measurements through
    the historical full analysis instead of risking a different mode choice.
    """
    return bool(
        loudnorm_linear_mode_diagnostics(
            settings,
            measurements,
            safety_margin_db=safety_margin_db,
        )["eligible"]
    )


def loudnorm_linear_mode_diagnostics(
    settings: LoudnessSettings,
    measurements: dict[str, str],
    *,
    safety_margin_db: float = LOUDNORM_LINEAR_SAFETY_MARGIN_DB,
) -> dict[str, float | str | bool | None]:
    """Explain the guarded linear decision with exportable margins."""
    diagnostics: dict[str, float | str | bool | None] = {
        "eligible": False,
        "reason": "invalid_measurements",
        "gain_db": None,
        "predicted_true_peak_dbtp": None,
        "true_peak_margin_db": None,
        "lra_margin_lu": None,
        "safety_margin_db": max(0.0, float(safety_margin_db)),
    }
    if not measurements_are_finite(measurements):
        return diagnostics
    try:
        measured_i = float(measurements["input_i"])
        measured_tp = float(measurements["input_tp"])
        measured_lra = float(measurements["input_lra"])
        measured_thresh = float(measurements["input_thresh"])
    except (KeyError, TypeError, ValueError):
        return diagnostics
    sentinel_reasons = (
        (measured_i == 0.0, "missing_integrated_loudness"),
        (measured_tp == 99.0, "missing_true_peak"),
        (measured_lra == 0.0, "missing_loudness_range"),
        (measured_thresh == -70.0, "missing_threshold"),
    )
    for is_missing, reason in sentinel_reasons:
        if is_missing:
            diagnostics["reason"] = reason
            return diagnostics
    margin = max(0.0, float(safety_margin_db))
    gain = settings.integrated_lufs - measured_i
    predicted_peak = measured_tp + gain
    peak_margin = settings.true_peak - predicted_peak
    lra_margin = settings.loudness_range - measured_lra
    peak_ok = peak_margin >= margin
    lra_ok = lra_margin >= margin
    if not peak_ok and not lra_ok:
        reason = "true_peak_and_loudness_range_limits"
    elif not peak_ok:
        reason = "true_peak_limit"
    elif not lra_ok:
        reason = "loudness_range_limit"
    else:
        reason = "eligible"
    diagnostics.update(
        {
            "eligible": peak_ok and lra_ok,
            "reason": reason,
            "gain_db": gain,
            "predicted_true_peak_dbtp": predicted_peak,
            "true_peak_margin_db": peak_margin,
            "lra_margin_lu": lra_margin,
        }
    )
    return diagnostics


def dynamic_mp3_true_peak_target(
    output: Path | str,
    settings: LoudnessSettings,
    measurements: dict[str, str],
    *,
    margin_db: float = MP3_DYNAMIC_TRUE_PEAK_MARGIN_DB,
) -> float | None:
    """Return the internal target for a dynamic MP3 second pass.

    ``None`` means that the selected output is not MP3 or that FFmpeg can use
    the verified linear path, both of which must retain the requested target.
    The lower bound mirrors the true-peak range exposed by the interface and
    accepted by ``loudnorm``.
    """
    if Path(output).suffix.lower() != ".mp3":
        return None
    diagnostics = loudnorm_linear_mode_diagnostics(settings, measurements)
    if bool(diagnostics["eligible"]):
        return None
    reserve = max(0.0, float(margin_db))
    return max(
        LOUDNORM_MIN_TRUE_PEAK_DBTP,
        float(settings.true_peak) - reserve,
    )


def dynamic_mp3_output_is_strictly_compliant(
    settings: LoudnessSettings,
    output_measurements: dict[str, str],
    *,
    lufs_tolerance: float = STRICT_TARGET_LUFS_TOLERANCE,
) -> bool:
    """Check the user targets without the QC true-peak grace interval."""
    if not measurements_are_finite(output_measurements):
        return False
    try:
        loudness = float(output_measurements["input_i"])
        true_peak = float(output_measurements["input_tp"])
    except (KeyError, TypeError, ValueError):
        return False
    return abs(loudness - float(settings.integrated_lufs)) <= max(
        0.0, float(lufs_tolerance)
    ) and true_peak <= float(settings.true_peak)


def next_dynamic_mp3_true_peak_target(
    settings: LoudnessSettings,
    output_measurements: dict[str, str],
    current_internal_target: float,
    *,
    lufs_tolerance: float = STRICT_TARGET_LUFS_TOLERANCE,
    guard_db: float = MP3_DYNAMIC_RETRY_GUARD_DB,
    minimum_step_db: float = MP3_DYNAMIC_RETRY_MIN_STEP_DB,
) -> float | None:
    """Return one bounded feedback adjustment for a dynamic MP3 retry.

    A final peak above the requested ceiling lowers the next internal target.
    If the final loudness is below tolerance, measured peak headroom may instead
    relax the internal target.  No adjustment is made for a compliant result,
    an over-loud result, or when the measured headroom cannot support a useful
    step.  The returned target always stays within loudnorm's accepted range.
    """
    if not measurements_are_finite(output_measurements):
        return None
    try:
        loudness = float(output_measurements["input_i"])
        true_peak = float(output_measurements["input_tp"])
        current = float(current_internal_target)
    except (KeyError, TypeError, ValueError):
        return None

    requested_peak = float(settings.true_peak)
    requested_loudness = float(settings.integrated_lufs)
    tolerance = max(0.0, float(lufs_tolerance))
    guard = max(0.0, float(guard_db))
    minimum_step = max(0.0, float(minimum_step_db))
    guarded_peak = requested_peak - guard

    if true_peak > requested_peak:
        candidate = current - (true_peak - guarded_peak)
    elif loudness < requested_loudness - tolerance:
        guarded_loudness_floor = requested_loudness - max(0.0, tolerance - guard)
        required_relaxation = guarded_loudness_floor - loudness
        available_peak_headroom = guarded_peak - true_peak
        relaxation = min(required_relaxation, available_peak_headroom)
        if relaxation < minimum_step:
            return None
        candidate = current + relaxation
    else:
        return None

    bounded = min(
        requested_peak,
        max(LOUDNORM_MIN_TRUE_PEAK_DBTP, candidate),
    )
    if abs(bounded - current) < minimum_step:
        return None
    return round(bounded, 6)


def next_safe_target_correction_gain(
    settings: LoudnessSettings,
    output_measurements: dict[str, str],
    current_post_gain_db: float = 0.0,
    *,
    lufs_tolerance: float = STRICT_TARGET_LUFS_TOLERANCE,
    guard_db: float = TARGET_CORRECTION_GUARD_DB,
    minimum_step_db: float = TARGET_CORRECTION_MIN_STEP_DB,
) -> float | None:
    """Return a safer total post-normalization gain for a lossless retry.

    Positive correction is capped by measured True Peak headroom.  Negative
    correction is always peak-safe.  The returned value is the total gain to
    append to a fresh conversion from the original source, never a gain to
    apply recursively to an already encoded candidate.
    """
    if not measurements_are_finite(output_measurements):
        return None
    try:
        output_lufs = float(output_measurements["input_i"])
        output_peak = float(output_measurements["input_tp"])
        current_gain = float(current_post_gain_db)
    except (KeyError, TypeError, ValueError):
        return None

    requested_loudness = float(settings.integrated_lufs)
    correction = requested_loudness - output_lufs
    tolerance = max(0.0, float(lufs_tolerance))
    minimum_step = max(0.0, float(minimum_step_db))
    if abs(correction) <= tolerance:
        return None

    if correction > 0.0:
        guarded_peak = float(settings.true_peak) - max(0.0, float(guard_db))
        available_headroom = guarded_peak - output_peak
        if available_headroom < minimum_step:
            return None
        correction = min(correction, available_headroom)
    if abs(correction) < minimum_step:
        return None
    return round(current_gain + correction, 6)


def measurements_are_already_compliant(
    settings: LoudnessSettings,
    measurements: dict[str, str],
    *,
    lufs_tolerance: float = ALREADY_COMPLIANT_LUFS_TOLERANCE,
) -> bool:
    """Return whether a measured source already satisfies both targets."""
    if not measurements_are_finite(measurements):
        return False
    try:
        loudness = float(measurements["input_i"])
        true_peak = float(measurements["input_tp"])
    except (KeyError, TypeError, ValueError):
        return False
    return (
        abs(loudness - settings.integrated_lufs) <= max(0.0, float(lufs_tolerance))
        and true_peak <= settings.true_peak
    )


def loudnorm_conversion_filter(
    settings: LoudnessSettings, measurements: dict[str, str]
) -> str:
    return (
        f"loudnorm=I={settings.integrated_lufs:g}"
        f":LRA={settings.loudness_range:g}"
        f":TP={settings.true_peak:g}"
        f":measured_I={measurements['input_i']}"
        f":measured_LRA={measurements['input_lra']}"
        f":measured_TP={measurements['input_tp']}"
        f":measured_thresh={measurements['input_thresh']}"
        f":offset={measurements['target_offset']}"
        ":linear=true:print_format=summary"
    )


def calculate_loudness_gain_db(
    settings: LoudnessSettings,
    measurements: dict[str, str],
    language: str = "fr",
) -> float:
    if not measurements_are_finite(measurements):
        raise ValueError(core_text(language, "loudness_unmeasurable"))
    return settings.integrated_lufs - float(measurements["input_i"])


def dbtp_to_peak_ratio(dbtp: float) -> float:
    return 10.0 ** (dbtp / 20.0)


def analysis_command(
    ffmpeg: str, source: Path, settings: LoudnessSettings
) -> list[str]:
    return [
        ffmpeg,
        "-hide_banner",
        "-nostats",
        "-i",
        str(source),
        "-map",
        "0:a:0",
        "-af",
        loudnorm_analysis_filter(settings),
        "-f",
        "null",
        "-",
    ]


def ebur128_analysis_command(ffmpeg: str, source: Path) -> list[str]:
    return [
        ffmpeg,
        "-hide_banner",
        "-nostats",
        "-i",
        str(source),
        "-map",
        "0:a:0",
        "-af",
        ebur128_analysis_filter(),
        "-f",
        "null",
        "-",
    ]


def fast_analysis_command(
    ffmpeg: str, source: Path, settings: LoudnessSettings
) -> list[str]:
    return [
        ffmpeg,
        "-hide_banner",
        "-nostats",
        "-i",
        str(source),
        "-map",
        "0:a:0",
        "-af",
        loudnorm_fast_analysis_filter(settings),
        "-f",
        "null",
        "-",
    ]


def conversion_command(
    ffmpeg: str,
    source: Path,
    temporary_output: Path,
    settings: LoudnessSettings,
    measurements: dict[str, str],
    post_gain_db: float = 0.0,
) -> list[str]:
    audio_filter = loudnorm_conversion_filter(settings, measurements)
    if abs(float(post_gain_db)) >= 0.000001:
        audio_filter += f",volume={float(post_gain_db):.8f}dB:precision=double"
    command = [
        ffmpeg,
        "-hide_banner",
        "-nostats",
        "-y",
        "-i",
        str(source),
        "-map",
        "0:a:0",
        "-map_metadata",
        "0",
        "-af",
        audio_filter,
    ]
    command.extend(_artwork_arguments(temporary_output))
    command.extend(source_sample_rate_arguments(temporary_output, measurements))
    command.extend(
        audio_encoding_arguments(
            temporary_output,
            settings.quality,
            measurements.get("_input_codec"),
            measurements.get("_input_bit_depth"),
        )
    )
    command.append(str(temporary_output))
    return command


def audio_encoding_arguments(
    output: Path,
    quality: int,
    input_codec: str | None = None,
    input_bit_depth: str | int | None = None,
) -> list[str]:
    """Return an encoder configuration that matches the output container.

    The UI keeps one simple 0..9 scale: 0 favours fidelity and 9 favours a
    smaller file. Lossless formats remain lossless. FLAC, WAV and AIFF keep
    the source PCM depth when FFmpeg's target codec supports it.
    """
    extension = output.suffix.lower()
    quality = max(0, min(9, int(quality)))
    try:
        bit_depth = int(input_bit_depth) if input_bit_depth is not None else 0
    except (TypeError, ValueError):
        bit_depth = 0
    if not bit_depth:
        codec_depth = re.match(r"pcm_[suf](?P<bits>\d+)", input_codec or "")
        if codec_depth is not None:
            bit_depth = int(codec_depth.group("bits"))

    if extension == ".mp3":
        return [
            "-c:a",
            "libmp3lame",
            "-q:a",
            str(quality),
            "-id3v2_version",
            "3",
        ]
    if extension == ".flac":
        arguments = ["-c:a", "flac"]
        if bit_depth and bit_depth <= 16:
            arguments.extend(["-sample_fmt", "s16"])
        elif bit_depth:
            arguments.extend(["-sample_fmt", "s32"])
        arguments.extend(["-compression_level", "8"])
        return arguments
    if extension == ".wav":
        if bit_depth <= 16 and bit_depth:
            codec = "pcm_s16le"
        elif bit_depth >= 32:
            codec = "pcm_s32le"
        else:
            codec = "pcm_s24le"
        return ["-c:a", codec]
    if extension in {".aif", ".aiff"}:
        if bit_depth <= 16 and bit_depth:
            codec = "pcm_s16be"
        elif bit_depth >= 32:
            codec = "pcm_s32be"
        else:
            codec = "pcm_s24be"
        return ["-c:a", codec]
    if extension == ".m4a":
        bitrates = (256, 256, 224, 192, 176, 160, 144, 128, 96, 80)
        return [
            "-c:a",
            "aac",
            "-b:a",
            f"{bitrates[quality]}k",
            "-movflags",
            "+faststart",
        ]
    if extension == ".ogg":
        # Vorbis uses the opposite scale (larger is better).
        return ["-c:a", "libvorbis", "-q:a", str(max(1, 9 - quality))]
    if extension == ".opus":
        bitrates = (192, 176, 160, 144, 128, 112, 96, 80, 72, 64)
        return [
            "-c:a",
            "libopus",
            "-b:a",
            f"{bitrates[quality]}k",
            "-vbr",
            "on",
        ]
    raise ValueError(f"Unsupported audio output format: {extension or output}")


def source_sample_rate_arguments(
    output: Path,
    measurements: dict[str, str],
) -> list[str]:
    """Return every supported output to the source rate after loudnorm."""
    if output.suffix.lower() not in SUPPORTED_AUDIO_EXTENSIONS:
        return []
    try:
        sample_rate = int(measurements["_input_sample_rate"])
    except (KeyError, TypeError, ValueError):
        return []
    if not 1_000 <= sample_rate <= 768_000:
        return []
    if output.suffix.lower() == ".opus" and sample_rate not in {
        8_000,
        12_000,
        16_000,
        24_000,
        48_000,
    }:
        sample_rate = 48_000
    return ["-ar", str(sample_rate)]


def _artwork_arguments(output: Path) -> list[str]:
    """Preserve an attached picture only in containers that support it well."""
    if output.suffix.lower() in {".mp3", ".flac", ".m4a"}:
        return ["-map", "0:v?", "-c:v", "copy"]
    return []


def replaygain_command(
    ffmpeg: str,
    source: Path,
    temporary_output: Path,
    track_gain_db: float,
    track_peak_dbtp: float,
) -> list[str]:
    command = [
        ffmpeg,
        "-hide_banner",
        "-nostats",
        "-y",
        "-i",
        str(source),
        "-map",
        "0:a:0",
        "-map_metadata",
        "0",
        "-c:a",
        "copy",
        "-metadata",
        f"REPLAYGAIN_TRACK_GAIN={track_gain_db:+.2f} dB",
        "-metadata",
        f"REPLAYGAIN_TRACK_PEAK={dbtp_to_peak_ratio(track_peak_dbtp):.8f}",
    ]
    command.extend(_artwork_arguments(temporary_output))
    suffix = temporary_output.suffix.lower()
    if suffix == ".mp3":
        command.extend(["-id3v2_version", "3"])
    elif suffix in {".aif", ".aiff"}:
        # AIFF stores ReplayGain's free-form fields in an ID3 chunk.
        command.extend(["-write_id3v2", "1", "-id3v2_version", "3"])
    elif suffix == ".m4a":
        # Preserve arbitrary metadata keys in the MP4 container.
        command.extend(["-movflags", "use_metadata_tags"])
    command.append(str(temporary_output))
    return command


def write_replaygain_container_tags(
    output: Path,
    track_gain_db: float,
    track_peak_dbtp: float,
) -> None:
    """Write WAV ReplayGain tags without changing the audio stream.

    FFmpeg's WAV muxer does not retain arbitrary ReplayGain keys.  A compact
    ID3v2.3 ``id3 `` chunk is therefore added to the temporary RIFF file.  The
    rewrite copies every existing chunk byte for byte and atomically replaces
    the temporary output only after the new RIFF size has been validated.
    Other containers are fully handled by :func:`replaygain_command`.
    """
    if output.suffix.lower() != ".wav":
        return

    tag = _replaygain_id3v23_tag(track_gain_db, track_peak_dbtp)
    replacement = output.with_name(f".{output.name}.{uuid.uuid4().hex}.replaygain")
    try:
        with output.open("rb") as source, replacement.open("wb+") as target:
            header = source.read(12)
            if len(header) != 12 or header[:4] != b"RIFF" or header[8:] != b"WAVE":
                raise ValueError("ReplayGain WAV requires a standard RIFF/WAVE file.")
            target.write(header[:4])
            target.write(b"\x00\x00\x00\x00")
            target.write(header[8:])

            existing_tag_written = False
            while True:
                chunk_header = source.read(8)
                if not chunk_header:
                    break
                if len(chunk_header) != 8:
                    raise ValueError("Truncated WAV chunk header.")
                chunk_id = chunk_header[:4]
                chunk_size = struct.unpack("<I", chunk_header[4:])[0]
                if chunk_id.lower() == b"id3 " and not existing_tag_written:
                    _discard_exact(source, chunk_size + (chunk_size & 1))
                    _write_riff_chunk(target, b"id3 ", tag)
                    existing_tag_written = True
                    continue
                target.write(chunk_header)
                _copy_exact(source, target, chunk_size + (chunk_size & 1))

            if not existing_tag_written:
                _write_riff_chunk(target, b"id3 ", tag)
            final_size = target.tell()
            riff_size = final_size - 8
            if riff_size > 0xFFFFFFFF:
                raise ValueError("ReplayGain WAV exceeds the RIFF 4 GiB limit.")
            target.seek(4)
            target.write(struct.pack("<I", riff_size))
            target.flush()
            os.fsync(target.fileno())
        os.chmod(replacement, output.stat().st_mode)
        os.replace(replacement, output)
    finally:
        try:
            replacement.unlink()
        except FileNotFoundError:
            pass


def _synchsafe_size(value: int) -> bytes:
    if not 0 <= value <= 0x0FFFFFFF:
        raise ValueError("ID3 payload is too large.")
    return bytes(
        (
            (value >> 21) & 0x7F,
            (value >> 14) & 0x7F,
            (value >> 7) & 0x7F,
            value & 0x7F,
        )
    )


def _id3v23_text_frame(description: str, value: str) -> bytes:
    # ReplayGain descriptions and values are ASCII, so ID3's Latin-1 encoding
    # avoids BOM and version-specific Unicode ambiguities.
    payload = b"\x00" + description.encode("ascii") + b"\x00" + value.encode("ascii")
    return b"TXXX" + struct.pack(">I", len(payload)) + b"\x00\x00" + payload


def _replaygain_id3v23_tag(
    track_gain_db: float,
    track_peak_dbtp: float,
) -> bytes:
    frames = b"".join(
        (
            _id3v23_text_frame(
                "REPLAYGAIN_TRACK_GAIN",
                f"{track_gain_db:+.2f} dB",
            ),
            _id3v23_text_frame(
                "REPLAYGAIN_TRACK_PEAK",
                f"{dbtp_to_peak_ratio(track_peak_dbtp):.8f}",
            ),
        )
    )
    padding = b"\x00" * 256
    payload = frames + padding
    return b"ID3\x03\x00\x00" + _synchsafe_size(len(payload)) + payload


def _copy_exact(source: Any, target: Any, size: int) -> None:
    remaining = size
    while remaining:
        block = source.read(min(1024 * 1024, remaining))
        if not block:
            raise ValueError("Truncated WAV chunk.")
        target.write(block)
        remaining -= len(block)


def _discard_exact(source: Any, size: int) -> None:
    remaining = size
    while remaining:
        block = source.read(min(1024 * 1024, remaining))
        if not block:
            raise ValueError("Truncated WAV metadata chunk.")
        remaining -= len(block)


def _write_riff_chunk(target: Any, chunk_id: bytes, payload: bytes) -> None:
    target.write(chunk_id)
    target.write(struct.pack("<I", len(payload)))
    target.write(payload)
    if len(payload) & 1:
        target.write(b"\x00")


def metadata_dump_command(ffmpeg: str, source: Path) -> list[str]:
    return [
        ffmpeg,
        "-hide_banner",
        "-nostats",
        "-i",
        str(source),
        "-map_metadata",
        "0",
        "-map_metadata",
        "0:s:a:0",
        "-f",
        "ffmetadata",
        "-",
    ]


def replaygain_metadata_is_present(metadata: str) -> bool:
    normalized = metadata.upper()
    required = {
        "REPLAYGAIN_TRACK_GAIN",
        "REPLAYGAIN_TRACK_PEAK",
    }
    return all(field in normalized for field in required)


def assess_quality(
    settings: LoudnessSettings,
    input_measurements: dict[str, str],
    output_measurements: dict[str, str],
    *,
    applied_gain_db: float | None = None,
    preserve_audio: bool = False,
    lufs_tolerance: float = QUALITY_CONTROL_LUFS_TOLERANCE,
    peak_tolerance: float = QUALITY_CONTROL_TRUE_PEAK_TOLERANCE_DB,
    language: str = "fr",
) -> QualityResult:
    if not measurements_are_finite(input_measurements):
        if measurements_are_finite(output_measurements):
            return QualityResult(False, core_text(language, "output_not_silent"))
        return QualityResult(True, core_text(language, "silent_preserved"))
    if not measurements_are_finite(output_measurements):
        return QualityResult(False, core_text(language, "output_unmeasurable"))

    input_lufs = float(input_measurements["input_i"])
    output_lufs = float(output_measurements["input_i"])
    input_peak = float(input_measurements["input_tp"])
    output_peak = float(output_measurements["input_tp"])
    issues: list[str] = []

    if preserve_audio:
        if abs(output_lufs - input_lufs) - lufs_tolerance > 1e-9:
            issues.append(
                core_text(
                    language,
                    "loudness_changed",
                    value=output_lufs - input_lufs,
                )
            )
        if abs(output_peak - input_peak) > peak_tolerance:
            issues.append(
                core_text(
                    language,
                    "peak_changed",
                    value=output_peak - input_peak,
                )
            )
    else:
        expected_lufs = (
            settings.integrated_lufs
            if applied_gain_db is None
            else input_lufs + applied_gain_db
        )
        if abs(output_lufs - expected_lufs) - lufs_tolerance > 1e-9:
            loudness_issue = core_text(
                language,
                "unexpected_loudness",
                actual=output_lufs,
                expected=expected_lufs,
            )
            issues.append(loudness_issue)
        if output_peak > settings.true_peak + peak_tolerance:
            issues.append(
                core_text(
                    language,
                    "peak_above_limit",
                    value=output_peak,
                )
            )

    if issues:
        return QualityResult(False, " ; ".join(issues))
    return QualityResult(True, core_text(language, "measurements_ok"))
