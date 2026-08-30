#!/usr/bin/env python3
"""Generate the complete multilingual LUFScale PDF guides."""

from __future__ import annotations

import html
import argparse
import re
import sys
from pathlib import Path
from typing import Iterable

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
APP_ICON_PATH = PROJECT_ROOT / "assets" / "branding" / "LUFScale_logo.png"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from lufscale.audio.core import (  # noqa: E402
    ALREADY_COMPLIANT_LUFS_TOLERANCE,
    LOUDNORM_LINEAR_SAFETY_MARGIN_DB,
    LOUDNORM_MIN_TRUE_PEAK_DBTP,
    MP3_DYNAMIC_RETRY_GUARD_DB,
    MP3_DYNAMIC_RETRY_MIN_STEP_DB,
    MP3_DYNAMIC_RETRY_MAX_ATTEMPTS,
    MP3_DYNAMIC_TRUE_PEAK_MARGIN_DB,
    QUALITY_CONTROL_LUFS_TOLERANCE,
    QUALITY_CONTROL_TRUE_PEAK_TOLERANCE_DB,
    STRICT_TARGET_LUFS_TOLERANCE,
    TARGET_CORRECTION_MAX_ATTEMPTS,
)
from lufscale.i18n.guide_technical import (  # noqa: E402
    COMPLIANCE_COPY,
    REFERENCE_COPY,
    TECHNICAL_COPY,
)
from lufscale.i18n.guide_build import PLATFORM_BUILD_COPY  # noqa: E402
from lufscale.i18n.guide_checks import USEFUL_CHECKS_COPY  # noqa: E402
from lufscale.i18n.loader import LANGUAGES, translate  # noqa: E402
from lufscale.resources import PDF_GUIDES  # noqa: E402
from lufscale.ui.settings import PRESETS  # noqa: E402
from lufscale.version import (  # noqa: E402
    APP_AUTHOR,
    APP_RELEASE_YEAR,
    APP_VERSION,
    APP_WEBSITE_URL,
)


PAGE_WIDTH, PAGE_HEIGHT = A4
BLUE = colors.HexColor("#2463eb")
BLUE_DARK = colors.HexColor("#18345c")
GREEN = colors.HexColor("#16895d")
INK = colors.HexColor("#172033")
MUTED = colors.HexColor("#59677a")
LINE = colors.HexColor("#c9d5e5")
PANEL = colors.HexColor("#f9fbfe")
SOFT_BLUE = colors.HexColor("#eef5ff")
FORMULA_PANEL = colors.HexColor("#edf3fb")
MATH_FONT = "Guide-Math-Regular"
DOCUMENT_BODY_SIZE = 6.7


MACOS_GUIDE_IDENTITY_LABELS = {
    "fr": "LUFScale pour macOS - version {version}",
    "en": "LUFScale for macOS - version {version}",
    "es": "LUFScale para macOS - versión {version}",
    "it": "LUFScale per macOS - versione {version}",
    "pt": "LUFScale para macOS - versão {version}",
    "ru": "LUFScale для macOS - версия {version}",
    "ja": "macOS版 LUFScale - バージョン {version}",
    "hi": "macOS के लिए LUFScale - संस्करण {version}",
    "zh": "LUFScale macOS 版 - 版本 {version}",
    "ko": "macOS용 LUFScale - 버전 {version}",
    "id": "LUFScale untuk macOS - versi {version}",
    "tr": "macOS için LUFScale - sürüm {version}",
}

LOG_LEGEND_TITLES = {
    "fr": "Repères de couleur du journal de traitement",
    "en": "Processing-log colour key",
    "es": "Leyenda de colores del registro de procesamiento",
    "it": "Legenda colori del registro di elaborazione",
    "pt": "Legenda de cores do registo de processamento",
    "ru": "Цветовые обозначения журнала обработки",
    "ja": "処理ログの色分け",
    "hi": "प्रोसेसिंग लॉग का रंग संकेत",
    "zh": "处理日志颜色说明",
    "ko": "처리 로그 색상 안내",
    "id": "Keterangan warna log pemrosesan",
    "tr": "İşlem günlüğü renk anahtarı",
}


