"""Input validation, artwork repair and safe delivery of completed audio."""
from __future__ import annotations

import errno
import io
import math
import os
from pathlib import Path
import shutil
import uuid

from PIL import Image
from mutagen.id3 import ID3, ID3NoHeaderError


class InvalidAudioError(ValueError):
    pass


class ArtworkError(ValueError):
    pass


def validate_measurements(measurements):
    """Reject unsafe measured parameters; preserve the normal silence case."""
    values = {k: float(measurements[k]) for k in
              ('input_i', 'input_tp', 'input_lra', 'input_thresh', 'target_offset')}
    if values['input_i'] == -math.inf and values['input_tp'] == -math.inf:
        return
    ranges = {'input_i': (-99, 0), 'input_tp': (-99, 99),
              'input_lra': (0, 99), 'input_thresh': (-99, 0), 'target_offset': (-99, 99)}
    for key, value in values.items():
        low, high = ranges[key]
        if not math.isfinite(value) or not low <= value <= high:
            raise InvalidAudioError(f'{key}={value:g}; allowed range: {low} to {high}')


def repaired_mp3_source(source: Path, folder: Path) -> tuple[Path, int]:
    """Repair APIC on a private copy. Never rewrite the original MP3/audio."""
    if source.suffix.lower() != '.mp3':
        return source, 0
    try:
        tags = ID3(source)
    except ID3NoHeaderError:
        return source, 0
    fixed = 0
    for picture in tags.getall('APIC'):
        # ID3 permits linked pictures. Do not download remote content.
        if picture.mime == '-->':
            raise ArtworkError('Linked artwork cannot be embedded automatically')
        try:
            with Image.open(io.BytesIO(picture.data)) as img:
                detected = img.format
                img.load()
                expected = {'JPEG': 'image/jpeg', 'PNG': 'image/png'}.get(detected)
                if expected and picture.mime.lower() in (
                        (expected, 'image/jpg') if detected == 'JPEG' else (expected,)):
                    continue
                if expected:
                    picture.mime = expected
                else:
                    encoded = io.BytesIO()
                    img.convert('RGBA' if 'A' in img.getbands() else 'RGB').save(encoded, format='PNG')
                    picture.data = encoded.getvalue()
                    picture.mime = 'image/png'
                fixed += 1
        except Exception as exc:
            raise ArtworkError(f'Artwork cannot be decoded: {exc}') from exc
    if not fixed:
        return source, 0
    input_folder = folder / 'input'
    input_folder.mkdir()
    target = input_folder / source.name
    shutil.copy2(source, target)
    tags.save(target, v2_version=3)
    return target, fixed


def require_destination_volume(destination: Path):
    # Do not recreate /Volumes/Name as a directory on the internal disk after
    # a removable drive disappears. Mount points supplied by macOS are real.
    parts = destination.absolute().parts
    if len(parts) >= 3 and parts[1] == 'Volumes':
        mount = Path(*parts[:3])
        if not mount.is_mount():
            raise OSError(errno.ENODEV, 'Destination volume is not mounted', str(mount))


def publish_completed(source: Path, destination: Path, wait):
    """Stage on the destination volume, flush, then atomically replace."""
    require_destination_volume(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = destination.with_name(f'.{destination.name}.{uuid.uuid4().hex}.delivery')
    try:
        with source.open('rb') as src, staging.open('xb') as dst:
            while True:
                wait()
                block = src.read(1024 * 1024)
                if not block:
                    break
                dst.write(block)
            dst.flush()
            os.fsync(dst.fileno())
        wait()
        require_destination_volume(destination)
        os.replace(staging, destination)
    finally:
        try:
            staging.unlink(missing_ok=True)
        except OSError:
            pass
