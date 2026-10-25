import shutil
import subprocess
import tempfile
import unittest
import contextlib
import io
import os
import runpy
import sys
import threading
from unittest import mock
from pathlib import Path


@unittest.skipUnless(shutil.which("zsh"), "requires zsh")
class BuildProgressTests(unittest.TestCase):
    def run_fixture(self, exit_code):
        source = Path(__file__).parents[1] / "tools/Build_Progress_macOS.command"
        with tempfile.TemporaryDirectory(prefix="lufscale test ") as temp:
            root = Path(temp)
            (root / "tools").mkdir()
            shutil.copy2(source, root / "tools/Build_Progress_macOS.command")
            (root / "Create_Community_Distribution_macOS.command").write_text(
                'printf "2|Fixture stage\\n" > "$LUFSCALE_PROGRESS_FILE"\n'
                'echo detailed-build-output\necho detailed-error-output >&2\n'
                f'sleep 0.1\nexit {exit_code}\n'
            )
            result = subprocess.run([shutil.which("zsh"), str(root / "tools/Build_Progress_macOS.command")],
                                    capture_output=True, text=True, timeout=10)
            logs = list((root / "build-logs").glob("*.log"))
            self.assertEqual(len(logs), 1)
            self.assertIn("detailed-build-output", logs[0].read_text())
            self.assertIn("detailed-error-output", logs[0].read_text())
            return result

    def test_success_hides_detail_and_finishes_bar(self):
        result = self.run_fixture(0)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("8/8", result.stdout)
        self.assertNotIn("detailed-build-output", result.stdout)

    def test_failure_preserves_exit_code_and_shows_diagnostic(self):
        result = self.run_fixture(7)
        self.assertEqual(result.returncode, 7, result.stderr)
        self.assertIn("FAILED", result.stdout)
        self.assertIn("detailed-error-output", result.stdout)
        self.assertNotIn("8/8", result.stdout)

    def test_success_retains_one_completed_bar_per_stage(self):
        result = self.run_fixture(0)
        self.assertEqual(result.stdout.count("[====================] Complete"), 8)
        for stage in range(1, 9):
            self.assertIn(f"Stage {stage}/8", result.stdout)


class FFmpegStreamingTests(unittest.TestCase):
    def test_command_output_is_visible_before_process_finishes(self):
        script = Path(__file__).parents[1] / "tools/build_bundled_ffmpeg_macos.py"
        run = runpy.run_path(str(script))["run"]
        observed = threading.Event()
        result = []
        errors = []
        class Sink(io.StringIO):
            def write(self, value):
                if value.startswith("CC "):
                    observed.set()
                return super().write(value)
        with tempfile.TemporaryDirectory() as temp:
            detail = Path(temp) / "detail"
            def worker():
                try:
                    result.append(run([sys.executable, "-c",
                        "import time; print('CC object.o', flush=True); time.sleep(1); print('done')"]))
                except Exception as exc:
                    errors.append(exc)
            with mock.patch.dict(os.environ, {"LUFSCALE_DETAIL_FILE": str(detail)}):
                with contextlib.redirect_stdout(Sink()):
                    thread = threading.Thread(target=worker)
                    thread.start()
                    try:
                        self.assertTrue(observed.wait(5))
                        self.assertTrue(thread.is_alive(), "output was buffered until command exit")
                    finally:
                        thread.join(5)
                self.assertFalse(errors, errors)
                self.assertEqual(result, ["CC object.o\ndone\n"])
                self.assertIn("1 operations", detail.read_text())