DOC_LABELS = {
    "fr": {
        "guide": "Guide graphique",
        "tagline": "Uniformiser le volume perçu sans modifier les originaux",
        "quick": "Démarrage rapide",
        "audio": "Comprendre les réglages Audio",
        "options": "Comprendre les Options",
        "processing": "Ce qui se passe pendant le traitement",
        "recommended": "Réglages conseillés et repères",
        "technical": "Annexe technique",
        "formulas": "Annexe technique - calculs et formules",
        "release": "Nouveautés et références",
        "preset_note": "Ces préréglages sont des choix pratiques de l’application, pas des normes universelles.",
        "refs": "Références techniques officielles",
        "gating": "Filtrage par seuils",
        "bs_body": "Les énergies des canaux, pondérées K, sont combinées pour calculer la sonie intégrée.",
        "gating_body": "Les seuils absolu et relatif sélectionnent les blocs retenus dans la mesure intégrée.",
    },
    "en": {
        "guide": "Visual guide",
        "tagline": "Normalize perceived loudness without changing the originals",
        "quick": "Quick start",
        "audio": "Understanding Audio settings",
        "options": "Understanding Options",
        "processing": "What happens during processing",
        "recommended": "Recommended settings and reference points",
        "technical": "Technical appendix",
        "formulas": "Technical appendix - calculations and formulas",
        "release": "What is new and references",
        "preset_note": "These presets are practical application choices, not universal standards.",
        "refs": "Official technical references",
        "gating": "Gating",
        "bs_body": "K-weighted channel energies are combined to calculate integrated loudness.",
        "gating_body": "Absolute and relative gates select the blocks retained by the integrated measurement.",
    },
    "es": {
        "guide": "Guía visual",
        "tagline": "Uniformar el volumen percibido sin modificar los originales",
        "quick": "Inicio rápido",
        "audio": "Comprender los ajustes de Audio",
        "options": "Comprender las Opciones",
        "processing": "Qué ocurre durante el procesamiento",
        "recommended": "Ajustes aconsejados y referencias",
        "technical": "Anexo técnico",
        "formulas": "Anexo técnico - cálculos y fórmulas",
        "release": "Novedades y referencias",
        "preset_note": "Estos preajustes son elecciones prácticas de la aplicación, no normas universales.",
        "refs": "Referencias técnicas oficiales",
        "gating": "Umbrales de medida",
        "bs_body": "Las energías de los canales, ponderadas K, se combinan para calcular la sonoridad integrada.",
        "gating_body": "Los umbrales absoluto y relativo seleccionan los bloques usados por la medición integrada.",
    },
    "it": {
        "guide": "Guida visuale",
        "tagline": "Uniformare il volume percepito senza modificare gli originali",
        "quick": "Avvio rapido",
        "audio": "Capire le impostazioni Audio",
        "options": "Capire le Opzioni",
        "processing": "Cosa accade durante l’elaborazione",
        "recommended": "Impostazioni consigliate e riferimenti",
        "technical": "Appendice tecnica",
        "formulas": "Appendice tecnica - calcoli e formule",
        "release": "Novità e riferimenti",
        "preset_note": "Queste preimpostazioni sono scelte pratiche dell’applicazione, non norme universali.",
        "refs": "Riferimenti tecnici ufficiali",
        "gating": "Soglie di misura",
        "bs_body": "Le energie dei canali, pesate K, vengono combinate per calcolare la sonorità integrata.",
        "gating_body": "Le soglie assoluta e relativa selezionano i blocchi usati dalla misura integrata.",
    },
    "pt": {
        "guide": "Guia visual",
        "tagline": "Uniformizar o volume percebido sem alterar os originais",
        "quick": "Início rápido",
        "audio": "Compreender as definições de Áudio",
        "options": "Compreender as Opções",
        "processing": "O que acontece durante o processamento",
        "recommended": "Definições aconselhadas e referências",
        "technical": "Anexo técnico",
        "formulas": "Anexo técnico - cálculos e fórmulas",
        "release": "Novidades e referências",
        "preset_note": "Estas predefinições são escolhas práticas da aplicação, não normas universais.",
        "refs": "Referências técnicas oficiais",
        "gating": "Limiares de medição",
        "bs_body": "As energias dos canais, ponderadas K, são combinadas para calcular a sonoridade integrada.",
        "gating_body": "Os limiares absoluto e relativo selecionam os blocos usados na medição integrada.",
    },
    "ru": {
        "guide": "Наглядное руководство",
        "tagline": "Выравнивание воспринимаемой громкости без изменения оригиналов",
        "quick": "Быстрый запуск",
        "audio": "Настройки аудио",
        "options": "Параметры",
        "processing": "Что происходит во время обработки",
        "recommended": "Рекомендуемые настройки и ориентиры",
        "technical": "Техническое приложение",
        "formulas": "Техническое приложение - расчёты и формулы",
        "release": "Изменения и ссылки",
        "preset_note": "Эти наборы являются практическими вариантами приложения, а не универсальными стандартами.",
        "refs": "Официальные технические источники",
        "gating": "Пороговый отбор",
        "bs_body": "Энергии каналов с K-взвешиванием объединяются для расчёта интегральной громкости.",
        "gating_body": "Абсолютный и относительный пороги выбирают блоки для интегрального измерения.",
    },
    "ja": {
        "guide": "ビジュアルガイド",
        "tagline": "元ファイルを変更せずに知覚音量を均一化",
        "quick": "クイックスタート",
        "audio": "オーディオ設定",
        "options": "オプション",
        "processing": "処理中の動作",
        "recommended": "推奨設定と目安",
        "technical": "技術付録",
        "formulas": "技術付録 - 計算と式",
        "release": "変更点と参考資料",
        "preset_note": "これらのプリセットはアプリの実用的な選択肢であり、普遍的な規格ではありません。",
        "refs": "公式技術資料",
        "gating": "ゲーティング",
        "bs_body": "K特性で重み付けした各チャンネルのエネルギーを組み合わせ、統合ラウドネスを算出します。",
        "gating_body": "絶対ゲートと相対ゲートにより、統合測定に使用するブロックを選択します。",
    },
    "hi": {
        "guide": "दृश्य मार्गदर्शिका",
        "tagline": "मूल फ़ाइलों को बदले बिना सुने जाने वाले वॉल्यूम को समान करें",
        "quick": "त्वरित शुरुआत",
        "audio": "ऑडियो सेटिंग समझें",
        "options": "विकल्प समझें",
        "processing": "प्रसंस्करण के दौरान क्या होता है",
        "recommended": "अनुशंसित सेटिंग और संदर्भ",
        "technical": "तकनीकी परिशिष्ट",
        "formulas": "तकनीकी परिशिष्ट - गणना और सूत्र",
        "release": "नया क्या है और संदर्भ",
        "preset_note": "ये प्रीसेट ऐप के व्यावहारिक विकल्प हैं, सार्वभौमिक मानक नहीं।",
        "refs": "आधिकारिक तकनीकी संदर्भ",
        "gating": "दहलीज-आधारित छनाई",
        "bs_body": "K-भारित चैनल ऊर्जाओं को मिलाकर समेकित ध्वनि-तीव्रता की गणना की जाती है।",
        "gating_body": "निरपेक्ष और सापेक्ष दहलीजें समेकित मापन में रखे जाने वाले खंड चुनती हैं।",
    },
    "zh": {
        "guide": "图形指南",
        "tagline": "不修改原文件，统一感知响度",
        "quick": "快速开始",
        "audio": "了解音频设置",
        "options": "了解选项",
        "processing": "处理过程中发生什么",
        "recommended": "建议设置和参考值",
        "technical": "技术附录",
        "formulas": "技术附录 - 计算与公式",
        "release": "更新与参考资料",
        "preset_note": "这些预设是应用中的实用选择，不是通用标准。",
        "refs": "官方技术参考资料",
        "gating": "门限筛选",
        "bs_body": "将经过K加权的各声道能量合并，用于计算综合响度。",
        "gating_body": "绝对门限和相对门限用于选择综合测量所采用的时间块。",
    },
    "ko": {
        "guide": "그래픽 안내서",
        "tagline": "원본을 변경하지 않고 체감 음량을 균일화",
        "quick": "빠른 시작",
        "audio": "오디오 설정 이해",
        "options": "옵션 이해",
        "processing": "처리 중 수행되는 작업",
        "recommended": "권장 설정과 기준",
        "technical": "기술 부록",
        "formulas": "기술 부록 - 계산과 공식",
        "release": "변경 사항과 참고 자료",
        "preset_note": "이 프리셋은 앱의 실용적인 선택이며 보편적인 표준이 아닙니다.",
        "refs": "공식 기술 참고 자료",
        "gating": "게이팅",
        "bs_body": "K 가중 채널 에너지를 합산해 통합 라우드니스를 계산합니다.",
        "gating_body": "절대 및 상대 게이트가 통합 측정에 사용할 블록을 선택합니다.",
    },
    "id": {
        "guide": "Panduan visual",
        "tagline": "Seragamkan volume yang dirasakan tanpa mengubah berkas asli",
        "quick": "Mulai cepat",
        "audio": "Memahami pengaturan Audio",
        "options": "Memahami Opsi",
        "processing": "Yang terjadi selama pemrosesan",
        "recommended": "Pengaturan yang disarankan dan acuan",
        "technical": "Lampiran teknis",
        "formulas": "Lampiran teknis - perhitungan dan rumus",
        "release": "Pembaruan dan referensi",
        "preset_note": "Prasetel ini adalah pilihan praktis aplikasi, bukan standar universal.",
        "refs": "Referensi teknis resmi",
        "gating": "Gating",
        "bs_body": "Energi kanal berbobot K digabungkan untuk menghitung kenyaringan terintegrasi.",
        "gating_body": "Gate absolut dan relatif memilih blok yang dipakai oleh pengukuran terintegrasi.",
    },
    "tr": {
        "guide": "Görsel kılavuz",
        "tagline": "Özgün dosyaları değiştirmeden algılanan ses düzeyini eşitleyin",
        "quick": "Hızlı başlangıç",
        "audio": "Ses ayarlarını anlama",
        "options": "Seçenekleri anlama",
        "processing": "İşleme sırasında ne olur",
        "recommended": "Önerilen ayarlar ve başvuru değerleri",
        "technical": "Teknik ek",
        "formulas": "Teknik ek - hesaplamalar ve formüller",
        "release": "Yenilikler ve kaynaklar",
        "preset_note": "Bu ön ayarlar uygulamanın pratik seçimleridir, evrensel standartlar değildir.",
        "refs": "Resmî teknik kaynaklar",
        "gating": "Geçitleme",
        "bs_body": "K ağırlıklı kanal enerjileri birleştirilerek tümleşik ses yüksekliği hesaplanır.",
        "gating_body": "Mutlak ve göreli geçitler, tümleşik ölçümde kullanılacak blokları seçer.",
    },
}


def _font_paths() -> dict[str, tuple[Path, Path]]:
    fonts = PROJECT_ROOT / "assets" / "fonts"
    paths = {
        "latin": (fonts / "DejaVuSans.ttf", fonts / "DejaVuSans-Bold.ttf"),
        "ja": (fonts / "NotoSansJP-Regular.ttf", fonts / "NotoSansJP-Bold.ttf"),
        "zh": (fonts / "NotoSansSC-Regular.ttf", fonts / "NotoSansSC-Bold.ttf"),
        "ko": (fonts / "NotoSansKR-Regular.ttf", fonts / "NotoSansKR-Bold.ttf"),
        "hi": (
            fonts / "NotoSansDevanagari-Regular.ttf",
            fonts / "NotoSansDevanagari-Bold.ttf",
        ),
    }
    missing = [str(path) for pair in paths.values() for path in pair if not path.is_file()]
    serif = fonts / "DejaVuSerif.ttf"
    if not serif.is_file():
        missing.append(str(serif))
    if missing:
        raise RuntimeError(
            "The PDF guide fonts bundled in assets/fonts are incomplete: "
            + ", ".join(missing)
        )
    return paths


def register_fonts() -> dict[str, tuple[str, str]]:
    registered: dict[str, tuple[str, str]] = {}
    for group, (regular_path, bold_path) in _font_paths().items():
        regular_name = f"Guide-{group}-Regular"
        bold_name = f"Guide-{group}-Bold"
        pdfmetrics.registerFont(TTFont(regular_name, regular_path, shapable=True))
        pdfmetrics.registerFont(TTFont(bold_name, bold_path, shapable=True))
        pdfmetrics.registerFontFamily(
            regular_name,
            normal=regular_name,
            bold=bold_name,
            italic=regular_name,
            boldItalic=bold_name,
        )
        registered[group] = (regular_name, bold_name)
    pdfmetrics.registerFont(
        TTFont(
            MATH_FONT,
            PROJECT_ROOT / "assets" / "fonts" / "DejaVuSerif.ttf",
            shapable=True,
        )
    )
    return registered


def font_group(language: str) -> str:
    return language if language in {"ja", "zh", "ko", "hi"} else "latin"


