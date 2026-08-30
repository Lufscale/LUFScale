"""Final journal alignment and Intel-guide spacing for LUFScale 2.0.14."""

from .translations_201300 import TRANSLATION_UPDATES_201300


def _intel_body_with_paragraph_gaps(language: str) -> str:
    """Separate the procedure, explanation and verification as paragraphs."""
    source = TRANSLATION_UPDATES_201300[language]["guide_intel_build_body"]
    lines = source.splitlines()
    first_step = next(
        index for index, line in enumerate(lines) if line.startswith("1. ")
    )
    intro = "\n".join(lines[:first_step]).strip()
    steps = [line for line in lines[first_step : first_step + 4] if line.strip()]
    following = [line for line in lines[first_step + 4 :] if line.strip()]
    return (
        intro
        + "\n\n"
        + "\n".join(steps)
        + "\n\n"
        + "\n\n".join(following)
    )


_VERSION_CHANGES = {
    "fr": "• Le bouton d’aide du journal est centré exactement avec les boutons Alerte et Erreur.\n• La procédure Intel de la page 5 sépare clairement les étapes, l’explication et le contrôle dans les douze guides.",
    "en": "• The processing-log Help button is centred exactly with the Warning and Error buttons.\n• The page 5 Intel procedure clearly separates the steps, explanation and check in all twelve guides.",
    "es": "• El botón de ayuda del registro queda centrado exactamente con los botones Alertas y Errores.\n• El procedimiento Intel de la página 5 separa claramente los pasos, la explicación y la comprobación en las doce guías.",
    "it": "• Il pulsante Aiuto del registro è centrato esattamente con i pulsanti Avvisi ed Errori.\n• La procedura Intel a pagina 5 separa chiaramente i passaggi, la spiegazione e il controllo in tutte le dodici guide.",
    "pt": "• O botão de ajuda do registo fica exatamente centrado com os botões Alertas e Erros.\n• O procedimento Intel da página 5 separa claramente os passos, a explicação e a verificação nos doze guias.",
    "ru": "• Кнопка справки журнала точно выровнена по центру кнопок предупреждений и ошибок.\n• Во всех 12 руководствах инструкция Intel на странице 5 чётко разделяет шаги, пояснение и проверку.",
    "ja": "• 処理ログのヘルプボタンを警告・エラーボタンの中央に正確に揃えました。\n• 12言語すべての5ページ目で、Intel手順の操作、説明、確認を明確に分けました。",
    "hi": "• Processing log का Help button अब Warning और Error buttons के केंद्र से ठीक संरेखित है।\n• सभी 12 guides में page 5 की Intel procedure में steps, explanation और check स्पष्ट रूप से अलग हैं।",
    "zh": "• 处理日志的帮助按钮现与警告和错误按钮精确居中对齐。\n• 十二种语言指南第5页的 Intel 步骤、说明和检查现已清晰分段。",
    "ko": "• 처리 로그의 도움말 버튼을 경고 및 오류 버튼의 중심과 정확히 맞췄습니다.\n• 12개 언어 안내서의 5쪽 Intel 절차에서 단계, 설명 및 확인을 명확히 구분했습니다.",
    "id": "• Tombol bantuan log kini tepat sejajar dengan pusat tombol Peringatan dan Kesalahan.\n• Prosedur Intel pada halaman 5 memisahkan langkah, penjelasan, dan pemeriksaan dengan jelas dalam kedua belas panduan.",
    "tr": "• İşlem günlüğü Yardım düğmesi, Uyarılar ve Hatalar düğmelerinin merkeziyle tam hizalandı.\n• On iki kılavuzun 5. sayfasındaki Intel yordamında adımlar, açıklama ve kontrol açıkça ayrıldı.",
}


TRANSLATION_UPDATES_201400 = {
    language: {
        "guide_intel_build_body": _intel_body_with_paragraph_gaps(language),
        "version_changes": _VERSION_CHANGES[language],
    }
    for language in TRANSLATION_UPDATES_201300
}


__all__ = ["TRANSLATION_UPDATES_201400"]
