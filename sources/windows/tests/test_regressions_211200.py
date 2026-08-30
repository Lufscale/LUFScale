from __future__ import annotations

import json
import runpy
import struct
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from lufscale.audio.core import (
    QUALITY_CONTROL_LUFS_TOLERANCE,
    QUALITY_CONTROL_TRUE_PEAK_TOLERANCE_DB,
    REQUIRED_AUDIO_ENCODERS,
    STRICT_TARGET_LUFS_TOLERANCE,
    LoudnessSettings,
    assess_quality,
    build_jobs,
    canonicalize_inputs,
    dynamic_mp3_output_is_strictly_compliant,
    is_supported_audio_file,
    iter_audio_files,
    metadata_dump_command,
    replaygain_command,
    validate_output,
)
from lufscale.i18n.loader import EXTRA_TEXTS, LANGUAGES, TEXTS, translate
from lufscale.i18n.guide_technical import (
    COMPLIANCE_COPY,
    REFERENCE_COPY,
    TECHNICAL_COPY,
)
from lufscale.i18n.guide_build import PLATFORM_BUILD_COPY
from lufscale.i18n.guide_checks import USEFUL_CHECKS_COPY
from lufscale.resources import PDF_GUIDES, localized_guide_path
from lufscale.ui.help_catalog import HELP_DIALOG_SECTIONS
from lufscale.ui.settings import SettingsController
from lufscale.version import APP_VERSION, APP_WEBSITE_URL


PROJECT_ROOT = Path(__file__).parents[1]