def sanitize(value: str) -> str:
    table = {
        ord("\u00a0"): " ",
        ord("\u2010"): "-",
        ord("\u2011"): "-",
        ord("\u2012"): "-",
        ord("\u2013"): "-",
        ord("\u2014"): "-",
        ord("\u2212"): "-",
        ord("\u2192"): "->",
    }
    return str(value).translate(table)


def rich(value: str) -> str:
    lines = sanitize(value).splitlines()
    rendered: list[str] = []
    for line in lines:
        indented = line.startswith("\t")
        content = line[1:].lstrip() if indented else line
        bold_line = content.startswith("**") and content.endswith("**")
        if bold_line:
            content = content[2:-2]
        escaped = html.escape(content) if content else "<br/>"
        if bold_line:
            escaped = f"<b>{escaped}</b>"
        if indented:
            escaped = "&nbsp;" * 4 + escaped
        rendered.append(escaped)
    return "<br/>".join(rendered)


def excerpt(value: str, max_characters: int) -> str:
    """Return complete translated sentences that fit a compact guide card."""
    cleaned = sanitize(value).strip()
    if len(cleaned) <= max_characters:
        return cleaned
    segments = [
        segment.strip()
        for segment in re.split(r"(?<=[.!?。！？])\s+|\n+", cleaned)
        if segment.strip()
    ]
    kept: list[str] = []
    for segment in segments:
        candidate = " ".join((*kept, segment))
        if len(candidate) > max_characters:
            break
        kept.append(segment)
    if kept:
        return " ".join(kept)
    if " " in cleaned[: max_characters + 1]:
        shortened = cleaned[: max_characters + 1].rsplit(" ", 1)[0]
    else:
        shortened = cleaned[:max_characters]
    return shortened.rstrip(" ,;:-") + "…"


def doc_text(language: str, key: str, max_characters: int) -> str:
    # CJK glyphs and Devanagari clusters occupy substantially more horizontal
    # space than Latin characters. Character budgets are therefore adjusted
    # before layout, preserving complete sentences without shrinking a whole
    # guide to an unreadable font.
    ratio = {
        "ja": 0.50,
        "zh": 0.54,
        "ko": 0.54,
        "hi": 0.74,
    }.get(language, 1.0)
    return excerpt(
        translate(language, key),
        max(70, int(max_characters * ratio)),
    )


def guide_distribution_features(language: str) -> str:
    """Return the macOS distribution bullets without duplicating GPL text."""
    feature_lines = [
        line.strip()
        for line in translate(language, "guide_license_feature").splitlines()
        if line.strip()
    ]
    return "\n".join(feature_lines[1:])


def combined_doc_text(
    language: str,
    keys: tuple[str, ...],
    max_characters: int,
    *,
    separator: str = "\n\n",
) -> str:
    """Join related help entries before making one coherent PDF excerpt."""
    ratio = {
        "ja": 0.50,
        "zh": 0.54,
        "ko": 0.54,
        "hi": 0.74,
    }.get(language, 1.0)
    return excerpt(
        separator.join(translate(language, key) for key in keys),
        max(70, int(max_characters * ratio)),
    )


def guide_paragraphs(language: str, key: str, count: int = 1) -> str:
    """Return complete leading tooltip paragraphs without truncating a sentence."""
    paragraphs = translate(language, key).strip().split("\n\n")
    return "\n".join(paragraphs[:count])


def guide_leading_lines(language: str, key: str, count: int) -> str:
    """Return the first non-empty tooltip lines, preserving complete bullets."""
    lines = [line.strip() for line in translate(language, key).splitlines() if line.strip()]
    return "\n".join(lines[:count])


def style(
    name: str,
    font: str,
    size: float,
    leading: float | None = None,
    color=INK,
    alignment=TA_LEFT,
    split_long_words: bool = True,
) -> ParagraphStyle:
    return ParagraphStyle(
        name,
        fontName=font,
        fontSize=size,
        leading=leading or size * 1.28,
        textColor=color,
        alignment=alignment,
        shaping=1,
        splitLongWords=split_long_words,
        spaceAfter=0,
        spaceBefore=0,
    )


def fit_paragraph(
    text: str,
    font: str,
    width: float,
    height: float,
    *,
    max_size: float = 8.2,
    min_size: float = 5.6,
    alignment=TA_LEFT,
    color=INK,
    raw_html: bool = False,
    leading_factor: float = 1.28,
    split_long_words: bool = True,
) -> tuple[Paragraph, float, float]:
    prepared = sanitize(text) if raw_html else rich(text)
    size = max_size
    while size >= min_size - 1e-6:
        paragraph = Paragraph(
            prepared,
            style(
                "fit",
                font,
                size,
                leading=size * max(1.0, float(leading_factor)),
                color=color,
                alignment=alignment,
                split_long_words=split_long_words,
            ),
        )
        used_width, used_height = paragraph.wrap(width, height)
        if used_height <= height + 0.01:
            return paragraph, used_width, used_height
        size -= 0.25
    raise ValueError(f"Paragraph does not fit: {sanitize(text)[:120]}")


def draw_paragraph(
    c: canvas.Canvas,
    text: str,
    x: float,
    top: float,
    width: float,
    height: float,
    font: str,
    **kwargs,
) -> float:
    paragraph, used_width, used_height = fit_paragraph(
        text, font, width, height, **kwargs
    )
    paragraph.drawOn(c, x, top - used_height)
    return used_height


def draw_card(
    c: canvas.Canvas,
    x: float,
    y: float,
    width: float,
    height: float,
    title: str,
    body: str,
    regular: str,
    bold: str,
    *,
    accent=BLUE,
    body_max: float = DOCUMENT_BODY_SIZE,
    body_min: float = DOCUMENT_BODY_SIZE,
    body_leading_factor: float = 1.28,
    body_split_long_words: bool = True,
) -> None:
    c.setFillColor(PANEL)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.8)
    c.roundRect(x, y, width, height, 6, fill=1, stroke=1)
    c.setStrokeColor(accent)
    c.setLineWidth(3)
    c.setLineCap(1)
    c.line(x + 10, y + 13, x + 10, y + height - 13)
    title_height = draw_paragraph(
        c,
        title,
        x + 23,
        y + height - 10,
        width - 33,
        24,
        bold,
        max_size=9.2,
        min_size=6.4,
    )
    body_top = y + height - 15 - title_height
    draw_paragraph(
        c,
        body,
        x + 23,
        body_top,
        width - 33,
        max(10, body_top - y - 10),
        regular,
        max_size=body_max,
        min_size=body_min,
        color=INK,
        leading_factor=body_leading_factor,
        split_long_words=body_split_long_words,
    )


def draw_page_header(
    c: canvas.Canvas,
    title: str,
    subtitle: str,
    regular: str,
    bold: str,
    *,
    show_app_icon: bool = False,
) -> float:
    c.setFillColor(BLUE)
    c.rect(0, PAGE_HEIGHT - 18, PAGE_WIDTH, 18, fill=1, stroke=0)
    if show_app_icon:
        if not APP_ICON_PATH.is_file():
            raise FileNotFoundError(APP_ICON_PATH)
        icon_size = 42
        icon_y = PAGE_HEIGHT - 98
        c.drawImage(
            str(APP_ICON_PATH),
            52,
            icon_y,
            icon_size,
            icon_size,
            preserveAspectRatio=True,
            mask="auto",
        )
        text_x = 52 + icon_size + 13
        title_top = PAGE_HEIGHT - 52
        title_height = draw_paragraph(
            c,
            title,
            text_x,
            title_top,
            PAGE_WIDTH - text_x - 52,
            30,
            bold,
            max_size=17.5,
            min_size=12.0,
        )
        if subtitle:
            subtitle_top = title_top - title_height - 3
            draw_paragraph(
                c,
                subtitle,
                text_x,
                subtitle_top,
                PAGE_WIDTH - text_x - 52,
                22,
                regular,
                max_size=8.4,
                min_size=6.3,
                color=MUTED,
            )
        return PAGE_HEIGHT - 132

    title_top = PAGE_HEIGHT - 58
    title_height = draw_paragraph(
        c,
        title,
        52,
        title_top,
        PAGE_WIDTH - 104,
        40,
        bold,
        max_size=17.5,
        min_size=12.0,
    )
    if subtitle:
        subtitle_top = title_top - title_height - 6
        subtitle_height = draw_paragraph(
            c,
            subtitle,
            52,
            subtitle_top,
            PAGE_WIDTH - 104,
            30,
            regular,
            max_size=8.4,
            min_size=6.3,
            color=MUTED,
        )
        return subtitle_top - subtitle_height - 12
    return title_top - title_height - 20


