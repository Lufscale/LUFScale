import importlib.util
from pathlib import Path
import plistlib
import struct
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('icon_check', ROOT/'tools/verify_application_icon.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


class IconPackagingTests(unittest.TestCase):
    def test_mac_declared_icon_matches_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            contents = root/'LUFScale.app/Contents'
            (contents/'Resources').mkdir(parents=True)
            icon = b'icns' + struct.pack('>I', 16) + b'icp4' + struct.pack('>I',8)
            source = root/'source.icns'
            source.write_bytes(icon)
            (contents/'Resources/LUFScale.icns').write_bytes(icon)
            plist = contents/'Info.plist'
            plist.write_bytes(plistlib.dumps({'CFBundleIconFile':'LUFScale.icns'}))
            check.verify_mac(root/'LUFScale.app',source)
            plist.write_bytes(plistlib.dumps({}))
            with self.assertRaises(ValueError): check.verify_mac(root/'LUFScale.app',source)
            plist.write_bytes(plistlib.dumps({'CFBundleIconFile':'missing.icns'}))
            with self.assertRaises(FileNotFoundError): check.verify_mac(root/'LUFScale.app',source)
            plist.write_bytes(plistlib.dumps({'CFBundleIconFile':'LUFScale.icns'}))
            source.write_bytes(icon+b'different')
            with self.assertRaises(ValueError): check.verify_mac(root/'LUFScale.app',source)

    def test_windows_ico_has_seven_sizes_and_rejects_truncation(self):
        icon = ROOT/'assets/branding/LUFScale.ico'
        self.assertEqual(len(check.ico_images(icon)),7)
        with tempfile.TemporaryDirectory() as tmp:
            truncated = Path(tmp)/'bad.ico'
            truncated.write_bytes(icon.read_bytes()[:-1])
            with self.assertRaises(ValueError): check.ico_images(truncated)

