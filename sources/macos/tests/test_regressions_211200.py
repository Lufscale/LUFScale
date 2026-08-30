from __future__ import annotations

import tempfile
import unittest
import ast
import os
import subprocess
import string
import sys
from pathlib import Path
from unittest import mock

from lufscale.audio.core import (
    QUALITY_CONTROL_LUFS_TOLERANCE,
    QUALITY_CONTROL_TRUE_PEAK_TOLERANCE_DB,
    STRICT_TARGET_LUFS_TOLERANCE,
    LoudnessSettings,
    assess_quality,
    build_jobs,
    dynamic_mp3_output_is_strictly_compliant,
    metadata_dump_command,
    replaygain_command,
)
from lufscale.version import APP_LICENSE, APP_VERSION, APP_WEBSITE_URL
from lufscale.i18n.guide_technical import (
    COMPLIANCE_COPY,
    REFERENCE_COPY,
    TECHNICAL_COPY,
)
from lufscale.i18n.guide_build import PLATFORM_BUILD_COPY
from lufscale.i18n.guide_checks import USEFUL_CHECKS_COPY
from lufscale.i18n.loader import EXTRA_TEXTS, LANGUAGES, TEXTS, translate
from lufscale.processing.ffmpeg import find_ffmpeg
from lufscale.ui.help_catalog import HELP_CONTENT_KEYS, HELP_DIALOG_SECTIONS
from lufscale.ui.settings import SettingsController