def draw_footer(
    c: canvas.Canvas,
    language_name: str,
    page_number: int,
    regular: str,
) -> None:
    footer = (
        f"LUFScale {APP_VERSION} - {language_name} - {APP_AUTHOR} - {APP_RELEASE_YEAR}"
    )
    c.setFillColor(MUTED)
    c.setFont(regular, 6.2)
    c.drawString(52, 30, sanitize(footer))
    c.drawCentredString(PAGE_WIDTH / 2, 30, str(page_number))
    c.drawRightString(PAGE_WIDTH - 52, 30, APP_WEBSITE_URL)


def draw_two_column_cards(
    c: canvas.Canvas,
    cards: Iterable[tuple[str, str]],
    top: float,
    bottom: float,
    regular: str,
    bold: str,
    *,
    rows: int,
    body_max: float = DOCUMENT_BODY_SIZE,
    body_min: float = DOCUMENT_BODY_SIZE,
    body_leading_factor: float = 1.28,
) -> None:
    cards = list(cards)
    gap_x = 12
    gap_y = 10
    x0 = 52
    total_width = PAGE_WIDTH - 104
    card_width = (total_width - gap_x) / 2
    card_height = (top - bottom - gap_y * (rows - 1)) / rows
    for index, (title, body) in enumerate(cards):
        row = index // 2
        column = index % 2
        x = x0 + column * (card_width + gap_x)
        y = top - (row + 1) * card_height - row * gap_y
        draw_card(
            c,
            x,
            y,
            card_width,
            card_height,
            title,
            body,
            regular,
            bold,
            body_max=body_max,
            body_min=body_min,
            body_leading_factor=body_leading_factor,
        )


def draw_card_rows(
    c: canvas.Canvas,
    rows: Iterable[Iterable[tuple[str, str]]],
    top: float,
    bottom: float,
    regular: str,
    bold: str,
    *,
    row_weights: Iterable[float] | None = None,
    body_max: float = DOCUMENT_BODY_SIZE,
    body_min: float = DOCUMENT_BODY_SIZE,
    body_leading_factor: float = 1.28,
) -> None:
    """Draw rows containing either two half-width cards or one wide card."""
    rows = [list(row) for row in rows]
    gap_x = 12
    gap_y = 10
    x0 = 52
    total_width = PAGE_WIDTH - 104
    weights = list(row_weights) if row_weights is not None else [1.0] * len(rows)
    if len(weights) != len(rows) or any(weight <= 0 for weight in weights):
        raise ValueError("Card-row weights must be positive and match the rows")
    available_height = top - bottom - gap_y * (len(rows) - 1)
    unit_height = available_height / sum(weights)
    current_top = top
    for row_index, row_cards in enumerate(rows):
        if len(row_cards) not in {1, 2}:
            raise ValueError("Each card row must contain one or two cards")
        card_height = unit_height * weights[row_index]
        y = current_top - card_height
        card_width = total_width if len(row_cards) == 1 else (total_width - gap_x) / 2
        for column, (title, body) in enumerate(row_cards):
            x = x0 + column * (card_width + gap_x)
            draw_card(
                c,
                x,
                y,
                card_width,
                card_height,
                title,
                body,
                regular,
                bold,
                body_max=body_max,
                body_min=body_min,
                body_leading_factor=body_leading_factor,
            )
        current_top = y - gap_y


