"""Check the packaging guard against missing, modified and wrong-version PDFs."""
import hashlib
import json
from pathlib import Path
import runpy
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
VERIFY = runpy.run_path(str(ROOT / 'tools/verify_approved_guides.py'))['verify']


class ApprovedGuideTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for relative in ['src/lufscale/version.py', 'src/lufscale/resources.py']:
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)
        names = runpy.run_path(str(ROOT / 'src/lufscale/resources.py'))['PDF_GUIDES'].values()
        directory = self.root / 'output/pdf'
        directory.mkdir(parents=True)
        hashes = {}
        for name in names:
            data = b'%PDF-1.4\n' + name.encode()
            (directory / name).write_bytes(data)
            hashes[name] = hashlib.sha256(data).hexdigest()
        (self.root / 'packaging').mkdir()
        self.manifest = self.root / 'packaging/approved-guides.json'
        self.manifest.write_text(json.dumps({'app_version': '2.2.3', 'sha256': hashes}))

    def test_real_approved_set(self):
        VERIFY(ROOT)

    def test_missing_guide_is_rejected(self):
        (self.root / 'output/pdf/Guide_LUFScale_FR.pdf').unlink()
        with self.assertRaises(ValueError): VERIFY(self.root)

    def test_modified_guide_is_rejected(self):
        (self.root / 'output/pdf/Guide_LUFScale_FR.pdf').write_bytes(b'%PDF-1.4\nchanged')
        with self.assertRaisesRegex(ValueError, 'damaged or has changed'): VERIFY(self.root)

    def test_extra_guide_is_rejected(self):
        (self.root / 'output/pdf/other.pdf').write_bytes(b'%PDF-1.4')
        with self.assertRaises(ValueError): VERIFY(self.root)

    def test_wrong_version_is_rejected(self):
        data = json.loads(self.manifest.read_text()); data['app_version'] = '2.2.2'
        self.manifest.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'application version'): VERIFY(self.root)

    def test_manifest_cannot_drop_a_language(self):
        data = json.loads(self.manifest.read_text()); del data['sha256']['Guide_LUFScale_FR.pdf']
        self.manifest.write_text(json.dumps(data))
        with self.assertRaises(ValueError): VERIFY(self.root)
