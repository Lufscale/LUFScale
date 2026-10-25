"""Exercise the actual PyInstaller input validation without native compilation."""
import os
from pathlib import Path
import runpy
import shutil
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]

class PackagedGuidesTests(unittest.TestCase):
    def check_specs(self, modification=None, error=None):
        specs = sorted((ROOT / 'packaging').glob('*/*.spec'))
        self.assertTrue(specs)
        for spec in specs:
            with self.subTest(spec=spec.name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                for relative in ('src/lufscale/resources.py', 'src/lufscale/version.py'):
                    target = root / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(ROOT / relative, target)
                guides = root / 'output/pdf'
                guides.mkdir(parents=True)
                names = runpy.run_path(str(ROOT / 'src/lufscale/resources.py'))['PDF_GUIDES']
                for name in names.values():
                    (guides / name).write_bytes(b'fixture')
                if modification:
                    modification(guides)
                for relative in ('.build-macos/LUFScale.icns', 'assets/branding/LUFScale.ico', 'ffmpeg'):
                    target = root / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(b'fixture')
                prefix = spec.read_text().split('a = Analysis(', 1)[0]
                namespace = {'SPECPATH': str(root / 'packaging' / spec.parent.name)}
                with patch.dict(os.environ, {'LUFSCALE_BUNDLED_FFMPEG': str(root / 'ffmpeg'),
                                              'LUFSCALE_GUIDES_DIR': str(guides)}):
                    if error:
                        with self.assertRaisesRegex(FileNotFoundError, error):
                            exec(compile(prefix, str(spec), 'exec'), namespace)
                    else:
                        exec(compile(prefix, str(spec), 'exec'), namespace)

    def test_all_twelve_guides_accepted(self):
        self.check_specs()

    def test_missing_translation_rejected(self):
        self.check_specs(lambda guides: (guides / 'Guide_LUFScale_FR.pdf').unlink(), 'Guide_LUFScale_FR.pdf')

    def test_empty_translation_rejected(self):
        self.check_specs(lambda guides: (guides / 'Guide_LUFScale_FR.pdf').write_bytes(b''), 'Guide_LUFScale_FR.pdf')

    def test_unexpected_guide_rejected(self):
        self.check_specs(lambda guides: (guides / 'unexpected.pdf').write_bytes(b'fixture'), 'unexpected.pdf')
