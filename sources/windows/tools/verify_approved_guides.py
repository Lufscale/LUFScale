"""Validate the approved PDF set before packaging; never regenerate it."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]


def verify(root: Path = ROOT) -> None:
    version = runpy.run_path(str(root / 'src/lufscale/version.py'))['APP_VERSION']
    expected = set(runpy.run_path(str(root / 'src/lufscale/resources.py'))['PDF_GUIDES'].values())
    manifest = json.loads((root / 'packaging/approved-guides.json').read_text(encoding='utf-8'))
    if manifest.get('app_version') != version:
        raise ValueError('The approved guide manifest does not match the application version.')
    hashes = manifest.get('sha256', {})
    directory = root / 'output/pdf'
    actual = {p.name for p in directory.glob('*.pdf') if p.is_file()}
    if len(expected) != 12 or set(hashes) != expected or actual != expected:
        raise ValueError('Exactly twelve approved guides are required; a guide is missing or unexpected.')
    for name in sorted(expected):
        data = (directory / name).read_bytes()
        if not data.startswith(b'%PDF-') or hashlib.sha256(data).hexdigest() != hashes[name]:
            raise ValueError(f'The approved guide is damaged or has changed: {name}')
    print(f'Verified all twelve approved PDF guides for LUFScale {version}.')


if __name__ == '__main__':
    verify()
