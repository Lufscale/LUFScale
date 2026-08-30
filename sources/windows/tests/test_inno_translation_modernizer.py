from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.modernize_inno_translation import build_translation, read_sections


PROJECT_ROOT = Path(__file__).parents[1]
HINDI_SUPPLEMENT = (
    PROJECT_ROOT
    / "packaging/windows/languages/Hindi-6.7.3-supplement.isl"
)


class InnoTranslationModernizerTests(unittest.TestCase):
    def test_build_filters_obsolete_entries_and_fills_current_messages(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            reference = root / "Default.isl"
            legacy = root / "Legacy.isl"
            supplement = root / "Supplement.isl"
            output = root / "Current.isl"
            reference.write_text(
                "[Messages]\nGreeting=Hello %1\nNewMessage=Install [name]\n"
                "[CustomMessages]\nLaunch=Launch %1\n",
                encoding="utf-8",
            )
            legacy.write_text(
                "[LangOptions]\nLanguageName=Test\nLanguageID=$0409\n"
                "LanguageCodePage=0\nTitleFontSize=35\n"
                "[Messages]\nGreeting=Bonjour %1\nObsoleteMessage=Old\n"
                "[CustomMessages]\nLaunch=Lancer %1\n",
                encoding="utf-8",
            )
            supplement.write_text(
                "[Messages]\nNewMessage=Installer [name]\n",
                encoding="utf-8",
            )

            build_translation(
                reference,
                legacy,
                supplement,
                output,
                "Test",
                "6.7.3",
            )

            current = read_sections(output)
            self.assertEqual(
                current["Messages"],
                {"Greeting": "Bonjour %1", "NewMessage": "Installer [name]"},
            )
            self.assertEqual(current["CustomMessages"], {"Launch": "Lancer %1"})
            self.assertNotIn("TitleFontSize", current["LangOptions"])
            self.assertNotIn("ObsoleteMessage", current["Messages"])

    def test_placeholder_mismatch_stops_generation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            reference = root / "Default.isl"
            legacy = root / "Legacy.isl"
            supplement = root / "Supplement.isl"
            reference.write_text(
                "[Messages]\nGreeting=Hello %1\n[CustomMessages]\n",
                encoding="utf-8",
            )
            legacy.write_text(
                "[LangOptions]\nLanguageName=Test\nLanguageID=$0409\n"
                "LanguageCodePage=0\n[Messages]\nGreeting=Hello\n"
                "[CustomMessages]\n",
                encoding="utf-8",
            )
            supplement.write_text("[Messages]\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Placeholder mismatch"):
                build_translation(
                    reference,
                    legacy,
                    supplement,
                    root / "Current.isl",
                    "Test",
                    "6.7.3",
                )

    def test_hindi_supplement_covers_missing_and_incompatible_messages(self) -> None:
        sections = read_sections(HINDI_SUPPLEMENT)
        messages = sections["Messages"]
        self.assertEqual(len(messages), 70)
        for key in (
            "PrivilegesRequiredOverrideTitle",
            "DownloadingLabel2",
            "ArchiveUnsupportedFormat",
            "VerificationFileHashIncorrect",
            "UninstallDisplayNameMarkCurrentUser",
            "InvalidParameter",
            "WindowsVersionNotSupported",
            "FinishedRestartLabel",
        ):
            self.assertIn(key, messages)
        self.assertEqual(
            sections["CustomMessages"],
            {"AutoStartProgram": "%1 को स्वचालित रूप से आरंभ करें"},
        )
        for obsolete in (
            "MissingWOW64APIs",
            "EntryAbortRetryIgnore",
            "FileAbortRetryIgnore",
            "ExistingFileReadOnly",
            "FileExists",
            "ExistingFileNewer",
        ):
            self.assertNotIn(obsolete, messages)


if __name__ == "__main__":
    unittest.main()
