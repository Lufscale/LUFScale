"""Focused interface and guide corrections for LUFScale 2.0.16."""

from .translations_201500 import TRANSLATION_UPDATES_201500


_FILE_LABELS = {
    "fr": "fichier",
    "en": "file",
    "es": "archivo",
    "it": "binario",
    "pt": "ficheiro",
    "ru": "файл",
    "ja": "ファイル",
    "hi": "फ़ाइल",
    "zh": "文件",
    "ko": "파일",
    "id": "berkas",
    "tr": "dosya",
}


_VERSION_CHANGES = {
    "fr": "• Le contrôle des deux binaires Intel est libellé dans la langue de chaque guide.\n• Le bouton d’aide du journal est remonté et entièrement dégagé du bord droit, sans déplacer Alerte ni Erreur.",
    "en": "• The two Intel binary checks are labelled in each guide’s language.\n• The processing-log Help button is raised and fully cleared from the right edge without moving Warning or Error.",
    "es": "• La comprobación de los dos binarios Intel está rotulada en el idioma de cada guía.\n• El botón de ayuda del registro se ha subido y separado completamente del borde derecho sin mover Alertas ni Errores.",
    "it": "• Il controllo dei due binari Intel è indicato nella lingua di ogni guida.\n• Il pulsante Aiuto del registro è stato alzato e liberato completamente dal bordo destro senza spostare Avvisi o Errori.",
    "pt": "• A verificação dos dois binários Intel é indicada no idioma de cada guia.\n• O botão de ajuda do registo foi elevado e totalmente afastado da margem direita sem mover Alertas nem Erros.",
    "ru": "• Проверка двух двоичных файлов Intel подписана на языке каждого руководства.\n• Кнопка справки журнала поднята и полностью отведена от правого края без перемещения кнопок предупреждений и ошибок.",
    "ja": "• Intel用2バイナリの確認表記を各ガイドの言語に統一しました。\n• 警告・エラーボタンを動かさず、処理ログのヘルプボタンを上げて右端から完全に離しました。",
    "hi": "• दोनों Intel बाइनरी की जाँच का नाम प्रत्येक मार्गदर्शिका की भाषा में दिया गया है।\n• चेतावनी या त्रुटि को बदले बिना प्रसंस्करण लॉग का सहायता बटन ऊपर किया गया और दाएँ किनारे से पूरी तरह अलग रखा गया है।",
    "zh": "• 两个Intel二进制文件的检查标签均使用各指南对应的语言。\n• 在不移动警告和错误按钮的情况下，将处理日志帮助按钮上移并与右边缘完全分离。",
    "ko": "• 두 Intel 바이너리 확인 문구를 각 안내서의 언어로 표시합니다.\n• 경고 및 오류 버튼은 그대로 두고 처리 로그 도움말 버튼을 위로 올려 오른쪽 가장자리에서 완전히 분리했습니다.",
    "id": "• Pemeriksaan kedua biner Intel diberi label dalam bahasa setiap panduan.\n• Tombol bantuan log dinaikkan dan dijauhkan sepenuhnya dari tepi kanan tanpa memindahkan Peringatan atau Kesalahan.",
    "tr": "• İki Intel ikilisinin denetimi her kılavuzun kendi dilinde adlandırılır.\n• Uyarılar ve Hatalar yerinden oynatılmadan işlem günlüğü Yardım düğmesi yukarı alınmış ve sağ kenardan tamamen ayrılmıştır.",
}


def _localized_intel_body(language: str) -> str:
    body = TRANSLATION_UPDATES_201500[language]["guide_intel_build_body"]
    return body.replace('file "', f'{_FILE_LABELS[language]} "')


TRANSLATION_UPDATES_201600 = {
    language: {
        **TRANSLATION_UPDATES_201500[language],
        "guide_intel_build_body": _localized_intel_body(language),
        "version_changes": _VERSION_CHANGES[language],
    }
    for language in TRANSLATION_UPDATES_201500
}


__all__ = ["TRANSLATION_UPDATES_201600"]