class ReleaseRegressionTests(unittest.TestCase):
    def test_release_version(self) -> None:
        self.assertEqual(APP_VERSION, "2.1.12")
        project_root = Path(__file__).parents[1]
        self.assertTrue((project_root / "RELEASE_2.1.12.md").is_file())
        self.assertTrue((project_root / "VALIDATION_2.1.12.md").is_file())
        self.assertTrue(
            (project_root / "src/lufscale/i18n/translations_211100.py").is_file()
        )
        self.assertFalse((project_root / "RELEASE_2.1.8.md").exists())
        self.assertFalse((project_root / "VALIDATION_2.1.8.md").exists())

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

        project_root = Path(__file__).parents[1]
        application = (
            project_root / "src/lufscale/application.py"
        ).read_text(encoding="utf-8")
        widgets = (
            project_root / "src/lufscale/ui/widgets/components.py"
        ).read_text(encoding="utf-8")
        theme = (
            project_root / "src/lufscale/ui/themes.py"
        ).read_text(encoding="utf-8")
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

    def test_pdf_overview_restores_macos_features_and_aligned_steps(self) -> None:
        project_root = Path(__file__).parents[1]
        generator = (project_root / "tools/generate_guides.py").read_text(
            encoding="utf-8"
        )
        for marker in (
            "def guide_distribution_features(language: str)",
            "feature_lines[1:]",
            "step_height = 66",
            "step_gap = (interface_height - 4 * step_height) / 3",
            "marker_y = card_y + step_height / 2",
            "x + width - 72, progress_y - 1, 44, 16",
        ):
            self.assertIn(marker, generator)
        self.assertNotIn('sanitize(translate(language, "start"))[:13]', generator)

    def test_processing_log_uses_native_inverse_text_and_script_safe_gaps(self) -> None:
        project_root = Path(__file__).parents[1]
        execution = (
            project_root / "src/lufscale/ui/execution.py"
        ).read_text(encoding="utf-8")
        for marker in (
            "LOG_LINE_HEIGHT_PX = 16.0",
            "LOG_DEVANAGARI_LINE_HEIGHT_PX = 19.0",
            "LOG_JAPANESE_LINE_HEIGHT_PX = 16.0",
            "LOG_JAPANESE_BADGE_HEIGHT_PX = 15.0",
            "LOG_CJK_BADGE_RAISE_PX = 2.0",
            "LOG_CHINESE_LINE_HEIGHT_PX = 16.0",
            "LOG_KOREAN_LINE_HEIGHT_PX = 16.0",
            "LOG_HIGHLIGHT_GAP_PX = 1.0",
            "def uses_cjk_lufs_badge(",
            'if language in {"ja", "zh"}:',
            "def inverse_log_text_format(",
            "inverse_format = QTextCharFormat(source_format)",
            "inverse_format.setForeground(QBrush(QColor(background_color)))",
            "inverse_format.setBackground(QBrush(QColor(text_color)))",
            "def make_cjk_lufs_badge_format(",
            "class CjkLufsBadgeTextObject(QPyTextObject):",
            "QFontMetricsF(char_format.font()).horizontalAdvance(label)",
            "return QSizeF(width, LOG_JAPANESE_BADGE_HEIGHT_PX)",
            "paint_rectangle.translate(0.0, -LOG_CJK_BADGE_RAISE_PX)",
            "painter.fillRect(paint_rectangle, background_color)",
            "painter.setFont(char_format.font())",
            "painter.drawText(QPointF(paint_rectangle.left(), baseline), label)",
            "def _ensure_cjk_lufs_handler(self) -> bool:",
            "self._cjk_lufs_handler: CjkLufsBadgeTextObject | None = None",
            "self._cjk_lufs_handler_attempted = True",
            "layout.registerHandler(JAPANESE_LUFS_OBJECT_TYPE, handler)",
            "except (AttributeError, RuntimeError, TypeError):",
            "def log_highlight_gap_px(",
            "del message, language",
            "return LOG_HIGHLIGHT_GAP_PX",
            "def log_content_line_height_px(",
            "if language in LOG_LANGUAGE_LINE_HEIGHTS_PX:",
            "or KOREAN_LOG_PATTERN.search(message)",
            "or DEVANAGARI_LOG_PATTERN.search(message)",
            "or HAN_LOG_PATTERN.search(message)",
            "return line_height",
            "- log_highlight_gap_px(message, language)",
            "surrounding_format = cursor.charFormat()",
            "cursor.insertText(",
            'f" {transition} ",',
            "OBJECT_REPLACEMENT_CHARACTER,",
            "make_cjk_lufs_badge_format(",
            "inverse_log_text_format(",
            "block_format.setTopMargin(0.0)",
            "if uses_cjk_lufs_badge(message, self.owner.language):",
            "block_format.setBottomMargin(0.0)",
            "LOG_JAPANESE_LINE_HEIGHT_PX",
            "block_format.setBottomMargin(",
            "log_highlight_gap_px(message, self.owner.language)",
            "log_content_line_height_px(message, self.owner.language)",
            "QTextBlockFormat.LineHeightTypes.FixedHeight.value",
            "cursor.setBlockFormat(block_format)",
            "cursor.movePosition(QTextCursor.MoveOperation.End)",
            "cursor.insertBlock(block_format)",
            "cursor.insertHtml(",
            "if not cursor.atStart():",
        ):
            self.assertIn(marker, execution)
        tree = ast.parse(execution)
        constants = {
            node.targets[0].id: node.value.value
            for node in tree.body
            if isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and isinstance(node.value, ast.Constant)
            and isinstance(node.value.value, (int, float))
        }
        self.assertEqual(constants["LOG_LINE_HEIGHT_PX"], 16)
        self.assertEqual(constants["LOG_DEVANAGARI_LINE_HEIGHT_PX"], 19)
        self.assertEqual(constants["LOG_JAPANESE_LINE_HEIGHT_PX"], 16)
        self.assertEqual(constants["LOG_JAPANESE_BADGE_HEIGHT_PX"], 15)
        self.assertEqual(constants["LOG_CJK_BADGE_RAISE_PX"], 2)
        self.assertEqual(constants["LOG_CHINESE_LINE_HEIGHT_PX"], 16)
        self.assertEqual(constants["LOG_KOREAN_LINE_HEIGHT_PX"], 16)
        self.assertEqual(constants["LOG_HIGHLIGHT_GAP_PX"], 1)
        self.assertEqual(constants["LOG_LINE_HEIGHT_PX"] - 1, 15)
        self.assertEqual(
            constants["LOG_DEVANAGARI_LINE_HEIGHT_PX"]
            + constants["LOG_HIGHLIGHT_GAP_PX"],
            20,
        )
        self.assertEqual(
            constants["LOG_JAPANESE_LINE_HEIGHT_PX"]
            - constants["LOG_JAPANESE_BADGE_HEIGHT_PX"],
            1,
        )
        self.assertEqual(
            constants["LOG_CHINESE_LINE_HEIGHT_PX"]
            - constants["LOG_JAPANESE_BADGE_HEIGHT_PX"],
            1,
        )
        self.assertEqual(
            constants["LOG_KOREAN_LINE_HEIGHT_PX"]
            + constants["LOG_HIGHLIGHT_GAP_PX"],
            17,
        )
        inverse_function = execution.split(
            "def inverse_log_text_format", 1
        )[1].split("def make_cjk_lufs_badge_format", 1)[0]
        self.assertNotIn("setFont", inverse_function)
        self.assertNotIn("QFont", inverse_function)
        self.assertNotIn("font-family", inverse_function)
        self.assertNotIn("font-size", inverse_function)
        self.assertNotIn("font-weight", inverse_function)
        for bitmap_marker in (
            "cursor.insertImage(",
            "ImageResource",
            "devicePixelRatioF()",
            "make_lufs_badge_image",
            "QImage",
        ):
            self.assertNotIn(bitmap_marker, execution)
        for unsupported_marker in (
            "QTextObjectInterface",
            "LUFS_BADGE_OBJECT_TYPE",
        ):
            self.assertNotIn(unsupported_marker, execution)
        self.assertNotIn("background-color:{highlight_color}", execution)
        self.assertNotIn("LOG_EXPANDED_HIGHLIGHT_GAP_PX", execution)
        japanese_branch = execution.split(
            "if uses_cjk_lufs_badge(message, self.owner.language):",
            1,
        )[1].split("else:", 1)[0]
        self.assertIn(
            "QTextBlockFormat.LineHeightTypes.FixedHeight.value",
            japanese_branch,
        )
        self.assertNotIn(
            "QTextBlockFormat.LineHeightTypes.LineDistanceHeight.value",
            japanese_branch,
        )
        self.assertNotIn(
            "QTextBlockFormat.LineHeightTypes.LineDistanceHeight.value",
            execution,
        )
        self.assertNotIn("document().isEmpty()", execution)
        self.assertNotIn(
            "QTextBlockFormat.LineHeightTypes.FixedHeight,",
            execution,
        )
        self.assertNotIn("self.owner.log_box.append(", execution)
        for language, _label in LANGUAGES:
            self.assertTrue(
                translate(language, "version_changes").startswith("• "),
                language,
            )

    def test_open_source_license_is_declared_and_bundled(self) -> None:
        self.assertEqual(APP_LICENSE, "GPL-3.0-or-later")
        project_root = Path(__file__).parents[1]
        license_text = (project_root / "LICENSE").read_text(encoding="utf-8")
        copyright_text = (project_root / "COPYRIGHT").read_text(encoding="utf-8")
        self.assertIn("GNU GENERAL PUBLIC LICENSE", license_text)
        self.assertIn("either version 3", copyright_text)

    def test_community_bundle_embeds_only_the_verified_ffmpeg(self) -> None:
        project_root = Path(__file__).parents[1]
        spec = (project_root / "packaging/macos/LUFScale.spec").read_text(
            encoding="utf-8"
        )
        community_script = (
            project_root / "Create_Community_Distribution_macOS.command"
        ).read_text(encoding="utf-8")
        self.assertIn('excludes=["imageio_ffmpeg"]', spec)
        self.assertIn('binaries=[(str(BUNDLED_FFMPEG), ".")]', spec)
        self.assertIn("corresponding-source", community_script)
        self.assertIn("FFMPEG_BUILD_MANIFEST.json", community_script)
        self.assertIn("LUFSCALE_RUNTIME_MANIFEST.json", community_script)
        self.assertIn("RELEASE_2.1.12.md", community_script)
        self.assertIn("VALIDATION_2.1.12.md", community_script)
        self.assertIn('PROJECT_ROOT / "RELEASE_2.1.12.md"', spec)
        self.assertIn('PROJECT_ROOT / "VALIDATION_2.1.12.md"', spec)
        self.assertIn('"LUFSCALE_RUNTIME_MANIFEST.json"', spec)

    def test_bundled_ffmpeg_sources_are_pinned(self) -> None:
        project_root = Path(__file__).parents[1]
        build_script = (
            project_root / "tools" / "build_bundled_ffmpeg_macos.py"
        ).read_text(encoding="utf-8")
        for version in ("7.1.5", "4.0", "1.3.6", "1.3.7", "1.6.1"):
            self.assertIn(f'version="{version}"', build_script)
        self.assertIn("--enable-libmp3lame", build_script)
        self.assertIn("--enable-libvorbis", build_script)
        self.assertIn("--enable-libopus", build_script)
        self.assertIn('if "--enable-gpl" in configuration', build_script)
        self.assertIn('or "--enable-nonfree" in configuration', build_script)
        self.assertNotIn("urllib.request", build_script)
        self.assertIn('"--proto"', build_script)
        self.assertIn('"=https"', build_script)
        self.assertNotIn('"--insecure"', build_script)
        self.assertIn('"--show-sdk-path"', build_script)
        self.assertIn('"SDKROOT": sdk_root', build_script)
        self.assertIn('"-isysroot"', build_script)
        self.assertIn("lufscale-compiler-check", build_script)
        self.assertIn("lame-abi-check", build_script)
        for cache_name in (
            "ac_cv_sizeof_short",
            "ac_cv_sizeof_unsigned_short",
            "ac_cv_sizeof_int",
            "ac_cv_sizeof_unsigned_int",
            "ac_cv_sizeof_long",
            "ac_cv_sizeof_unsigned_long",
            "ac_cv_sizeof_long_long",
            "ac_cv_sizeof_unsigned_long_long",
            "ac_cv_sizeof_float",
            "ac_cv_sizeof_double",
        ):
            self.assertIn(f'"{cache_name}"', build_script)
        self.assertIn('"LC_ALL": "C"', build_script)
        self.assertIn('"CONFIG_SITE"', build_script)
        self.assertIn('"build-diagnostics"', build_script)
        self.assertIn('f"{build.name}-config.log"', build_script)
        self.assertIn("last 160 lines", build_script)
        self.assertIn("preserve_make_flags=True", build_script)
        self.assertIn("CFLAGS={env['CFLAGS']}", build_script)
        self.assertIn("CXXFLAGS={env['CXXFLAGS']}", build_script)
        self.assertIn("LDFLAGS={env['LDFLAGS']}", build_script)
        self.assertNotIn("-force_cpusubtype_ALL\"", build_script)
        self.assertIn('Path("/private/tmp")', build_script)
        self.assertIn('f"lufscale-{APP_VERSION}-ffmpeg-{os.getuid()}"', build_script)
        self.assertIn("safe_build_base.chmod(0o700)", build_script)
        self.assertNotIn(
            'build_root = PROJECT_ROOT / ".construction-ffmpeg"', build_script
        )
        self.assertIn("Errors found", build_script)

    def test_community_scripts_keep_the_app_and_remove_only_collect(self) -> None:
        project_root = Path(__file__).parents[1]
        scripts = sorted(path.name for path in project_root.glob("*.command"))
        self.assertEqual(scripts, ["Create_Community_Distribution_macOS.command"])
        internal_builder = (
            project_root / "tools/Internal_Application_Builder_macOS.command"
        )
        self.assertTrue(internal_builder.is_file())
        community_script = (
            project_root / "Create_Community_Distribution_macOS.command"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "./tools/Internal_Application_Builder_macOS.command",
            community_script,
        )
        self.assertIn('/bin/rm -rf -- "$collect_path"', community_script)
        self.assertNotIn('/bin/rm -rf -- "$app_path"', community_script)
        self.assertIn("LUFScale.app, the publishable ZIP", community_script)
        self.assertIn('[[ -s "$release_zip" && -s "$release_zip.sha256" ]]', community_script)
        self.assertNotIn("ERREUR", community_script)

    def test_public_root_filenames_are_international(self) -> None:
        project_root = Path(__file__).parents[1]
        self.assertTrue((project_root / "OPEN_LUFSCALE_ON_MACOS.md").is_file())
        self.assertFalse((project_root / "OUVRIR_LUFSCALE_SUR_MACOS.md").exists())
        for path in project_root.iterdir():
            if not path.is_file():
                continue
            self.assertNotIn("OUVRIR", path.name)
            self.assertNotIn("CRÉER", path.name.upper())
            self.assertNotIn("DISTRIBUTION_COMMUNAUTAIRE", path.name.upper())
        for relative in (
            "Create_Community_Distribution_macOS.command",
            "tools/Internal_Application_Builder_macOS.command",
            "packaging/macos/LUFScale.spec",
            "README.md",
        ):
            content = (project_root / relative).read_text(encoding="utf-8")
            self.assertIn("OPEN_LUFSCALE_ON_MACOS.md", content, relative)
            self.assertNotIn("OUVRIR_LUFSCALE_SUR_MACOS.md", content, relative)

    def test_public_text_files_use_english_by_default(self) -> None:
        project_root = Path(__file__).parents[1]
        paths = [
            *project_root.glob("*.md"),
            *project_root.glob("*.command"),
            *project_root.glob("tools/*.command"),
            project_root / "COPYRIGHT",
            project_root / "LICENSE",
            project_root / "packaging/generated/README.md",
            *project_root.glob("third_party_licenses/*.txt"),
            *project_root.glob("assets/fonts/*OFL.txt"),
        ]
        forbidden = (
            "Validation de LUFScale",
            "Distribution open source de LUFScale",
            "Ouvrir la distribution",
            "Construire l’application",
            "Le logiciel",
            "La distribution communautaire",
            "L’utilisateur final",
            "fichier d’empreinte",
            "ERREUR —",
        )
        for path in paths:
            content = path.read_text(encoding="utf-8")
            for phrase in forbidden:
                self.assertNotIn(phrase, content, str(path.relative_to(project_root)))

    def test_replaygain_graphs_are_published_from_one_measurement(self) -> None:
        project_root = Path(__file__).parents[1]
        conversion = (
            project_root / "src/lufscale/processing/conversion.py"
        ).read_text(encoding="utf-8")
        self.assertIn("def _emit_replaygain_estimate", conversion)
        self.assertIn("self._emit_replaygain_estimate(\n                measurements", conversion)
        self.assertIn("before,\n                estimated_playback", conversion)

    def test_analyze_only_is_fresh_while_replaygain_may_use_cache(self) -> None:
        project_root = Path(__file__).parents[1]
        conversion = (
            project_root / "src/lufscale/processing/conversion.py"
        ).read_text(encoding="utf-8")
        self.assertIn(
            'None\n                if self.operation == "analyze"\n'
            '                else self._cached_measurements([job.source])',
            conversion,
        )
        self.assertIn(
            'measurements = self._analyze_path(job.source)',
            conversion,
        )
        self.assertIn(
            'self._store_measurements([job.source], measurements)',
            conversion,
        )

    def test_issue_buttons_meet_the_journal_frame(self) -> None:
        project_root = Path(__file__).parents[1]
        results_panel = (
            project_root / "src/lufscale/ui/panels/results.py"
        ).read_text(encoding="utf-8")
        self.assertIn("log_column.setSpacing(0)", results_panel)
        self.assertIn("log_column.addSpacing(3)", results_panel)
        self.assertIn('log_help_button = OptionHelpButton()', results_panel)
        self.assertIn('log_help_slot.setFixedSize(28, 28)', results_panel)
        self.assertIn(
            'log_help_slot_layout.setContentsMargins(0, 0, 6, 6)',
            results_panel,
        )
        self.assertIn('log_header.setSpacing(0)', results_panel)
        self.assertEqual(results_panel.count('log_header.addSpacing(6)'), 2)
        self.assertNotIn('log_header.addSpacing(2)', results_panel)
        self.assertNotIn('log_header.addSpacing(4)', results_panel)
        self.assertIn('log_header.setContentsMargins(0, 0, 0, 0)', results_panel)
        normalized = " ".join(results_panel.split())
        for widget in (
            "log_title_label",
            "warnings_button",
            "errors_button",
            "log_help_slot",
        ):
            self.assertIn(
                f"{widget}, 0, Qt.AlignmentFlag.AlignBottom", normalized
            )
        self.assertNotIn(
            "log_help_button, 0, Qt.AlignmentFlag.AlignBottom", normalized
        )

    def test_issue_buttons_keep_accessibility_without_hover_tooltips(self) -> None:
        application = (
            Path(__file__).parents[1] / "src/lufscale/application.py"
        ).read_text(encoding="utf-8")
        refresh = application.split("def _refresh_issue_buttons", 1)[1].split(
            "@Slot", 1
        )[0]
        self.assertIn('button.setToolTip("")', refresh)
        self.assertIn(
            "button.setAccessibleDescription(self.t(accessibility_key))",
            refresh,
        )
        self.assertNotIn("button.setToolTip(self.t(", refresh)

    def test_macos_build_reports_bundle_component_sizes(self) -> None:
        project_root = Path(__file__).parents[1]
        build_script = (
            project_root / "tools/Internal_Application_Builder_macOS.command"
        ).read_text(encoding="utf-8")
        for marker in (
            'tree_bytes()',
            'Bundle size report:',
            'Bundled FFmpeg:',
            'Contents/Frameworks:',
            'Contents/Resources:',
            'Regular files:',
        ):
            self.assertIn(marker, build_script)

    def test_guides_document_apple_silicon_and_intel_validation_boundary(self) -> None:
        automatic_resume_markers = {
            "fr": "reprend automatiquement",
            "en": "resumes automatically",
            "es": "continúa automáticamente",
            "it": "riprende automaticamente",
            "pt": "continua automaticamente",
            "ru": "сборка продолжится сама",
            "ja": "自動的に再開",
            "hi": "अपने-आप आगे बढ़ेगा",
            "zh": "自动继续",
            "ko": "자동으로 계속",
            "id": "melanjutkan otomatis",
            "tr": "otomatik olarak devam",
        }
        for language, _label in LANGUAGES:
            feature = translate(language, "guide_license_feature")
            body = translate(language, "guide_intel_build_body")
            for marker in ("Apple Silicon", "Intel", "12"):
                self.assertIn(marker, feature, language)
                self.assertIn(marker, body, language)
            for marker in (
                "Python",
                "uv 0.12.5",
                "SHA-256",
                ".build-tools",
                "pkg-config",
                "sudo",
                "./Create_Community_Distribution_macOS.command",
                "x86_64",
                "FFmpeg",
                "PySide6/Qt",
            ):
                self.assertIn(marker, body, (language, marker))
            for step in ("1.", "2.", "3.", "4."):
                self.assertIn(f"\n{step} ", body, (language, step))
            self.assertIn("\n\n1. ", body, language)
            self.assertIn("./Create_Community_Distribution_macOS.command", body)
            self.assertNotIn("brew install pkg-config", body, language)
            compact_sections = body.splitlines()
            fourth_step = next(
                index for index, line in enumerate(compact_sections)
                if line.startswith("4. ")
            )
            self.assertEqual(compact_sections[fourth_step + 1], "", language)
            self.assertTrue(compact_sections[fourth_step + 2].strip(), language)
            self.assertEqual(compact_sections[fourth_step + 3], "", language)
            self.assertTrue(compact_sections[fourth_step + 4].strip(), language)
            self.assertIn("dist/LUFScale.app/Contents/MacOS/LUFScale", body)
            self.assertIn("dist/LUFScale.app/Contents/Frameworks/ffmpeg", body)
            self.assertIn(automatic_resume_markers[language], body, language)
        project_root = Path(__file__).parents[1]
        readme = (project_root / "README.md").read_text(encoding="utf-8")
        opening = (project_root / "OPEN_LUFSCALE_ON_MACOS.md").read_text(
            encoding="utf-8"
        )
        for document in (readme, opening):
            self.assertIn("Apple Silicon", document)
            self.assertIn("Intel", document)
            self.assertIn("macOS 12", document)
            self.assertIn("functional", document)

    def test_author_baseline_and_guide_card_body_size_are_fixed(self) -> None:
        project_root = Path(__file__).parents[1]
        header = (project_root / "src/lufscale/ui/panels/header.py").read_text(
            encoding="utf-8"
        )
        guides = (project_root / "tools/generate_guides.py").read_text(
            encoding="utf-8"
        )
        self.assertIn('subtitle_row.setContentsMargins(0, 0, 0, 3)', header)
        self.assertIn('DOCUMENT_BODY_SIZE = 6.7', guides)
        self.assertNotRegex(guides, r"body_(?:max|min)=\d")
        self.assertIn('body_leading_factor=1.15', guides)

    def test_localized_option_badges_fit_the_active_font(self) -> None:
        project_root = Path(__file__).parents[1]
        application = (project_root / "src/lufscale/application.py").read_text(
            encoding="utf-8"
        )
        settings = (project_root / "src/lufscale/ui/panels/settings.py").read_text(
            encoding="utf-8"
        )
        self.assertIn("def _fit_option_row_acronyms", application)
        self.assertIn("horizontalAdvance(label.text()) + 16", application)
        self.assertIn("label.setFixedWidth(width)", application)
        self.assertNotIn("acronym_label.setFixedWidth(48)", settings)

    def test_long_help_dialogs_remain_scrollable_and_resizable(self) -> None:
        project_root = Path(__file__).parents[1]
        dialogs_source = (project_root / "src/lufscale/ui/dialogs.py").read_text(
            encoding="utf-8"
        )
        dialogs = dialogs_source.split("class CompletionSummaryDialog", 1)[0]
        self.assertIn("text_view.setMaximumHeight(maximum_text_height)", dialogs)
        self.assertIn("self.setMaximumSize(dialog_width, maximum_height)", dialogs)
        self.assertNotIn("text_view.setFixedHeight(visible_text_height)", dialogs)
        self.assertNotIn("self.setFixedSize(dialog_width, dialog_height)", dialogs)

    def test_all_active_help_texts_are_explicitly_localized(self) -> None:
        help_keys = sorted(HELP_CONTENT_KEYS)
        for language, _label in LANGUAGES:
            if language not in {"fr", "en"}:
                for key in help_keys:
                    self.assertIn(key, EXTRA_TEXTS[language], f"{language}/{key}")
            journal = translate(language, "log_help_text")
            self.assertGreater(len(journal), 300, language)
            self.assertGreaterEqual(journal.count("\n\n"), 3, language)
        for language, _label in LANGUAGES:
            self.assertIn("GPL-3.0-or-later", translate(language, "guide_license_body"))
            self.assertIn(
                "GPL-3.0-or-later",
                translate(language, "guide_license_feature"),
            )

    def test_pdf_log_legend_is_explicitly_localized_and_uniform(self) -> None:
        legend_keys = (
            "guide_log_legend_success",
            "guide_log_legend_compliant",
            "guide_log_legend_warning",
            "guide_log_legend_cancelled",
            "guide_log_legend_error",
        )
        for language, _label in LANGUAGES:
            for key in legend_keys:
                value = translate(language, key)
                self.assertTrue(value.strip(), f"{language}/{key}")
                if language not in {"fr", "en"}:
                    self.assertIn(key, EXTRA_TEXTS[language])
        project_root = Path(__file__).parents[1]
        guides = (project_root / "tools/generate_guides.py").read_text(
            encoding="utf-8"
        )
        self.assertIn("badge_width = 96", guides)
        self.assertIn("max_size=5.4,\n            min_size=5.4", guides)
        self.assertNotIn("LOG_LEGEND_COPY", guides)

    def test_pdf_moves_licence_to_page_one_and_keeps_macos_build_on_page_five(self) -> None:
        for language, _label in LANGUAGES:
            licence = translate(language, "guide_license_body")
            build = PLATFORM_BUILD_COPY[language]
            self.assertIn("GPL-3.0-or-later", licence, language)
            self.assertNotIn("xcode-select --install", licence, language)
            self.assertTrue(build["title"].strip(), language)
            for marker in (
                "Apple Silicon", "Intel", "arm64", "x86_64",
                "./Create_Community_Distribution_macOS.command",
                "dist/LUFScale.app",
                "dist/LUFScale-2.1.12-macOS-arm64-community.zip",
                "dist/LUFScale-2.1.12-macOS-arm64-community.zip.sha256",
                "dist/LUFScale-2.1.12-macOS-x86_64-community.zip",
                "dist/LUFScale-2.1.12-macOS-x86_64-community.zip.sha256",
                ".app (",
                ".zip (",
                ".sha256 (",
            ):
                self.assertIn(marker, build["body"], (language, marker))
            for forbidden in (
                "Windows",
                "Create_Offline_Installer_Windows.cmd",
                "dist\\LUFScale-2.1.12-Setup-x64.exe",
                "dist\\LUFScale-2.1.12-Portable-x64.exe",
            ):
                self.assertNotIn(forbidden, build["title"] + build["body"], (language, forbidden))
            output_lines = build["body"].splitlines()
            self.assertEqual(
                output_lines.count("\t**./Create_Community_Distribution_macOS.command**"),
                2,
                language,
            )
            self.assertEqual(output_lines.count("\t**dist/LUFScale.app**"), 2, language)
            for output_path in (
                "\t**dist/LUFScale-2.1.12-macOS-arm64-community.zip**",
                "\t**dist/LUFScale-2.1.12-macOS-arm64-community.zip.sha256**",
                "\t**dist/LUFScale-2.1.12-macOS-x86_64-community.zip**",
                "\t**dist/LUFScale-2.1.12-macOS-x86_64-community.zip.sha256**",
            ):
                self.assertEqual(output_lines.count(output_path), 1, (language, output_path))
            self.assertEqual(
                sum(not line.strip() for line in output_lines),
                10,
                language,
            )
            command_indexes = [
                index
                for index, line in enumerate(output_lines)
                if line == "\t**./Create_Community_Distribution_macOS.command**"
            ]
            for index in command_indexes:
                self.assertFalse(output_lines[index - 1].strip(), language)
                self.assertFalse(output_lines[index + 1].strip(), language)
            app_indexes = [
                index for index, line in enumerate(output_lines)
                if line == "\t**dist/LUFScale.app**"
            ]
            self.assertFalse(output_lines[app_indexes[0] - 1].strip(), language)
            self.assertFalse(output_lines[app_indexes[1] - 1].strip(), language)
            self.assertEqual(
                output_lines[app_indexes[0] + 1],
                "\t**dist/LUFScale-2.1.12-macOS-arm64-community.zip**",
                language,
            )
            self.assertEqual(
                output_lines[app_indexes[1] + 1],
                "\t**dist/LUFScale-2.1.12-macOS-x86_64-community.zip**",
                language,
            )
            self.assertEqual(
                sum(line.startswith(".app (") for line in output_lines),
                1,
                language,
            )
            self.assertEqual(
                sum(
                    line.startswith(".zip (") for line in output_lines
                ),
                1,
                language,
            )
            intel_index = next(
                index
                for index, line in enumerate(output_lines)
                if "Intel" in line and "x86_64" in line
            )
            self.assertFalse(output_lines[intel_index - 1].strip(), language)
            self.assertEqual(sum(line.startswith(".sha256 (") for line in output_lines), 1, language)
        generator = (
            Path(__file__).parents[1] / "tools/generate_guides.py"
        ).read_text(encoding="utf-8")
        quick_page = generator.split("def page_quick_start", 1)[1].split(
            "def page_audio", 1
        )[0]
        technical_page = generator.split("def page_technical", 1)[1].split(
            "def draw_formula_card", 1
        )[0]
        footer = generator.split("def draw_footer", 1)[1].split(
            "def draw_two_column_cards", 1
        )[0]
        self.assertIn('translate(language, "guide_license_title")', quick_page)
        self.assertIn('translate(language, "guide_license_body")', quick_page)
        self.assertNotIn('translate(language, "guide_license_title")', technical_page)
        self.assertNotIn('translate(language, "guide_license_body")', technical_page)
        self.assertIn("c.drawCentredString(PAGE_WIDTH / 2, 30, str(page_number))", footer)
        self.assertIn("c.drawRightString(PAGE_WIDTH - 52, 30, APP_WEBSITE_URL)", footer)
        self.assertIn("PLATFORM_BUILD_COPY[language]", generator)
        self.assertIn("body_max=DOCUMENT_BODY_SIZE", generator)
        self.assertIn("body_min=DOCUMENT_BODY_SIZE", generator)
        self.assertIn(
            "body_max=DOCUMENT_BODY_SIZE,\n"
            "        body_min=DOCUMENT_BODY_SIZE",
            generator,
        )
        self.assertNotIn("PLATFORM_BUILD_BODY_SIZE", generator)
        self.assertIn("c, cards, 614, 266", generator)
        self.assertIn("PAGE_WIDTH - 104,\n        222,", generator)
        self.assertIn('separator="\\n \\n"', generator)
        self.assertIn('"&nbsp;" * 4', generator)
        self.assertIn('escaped = f"<b>{escaped}</b>"', generator)
        self.assertIn("pdfmetrics.registerFontFamily(", generator)

    def test_pdf_technical_prose_is_explicit_in_every_language(self) -> None:
        language_codes = {language for language, _label in LANGUAGES}
        for catalogue in (
            REFERENCE_COPY,
            TECHNICAL_COPY,
            COMPLIANCE_COPY,
            USEFUL_CHECKS_COPY,
        ):
            self.assertEqual(set(catalogue), language_codes)
        for language in language_codes:
            self.assertEqual(set(REFERENCE_COPY[language]), set(REFERENCE_COPY["en"]))
            self.assertEqual(set(TECHNICAL_COPY[language]), set(TECHNICAL_COPY["en"]))
            self.assertEqual(set(COMPLIANCE_COPY[language]), set(COMPLIANCE_COPY["en"]))
            self.assertEqual(
                set(USEFUL_CHECKS_COPY[language]),
                set(USEFUL_CHECKS_COPY["en"]),
            )
            self.assertEqual(len(USEFUL_CHECKS_COPY[language]["cards"]), 3)
            self.assertEqual(len(COMPLIANCE_COPY[language]["headings"]), 8)
            descriptions = COMPLIANCE_COPY[language]["descriptions"]
            self.assertEqual(len(descriptions), 8)
            self.assertEqual(len(set(descriptions)), 8)
            self.assertTrue(all(description.strip() for description in descriptions))
            if language == "en":
                continue
            for key, english in TECHNICAL_COPY["en"].items():
                self.assertNotEqual(TECHNICAL_COPY[language][key], english)
            self.assertNotEqual(
                COMPLIANCE_COPY[language]["subtitle"],
                COMPLIANCE_COPY["en"]["subtitle"],
            )
            self.assertNotEqual(
                COMPLIANCE_COPY[language]["headings"],
                COMPLIANCE_COPY["en"]["headings"],
            )
        generator = (
            Path(__file__).parents[1] / "tools/generate_guides.py"
        ).read_text(encoding="utf-8")
        self.assertNotIn('TECHNICAL_COPY.get(language', generator)
        self.assertNotIn('if language == "fr":\n        subtitle', generator)
        self.assertIn('descriptions = compliance_copy["descriptions"]', generator)
        compliance_source = generator.split("def page_compliance", 1)[1].split(
            "def page_release", 1
        )[0]
        for index in range(8):
            self.assertIn(f"descriptions[{index}]", compliance_source)
        self.assertNotIn('technical_copy(language, "dynamic")', compliance_source)
        self.assertNotIn('technical_copy(language, "retries")', compliance_source)
        self.assertNotIn('technical_copy(language, "qc_off")', compliance_source)

    def test_pdf_audio_options_and_useful_checks_are_unambiguous(self) -> None:
        project_root = Path(__file__).parents[1]
        for language, _label in LANGUAGES:
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
            checks = USEFUL_CHECKS_COPY[language]
            self.assertTrue(checks["heading"].strip(), language)
            self.assertTrue(
                all(title.strip() and body.strip() for title, body in checks["cards"]),
                language,
            )

        generator = (project_root / "tools/generate_guides.py").read_text("utf-8")
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

    def test_public_builders_document_their_internal_workers(self) -> None:
        project_root = Path(__file__).parents[1]
        readme = (project_root / "README.md").read_text(encoding="utf-8")
        create_script = (
            project_root / "Create_Community_Distribution_macOS.command"
        ).read_text(encoding="utf-8")
        self.assertIn("Create_Community_Distribution_macOS.command", readme)
        self.assertIn("Internal_Application_Builder_macOS.command", readme)
        self.assertIn(
            "./tools/Internal_Application_Builder_macOS.command", create_script
        )

    def test_macos_builder_bootstraps_private_python_without_elevation(self) -> None:
        project_root = Path(__file__).parents[1]
        builder = (
            project_root / "tools/Internal_Application_Builder_macOS.command"
        ).read_text("utf-8")
        for marker in (
            'python_version="3.13.15"',
            'uv_version="0.12.5"',
            'uv_python_dir="$build_tools_dir/python"',
            'uv_cache_dir="$build_tools_dir/uv-cache"',
            'UV_MANAGED_PYTHON=1',
            'python install "$python_version"',
            'python find "$python_version"',
            "5bb0e5fe008a773c3dbcb97ff79cd89e1241464fe9d2f986d52ad8f1b037bd62",
            "b3b2137477cf96c9686ebfb71524614cec780c673fd73e59bce099aef02e70e8",
            "xcode-select --install",
            "Waiting for the Xcode Command Line Tools installation to finish",
            "Continuing the LUFScale build automatically",
            '/bin/sleep "$poll_seconds"',
            'export PATH="$project_root/tools:$PATH"',
        ):
            self.assertIn(marker, builder)
        for forbidden in (
            "/usr/bin/sudo",
            "/usr/sbin/installer",
            "pkgutil --check-signature",
            "/Library/Frameworks/Python.framework",
            "python.org/ftp/python",
        ):
            self.assertNotIn(forbidden, builder)
        self.assertNotIn("Complete it, then run this builder again", builder)
        self.assertTrue((project_root / "tools/pkg-config").is_file())
        self.assertTrue((project_root / "tools/pkg_config_lite.py").is_file())

    def test_csv_and_auto_start_are_disabled_by_default(self) -> None:
        project_root = Path(__file__).parents[1]
        panel = (project_root / "src/lufscale/ui/panels/settings.py").read_text(
            "utf-8"
        )
        settings = (project_root / "src/lufscale/ui/settings.py").read_text("utf-8")
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

    def test_private_pkg_config_resolves_static_dependency_graph(self) -> None:
        project_root = Path(__file__).parents[1]
        helper = project_root / "tools/pkg_config_lite.py"
        with tempfile.TemporaryDirectory() as temporary:
            pc_dir = Path(temporary)
            (pc_dir / "ogg.pc").write_text(
                "prefix=/opt/audio\nlibdir=${prefix}/lib\nincludedir=${prefix}/include\n"
                "Name: ogg\nVersion: 1.3.6\nLibs: -L${libdir} -logg\n"
                "Cflags: -I${includedir}\n",
                encoding="utf-8",
            )
            (pc_dir / "vorbis.pc").write_text(
                "prefix=/opt/audio\nlibdir=${prefix}/lib\nincludedir=${prefix}/include\n"
                "Name: vorbis\nVersion: 1.3.7\nRequires.private: ogg >= 1.3.0\n"
                "Libs: -L${libdir} -lvorbis\nLibs.private: -lm\n"
                "Cflags: -I${includedir}\n",
                encoding="utf-8",
            )
            environment = {**os.environ, "PKG_CONFIG_LIBDIR": str(pc_dir)}
            completed = subprocess.run(
                [
                    sys.executable,
                    str(helper),
                    "--libs",
                    "--static",
                    "vorbis >= 1.3.0",
                ],
                check=True,
                capture_output=True,
                text=True,
                env=environment,
            )
            self.assertEqual(
                completed.stdout.strip(),
                "-L/opt/audio/lib -lvorbis -lm -logg",
            )

    def test_private_pkg_config_accepts_lame_version_probe(self) -> None:
        project_root = Path(__file__).parents[1]
        helper = project_root / "tools/pkg_config_lite.py"
        for arguments, expected_status in (
            (["--atleast-pkgconfig-version", "0.9.0"], 0),
            (["--atleast-pkgconfig-version=0.9.0"], 0),
            (["--atleast-pkgconfig-version", "99.0"], 1),
        ):
            completed = subprocess.run(
                [sys.executable, str(helper), *arguments],
                check=False,
                capture_output=True,
                text=True,
                timeout=5,
            )
            self.assertEqual(completed.returncode, expected_status, arguments)

        with tempfile.TemporaryDirectory() as temporary:
            completed = subprocess.run(
                [
                    sys.executable,
                    str(helper),
                    "--exists",
                    "--print-errors",
                    "libmpg123 >= 1.26.0",
                ],
                check=False,
                capture_output=True,
                text=True,
                timeout=5,
                env={**os.environ, "PKG_CONFIG_LIBDIR": temporary},
            )
        self.assertEqual(completed.returncode, 1)
        self.assertIn("libmpg123", completed.stderr)

    def test_source_distribution_is_macos_only(self) -> None:
        project_root = Path(__file__).parents[1]
        absent = (
            "tools/Internal_Application_Builder_Windows.ps1",
            "tools/Internal_Installer_Orchestrator_Windows.ps1",
            "OPEN_LUFSCALE_ON_WINDOWS.md",
            "packaging/windows",
            "output/pdf/windows",
            "tools/prepare_bundled_ffmpeg_windows.py",
        )
        for relative in absent:
            self.assertFalse((project_root / relative).exists(), relative)
        requirements = (project_root / "requirements.txt").read_text("utf-8")
        self.assertNotIn("imageio-ffmpeg", requirements)
        sbom = (project_root / "SBOM.cdx.json").read_text("utf-8")
        self.assertNotIn("Windows", sbom)
        self.assertNotIn("imageio-ffmpeg", sbom)

    def test_macos_build_verifies_every_embedded_runtime(self) -> None:
        project_root = Path(__file__).parents[1]
        build = (
            project_root / "tools/Internal_Application_Builder_macOS.command"
        ).read_text("utf-8")
        manifest_tool = (
            project_root / "tools/generate_runtime_manifest.py"
        ).read_text("utf-8")
        for marker in (
            "The Python runtime was not included",
            "The PySide6/Qt runtime was not included",
            "LUFSCALE_RUNTIME_MANIFEST.json",
            "non-system external runtime",
            "reportlab==4.4.3",
            "tools/generate_guides.py",
        ):
            self.assertIn(marker, build)
        for marker in (
            '"python": platform.python_version()',
            '"pyside6_qt": PySide6.__version__',
            '"ffmpeg"',
            '"end_user_external_runtime_required": False',
        ):
            self.assertIn(marker, manifest_tool)

    def test_documented_quality_thresholds_match_runtime(self) -> None:
        self.assertEqual(STRICT_TARGET_LUFS_TOLERANCE, 0.50)
        self.assertEqual(QUALITY_CONTROL_LUFS_TOLERANCE, 0.60)
        self.assertEqual(QUALITY_CONTROL_TRUE_PEAK_TOLERANCE_DB, 0.25)
        settings = LoudnessSettings(integrated_lufs=-14.0, true_peak=-2.0)
        base = {
            "input_lra": "4.0",
            "input_thresh": "-24.0",
            "target_offset": "0.0",
        }

        strict_edge = {**base, "input_i": "-14.50", "input_tp": "-2.00"}
        strict_outside = {**base, "input_i": "-14.51", "input_tp": "-2.00"}
        self.assertTrue(dynamic_mp3_output_is_strictly_compliant(settings, strict_edge))
        self.assertFalse(
            dynamic_mp3_output_is_strictly_compliant(settings, strict_outside)
        )

        input_measurements = {
            **base,
            "input_i": "-18.0",
            "input_tp": "-5.0",
        }
        qc_edge = {**base, "input_i": "-14.60", "input_tp": "-1.75"}
        qc_outside = {**base, "input_i": "-14.61", "input_tp": "-1.74"}
        self.assertTrue(
            assess_quality(settings, input_measurements, qc_edge).passed
        )
        self.assertFalse(
            assess_quality(settings, input_measurements, qc_outside).passed
        )

        generator = (
            Path(__file__).parents[1] / "tools/generate_guides.py"
        ).read_text(encoding="utf-8")
        for constant in (
            "STRICT_TARGET_LUFS_TOLERANCE",
            "QUALITY_CONTROL_LUFS_TOLERANCE",
            "QUALITY_CONTROL_TRUE_PEAK_TOLERANCE_DB",
            "MP3_DYNAMIC_RETRY_MIN_STEP_DB",
        ):
            self.assertGreaterEqual(generator.count(constant), 2, constant)
        self.assertIn("strict<sub>OK</sub>", generator)
        self.assertNotIn("QC<sub>retry</sub>", generator)

    def test_help_dialogs_share_the_french_section_structure(self) -> None:
        self.assertEqual(len(HELP_DIALOG_SECTIONS), 16)
        self.assertEqual(len(HELP_CONTENT_KEYS), 21)
        for dialog, sections in HELP_DIALOG_SECTIONS.items():
            self.assertTrue(sections, dialog)
            for language, _label in LANGUAGES:
                localized = [translate(language, key) for key in sections]
                self.assertEqual(len(localized), len(sections), f"{language}/{dialog}")
                self.assertTrue(all(value.strip() for value in localized))

    def test_detailed_help_keeps_technical_reference_points(self) -> None:
        required_markers = {
            "volume_tooltip": ("-18", "-16", "-14"),
            "target_tooltip": ("-18", "-16", "-14", "2 LU"),
            "peak_tooltip": ("-1", "-2", "0 dBTP"),
            "quality_tooltip": (
                "0", "1", "2", "3", "4", "5", "9",
                "FLAC", "WAV", "AIFF", "MP3", "M4A", "OGG", "Opus",
            ),
            "parallel_tooltip": ("4", "70", "92", "16", "CPU"),
            "quality_control_tooltip": ("0.50", "0.60", "MP3", "WAV", "AIFF", "FLAC"),
        }
        for language, _label in LANGUAGES:
            for key, markers in required_markers.items():
                localized = translate(language, key).replace(",", ".")
                for marker in markers:
                    self.assertIn(marker, localized, f"{language}/{key}/{marker}")

    def test_guides_open_with_purpose_and_drop_retired_analysis_copy(self) -> None:
        for language, _label in LANGUAGES:
            title = EXTRA_TEXTS.get(language, {}).get(
                "guide_quality_priority_title",
                TEXTS["guide_quality_priority_title"][0 if language == "fr" else 1],
            )
            body = EXTRA_TEXTS.get(language, {}).get(
                "guide_quality_priority_body",
                TEXTS["guide_quality_priority_body"][0 if language == "fr" else 1],
            )
            method = EXTRA_TEXTS.get(language, {}).get(
                "guide_analysis_method",
                TEXTS["guide_analysis_method"][0 if language == "fr" else 1],
            )
            self.assertIn("LUFScale", title, language)
            self.assertIn("LUFScale", body, language)
            self.assertIn("LUFScale", method, language)
        self.assertEqual(TEXTS["guide_quality_priority_title"][0], "À quoi sert LUFScale ?")
        self.assertNotIn("variantes Rapide", TEXTS["guide_analysis_method"][0])
        self.assertNotIn("Fast and Adaptive", TEXTS["guide_analysis_method"][1])

    def test_explicit_external_ffmpeg_path_is_recognized(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            ffmpeg = Path(temporary) / "ffmpeg"
            ffmpeg.touch()
            with mock.patch.dict(
                "os.environ", {"IMAGEIO_FFMPEG_EXE": str(ffmpeg)}
            ):
                find_ffmpeg.cache_clear()
                self.assertEqual(find_ffmpeg(), str(ffmpeg))
        find_ffmpeg.cache_clear()

    def test_bundled_ffmpeg_has_priority_in_pyinstaller_resources(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            ffmpeg = root / "ffmpeg"
            ffmpeg.touch()
            with mock.patch(
                "lufscale.processing.ffmpeg.application_resource_folder",
                return_value=root,
            ):
                find_ffmpeg.cache_clear()
                self.assertEqual(find_ffmpeg(), str(ffmpeg))
        find_ffmpeg.cache_clear()

    def test_frozen_release_never_falls_back_to_external_ffmpeg(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            empty_root = Path(temporary)
            with (
                mock.patch(
                    "lufscale.processing.ffmpeg.application_resource_folder",
                    return_value=empty_root,
                ),
                mock.patch(
                    "lufscale.processing.ffmpeg.application_folder",
                    return_value=empty_root,
                ),
                mock.patch(
                    "lufscale.processing.ffmpeg.sys.frozen",
                    True,
                    create=True,
                ),
                mock.patch.dict(
                    "os.environ", {"IMAGEIO_FFMPEG_EXE": "/tmp/external-ffmpeg"}
                ),
                mock.patch("lufscale.processing.ffmpeg.shutil.which") as which,
            ):
                find_ffmpeg.cache_clear()
                self.assertIsNone(find_ffmpeg())
                which.assert_not_called()
        find_ffmpeg.cache_clear()

    def test_same_named_standalone_files_keep_supported_extensions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = root / "one" / "same.mp3"
            second = root / "two" / "same.mp3"
            first.parent.mkdir()
            second.parent.mkdir()
            first.touch()
            second.touch()

            jobs = build_jobs([first, second], root / "output")

            self.assertEqual(
                [job.destination.name for job in jobs],
                ["same.mp3", "same__2.mp3"],
            )
            self.assertTrue(all(job.destination.suffix == ".mp3" for job in jobs))

    def test_replaygain_command_has_required_container_flags(self) -> None:
        source = Path("source.wav")
        cases = {
            ".mp3": ("-id3v2_version", "3"),
            ".aif": ("-write_id3v2", "1"),
            ".aiff": ("-write_id3v2", "1"),
            ".m4a": ("-movflags", "use_metadata_tags"),
        }
        for suffix, required in cases.items():
            with self.subTest(suffix=suffix):
                command = replaygain_command(
                    "ffmpeg",
                    source,
                    Path(f"target{suffix}"),
                    2.5,
                    -1.0,
                )
                joined = "\0".join(command)
                self.assertIn("\0".join(required), joined)

    def test_metadata_dump_reads_container_and_audio_stream_tags(self) -> None:
        command = metadata_dump_command("ffmpeg", Path("target.ogg"))
        positions = [
            index for index, value in enumerate(command) if value == "-map_metadata"
        ]
        self.assertEqual(len(positions), 2)
        self.assertEqual(command[positions[0] + 1], "0")
        self.assertEqual(command[positions[1] + 1], "0:s:a:0")

    def test_active_messages_are_localized_in_all_selectable_languages(self) -> None:
        keys: set[str] = set()
        package_root = Path(__file__).parents[1] / "src" / "lufscale"
        for path in package_root.rglob("*.py"):
            if "i18n" in path.parts:
                continue
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                function = node.func
                name = (
                    function.id
                    if isinstance(function, ast.Name)
                    else function.attr
                    if isinstance(function, ast.Attribute)
                    else ""
                )
                if name not in {"t", "translate"}:
                    continue
                argument_index = 0 if name == "t" else 1
                if (
                    len(node.args) > argument_index
                    and isinstance(node.args[argument_index], ast.Constant)
                    and isinstance(node.args[argument_index].value, str)
                ):
                    keys.add(node.args[argument_index].value)
        for prefix in ("status_", "option_status_"):
            keys.update(key for key in TEXTS if key.startswith(prefix))
        # Combo-box item keys are passed through a helper as variables and
        # therefore cannot be discovered by the literal-call scan above.
        keys.update(
            {
                "preset_library",
                "preset_streaming",
                "preset_dynamic",
                "custom",
                "operation_convert",
                "operation_replaygain",
                "operation_analyze",
                "analysis_method_historical",
                "volume_soft",
                "volume_normal",
                "volume_loud",
            }
        )

        formatter = string.Formatter()

        def fields(value: str) -> set[str]:
            return {
                field
                for _literal, field, _spec, _conversion in formatter.parse(value)
                if field
            }

        for language, _label in LANGUAGES:
            for key in keys:
                if key not in TEXTS:
                    continue
                english = TEXTS[key][1]
                if language == "fr":
                    localized = TEXTS[key][0]
                elif language == "en":
                    localized = english
                else:
                    self.assertIn(key, EXTRA_TEXTS[language])
                    localized = EXTRA_TEXTS[language][key]
                self.assertEqual(
                    fields(localized),
                    fields(english),
                    f"placeholder mismatch: {language}/{key}",
                )

    def test_visible_ui_has_no_unintended_english_fallbacks(self) -> None:
        common = {"warning_list_title", "error_list_title"}
        older_catalogues = {
            "ru": {
                "analyze_operation", "cancelling", "ffmpeg_missing_message",
                "ffmpeg_no_lame", "folder", "loudness_meter_estimated",
                "loudness_meter_measured", "replaygain_operation",
                "scanning_folders",
            },
            "ja": {
                "analyze_operation", "cancelling", "ffmpeg_missing_message",
                "ffmpeg_no_lame", "folder", "loudness_meter_estimated",
                "loudness_meter_measured", "replaygain_operation",
                "scanning_folders",
            },
            "hi": {"loudness_comparison_replaygain_note"},
        }
        recent_catalogue = {
            "activity_cancelling", "analysis_method_adaptive",
            "analysis_method_fast", "analyze_operation", "cancelling",
            "convert_operation", "ffmpeg_missing", "ffmpeg_missing_message",
            "ffmpeg_no_lame", "loudness_meter_estimated",
            "loudness_meter_measured", "loudness_meter_title",
            "loudness_meter_tooltip", "loudness_meter_waiting",
            "loudness_score_acceptable", "loudness_score_check",
            "loudness_score_excellent", "loudness_score_needs_qc",
            "loudness_score_not_applicable", "loudness_score_tooltip",
            "loudness_score_waiting", "path_left", "path_right",
            "processing_completed", "replaygain_operation",
            "report_destination", "report_detail", "report_gain",
            "report_input_dbtp", "report_input_lufs", "report_operation",
            "report_output_dbtp", "report_output_lufs", "report_qc",
            "report_qc_engine", "report_seconds", "report_source",
            "scanning_folders", "true_peak_meter_title",
            "true_peak_meter_tooltip", "true_peak_meter_waiting",
            "errors_button_tooltip", "errors_dialog_title",
            "warnings_button_tooltip", "warnings_dialog_title",
            "loudness_meter_no_file",
        }
        for language, _label in LANGUAGES:
            if language in {"fr", "en"}:
                continue
            keys = set(common) | older_catalogues.get(language, set())
            if language in {"ko", "id", "tr"}:
                keys |= recent_catalogue
            for key in keys:
                self.assertNotEqual(
                    translate(language, key),
                    translate("en", key),
                    f"English fallback: {language}/{key}",
                )

    def test_hindi_guide_prose_does_not_mix_in_english_sentences(self) -> None:
        values = list(REFERENCE_COPY["hi"].values())
        values += list(TECHNICAL_COPY["hi"].values())
        values += [COMPLIANCE_COPY["hi"]["subtitle"]]
        values += list(COMPLIANCE_COPY["hi"]["headings"])
        values += list(COMPLIANCE_COPY["hi"]["descriptions"])
        values += [
            translate("hi", key)
            for key in (
                "guide_analysis_method", "guide_analyze_prediction_title",
                "guide_analyze_prediction_body", "guide_file_processing_title",
                "guide_file_processing_body", "guide_intel_build_title",
                "guide_intel_build_body", "guide_license_body",
                "guide_quality_priority_body", "operation_help_text",
                "quality_control_tooltip", "replaygain_qc_help_text",
                "version_changes",
            )
        ]
        prose = " ".join(values).lower()
        for phrase in (
            " english ", " target ", " output ", " internal ",
            " true peak ", " linear ", " feedback ", " retry ",
            " quality control ", " source package ", " processing ",
            " estimate ", " variant ", " validated ", " guaranteed ",
            " script ", " runtime ", " warranty ", " notices ",
        ):
            self.assertNotIn(phrase, f" {prose} ", phrase)


if __name__ == "__main__":
    unittest.main()
