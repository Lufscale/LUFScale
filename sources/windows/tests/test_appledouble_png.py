"""Regression coverage for the 2.2.3 import and artwork fixes."""
import contextlib
import io
import runpy
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from lufscale.audio.core import build_jobs, canonicalize_inputs, is_supported_audio_file
from lufscale.processing.runtime import concise_ffmpeg_error


class AppleDoubleTests(unittest.TestCase):
    def test_file_types(self):
        for extension in ("mp3", "flac", "wav", "aif", "aiff", "m4a", "ogg", "opus"):
            self.assertFalse(is_supported_audio_file(f"._track.{extension}"))
            self.assertTrue(is_supported_audio_file(f"track.{extension.upper()}"))
        self.assertTrue(is_supported_audio_file(".hidden.mp3"))
        self.assertTrue(is_supported_audio_file("song._part.mp3"))

    def test_recursive_and_direct_imports(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "album"
            source.mkdir()
            sub = source / "disc2"
            sub.mkdir()
            metadata = source / "__MACOSX"
            metadata.mkdir()
            paths = [source / "track.mp3", sub / "track.flac",
                     source / "._track.mp3", sub / "._track.flac",
                     metadata / "track.mp3"]
            for path in paths:
                path.write_bytes(b"fixture")
            jobs = build_jobs([source], root / "output")
            self.assertEqual({j.source for j in jobs}, set(paths[:2]))
            self.assertEqual(canonicalize_inputs(paths[2:]), [])
            self.assertEqual(canonicalize_inputs([metadata]), [])
            self.assertTrue(all(path.exists() for path in paths))

    def test_error_keeps_dimensions_before_generic_tail(self):
        error = concise_ffmpeg_error(
            "[mp3] dimensions not set\n"
            "Could not write header: Invalid argument\n"
            "Error while filtering\n"
            "Task finished with error code: -22 (Invalid argument)\n"
            "Terminating thread with return code -22\nConversion failed!"
        )
        self.assertIn("dimensions not set", error)
        self.assertIn("Conversion failed!", error)


@unittest.skipUnless(shutil.which("ffmpeg"), "requires a development FFmpeg")
class PNGIntegrationTests(unittest.TestCase):
    def test_builder_artwork_check_and_missing_decoder_failure(self):
        script = Path(__file__).parents[1] / "tools/prepare_bundled_ffmpeg_windows.py"
        validate = runpy.run_path(str(script))["validate_png_artwork"]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with contextlib.redirect_stdout(io.StringIO()):
                validate(Path(shutil.which("ffmpeg")), root)
            # Reproduce a runtime without PNG decoding, while keeping MP3
            # decoding and packet-copy enabled. Failure must not be hidden.
            result = subprocess.run([
                shutil.which("ffmpeg"), "-hide_banner", "-y",
                "-codec_whitelist", "mp3,mp3float,mjpeg",
                "-i", str(root / "png-source.mp3"), "-map", "0",
                "-c", "copy", str(root / "missing-decoder.mp3"),
            ], capture_output=True, text=True, timeout=30)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("dimensions not set", result.stderr)


if __name__ == "__main__":
    unittest.main()
