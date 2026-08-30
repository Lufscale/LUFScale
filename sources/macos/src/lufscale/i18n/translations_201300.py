"""Layout and documentation refinements for LUFScale 2.0.13."""

from .translations_201200 import TRANSLATION_UPDATES_201200


def _intel_body_with_compact_sections(language: str) -> str:
    """Keep translated copy while applying one shared typographic structure."""
    source = TRANSLATION_UPDATES_201200[language]["guide_intel_build_body"]
    lines = source.splitlines()
    first_step = next(
        index for index, line in enumerate(lines) if line.startswith("1. ")
    )
    intro = "\n".join(lines[:first_step]).strip()
    steps = [line for line in lines[first_step : first_step + 4] if line.strip()]
    following = [line for line in lines[first_step + 4 :] if line.strip()]
    for index, line in enumerate(steps):
        for command in (
            "xcode-select --install",
            "brew install pkg-config",
            "./Create_Community_Distribution_macOS.command",
        ):
            line = line.replace(command, f"“{command}”")
        steps[index] = line
    # One blank line separates the introduction from the numbered procedure.
    # The two explanatory paragraphs then use the same, smaller single break.
    return (
        intro
        + "\n\n"
        + "\n".join(steps)
        + "\n"
        + "\n".join(following)
    )


_VERSION_CHANGES = {
    "fr": "• L’en-tête du journal touche désormais son cadre et reprend l’espacement vertical des réglages.\n• La licence de la page 5 utilise une taille de texte fixe et plus lisible dans les douze guides.\n• La procédure Intel emploie des espacements réguliers et place les commandes entre guillemets.",
    "en": "• The processing-log header now meets its frame and follows the settings panel’s vertical spacing.\n• The page 5 licence uses a fixed, more readable text size in all twelve guides.\n• The Intel procedure uses consistent spacing and places commands in quotation marks.",
    "es": "• La cabecera del registro toca ahora su marco y adopta el espaciado vertical de los ajustes.\n• La licencia de la página 5 usa un tamaño fijo y más legible en las doce guías.\n• El procedimiento Intel usa espacios regulares y coloca los comandos entre comillas.",
    "it": "• L’intestazione del registro ora tocca il riquadro e riprende la spaziatura verticale delle impostazioni.\n• La licenza a pagina 5 usa una dimensione fissa e più leggibile nelle dodici guide.\n• La procedura Intel usa spazi regolari e racchiude i comandi tra virgolette.",
    "pt": "• O cabeçalho do registo passa a tocar no quadro e usa o espaçamento vertical das definições.\n• A licença da página 5 usa um tamanho fixo e mais legível nos doze guias.\n• O procedimento Intel usa espaçamento regular e coloca os comandos entre aspas.",
    "ru": "• Заголовок журнала теперь примыкает к рамке и использует вертикальные интервалы панели настроек.\n• Текст лицензии на странице 5 имеет одинаковый и более читаемый размер во всех 12 руководствах.\n• В инструкции Intel выровнены интервалы, а команды заключены в кавычки.",
    "ja": "• 処理ログのヘッダーを枠に接続し、設定パネルと同じ縦間隔にしました。\n• 12言語の5ページ目でライセンス本文を読みやすい固定サイズにしました。\n• Intel手順の間隔を統一し、コマンドを引用符で囲みました。",
    "hi": "• Processing log header अब frame से जुड़ता है और settings panel जैसी vertical spacing उपयोग करता है।\n• सभी 12 guides में page 5 licence का text size समान और अधिक पठनीय है।\n• Intel procedure में spacing समान है और commands quotation marks में हैं।",
    "zh": "• 处理日志标题栏现与边框相接，并采用设置面板相同的垂直间距。\n• 十二种语言指南第5页的许可证文字改为统一且更易读的字号。\n• Intel步骤采用一致间距，并为命令添加引号。",
    "ko": "• 처리 로그 머리글을 프레임에 붙이고 설정 패널과 같은 세로 간격을 적용했습니다.\n• 12개 언어 안내서의 5쪽 라이선스 본문을 더 읽기 쉬운 고정 크기로 통일했습니다.\n• Intel 절차의 간격을 통일하고 명령을 따옴표로 묶었습니다.",
    "id": "• Header log kini menyentuh bingkai dan memakai jarak vertikal yang sama dengan panel pengaturan.\n• Teks lisensi halaman 5 memakai ukuran tetap yang lebih mudah dibaca dalam dua belas panduan.\n• Prosedur Intel memakai jarak konsisten dan menempatkan perintah dalam tanda kutip.",
    "tr": "• İşlem günlüğü başlığı artık çerçeveye bitişik ve ayarlar paneliyle aynı dikey aralığı kullanıyor.\n• On iki kılavuzda 5. sayfadaki lisans metni sabit ve daha okunaklı boyuttadır.\n• Intel adımları tutarlı aralık kullanır ve komutlar tırnak içine alınır.",
}


TRANSLATION_UPDATES_201300 = {
    language: {
        "guide_intel_build_body": _intel_body_with_compact_sections(language),
        "version_changes": _VERSION_CHANGES[language],
    }
    for language in TRANSLATION_UPDATES_201200
}


__all__ = ["TRANSLATION_UPDATES_201300"]