class WindowsPortRegressionTests(unittest.TestCase):
    def test_language_popup_marks_only_the_current_choice(self) -> None:
        self.assertEqual(len(LANGUAGES), 12)
        widgets = (
            PROJECT_ROOT / "src/lufscale/ui/widgets/components.py"
        ).read_text("utf-8")
        header = (
            PROJECT_ROOT / "src/lufscale/ui/panels/header.py"
        ).read_text("utf-8")
        delegate = widgets.split(
            "class _CurrentLanguageCheckDelegate", 1
        )[1].split("class LanguageComboBox", 1)[0]
        language_combo = widgets.split("class LanguageComboBox", 1)[1].split(
            "class OptionHelpButton", 1
        )[0]

        self.assertIn("language_combo = LanguageComboBox()", header)
        self.assertIn(
            "self.view().setItemDelegate(self._current_language_delegate)",
            language_combo,
        )
        self.assertIn(
            "index.row() != self._combo.currentIndex()",
            delegate,
        )
        self.assertIn("painter.drawLine", delegate)
        self.assertNotIn("paintEvent", language_combo)
        self.assertNotIn("CheckStateRole", delegate + language_combo + header)

    def test_release_identity_and_records(self) -> None:
        self.assertEqual(APP_VERSION, "2.1.12")
        self.assertTrue((PROJECT_ROOT / "RELEASE_2.1.12.md").is_file())
        self.assertTrue((PROJECT_ROOT / "VALIDATION_2.1.12.md").is_file())
        self.assertFalse((PROJECT_ROOT / "RELEASE_2.1.8.md").exists())
        self.assertFalse((PROJECT_ROOT / "VALIDATION_2.1.8.md").exists())
        sbom = json.loads((PROJECT_ROOT / "SBOM.cdx.json").read_text("utf-8"))
        self.assertEqual(sbom["metadata"]["component"]["version"], APP_VERSION)

        version_info = (
            PROJECT_ROOT / "packaging/windows/version_info.txt"
        ).read_text("utf-8")
        for marker in (
            "filevers=(2, 1, 12, 0)",
            "prodvers=(2, 1, 12, 0)",
            "StringStruct('FileVersion', '2.1.12')",
            "StringStruct('ProductVersion', '2.1.12')",
        ):
            self.assertIn(marker, version_info)

    def test_official_website_link_is_visible_localized_and_actionable(self) -> None:
        self.assertEqual(APP_WEBSITE_URL, "https://lufscale.net")
        for language, _label in LANGUAGES:
            self.assertTrue(translate(language, "official_website").strip())
            self.assertTrue(
                translate(language, "official_website_tooltip").strip()
            )
            if language not in {"fr", "en"}:
                self.assertIn("official_website", EXTRA_TEXTS[language])
                self.assertIn("official_website_tooltip", EXTRA_TEXTS[language])

        application = (
            PROJECT_ROOT / "src/lufscale/application.py"
        ).read_text("utf-8")
        widgets = (
            PROJECT_ROOT / "src/lufscale/ui/widgets/components.py"
        ).read_text("utf-8")
        theme = (
            PROJECT_ROOT / "src/lufscale/ui/themes.py"
        ).read_text("utf-8")
        for marker in (
            "ExternalLinkButton(APP_WEBSITE_URL)",
            "status_bar.setContentsMargins(8, 0, 5, 0)",
            "status_bar.addPermanentWidget(self.website_link)",
            "self.website_link.clicked.connect(self.open_official_website)",
            'QDesktopServices.openUrl(QUrl(APP_WEBSITE_URL))',
            "self.t('official_website')",
        ):
            self.assertIn(marker, application)
        self.assertIn("link_font.setUnderline(enabled)", widgets)
        self.assertIn("QPushButton#websiteLink:hover", theme)
        website_style = theme.split(
            "QPushButton#websiteLink {", 1
        )[1].split("}", 1)[0]
        self.assertIn("color: #9eabb8", website_style)
        self.assertIn("font-size: 12px", website_style)
        self.assertIn("font-weight: 400", website_style)
        self.assertNotIn("#63b5eb", website_style)

    def test_pdf_overview_uses_aligned_steps_and_complete_start_label(self) -> None:
        generator = (PROJECT_ROOT / "tools/generate_guides.py").read_text("utf-8")
        for marker in (
            "step_height = 66",
            "step_gap = (interface_height - 4 * step_height) / 3",
            "marker_y = card_y + step_height / 2",
            'translate(language, "start"),',
            "progress_width = width - 115",
            "cpu_right_x = x + width - 77",
            "start_button_x = x + width - 72",
            "start_button_width = 44",
        ):
            self.assertIn(marker, generator)
        self.assertNotIn('sanitize(translate(language, "start"))[:13]', generator)
        self.assertNotIn("width - 100", generator)

    def test_processing_log_preserves_compact_script_aware_spacing(self) -> None:
        execution = (
            PROJECT_ROOT / "src/lufscale/ui/execution.py"
        ).read_text("utf-8")
        for marker in (
            'LOG_TEXT_FONT_FAMILY = "DejaVu Sans"',
            "LOG_TEXT_FONT_SIZE_PX = 12",
            "LOG_TEXT_FONT_WEIGHT = 400",
            "LOG_LINE_HEIGHT_PX = 16.0",
            "LOG_SCRIPT_FONT_SIZE_PX = 11",
            "LOG_SCRIPT_FONT_WEIGHT = 600",
            "LOG_KOREAN_LINE_HEIGHT_PX = 17.0",
            "LOG_CHINESE_LINE_HEIGHT_PX = 19.0",
            "LOG_HIGHLIGHT_GAP_PX = 1.0",
            "LOG_JAPANESE_LINE_HEIGHT_PX = 17.0",
            "LOG_DEVANAGARI_LINE_HEIGHT_PX = 20.0",
            "LOG_DEVANAGARI_WINDOWS_11_GAP_PX = 3.0",
            "WINDOWS_11_MINIMUM_BUILD = 22000",
            '"ja": (JAPANESE_LOG_RUN_PATTERN, "Noto Sans JP Thin")',
            '"ko": (KOREAN_LOG_RUN_PATTERN, "Noto Sans KR Thin")',
            "def compact_script_runs_html(safe_message: str, language: str) -> str:",
            "compact_script_runs_html(html.escape(message), language)",
            "def log_line_height_px(message: str, language: str = \"\") -> float:",
            "JAPANESE_LOG_PATTERN.search(message)",
            "KOREAN_LOG_PATTERN.search(message)",
            "HAN_LOG_PATTERN.search(message)",
            "DEVANAGARI_LOG_PATTERN.search(message)",
            "def log_content_line_height_px(message: str, language: str = \"\") -> float:",
            "def log_highlight_gap_px(message: str, language: str = \"\") -> float:",
            "uses_devanagari = language == \"hi\" or DEVANAGARI_LOG_PATTERN.search(message)",
            "log_highlight_gap_px(message, language)",
            "log_content_line_height_px(message, self.owner.language),",
            "block_format.setTopMargin(0.0)",
            "log_highlight_gap_px(message, self.owner.language)",
            "QTextBlockFormat.LineHeightTypes.FixedHeight.value",
            "cursor.setBlockFormat(block_format)",
            "cursor.movePosition(QTextCursor.MoveOperation.End)",
            "cursor.insertBlock(block_format)",
            "cursor.insertHtml(",
            "def inverse_log_text_format(",
            "source_format: QTextCharFormat,",
            "inverse_format = QTextCharFormat(source_format)",
            "inverse_format.setForeground(QBrush(QColor(background_color)))",
            "inverse_format.setBackground(QBrush(QColor(text_color)))",
            "surrounding_format = cursor.charFormat()",
            "cursor.insertText(",
            "inverse_log_text_format(",
            "surrounding_format,",
            'if self.owner.language == "hi" and is_windows_11_or_newer():',
            "transition_format.clearBackground()",
            "transition_format.setFontStyleStrategy(",
            "CONTROLLED_LOG_HIGHLIGHT_HEIGHT_PROPERTY",
            "QFont.StyleStrategy.NoFontMerging",
            "if not cursor.atStart():",
        ):
            self.assertIn(marker, execution)
        self.assertEqual(
            execution.count("QFont.StyleStrategy.NoFontMerging"),
            1,
        )
        self.assertNotIn("LOG_JAPANESE_LUFS_LINE_HEIGHT_PX", execution)
        self.assertNotIn("LOG_JAPANESE_HIGHLIGHT_HEIGHT_PX", execution)
        self.assertNotIn("LOG_JAPANESE_HIGHLIGHT_FILL_HEIGHT_PX", execution)
        inverse_function = execution.split("def inverse_log_text_format", 1)[1].split(
            "def log_content_line_height_px", 1
        )[0]
        self.assertNotIn("setFont", inverse_function)
        self.assertNotIn("QFont", inverse_function)
        self.assertNotIn("LOG_BADGE_FONT_", execution)
        self.assertNotIn("LOG_BADGE_SUBPIXEL_WEIGHT_OFFSET_PX", execution)
        self.assertNotIn("LOG_JAPANESE_LINE_HEIGHT_PX = 25.0", execution)
        self.assertNotIn("def log_line_bottom_margin_px", execution)
        self.assertNotIn("document().isEmpty()", execution)
        for bitmap_marker in (
            "QImage",
            "QPainter",
            "QTextImageFormat",
            "cursor.insertImage(",
            "ImageResource",
            "devicePixelRatioF()",
            "make_lufs_badge_image",
        ):
            self.assertNotIn(bitmap_marker, execution)
        self.assertNotIn(
            "QTextBlockFormat.LineHeightTypes.FixedHeight,\n",
            execution,
        )
        render_method = execution.split("def _render_log_entry", 1)[1].split(
            "def rerender_log_entries", 1
        )[0]
        self.assertLess(
            render_method.index("self._insert_log_message("),
            render_method.index("cursor.setBlockFormat(block_format)"),
        )
        self.assertNotIn("self.owner.log_box.append(", execution)
        themes = (PROJECT_ROOT / "src/lufscale/ui/themes.py").read_text("utf-8")
        log_style = themes.split("QTextEdit#logBox {", 1)[1].split("}", 1)[0]
        for marker in (
            'font-family: "DejaVu Sans", "Noto Sans Devanagari",',
            '"Noto Sans SC Thin", "Noto Sans JP Thin", "Noto Sans KR Thin",',
            "font-size: 12px;",
            "font-weight: 400;",
        ):
            self.assertIn(marker, log_style)
        self.assertNotIn("monospace", log_style)
        for language, _label in LANGUAGES:
            self.assertTrue(
                translate(language, "version_changes").startswith("• "),
                language,
            )

    def test_appledouble_audio_sidecars_are_never_processed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "album"
            nested = root / "disc"
            nested.mkdir(parents=True)
            real_mp3 = nested / "song.mp3"
            real_wav = nested / ".hidden-track.wav"
            mp3_sidecar = nested / "._song.mp3"
            wav_sidecar = nested / "._sample.wav"
            for path in (real_mp3, real_wav, mp3_sidecar, wav_sidecar):
                path.write_bytes(b"test")

            self.assertTrue(is_supported_audio_file(real_mp3))
            self.assertTrue(is_supported_audio_file(real_wav))
            self.assertFalse(is_supported_audio_file(mp3_sidecar))
            self.assertFalse(is_supported_audio_file(wav_sidecar))
            self.assertEqual(
                list(iter_audio_files(root)),
                [real_wav, real_mp3],
            )
            self.assertEqual(canonicalize_inputs([mp3_sidecar]), [])
            jobs = build_jobs([root], Path(temporary) / "output")
            self.assertEqual(
                [job.source for job in jobs],
                [real_wav, real_mp3],
            )

    def test_selected_folder_contents_start_at_destination_root(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "selected-album"
            nested = source / "disc-2"
            nested.mkdir(parents=True)
            direct_track = source / "track-01.mp3"
            nested_track = nested / "track-02.flac"
            direct_track.touch()
            nested_track.touch()
            output = root / "normalized"

            jobs = build_jobs([source], output)

            self.assertEqual(
                [(job.source, job.destination) for job in jobs],
                [
                    (direct_track, output / "track-01.mp3"),
                    (nested_track, output / "disc-2/track-02.flac"),
                ],
            )
            self.assertNotIn(source.name, jobs[0].destination.parts)

    def test_multiple_folder_roots_merge_without_output_collisions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = root / "first-album"
            second = root / "second-album"
            first.mkdir()
            second.mkdir()
            first_track = first / "same.mp3"
            second_track = second / "same.mp3"
            first_track.touch()
            second_track.touch()
            output = root / "normalized"

            jobs = build_jobs([first, second], output)

            self.assertEqual(
                [job.destination for job in jobs],
                [output / "same.mp3", output / "same__2.mp3"],
            )

    def test_source_parent_is_valid_for_flattened_folder_output(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            source = output / "selected-album"
            source.mkdir()
            (source / "track.mp3").touch()
            self.assertIsNone(validate_output([source], output))
            jobs = build_jobs([source], output)
            self.assertEqual(jobs[0].destination, output / "track.mp3")

    def test_sources_panel_has_the_same_visible_lower_edge_as_settings(self) -> None:
        project_root = Path(__file__).parents[1]
        themes = (
            project_root / "src/lufscale/ui/themes.py"
        ).read_text(encoding="utf-8")
        sources_rule = themes.split(
            'QFrame#panel[role="sources"] {', 1
        )[1].split("}", 1)[0]
        self.assertIn("border-bottom-color: #4c5865;", sources_rule)
        self.assertIn('QFrame#panel[role="settings"] {', themes)

    def test_source_safety_message_stays_visible_when_sources_are_added(self) -> None:
        application = (
            PROJECT_ROOT / "src/lufscale/application.py"
        ).read_text("utf-8")
        source_management = (
            PROJECT_ROOT / "src/lufscale/ui/source_management.py"
        ).read_text("utf-8")
        for marker in (
            "status_bar.messageChanged.connect(",
            "self._restore_source_safety_status",
            "def _restore_source_safety_status(self, message: str) -> None:",
            "QTimer.singleShot(0, self._show_source_safety_if_empty)",
            "def _show_source_safety_if_empty(self) -> None:",
            "if not status_bar.currentMessage():",
            "status_bar.showMessage(self._source_safety_status_text())",
        ):
            self.assertIn(marker, application)
        self.assertNotIn('owner.t("sources_added"', source_management)

    def test_issue_buttons_keep_accessibility_without_hover_tooltips(self) -> None:
        application = (
            PROJECT_ROOT / "src/lufscale/application.py"
        ).read_text("utf-8")
        refresh = application.split("def _refresh_issue_buttons", 1)[1].split(
            "@Slot", 1
        )[0]
        self.assertIn('button.setToolTip("")', refresh)
        self.assertIn(
            "button.setAccessibleDescription(self.t(accessibility_key))",
            refresh,
        )
        self.assertNotIn("button.setToolTip(self.t(", refresh)

    def test_windows_build_entry_points_are_complete_and_english(self) -> None:
        build = (
            PROJECT_ROOT / "tools/Internal_Application_Builder_Windows.ps1"
        ).read_text("utf-8")
        installer_builder = (
            PROJECT_ROOT / "tools/Internal_Installer_Orchestrator_Windows.ps1"
        ).read_text("utf-8")
        launcher = (
            PROJECT_ROOT / "Create_Offline_Installer_Windows.cmd"
        ).read_text("utf-8")
        for marker in (
            "[Environment]::Is64BitOperatingSystem",
            "pyinstaller==6.21.0",
            "reportlab==4.4.3",
            "generate_guides.py --output-dir",
            "prepare_bundled_ffmpeg_windows.py",
            "LUFSCALE_BUNDLED_FFMPEG",
            "packaging\\windows\\LUFScale.spec",
            "packaging\\windows\\LUFScale-Portable.spec",
            "pyi-archive_viewer.exe",
            "LUFScale-2.1.12-Portable-x64.exe",
            "exactly one ffmpeg.exe",
            "loudnorm",
            "libmp3lame",
            "OPEN_LUFSCALE_ON_WINDOWS.md",
            'Remove-Item -LiteralPath $BuildEnvironment -Recurse -Force',
            'Fail "The isolated Python build environment could not be created."',
            'Fail "The pinned pip build dependency could not be prepared."',
            'Fail "The pinned Windows build dependencies could not be installed."',
            "@(Get-ChildItem $GuideDirectory -Filter *.pdf -File).Count",
            "@(Get-ChildItem $ApplicationDirectory -Filter ffmpeg.exe -File -Recurse).Count",
            '@(Get-ChildItem (Join-Path $ApplicationDirectory "output\\pdf") -Filter *.pdf -File).Count',
        ):
            self.assertIn(marker, build)
        self.assertNotIn(
            "(Get-ChildItem $ApplicationDirectory -Filter ffmpeg.exe -File -Recurse).Count",
            build.replace(
                "@(Get-ChildItem $ApplicationDirectory -Filter ffmpeg.exe -File -Recurse).Count",
                "",
            ),
        )
        for marker in (
            "Internal_Application_Builder_Windows.ps1",
            '$PythonVersion = "3.13.15"',
            'https://www.nuget.org/api/v2/package/python/$PythonVersion',
            '$PythonSha512 = "0ad3164e412912412d89ee9e8a9d8292893427812a67b9e43d8ef6766871faa7f10dc15899e3691c14e0336fd79da3d39eaa843eac1e3e056a9151ad336bac04"',
            "Get-AuthenticodeSignature",
            "Python Software Foundation",
            "function Test-ExpectedPythonRuntime",
            "function Download-VerifiedArchive",
            "Get-FileHash -Algorithm SHA512 $Destination",
            'python-$PythonVersion-nuget.zip',
            'python-$PythonVersion-extracting',
            "Expand-Archive -LiteralPath $PythonArchive",
            'Join-Path $PythonExtractionDirectory "tools"',
            "without Windows installation or registry changes",
            ') -join " "',
            "innosetup-$InnoVersion.exe",
            "$InnoPublisherPattern = '(?i)^CN=Pyrsys B\\.V\\.,\\s*O=Pyrsys B\\.V\\.(?:,|$)'",
            "Download-VerifiedInstaller $InnoUrl $InnoInstaller $InnoPublisherPattern",
            '$InnoArgumentLine = @(',
            "-ArgumentList $InnoArgumentLine",
            "innosetup-$InnoVersion-install.log",
            "ISCC.exe",
            "Get-FileHash -Algorithm SHA256",
            'Join-Path $ToolsDirectory "inno-languages-$InnoVersion"',
            "function Download-VerifiedTranslation",
            "raw.githubusercontent.com/jrsoftware/issrc/1ae7bf81dc0d2013235dfe4bb0b6f4e4a0b6b25c/Files/Languages/ChineseSimplified.isl",
            "e0b0b350e2245f3c5e65586dfe43d574f6e7f06f2261149aba284954b3fc9a8d",
            "raw.githubusercontent.com/jrsoftware/issrc/is-6_7_3/Files/Languages/Unofficial/Hindi.islu",
            "fbb1045f3b25842bb926bdd5400d07875f4c8572b04ffab14bb7add9882cc19b",
            'Name = "Hindi-legacy.islu"',
            "raw.githubusercontent.com/jrsoftware/issrc/1ae7bf81dc0d2013235dfe4bb0b6f4e4a0b6b25c/Files/Languages/Unofficial/Indonesian.isl",
            "06232efff765902ddf7be78e39f1c5471b7e35f4c7c537deeb76692f3b5e208d",
            "foreach ($Translation in $InnoAdditionalTranslations)",
            'Join-Path $ScriptDirectory "modernize_inno_translation.py"',
            'packaging\\windows\\languages\\Hindi-6.7.3-supplement.isl',
            '--reference $InnoDefaultMessages',
            '--legacy $HindiLegacyMessages',
            '--supplement $HindiSupplement',
            '--output $HindiCurrentMessages',
            'Fail "The complete Hindi Inno Setup translation could not be generated."',
            "LUFScale-2.1.12-Setup-x64.exe",
            "LUFScale-2.1.12-Portable-x64.exe",
            "$PortableChecksum",
        ):
            self.assertIn(marker, installer_builder)
        self.assertIn(
            'Fail "Unexpected publisher for ${Path}: $($Signature.SignerCertificate.Subject)"',
            installer_builder,
        )
        self.assertNotIn('Unexpected publisher for $Path:', installer_builder)
        self.assertNotIn("-ArgumentList $PythonArguments", installer_builder)
        self.assertNotIn("python-$PythonVersion-amd64.exe", installer_builder)
        self.assertNotIn("PythonInstallLog", installer_builder)
        self.assertNotIn("PythonStaleUninstallLog", installer_builder)
        self.assertNotIn("Get-RegisteredPythonCandidates", installer_builder)
        self.assertNotIn("Find-StaleLufscaleRegisteredPython", installer_builder)
        self.assertNotIn("Registry::", installer_builder)
        self.assertNotIn('"/uninstall"', installer_builder)
        self.assertNotIn("TargetDir=", installer_builder)
        self.assertNotIn("uninstall Python", installer_builder)
        self.assertNotIn("-ArgumentList $InnoArguments", installer_builder)
        self.assertNotIn('"Martijn Laan|Jordan Russell"', installer_builder)
        self.assertIn("tools\\Internal_Installer_Orchestrator_Windows.ps1", launcher)
        self.assertIn("-ExecutionPolicy Bypass", launcher)
        self.assertNotIn("Get-Command py.exe", installer_builder)
        self.assertNotIn("Get-Command python.exe", installer_builder)
        for forbidden in ("ERREUR", "Création", "terminée avec succès"):
            self.assertNotIn(forbidden, build + installer_builder + launcher)

    def test_offline_installer_definition_contains_the_full_payload(self) -> None:
        setup = (PROJECT_ROOT / "packaging/windows/LUFScale.iss").read_text("utf-8")
        for marker in (
            '#define MyAppVersion "2.1.12"',
            "PrivilegesRequired=lowest",
            "ArchitecturesAllowed=x64compatible",
            "MinVersion=10.0.17763",
            "OutputBaseFilename=LUFScale-2.1.12-Setup-x64",
            'Source: "..\\..\\dist\\LUFScale\\*"',
            'Filename: "{uninstallexe}"',
            "desktopicon",
            "SolidCompression=yes",
            "ShowLanguageDialog=yes",
            "MissingMessagesWarning=yes",
            "NotRecognizedMessagesWarning=yes",
        ):
            self.assertIn(marker, setup)
        language_section = setup.split("[Languages]", 1)[1].split("[Tasks]", 1)[0]
        expected_languages = {
            "english": "compiler:Default.isl",
            "french": "compiler:Languages\\French.isl",
            "spanish": "compiler:Languages\\Spanish.isl",
            "italian": "compiler:Languages\\Italian.isl",
            "portuguese": "compiler:Languages\\Portuguese.isl",
            "russian": "compiler:Languages\\Russian.isl",
            "japanese": "compiler:Languages\\Japanese.isl",
            "hindi": "Hindi.isl",
            "chinese": "ChineseSimplified.isl",
            "korean": "compiler:Languages\\Korean.isl",
            "indonesian": "Indonesian.isl",
            "turkish": "compiler:Languages\\Turkish.isl",
        }
        self.assertEqual(language_section.count('Name: "'), 12)
        for language, message_file in expected_languages.items():
            self.assertIn(f'Name: "{language}"', language_section)
            self.assertIn(message_file, language_section)
        for forbidden in ("http://", "https://", "download", "DownloadTemporaryFile", "[Code]"):
            self.assertNotIn(forbidden, setup)

    def test_windows_spec_is_portable_one_folder(self) -> None:
        spec = (PROJECT_ROOT / "packaging/windows/LUFScale.spec").read_text("utf-8")
        self.assertIn('name="LUFScale"', spec)
        self.assertIn("console=False", spec)
        self.assertIn("upx=False", spec)
        self.assertIn('contents_directory="."', spec)
        self.assertIn('binaries=[(str(BUNDLED_FFMPEG), ".")]', spec)
        self.assertIn('excludes=["imageio_ffmpeg"]', spec)
        self.assertIn("OPEN_LUFSCALE_ON_WINDOWS.md", spec)
        self.assertIn("FFMPEG_WINDOWS_BUILD_MANIFEST.json", spec)
        self.assertNotIn("BUNDLE(", spec)
        self.assertNotIn("argv_emulation", spec)

    def test_windows_spec_builds_single_file_portable_application(self) -> None:
        spec = (
            PROJECT_ROOT / "packaging/windows/LUFScale-Portable.spec"
        ).read_text("utf-8")
        for marker in (
            'name="LUFScale-2.1.12-Portable-x64"',
            "a.binaries",
            "a.datas",
            "console=False",
            "upx=False",
            'binaries=[(str(BUNDLED_FFMPEG), ".")]',
            "OPEN_LUFSCALE_ON_WINDOWS.md",
            "FFMPEG_WINDOWS_BUILD_MANIFEST.json",
        ):
            self.assertIn(marker, spec)
        for forbidden in ("exclude_binaries=True", "COLLECT(", "contents_directory="):
            self.assertNotIn(forbidden, spec)

    def test_csv_and_auto_start_are_disabled_by_default(self) -> None:
        panel = (PROJECT_ROOT / "src/lufscale/ui/panels/settings.py").read_text(
            "utf-8"
        )
        settings = (PROJECT_ROOT / "src/lufscale/ui/settings.py").read_text("utf-8")
        self.assertIn("report_check.setChecked(False)", panel)
        self.assertIn("auto_start_check.setChecked(False)", panel)
        self.assertIn('store.value("generate_report", False, type=bool)', settings)
        self.assertIn('store.value("auto_start", False, type=bool)', settings)

        owner = mock.MagicMock()
        owner.output_path = None
        owner.settings_store.value.side_effect = (
            lambda _key, default, type=None: default
        )
        owner.preset_combo.findData.return_value = 0
        owner.operation_combo.findData.return_value = 0
        owner.analysis_method_combo.findData.return_value = 0
        owner.volume_combo.findData.return_value = 0
        owner.volume_combo.currentIndex.return_value = 0
        owner.lufs_spin.value.return_value = -16.0
        SettingsController(owner).restore()
        owner.report_check.setChecked.assert_called_with(False)
        owner.auto_start_check.setChecked.assert_called_with(False)

    def test_windows_ffmpeg_preparer_validates_architecture_and_capabilities(self) -> None:
        source = (
            PROJECT_ROOT / "tools/prepare_bundled_ffmpeg_windows.py"
        ).read_text("utf-8")
        for marker in (
            'if os.name != "nt"',
            "0x8664",
            'installed_version != "0.6.0"',
            '"-filters"',
            '"-encoders"',
            "REQUIRED_AUDIO_ENCODERS",
            '"--enable-nonfree"',
            "binary_sha256",
            "imageio/imageio-ffmpeg-builds",
        ):
            self.assertIn(marker, source)

        namespace = runpy.run_path(
            str(PROJECT_ROOT / "tools/prepare_bundled_ffmpeg_windows.py"),
            run_name="lufscale_ffmpeg_windows_test",
        )
        with tempfile.TemporaryDirectory() as temporary:
            executable = Path(temporary) / "ffmpeg.exe"
            image = bytearray(512)
            image[:2] = b"MZ"
            struct.pack_into("<I", image, 0x3C, 0x80)
            image[0x80:0x84] = b"PE\0\0"
            struct.pack_into("<H", image, 0x84, 0x8664)
            executable.write_bytes(image)
            self.assertEqual(namespace["pe_machine"](executable), 0x8664)

    def test_every_language_has_windows_guide_and_neutral_runtime_text(self) -> None:
        for language, _label in LANGUAGES:
            for key in (
                "guide_license_feature",
                "guide_build_title",
                "guide_build_body",
                "open_folder",
                "open_output_error",
                "guide_open_error",
            ):
                self.assertTrue(
                    translate(language, key, path="C:\\Test", error="test").strip(),
                    (language, key),
                )
            body = translate(language, "guide_build_body")
            for marker in (
                "Windows",
                "x86-64",
                "Python",
                "LUFScale-2.1.12-Setup-x64.exe",
                "SmartScreen",
            ):
                self.assertIn(marker, body, (language, marker))
            self.assertIn("Windows", translate(language, "guide_license_feature"))
            self.assertIn("Windows", translate(language, "version_changes"))

    def test_windows_guide_shortcuts_and_structure_match_the_french_reference(self) -> None:
        for language, _label in LANGUAGES:
            selection = translate(language, "source_selection_tooltip")
            self.assertIn("Ctrl", selection, language)
            self.assertNotIn("⌘", selection, language)
            self.assertNotIn("Command", selection, language)

        language_codes = {language for language, _label in LANGUAGES}
        for catalogue in (
            REFERENCE_COPY,
            TECHNICAL_COPY,
            COMPLIANCE_COPY,
            PLATFORM_BUILD_COPY,
            USEFUL_CHECKS_COPY,
        ):
            self.assertEqual(set(catalogue), language_codes)
            french_keys = set(catalogue["fr"])
            for language in language_codes:
                self.assertEqual(set(catalogue[language]), french_keys, language)

        generator = (PROJECT_ROOT / "tools/generate_guides.py").read_text("utf-8")
        technical_page = generator.split("def page_technical", 1)[1].split(
            "def draw_formula_card", 1
        )[0]
        quick_page = generator.split("def page_quick_start", 1)[1].split(
            "def page_audio", 1
        )[0]
        footer = generator.split("def draw_footer", 1)[1].split(
            "def draw_two_column_cards", 1
        )[0]
        self.assertNotIn("cards[:6]", technical_page)
        self.assertIn("compact_card_rows = 4", technical_page)
        self.assertIn("c, cards, 590, compact_cards_bottom", technical_page)
        self.assertIn('translate(language, "guide_license_title")', quick_page)
        self.assertIn('translate(language, "guide_license_body")', quick_page)
        self.assertNotIn('translate(language, "guide_license_title")', technical_page)
        self.assertNotIn('translate(language, "guide_license_body")', technical_page)
        self.assertIn("c.drawCentredString(PAGE_WIDTH / 2, 30, str(page_number))", footer)
        self.assertIn("c.drawRightString(PAGE_WIDTH - 52, 30, APP_WEBSITE_URL)", footer)
        for required in (
            'translate(language, "quality_control")',
            'translate(language, "parallel")',
        ):
            self.assertIn(required, technical_page)

        # Trace every catalogue key actually requested by the seven-page
        # French reference. Every translated guide must provide that complete
        # set, so a future section cannot silently fall back to English.
        generator_namespace = runpy.run_path(
            str(PROJECT_ROOT / "tools/generate_guides.py"),
            run_name="lufscale_windows_guide_structure_test",
        )
        document_labels = generator_namespace["DOC_LABELS"]
        self.assertEqual(set(document_labels), language_codes)
        french_label_keys = set(document_labels["fr"])
        for language in language_codes:
            self.assertEqual(
                set(document_labels[language]),
                french_label_keys,
                language,
            )

        required_document_keys: set[str] = set()
        original_translate = generator_namespace["translate"]

        def traced_translate(language: str, key: str, **values):
            required_document_keys.add(key)
            return original_translate(language, key, **values)

        generate_guide = generator_namespace["generate_guide"]
        generate_guide.__globals__["translate"] = traced_translate
        with tempfile.TemporaryDirectory() as temporary:
            generate_guide(
                "fr",
                "Français",
                generator_namespace["register_fonts"](),
                output_dir=Path(temporary),
            )
        self.assertGreaterEqual(len(required_document_keys), 75)
        for language in language_codes - {"fr", "en"}:
            self.assertFalse(
                required_document_keys - set(EXTRA_TEXTS[language]),
                language,
            )

    def test_pdf_audio_options_and_useful_checks_are_unambiguous(self) -> None:
        language_codes = {language for language, _label in LANGUAGES}
        self.assertEqual(set(USEFUL_CHECKS_COPY), language_codes)
        for language in language_codes:
            checks = USEFUL_CHECKS_COPY[language]
            self.assertEqual(set(checks), {"heading", "cards"}, language)
            self.assertEqual(len(checks["cards"]), 3, language)
            self.assertTrue(checks["heading"].strip(), language)
            self.assertTrue(
                all(title.strip() and body.strip() for title, body in checks["cards"]),
                language,
            )

            peak = translate(language, "peak_tooltip").split("\n\n", 1)[0]
            quality = translate(language, "quality_tooltip").split("\n\n", 1)[0]
            parallel_lines = [
                line
                for line in translate(language, "parallel_tooltip").splitlines()
                if line.strip()
            ]
            self.assertNotEqual(peak, quality, language)
            self.assertTrue(
                all(marker in parallel_lines[1] for marker in ("4", "70", "92")),
                language,
            )

        generator = (PROJECT_ROOT / "tools/generate_guides.py").read_text("utf-8")
        audio_page = generator.split("def page_audio", 1)[1].split(
            "def page_options", 1
        )[0]
        recommended_page = generator.split("def page_recommended", 1)[1].split(
            "def technical_copy", 1
        )[0]
        self.assertIn('guide_paragraphs(language, "peak_tooltip")', audio_page)
        self.assertIn('guide_paragraphs(language, "quality_tooltip")', audio_page)
        self.assertIn(
            'guide_leading_lines(language, "parallel_tooltip", 2)', audio_page
        )
        self.assertIn('translate(language, "auto_start")', audio_page)
        self.assertNotIn('("report_tooltip", "auto_start_tooltip")', audio_page)
        self.assertIn("USEFUL_CHECKS_COPY[language]", recommended_page)
        self.assertNotIn(
            'translate(language, "guide_file_processing_title")', recommended_page
        )

    def test_guide_generator_is_windows_only(self) -> None:
        generator = (PROJECT_ROOT / "tools/generate_guides.py").read_text("utf-8")
        for marker in (
            "GUIDE_IDENTITY_LABELS",
            '"guide_license_body"',
            "PLATFORM_BUILD_COPY[language]",
            "LUFScale Windows visual guide",
            "output_dir.resolve()",
        ):
            self.assertIn(marker, generator)
        for forbidden in ("--platform", "guide_intel"):
            self.assertNotIn(forbidden, generator)

    def test_pdf_build_appendix_covers_only_windows_in_every_language(self) -> None:
        self.assertEqual(set(PLATFORM_BUILD_COPY), {code for code, _ in LANGUAGES})
        for language, _label in LANGUAGES:
            build = PLATFORM_BUILD_COPY[language]
            self.assertTrue(build["title"].strip(), language)
            for marker in (
                "Windows", "x64",
                "Create_Offline_Installer_Windows.cmd",
                "dist\\LUFScale-2.1.12-Setup-x64.exe",
                "dist\\LUFScale-2.1.12-Setup-x64.exe.sha256",
                "dist\\LUFScale-2.1.12-Portable-x64.exe",
                "dist\\LUFScale-2.1.12-Portable-x64.exe.sha256",
                ".exe Setup (",
                ".exe Portable (",
                ".sha256 (",
            ):
                self.assertIn(marker, build["body"], (language, marker))
            for forbidden in (
                "Apple Silicon",
                "Intel",
                "./Create_Community_Distribution_macOS.command",
                "dist/LUFScale.app",
                "dist/LUFScale-2.1.12-macOS-arm64-community.zip",
                "dist/LUFScale-2.1.12-macOS-x86_64-community.zip",
            ):
                self.assertNotIn(forbidden, build["title"] + build["body"], (language, forbidden))
            output_lines = build["body"].splitlines()
            self.assertEqual(
                output_lines.count("\t**.\\Create_Offline_Installer_Windows.cmd**"),
                1,
                language,
            )
            for output_path in (
                "\t**dist\\LUFScale-2.1.12-Setup-x64.exe**",
                "\t**dist\\LUFScale-2.1.12-Setup-x64.exe.sha256**",
                "\t**dist\\LUFScale-2.1.12-Portable-x64.exe**",
                "\t**dist\\LUFScale-2.1.12-Portable-x64.exe.sha256**",
            ):
                self.assertEqual(output_lines.count(output_path), 1, (language, output_path))
            self.assertEqual(
                sum(not line.strip() for line in output_lines),
                5,
                language,
            )
            command_index = output_lines.index("\t**.\\Create_Offline_Installer_Windows.cmd**")
            self.assertFalse(output_lines[command_index - 1].strip(), language)
            self.assertFalse(output_lines[command_index + 1].strip(), language)
            setup_index = output_lines.index("\t**dist\\LUFScale-2.1.12-Setup-x64.exe**")
            self.assertFalse(output_lines[setup_index - 1].strip(), language)
            self.assertEqual(output_lines[setup_index + 1], "\t**dist\\LUFScale-2.1.12-Setup-x64.exe.sha256**", language)
            self.assertEqual(output_lines[setup_index + 2], "\t**dist\\LUFScale-2.1.12-Portable-x64.exe**", language)
            self.assertEqual(output_lines[setup_index + 3], "\t**dist\\LUFScale-2.1.12-Portable-x64.exe.sha256**", language)
            self.assertFalse(output_lines[setup_index + 4].strip(), language)
            self.assertTrue(output_lines[setup_index + 5].startswith(".exe Setup ("), language)
            self.assertTrue(output_lines[setup_index + 6].startswith(".exe Portable ("), language)
            self.assertTrue(output_lines[setup_index + 7].startswith(".sha256 ("), language)
        generator = (PROJECT_ROOT / "tools/generate_guides.py").read_text("utf-8")
        self.assertIn('separator="\\n \\n"', generator)
        self.assertIn('"&nbsp;" * 4', generator)
        self.assertIn('escaped = f"<b>{escaped}</b>"', generator)
        self.assertIn("pdfmetrics.registerFontFamily(", generator)
        self.assertIn("PAGE_WIDTH - 104,\n        180,", generator)

    def test_quality_formula_descriptions_are_specific_in_every_language(self) -> None:
        language_codes = {language for language, _label in LANGUAGES}
        self.assertEqual(set(COMPLIANCE_COPY), language_codes)
        for language in language_codes:
            self.assertEqual(len(COMPLIANCE_COPY[language]["headings"]), 8)
            descriptions = COMPLIANCE_COPY[language]["descriptions"]
            self.assertEqual(len(descriptions), 8)
            self.assertEqual(len(set(descriptions)), 8)
            self.assertTrue(all(description.strip() for description in descriptions))
        generator = (PROJECT_ROOT / "tools/generate_guides.py").read_text("utf-8")
        self.assertIn('descriptions = compliance_copy["descriptions"]', generator)
        compliance_source = generator.split("def page_compliance", 1)[1].split(
            "def page_release", 1
        )[0]
        for index in range(8):
            self.assertIn(f"descriptions[{index}]", compliance_source)
        self.assertNotIn('technical_copy(language, "dynamic")', compliance_source)
        self.assertNotIn('technical_copy(language, "retries")', compliance_source)
        self.assertNotIn('technical_copy(language, "qc_off")', compliance_source)

    def test_pdf_generator_uses_only_bundled_dejavu_fonts(self) -> None:
        generator = (PROJECT_ROOT / "tools/generate_guides.py").read_text("utf-8")
        self.assertNotIn("/usr/share/fonts", generator)
        for filename in (
            "DejaVuSans.ttf",
            "DejaVuSans-Bold.ttf",
            "DejaVuSerif.ttf",
        ):
            font = PROJECT_ROOT / "assets" / "fonts" / filename
            self.assertTrue(font.is_file(), filename)
            self.assertGreater(font.stat().st_size, 100_000, filename)

    def test_windows_builder_recreates_and_validates_guide_directory(self) -> None:
        build = (
            PROJECT_ROOT / "tools/Internal_Application_Builder_Windows.ps1"
        ).read_text("utf-8")
        self.assertIn("New-Item -ItemType Directory -Force -Path $GuideDirectory", build)
        self.assertIn("if ($LASTEXITCODE -ne 0)", build)
        self.assertIn("if (-not (Test-Path $GuideDirectory))", build)

    def test_windows_icon_and_opening_document_are_present(self) -> None:
        icon = PROJECT_ROOT / "assets/branding/LUFScale.ico"
        self.assertGreater(icon.stat().st_size, 10_000)
        self.assertEqual(icon.read_bytes()[:4], b"\x00\x00\x01\x00")
        opening = (PROJECT_ROOT / "OPEN_LUFSCALE_ON_WINDOWS.md").read_text("utf-8")
        for marker in (
            "Windows 11 is recommended",
            "Windows 10 version 1809",
            "SmartScreen",
            "More info",
            "Run anyway",
            "Create_Offline_Installer_Windows.cmd",
            "SHA-256",
        ):
            self.assertIn(marker, opening)

    def test_windows_build_checks_every_runtime_encoder(self) -> None:
        build = (
            PROJECT_ROOT / "tools/Internal_Application_Builder_Windows.ps1"
        ).read_text("utf-8")
        preparer = (
            PROJECT_ROOT / "tools/prepare_bundled_ffmpeg_windows.py"
        ).read_text("utf-8")
        for encoder in REQUIRED_AUDIO_ENCODERS:
            self.assertIn(encoder, build)
        self.assertIn("REQUIRED_AUDIO_ENCODERS", preparer)

    def test_project_has_no_non_windows_packaging_assets(self) -> None:
        self.assertEqual(list(PROJECT_ROOT.glob("*.command")), [])
        self.assertEqual(list(PROJECT_ROOT.glob("*.ps1")), [])
        self.assertEqual(
            sorted(path.name for path in PROJECT_ROOT.glob("*.cmd")),
            ["Create_Offline_Installer_Windows.cmd"],
        )
        self.assertEqual(
            sorted(path.name for path in (PROJECT_ROOT / "packaging").iterdir()),
            ["generated", "windows"],
        )
        self.assertEqual(
            sorted(path.name for path in (PROJECT_ROOT / "tools").glob("*.py")),
            [
                "generate_guides.py",
                "modernize_inno_translation.py",
                "prepare_bundled_ffmpeg_windows.py",
            ],
        )
        self.assertEqual(
            sorted(path.name for path in (PROJECT_ROOT / "output/pdf").glob("*.pdf")),
            sorted(PDF_GUIDES.values()),
        )
        self.assertFalse((PROJECT_ROOT / "output/pdf/windows").exists())

    def test_public_records_are_windows_only(self) -> None:
        paths = [
            PROJECT_ROOT / "README.md",
            PROJECT_ROOT / "RELEASE_2.1.12.md",
            PROJECT_ROOT / "VALIDATION_2.1.12.md",
            PROJECT_ROOT / "THIRD_PARTY_NOTICES.md",
            PROJECT_ROOT / "SBOM.cdx.json",
            PROJECT_ROOT / "packaging/generated/README.md",
            PROJECT_ROOT / "tools/Internal_Application_Builder_Windows.ps1",
            PROJECT_ROOT / "tools/Internal_Installer_Orchestrator_Windows.ps1",
            PROJECT_ROOT / "Create_Offline_Installer_Windows.cmd",
            PROJECT_ROOT / "packaging/windows/LUFScale.iss",
            PROJECT_ROOT / "tools/generate_guides.py",
        ]
        for path in paths:
            content = path.read_text("utf-8")
            self.assertIn("Windows", content, str(path))

    def test_guide_resources_use_one_windows_directory(self) -> None:
        root = PROJECT_ROOT
        for language, filename in PDF_GUIDES.items():
            self.assertEqual(localized_guide_path(language, root), root / "output/pdf" / filename)

    def test_documented_quality_thresholds_match_runtime(self) -> None:
        self.assertEqual(STRICT_TARGET_LUFS_TOLERANCE, 0.50)
        self.assertEqual(QUALITY_CONTROL_LUFS_TOLERANCE, 0.60)
        self.assertEqual(QUALITY_CONTROL_TRUE_PEAK_TOLERANCE_DB, 0.25)
        settings = LoudnessSettings(integrated_lufs=-14.0, true_peak=-2.0)
        base = {"input_lra": "4.0", "input_thresh": "-24.0", "target_offset": "0.0"}
        self.assertTrue(
            dynamic_mp3_output_is_strictly_compliant(
                settings, {**base, "input_i": "-14.50", "input_tp": "-2.00"}
            )
        )
        self.assertFalse(
            dynamic_mp3_output_is_strictly_compliant(
                settings, {**base, "input_i": "-14.51", "input_tp": "-2.00"}
            )
        )
        input_measurements = {**base, "input_i": "-18.0", "input_tp": "-5.0"}
        self.assertTrue(
            assess_quality(
                settings,
                input_measurements,
                {**base, "input_i": "-14.60", "input_tp": "-1.75"},
            ).passed
        )

    def test_same_named_sources_keep_supported_extensions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = root / "one/same.mp3"
            second = root / "two/same.mp3"
            first.parent.mkdir()
            second.parent.mkdir()
            first.touch()
            second.touch()
            jobs = build_jobs([first, second], root / "output")
            self.assertEqual([job.destination.name for job in jobs], ["same.mp3", "same__2.mp3"])

    def test_replaygain_and_metadata_commands_keep_container_flags(self) -> None:
        for suffix, required in {
            ".mp3": ("-id3v2_version", "3"),
            ".aif": ("-write_id3v2", "1"),
            ".aiff": ("-write_id3v2", "1"),
            ".m4a": ("-movflags", "use_metadata_tags"),
        }.items():
            command = replaygain_command(
                "ffmpeg", Path("source.wav"), Path(f"target{suffix}"), 2.5, -1.0
            )
            self.assertIn("\0".join(required), "\0".join(command))
        metadata = metadata_dump_command("ffmpeg", Path("target.ogg"))
        positions = [index for index, value in enumerate(metadata) if value == "-map_metadata"]
        self.assertEqual([metadata[index + 1] for index in positions], ["0", "0:s:a:0"])

    def test_help_structure_and_active_keys_are_complete(self) -> None:
        for dialog, sections in HELP_DIALOG_SECTIONS.items():
            self.assertTrue(sections, dialog)
            for language, _label in LANGUAGES:
                self.assertTrue(all(translate(language, key).strip() for key in sections))
        for key in ("guide_intel_build_title", "guide_intel_build_body"):
            self.assertNotIn(key, TEXTS)


if __name__ == "__main__":
    unittest.main()