def draw_simple_interface(
    c: canvas.Canvas,
    x: float,
    y: float,
    width: float,
    height: float,
    regular: str,
    bold: str,
    language: str,
) -> None:
    """Draw the validated 1.23.2-style overview of the complete main window."""
    dark = colors.HexColor("#15202b")
    panel = colors.HexColor("#202d3a")
    field = colors.HexColor("#0d151d")
    border = colors.HexColor("#52677a")
    cyan = colors.HexColor("#39c3ee")
    purple = colors.HexColor("#c596ff")
    green = colors.HexColor("#58d99a")

    c.setFillColor(dark)
    c.setStrokeColor(colors.HexColor("#25384a"))
    c.setLineWidth(1.0)
    c.roundRect(x, y, width, height, 9, fill=1, stroke=1)

    # Header: identity, version, Help and language controls.
    c.setFillColor(colors.white)
    c.setFont(bold, 9.5)
    c.drawString(x + 12, y + height - 20, "LUFScale")
    c.setFillColor(colors.HexColor("#afbdd0"))
    author_size = 5.1
    title_width = pdfmetrics.stringWidth("LUFScale", bold, 9.5)
    author_width = pdfmetrics.stringWidth(APP_AUTHOR, regular, author_size)
    c.saveState()
    author_text = c.beginText(x + 12, y + height - 29)
    author_text.setFont(regular, author_size)
    author_text.setCharSpace(
        max(0.0, (title_width - author_width) / max(1, len(APP_AUTHOR) - 1))
    )
    author_text.textLine(sanitize(APP_AUTHOR))
    c.drawText(author_text)
    c.restoreState()
    c.setFillColor(panel)
    c.setStrokeColor(border)
    c.roundRect(x + width - 72, y + height - 30, 60, 17, 4, fill=1, stroke=1)
    c.setFillColor(colors.white)
    c.setFont(bold, 5.5)
    c.drawCentredString(x + width - 42, y + height - 24, sanitize(APP_VERSION))

    # Source drop area and destination field.
    drop_y = y + height - 92
    c.setFillColor(panel)
    c.setStrokeColor(cyan)
    c.setDash(3, 2)
    c.roundRect(x + 10, drop_y, width - 20, 45, 6, fill=1, stroke=1)
    c.setDash()
    draw_paragraph(
        c,
        translate(language, "drop_title"),
        x + 20,
        drop_y + 30,
        width - 40,
        19,
        bold,
        max_size=5.8,
        min_size=4.2,
        alignment=TA_CENTER,
        color=colors.white,
    )
    destination_y = drop_y - 29
    c.setFillColor(field)
    c.setStrokeColor(border)
    c.roundRect(x + 10, destination_y, width - 20, 20, 4, fill=1, stroke=1)
    c.setFillColor(colors.HexColor("#aebccc"))
    c.setFont(regular, 4.8)
    c.drawString(
        x + 16, destination_y + 7, sanitize(translate(language, "destination"))
    )

    # Settings panel with the Audio rows and Options/status lights.
    settings_y = destination_y - 116
    c.setFillColor(panel)
    c.setStrokeColor(border)
    c.roundRect(x + 10, settings_y, width - 20, 108, 5, fill=1, stroke=1)
    c.setFillColor(colors.white)
    c.setFont(bold, 5.4)
    c.drawString(x + 16, settings_y + 96, sanitize(translate(language, "settings")))
    labels = (
        translate(language, "preset"),
        translate(language, "operation"),
        translate(language, "volume"),
        translate(language, "target"),
        translate(language, "peak"),
    )
    for index, label in enumerate(labels):
        row_y = settings_y + 76 - index * 14
        c.setFillColor(colors.HexColor("#b9c7d5"))
        c.setFont(regular, 4.4)
        c.drawRightString(x + 73, row_y + 4, sanitize(label)[:24])
        c.setFillColor(field)
        c.setStrokeColor(colors.HexColor("#43586a"))
        c.roundRect(x + 78, row_y, width - 96, 11, 2, fill=1, stroke=1)
    for index in range(5):
        c.setFillColor(green if index in {1, 2, 3} else colors.HexColor("#637282"))
        c.circle(x + width - 18 - index * 11, settings_y + 96, 2.3, fill=1, stroke=0)

    # Progress/CPU row and the two lower information areas.
    progress_y = settings_y - 24
    c.setFillColor(field)
    c.setStrokeColor(border)
    c.roundRect(x + 10, progress_y, width - 100, 14, 3, fill=1, stroke=1)
    c.setFillColor(cyan)
    c.roundRect(x + 11, progress_y + 1, (width - 102) * 0.58, 12, 2, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont(bold, 4.8)
    c.drawRightString(x + width - 78, progress_y + 5, "CPU 48 %")
    c.setFillColor(BLUE)
    c.roundRect(x + width - 72, progress_y - 1, 44, 16, 3, fill=1, stroke=0)
    draw_paragraph(
        c,
        translate(language, "start"),
        x + width - 70,
        progress_y + 11,
        40,
        11,
        bold,
        max_size=4.4,
        min_size=2.8,
        alignment=TA_CENTER,
        color=colors.white,
    )

    lower_y = y + 12
    lower_h = max(30, progress_y - lower_y - 8)
    c.setFillColor(field)
    c.setStrokeColor(border)
    c.roundRect(x + 10, lower_y, width * 0.58, lower_h, 4, fill=1, stroke=1)
    c.setFillColor(colors.HexColor("#52dca4"))
    c.setFont(regular, 3.8)
    for row in range(5):
        c.drawString(
            x + 15,
            lower_y + lower_h - 10 - row * 7,
            sanitize(f"audio_{row + 1}.mp3  -14.{row} LUFS"),
        )
    graph_x = x + 18 + width * 0.58
    graph_w = width - (graph_x - x) - 10
    c.setFillColor(panel)
    c.setStrokeColor(border)
    c.roundRect(graph_x, lower_y, graph_w, lower_h, 4, fill=1, stroke=1)
    c.setStrokeColor(purple)
    c.setLineWidth(1.2)
    points = [0.45, 0.67, 0.38, 0.73, 0.50, 0.62]
    for index in range(len(points) - 1):
        x1 = graph_x + 7 + index * (graph_w - 14) / 5
        x2 = graph_x + 7 + (index + 1) * (graph_w - 14) / 5
        c.line(
            x1,
            lower_y + lower_h * points[index],
            x2,
            lower_y + lower_h * points[index + 1],
        )
    c.setStrokeColor(green)
    c.line(
        graph_x + 7,
        lower_y + lower_h * 0.25,
        graph_x + graph_w - 7,
        lower_y + lower_h * 0.25,
    )

    # The four numbered callouts reproduce the reference guide's visual map.
    markers = (
        (x + width - 16, drop_y + 33),
        (x + width - 16, destination_y + 10),
        (x + width - 16, settings_y + 54),
        (x + width - 16, progress_y + 7),
    )
    for number, (mx, my) in enumerate(markers, start=1):
        c.setFillColor(BLUE)
        c.circle(mx, my, 6.3, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont(bold, 5.4)
        c.drawCentredString(mx, my - 1.9, str(number))


def page_quick_start(c, language, language_name, labels, regular, bold) -> None:
    identity_labels = MACOS_GUIDE_IDENTITY_LABELS
    top = draw_page_header(
        c,
        labels["guide"],
        identity_labels.get(
            language,
            identity_labels["en"],
        ).format(version=APP_VERSION),
        regular,
        bold,
        show_app_icon=True,
    )
    c.setFillColor(INK)
    c.setFont(bold, 11)
    c.drawString(52, top + 2, sanitize(labels["quick"]))
    draw_card(
        c,
        52,
        615,
        PAGE_WIDTH - 104,
        80,
        translate(language, "guide_quality_priority_title"),
        translate(language, "guide_quality_priority_body"),
        regular,
        bold,
        accent=GREEN,
        body_max=DOCUMENT_BODY_SIZE,
    )
    draw_card(
        c,
        52,
        540,
        PAGE_WIDTH - 104,
        65,
        translate(language, "guide_license_title"),
        translate(language, "guide_license_body"),
        regular,
        bold,
        body_max=DOCUMENT_BODY_SIZE,
        body_min=DOCUMENT_BODY_SIZE,
        body_leading_factor=1.15,
    )
    draw_simple_interface(c, 52, 211, 245, 320, regular, bold, language)
    reference_steps = {
        "fr": (
            "Déposez un ou plusieurs dossiers ou fichiers audio. Tous les sous-dossiers sont analysés.",
            "Sélectionnez le dossier qui recevra les copies traitées avec la même arborescence.",
            "Choisissez un préréglage et l’opération souhaitée. Chaque fichier est traité séparément.",
            "Cliquez sur Uniformiser. La progression, le temps et l’utilisation CPU s’affichent en direct.",
        ),
        "en": (
            "Drop one or more folders or audio files. Every subfolder is scanned.",
            "Select the folder that will receive processed copies with the same tree.",
            "Choose a preset and the required operation. Every file is processed separately.",
            "Click Normalize. Progress, elapsed time and CPU use are displayed live.",
        ),
    }
    if language in reference_steps:
        bodies = reference_steps[language]
    else:
        bodies = (
            doc_text(language, "source_selection_tooltip", 120),
            doc_text(language, "destination_path_tooltip", 120),
            doc_text(language, "preset_tooltip", 120),
            excerpt(
                f"{translate(language, 'operation_convert_label')}. "
                f"{translate(language, 'cpu_tooltip')}",
                120,
            ),
        )
    steps = list(
        zip(
            (
                translate(language, "add_source_files"),
                translate(language, "destination"),
                translate(language, "settings"),
                translate(language, "start"),
            ),
            bodies,
        )
    )
    interface_y = 211
    interface_height = 320
    step_height = 66
    step_gap = (interface_height - 4 * step_height) / 3
    step_top = interface_y + interface_height
    for number, (title, body) in enumerate(steps, start=1):
        card_top = step_top - (number - 1) * (step_height + step_gap)
        card_y = card_top - step_height
        marker_y = card_y + step_height / 2
        c.setFillColor(BLUE)
        c.circle(322, marker_y, 12, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont(bold, 8)
        c.drawCentredString(322, marker_y - 3, str(number))
        draw_card(
            c,
            344,
            card_y,
            199,
            step_height,
            title,
            body,
            regular,
            bold,
            body_max=DOCUMENT_BODY_SIZE,
        )
    draw_card(
        c,
        52,
        50,
        PAGE_WIDTH - 104,
        150,
        translate(language, "help_title"),
        translate(language, "help_overview")
        + "\n"
        + guide_distribution_features(language),
        regular,
        bold,
        body_max=DOCUMENT_BODY_SIZE,
    )
    draw_footer(c, language_name, 1, regular)
    c.showPage()


def page_audio(c, language, language_name, labels, regular, bold) -> None:
    title = (
        f"{translate(language, 'settings')} - "
        f"{translate(language, 'audio_tab')} / "
        f"{translate(language, 'options_tab')}"
    )
    top = draw_page_header(
        c,
        title,
        translate(language, "help_title"),
        regular,
        bold,
    )
    # Audio and Options are intentionally presented together.  Each option has
    # its own card so its explanation cannot be confused with another setting.
    card_rows = [
        [
            (translate(language, "preset"), doc_text(language, "preset_tooltip", 220)),
            (translate(language, "guide_file_processing_title"), doc_text(language, "guide_file_processing_body", 350)),
        ],
        [
            ("ITU-R BS.1770", doc_text(language, "guide_analysis_method", 220)),
            (translate(language, "operation"), doc_text(language, "operation_tooltip", 250)),
        ],
        [
            (translate(language, "volume"), doc_text(language, "volume_tooltip", 210)),
            (translate(language, "target"), doc_text(language, "target_tooltip", 220)),
        ],
        [
            (translate(language, "peak"), guide_paragraphs(language, "peak_tooltip")),
            (translate(language, "quality"), guide_paragraphs(language, "quality_tooltip")),
        ],
        [(translate(language, "parallel"), guide_leading_lines(language, "parallel_tooltip", 2))],
        [
            (translate(language, "overwrite"), doc_text(language, "overwrite_tooltip", 220)),
            (translate(language, "resume"), doc_text(language, "resume_tooltip", 220)),
        ],
        [
            (translate(language, "quality_control"), doc_text(language, "quality_control_tooltip", 220)),
            (translate(language, "create_report"), doc_text(language, "report_tooltip", 260)),
        ],
        [
            (translate(language, "auto_start"), doc_text(language, "auto_start_tooltip", 260)),
            (translate(language, "skip_compliant"), doc_text(language, "skip_compliant_tooltip", 250)),
        ],
    ]
    draw_card_rows(
        c,
        card_rows,
        top - 8,
        58,
        regular,
        bold,
        row_weights=(1, 1, 1, 1, 1.2, 1, 1, 1),
        body_max=DOCUMENT_BODY_SIZE,
        body_min=DOCUMENT_BODY_SIZE,
        body_leading_factor=1.05,
    )
    draw_footer(c, language_name, 2, regular)
    c.showPage()


def page_options(c, language, language_name, labels, regular, bold) -> None:
    top = draw_page_header(
        c, labels["options"], translate(language, "source_safety"), regular, bold
    )
    cards = [
        (
            translate(language, "overwrite"),
            doc_text(language, "overwrite_tooltip", 430),
        ),
        (
            translate(language, "skip_compliant"),
            doc_text(language, "skip_compliant_tooltip", 430),
        ),
        (translate(language, "resume"), doc_text(language, "resume_tooltip", 430)),
        (
            translate(language, "quality_control"),
            doc_text(language, "quality_control_tooltip", 430),
        ),
        (
            translate(language, "create_report"),
            doc_text(language, "report_tooltip", 430),
        ),
        (
            translate(language, "auto_start"),
            doc_text(language, "auto_start_tooltip", 430),
        ),
    ]
    draw_two_column_cards(c, cards, top - 8, 58, regular, bold, rows=3, body_max=DOCUMENT_BODY_SIZE)
    draw_footer(c, language_name, 3, regular)
    c.showPage()


def draw_workflow(c, top: float, language: str, regular: str, bold: str) -> None:
    labels = [
        translate(language, "add_source_files"),
        translate(language, "analyze"),
        translate(language, "guide_file_processing_title"),
        translate(language, "quality_control"),
    ]
    x0 = 52
    gap = 13
    width = (PAGE_WIDTH - 104 - 3 * gap) / 4
    for index, label in enumerate(labels):
        x = x0 + index * (width + gap)
        accent = GREEN if index == 3 else BLUE
        c.setFillColor(SOFT_BLUE if index < 3 else colors.HexColor("#eefaf5"))
        c.setStrokeColor(accent)
        c.roundRect(x, top - 68, width, 58, 6, fill=1, stroke=1)
        c.setFillColor(accent)
        c.circle(x + 18, top - 28, 9, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont(bold, 6.8)
        c.drawCentredString(x + 18, top - 30.5, str(index + 1))
        draw_paragraph(
            c, label, x + 33, top - 18, width - 40, 38, bold, max_size=7.4, min_size=5.3
        )
        if index < 3:
            c.setStrokeColor(MUTED)
            c.line(x + width + 3, top - 39, x + width + gap - 3, top - 39)


def draw_log_legend(
    c: canvas.Canvas,
    language: str,
    x: float,
    y: float,
    width: float,
    height: float,
    regular: str,
    bold: str,
) -> None:
    labels = (
        translate(language, "status_ok"),
        translate(language, "already_compliant_badge"),
        translate(language, "status_warning"),
        translate(language, "status_cancelled"),
        translate(language, "status_error"),
    )
    bodies = tuple(
        translate(language, key)
        for key in (
            "guide_log_legend_success",
            "guide_log_legend_compliant",
            "guide_log_legend_warning",
            "guide_log_legend_cancelled",
            "guide_log_legend_error",
        )
    )
    swatches = (
        GREEN,
        colors.HexColor("#2d9d79"),
        colors.HexColor("#d98a22"),
        MUTED,
        colors.HexColor("#c85e69"),
    )
    c.setFillColor(PANEL)
    c.setStrokeColor(LINE)
    c.roundRect(x, y, width, height, 6, fill=1, stroke=1)
    header_height = 21
    draw_paragraph(
        c,
        LOG_LEGEND_TITLES.get(language, LOG_LEGEND_TITLES["en"]),
        x + 12,
        y + height - 6,
        width - 24,
        15,
        bold,
        max_size=8.0,
        min_size=5.4,
    )
    c.setStrokeColor(LINE)
    c.setLineWidth(0.55)
    c.line(
        x + 10,
        y + height - header_height,
        x + width - 10,
        y + height - header_height,
    )
    content_height = height - header_height
    row_height = content_height / 5
    for index, (label, body, swatch) in enumerate(zip(labels, bodies, swatches)):
        row_y = y + content_height - (index + 1) * row_height
        if index:
            c.setStrokeColor(LINE)
            c.setLineWidth(0.45)
            c.line(x + 10, row_y + row_height, x + width - 10, row_y + row_height)
        # A fixed, deliberately generous badge width lets every language use
        # exactly the same type size, including long Russian status labels.
        badge_width = 96
        c.setFillColor(swatch)
        c.roundRect(
            x + 12,
            row_y + 5,
            badge_width,
            row_height - 10,
            3,
            fill=1,
            stroke=0,
        )
        draw_paragraph(
            c,
            label,
            x + 16,
            row_y + row_height - 6,
            badge_width - 8,
            row_height - 9,
            bold,
            max_size=5.4,
            min_size=5.4,
            color=colors.white,
            alignment=TA_CENTER,
        )
        draw_paragraph(
            c,
            body,
            x + 119,
            row_y + row_height - 5,
            width - 133,
            row_height - 8,
            regular,
            max_size=DOCUMENT_BODY_SIZE,
            min_size=DOCUMENT_BODY_SIZE,
            color=INK,
        )


def page_processing(c, language, language_name, labels, regular, bold) -> None:
    top = draw_page_header(
        c,
        labels["processing"],
        translate(language, "guide_analysis_method"),
        regular,
        bold,
    )
    draw_workflow(c, top, language, regular, bold)
    cards = [
        (
            translate(language, "parallel"),
            combined_doc_text(language, ("parallel_tooltip", "cpu_tooltip"), 230),
        ),
        (
            translate(language, "analyze"),
            doc_text(language, "analyze_only_fresh_help_text", 180),
        ),
        (translate(language, "resume"), doc_text(language, "resume_tooltip", 230)),
        (
            translate(language, "quality_control"),
            doc_text(language, "quality_control_tooltip", 230),
        ),
        (
            translate(language, "loudness_comparison_title"),
            doc_text(language, "loudness_comparison_help_text", 245),
        ),
        (
            translate(language, "operation_analyze_label"),
            doc_text(language, "analysis_progress_help_text", 195),
        ),
        (
            translate(language, "log_title"),
            combined_doc_text(
                language, ("log_help_text", "replaygain_log_help_text"), 235
            ),
        ),
        (
            translate(language, "estimated_total_calculating"),
            translate(language, "guide_estimated_total_help"),
        ),
    ]
    draw_two_column_cards(
        c,
        cards,
        650,
        190,
        regular,
        bold,
        rows=4,
        body_max=DOCUMENT_BODY_SIZE,
    )
    draw_log_legend(c, language, 52, 58, PAGE_WIDTH - 104, 120, regular, bold)
    draw_footer(c, language_name, 3, regular)
    c.showPage()


def draw_preset_table(
    c, language: str, x: float, y: float, width: float, regular: str, bold: str
) -> None:
    headers = [
        translate(language, "preset"),
        translate(language, "target"),
        translate(language, "peak"),
        translate(language, "quality"),
    ]
    rows = [
        (translate(language, "preset_library"), *PRESETS["library"]),
        (translate(language, "preset_streaming"), *PRESETS["streaming"]),
        (translate(language, "preset_dynamic"), *PRESETS["dynamic"]),
    ]
    widths = [width * 0.42, width * 0.20, width * 0.23, width * 0.15]
    row_height = 28
    c.setFillColor(INK)
    c.rect(x, y + 3 * row_height, width, row_height, fill=1, stroke=0)
    current_x = x
    for header, column_width in zip(headers, widths):
        draw_paragraph(
            c,
            header,
            current_x + 6,
            y + 4 * row_height - 7,
            column_width - 12,
            18,
            bold,
            max_size=7.2,
            min_size=5.4,
            color=colors.white,
        )
        current_x += column_width
    for row_index, row in enumerate(rows):
        row_y = y + (2 - row_index) * row_height
        c.setFillColor(colors.white if row_index % 2 == 0 else SOFT_BLUE)
        c.setStrokeColor(LINE)
        c.rect(x, row_y, width, row_height, fill=1, stroke=1)
        values = [row[0], f"{row[1]:g} LUFS", f"{row[2]:g} dBTP", f"{row[3]:g}"]
        current_x = x
        for value, column_width in zip(values, widths):
            draw_paragraph(
                c,
                str(value),
                current_x + 6,
                row_y + row_height - 7,
                column_width - 12,
                18,
                regular,
                max_size=7.2,
                min_size=5.3,
            )
            current_x += column_width


def page_recommended(c, language, language_name, labels, regular, bold) -> None:
    top = draw_page_header(c, labels["recommended"], "", regular, bold)
    draw_preset_table(c, language, 52, top - 122, PAGE_WIDTH - 104, regular, bold)
    draw_paragraph(
        c,
        labels["preset_note"],
        52,
        top - 132,
        PAGE_WIDTH - 104,
        32,
        regular,
        max_size=7.8,
        min_size=6.2,
        color=MUTED,
    )
    checks = USEFUL_CHECKS_COPY[language]
    draw_paragraph(
        c,
        checks["heading"],
        52,
        578,
        PAGE_WIDTH - 104,
        28,
        bold,
        max_size=12.2,
        min_size=9.0,
        color=BLUE_DARK,
    )
    cards = checks["cards"]
    gap = 10
    card_width = (PAGE_WIDTH - 104 - 2 * gap) / 3
    for index, values in enumerate(cards):
        draw_card(
            c,
            52 + index * (card_width + gap),
            412,
            card_width,
            125,
            *values,
            regular,
            bold,
            body_max=DOCUMENT_BODY_SIZE,
        )
    reference_labels = REFERENCE_COPY[language]
    references = (
        f"{reference_labels['filters']}:\n"
        "https://ffmpeg.org/ffmpeg-filters.html\n\n"
        f"{reference_labels['codecs']}:\n"
        "https://ffmpeg.org/ffmpeg-codecs.html\n\n"
        f"{reference_labels['itu']}:\n"
        "https://www.itu.int/rec/R-REC-BS.1770-5-202311-I/en\n\n"
        f"{reference_labels['ebu']}:\n"
        "https://tech.ebu.ch/publications/r128\n\n"
        f"{reference_labels['replaygain']}:\n"
        "https://wiki.hydrogenaudio.org/index.php?title=Original_ReplayGain_specification"
    )
    draw_card(
        c,
        52,
        58,
        PAGE_WIDTH - 104,
        335,
        labels["refs"],
        references,
        regular,
        bold,
        accent=GREEN,
        body_max=DOCUMENT_BODY_SIZE,
    )
    draw_footer(c, language_name, 4, regular)
    c.showPage()


def technical_copy(language: str, key: str) -> str:
    return TECHNICAL_COPY[language][key]


def page_technical(c, language, language_name, labels, regular, bold) -> None:
    draw_page_header(
        c,
        labels["technical"],
        translate(language, "source_safety"),
        regular,
        bold,
    )
    draw_card(
        c,
        52,
        620,
        PAGE_WIDTH - 104,
        115,
        translate(language, "operation"),
        combined_doc_text(
            language,
            (
                "operation_help_text",
                "replaygain_qc_help_text",
            ),
            1450,
            separator="\n \n",
        )
        + "\n \n"
        + technical_copy(language, "qc_off"),
        regular,
        bold,
        accent=GREEN,
        body_max=DOCUMENT_BODY_SIZE,
    )
    cards = [
        ("ITU-R BS.1770", excerpt(technical_copy(language, "bs"), 120)),
        (
            technical_copy(language, "reference_heading"),
            doc_text(language, "guide_analysis_method", 130),
        ),
        (
            translate(language, "guide_file_processing_title"),
            doc_text(language, "guide_file_processing_body", 140),
        ),
        ("MP3", excerpt(technical_copy(language, "dynamic"), 105)),
        (
            translate(language, "quality"),
            excerpt(technical_copy(language, "formats"), 120),
        ),
        (
            translate(language, "skip_compliant"),
            excerpt(translate(language, "skip_compliant_tooltip"), 50),
        ),
        (
            translate(language, "quality_control"),
            excerpt(technical_copy(language, "retries"), 110),
        ),
        (
            translate(language, "parallel"),
            excerpt(technical_copy(language, "parallel"), 120),
        ),
    ]
    # Eight compact reference cards, followed by two clearly distinct full-
    # width cards. The macOS build card is deliberately taller so the command,
    # output label, and generated paths retain clear vertical separation.
    draw_two_column_cards(
        c, cards, 614, 266,
        regular,
        bold,
        rows=4,
        body_max=DOCUMENT_BODY_SIZE,
    )
    draw_card(
        c,
        52,
        38,
        PAGE_WIDTH - 104,
        222,
        PLATFORM_BUILD_COPY[language]["title"],
        PLATFORM_BUILD_COPY[language]["body"],
        regular,
        bold,
        body_max=DOCUMENT_BODY_SIZE,
        body_min=DOCUMENT_BODY_SIZE,
        body_leading_factor=1.0,
        body_split_long_words=False,
    )
    draw_footer(c, language_name, 5, regular)
    c.showPage()


def draw_formula_card(
    c, x, y, width, height, title, formula, body, regular, bold
) -> None:
    c.setFillColor(PANEL)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.8)
    c.roundRect(x, y, width, height, 6, fill=1, stroke=1)
    c.setStrokeColor(BLUE)
    c.setLineWidth(3)
    c.setLineCap(1)
    c.line(x + 10, y + 12, x + 10, y + height - 12)
    draw_paragraph(
        c,
        title,
        x + 23,
        y + height - 9,
        width - 34,
        21,
        bold,
        max_size=8.8,
        min_size=6.0,
    )
    formula_top = y + height - 32
    formula_height = 70
    formula_bottom = formula_top - formula_height
    c.setFillColor(FORMULA_PANEL)
    c.roundRect(
        x + 22,
        formula_bottom,
        width - 33,
        formula_height,
        4,
        fill=1,
        stroke=0,
    )
    draw_paragraph(
        c,
        formula,
        x + 27,
        formula_top - 6,
        width - 43,
        formula_height - 12,
        MATH_FONT,
        max_size=10.5,
        min_size=6.2,
        alignment=TA_CENTER,
        raw_html=True,
        # Mathematical subscripts and superscripts must remain visually tied
        # to their own row.  A generous leading prevents adjacent rows from
        # being read as one formula, especially in the three- and four-line
        # quality-control cards.
        leading_factor=1.95,
    )
    body_top = formula_bottom - 8
    draw_paragraph(
        c,
        body,
        x + 23,
        body_top,
        width - 34,
        max(10, body_top - y - 10),
        regular,
        max_size=DOCUMENT_BODY_SIZE,
        min_size=DOCUMENT_BODY_SIZE,
        color=MUTED,
    )


def page_formulas(c, language, language_name, labels, regular, bold) -> None:
    top = draw_page_header(
        c, labels["formulas"], "L = LUFS, TP = dBTP, G = dB", regular, bold
    )
    formulas = [
        (
            "ITU-R BS.1770",
            "z<sub>i</sub> = (1/T<sub>g</sub>) ∫ x<sub>i</sub><super>2</super>(t) dt<br/>L<sub>K</sub> = -0.691 + 10 log<sub>10</sub>(Σ G<sub>i</sub>z<sub>i</sub>)",
            labels["bs_body"],
        ),
        (
            f"ITU-R BS.1770 - {labels['gating']}",
            "T<sub>g</sub> = 400 ms; overlap = 75 %<br/>Γ<sub>a</sub> = -70 LKFS; Γ<sub>r</sub> = Γ<sub>loud</sub> - 10 LU",
            labels["gating_body"],
        ),
        (
            translate(language, "guide_file_processing_title"),
            "G<sub>file</sub> = L<sub>target</sub> - L<sub>input</sub>",
            doc_text(language, "guide_file_processing_body", 210),
        ),
        (
            translate(language, "guide_analyze_prediction_title"),
            "G<sub>est</sub> = L<sub>target</sub> - L<sub>input</sub><br/>TP<sub>est</sub> = min(TP<sub>input</sub> + G<sub>est</sub>, TP<sub>limit</sub>)",
            doc_text(language, "guide_analyze_prediction_body", 210),
        ),
        (
            translate(language, "skip_compliant"),
            f"|L<sub>in</sub> - T| ≤ {ALREADY_COMPLIANT_LUFS_TOLERANCE:.2f} LU<br/>TP<sub>in</sub> ≤ TP<sub>max</sub>",
            doc_text(language, "skip_compliant_tooltip", 210),
        ),
        (
            translate(language, "quality_control"),
            f"|L<sub>out</sub> - L<sub>expected</sub>| &gt; {QUALITY_CONTROL_LUFS_TOLERANCE:.2f} LU<br/>TP<sub>out</sub> &gt; TP<sub>limit</sub> + {QUALITY_CONTROL_TRUE_PEAK_TOLERANCE_DB:.2f} dB",
            doc_text(language, "quality_control_tooltip", 210),
        ),
        (
            translate(language, "loudness_comparison_title"),
            f"Δ = L - T<br/>R<sub>display</sub> = [-6, +6] LU ; τ<sub>QC</sub> = ±{QUALITY_CONTROL_LUFS_TOLERANCE:.2f} LU",
            doc_text(language, "loudness_comparison_tooltip", 210),
        ),
        (
            translate(language, "operation_replaygain"),
            "G<sub>tag</sub> = L<sub>target</sub> - L<sub>input</sub><br/>P<sub>peak</sub> = 10<super>TP/20</super>",
            combined_doc_text(
                language,
                ("replaygain_help_text", "replaygain_usefulness_text"),
                140,
            ),
        ),
    ]
    gap_x = 12
    gap_y = 10
    x0 = 52
    card_width = (PAGE_WIDTH - 104 - gap_x) / 2
    card_height = (top - 58 - 3 * gap_y) / 4
    for index, values in enumerate(formulas):
        row, column = divmod(index, 2)
        x = x0 + column * (card_width + gap_x)
        y = top - (row + 1) * card_height - row * gap_y
        draw_formula_card(c, x, y, card_width, card_height, *values, regular, bold)
    draw_footer(c, language_name, 6, regular)
    c.showPage()


def page_compliance(c, language, language_name, labels, regular, bold) -> None:
    title = f"{labels['technical']} - {translate(language, 'quality_control')}"
    compliance_copy = COMPLIANCE_COPY[language]
    subtitle = compliance_copy["subtitle"]
    headings = compliance_copy["headings"]
    descriptions = compliance_copy["descriptions"]
    top = draw_page_header(
        c,
        title,
        subtitle,
        regular,
        bold,
    )
    formulas = [
        (
            headings[0],
            f"G = L<sub>t</sub> - I<br/>TP<sub>pred</sub> = TP<sub>in</sub> + G<br/>m<sub>TP</sub> = TP<sub>req</sub> - TP<sub>pred</sub> ≥ {LOUDNORM_LINEAR_SAFETY_MARGIN_DB:.2f}<br/>m<sub>LRA</sub> = LRA<sub>t</sub> - LRA<sub>in</sub> ≥ {LOUDNORM_LINEAR_SAFETY_MARGIN_DB:.2f}",
            descriptions[0],
        ),
        (
            headings[1],
            f"TP<sub>safe</sub> = TP<sub>req</sub> - {MP3_DYNAMIC_TRUE_PEAK_MARGIN_DB:.2f} dB<br/>TP<sub>int,0</sub> = max({LOUDNORM_MIN_TRUE_PEAK_DBTP:g} dBTP, TP<sub>safe</sub>)",
            descriptions[1],
        ),
        (
            headings[2],
            f"|L<sub>out</sub> - L<sub>t</sub>| ≤ {STRICT_TARGET_LUFS_TOLERANCE:.2f} LU<br/>TP<sub>out</sub> ≤ TP<sub>req</sub>",
            descriptions[2],
        ),
        (
            headings[3],
            f"TP<sub>g</sub> = {MP3_DYNAMIC_RETRY_GUARD_DB:.2f} dB<br/>e<sub>TP</sub> = TP<sub>out</sub> - (TP<sub>req</sub> - TP<sub>g</sub>)<br/>TP<sub>int,n+1</sub> = TP<sub>int,n</sub> - e<sub>TP</sub>",
            descriptions[3],
        ),
        (
            headings[4],
            f"r = min[(L<sub>t</sub> - {STRICT_TARGET_LUFS_TOLERANCE - MP3_DYNAMIC_RETRY_GUARD_DB:.2f}) - L<sub>out</sub>,<br/>(TP<sub>req</sub> - {MP3_DYNAMIC_RETRY_GUARD_DB:.2f}) - TP<sub>out</sub>]<br/>TP<sub>int,n+1</sub> = TP<sub>int,n</sub> + r",
            descriptions[4],
        ),
        (
            headings[5],
            f"p = max(0, TP<sub>out</sub> - TP<sub>req</sub>)<br/>e<sub>L</sub> = max(0, |L<sub>out</sub> - L<sub>t</sub>| - {STRICT_TARGET_LUFS_TOLERANCE:.2f})<br/>d<sub>L</sub> = |L<sub>out</sub> - L<sub>t</sub>|<br/>score = (p&gt;0, e<sub>L</sub>&gt;0, p, e<sub>L</sub>, d<sub>L</sub>)",
            descriptions[5],
        ),
        (
            headings[6],
            f"N<sub>MP3</sub> ≤ {MP3_DYNAMIC_RETRY_MAX_ATTEMPTS}; N<sub>lossless</sub> ≤ {TARGET_CORRECTION_MAX_ATTEMPTS}",
            descriptions[6],
        ),
        (
            headings[7],
            f"ΔL = L<sub>out</sub> - L<sub>t</sub><br/>QC<sub>alert</sub> ⇔ |ΔL| &gt; {QUALITY_CONTROL_LUFS_TOLERANCE:.2f} ∨ TP<sub>out</sub> &gt; TP<sub>req</sub> + {QUALITY_CONTROL_TRUE_PEAK_TOLERANCE_DB:.2f}<br/>strict<sub>OK</sub> ⇔ |ΔL| ≤ {STRICT_TARGET_LUFS_TOLERANCE:.2f} ∧ TP<sub>out</sub> ≤ TP<sub>req</sub><br/>retry ⇔ ¬strict<sub>OK</sub> ∧ |TP<sub>int,n+1</sub> - TP<sub>int,n</sub>| ≥ {MP3_DYNAMIC_RETRY_MIN_STEP_DB:.2f}",
            descriptions[7],
        ),
    ]
    gap_x = 12
    gap_y = 10
    x0 = 52
    card_width = (PAGE_WIDTH - 104 - gap_x) / 2
    card_height = (top - 58 - 3 * gap_y) / 4
    for index, values in enumerate(formulas):
        row, column = divmod(index, 2)
        x = x0 + column * (card_width + gap_x)
        y = top - (row + 1) * card_height - row * gap_y
        draw_formula_card(c, x, y, card_width, card_height, *values, regular, bold)
    draw_footer(c, language_name, 7, regular)
    c.showPage()


def page_release(c, language, language_name, labels, regular, bold) -> None:
    top = draw_page_header(
        c, f"{labels['release']} - {APP_VERSION}", labels["tagline"], regular, bold
    )
    draw_card(
        c,
        52,
        475,
        PAGE_WIDTH - 104,
        top - 475,
        f"LUFScale {APP_VERSION}",
        translate(language, "version_changes"),
        regular,
        bold,
        accent=GREEN,
        body_max=DOCUMENT_BODY_SIZE,
    )
    draw_card(
        c,
        52,
        255,
        PAGE_WIDTH - 104,
        195,
        translate(language, "help_title"),
        translate(language, "help_overview"),
        regular,
        bold,
        body_max=DOCUMENT_BODY_SIZE,
    )
    references = (
        "ITU-R Recommendation BS.1770-5 (11/2023):\n"
        "https://www.itu.int/rec/R-REC-BS.1770-5-202311-I/en\n\n"
        "EBU R 128 v5.0 (11/2023):\n"
        "https://tech.ebu.ch/publications/r128\n\n"
        "FFmpeg filters - loudnorm and ebur128:\n"
        "https://ffmpeg.org/ffmpeg-filters.html\n\n"
        "FFmpeg codecs:\nhttps://ffmpeg.org/ffmpeg-codecs.html"
    )
    draw_card(
        c,
        52,
        62,
        PAGE_WIDTH - 104,
        170,
        labels["refs"],
        references,
        regular,
        bold,
        body_max=DOCUMENT_BODY_SIZE,
    )
    draw_footer(c, language_name, 8, regular)
    c.showPage()


def generate_guide(
    language: str,
    language_name: str,
    fonts: dict[str, tuple[str, str]],
    output_dir: Path | None = None,
) -> Path:
    labels = DOC_LABELS[language]
    regular, bold = fonts[font_group(language)]
    destination = output_dir or (PROJECT_ROOT / "output" / "pdf")
    output = destination / PDF_GUIDES[language]
    output.parent.mkdir(parents=True, exist_ok=True)
    document = canvas.Canvas(
        str(output),
        pagesize=A4,
        pageCompression=1,
        initialFontName=regular,
        initialFontSize=8,
        initialLeading=10,
        lang=language,
    )
    document.setTitle(f"LUFScale {APP_VERSION} - {language_name}")
    document.setSubject(f"LUFScale macOS visual guide - {language_name}")
    document.setAuthor(f"LUFScale - {APP_AUTHOR}")
    document.setCreator("LUFScale guide generator")
    document.setProducer("ReportLab")

    page_quick_start(document, language, language_name, labels, regular, bold)
    page_audio(document, language, language_name, labels, regular, bold)
    page_processing(document, language, language_name, labels, regular, bold)
    page_recommended(document, language, language_name, labels, regular, bold)
    page_technical(document, language, language_name, labels, regular, bold)
    page_formulas(document, language, language_name, labels, regular, bold)
    page_compliance(document, language, language_name, labels, regular, bold)
    document.save()
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PROJECT_ROOT / "output" / "pdf",
        help="Directory that receives the twelve PDF guides.",
    )
    arguments = parser.parse_args()
    fonts = register_fonts()
    generated = [
        generate_guide(
            language,
            language_name,
            fonts,
            output_dir=arguments.output_dir.resolve(),
        )
        for language, language_name in LANGUAGES
    ]
    for output in generated:
        print(output)


if __name__ == "__main__":
    main()
