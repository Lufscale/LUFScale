"""Focused interface correction for LUFScale 2.0.17."""

from .translations_201600 import TRANSLATION_UPDATES_201600


_VERSION_CHANGES = {
    "fr": "• Le bouton d’aide du journal conserve sa position. Alerte et Erreur sont décalés de 6 px vers la gauche afin d’obtenir le même espacement entre les trois commandes.",
    "en": "• The processing-log Help button keeps its position. Warning and Error move 6 px left so all three controls have equal spacing.",
    "es": "• El botón de ayuda del registro conserva su posición. Alertas y Errores se desplazan 6 px a la izquierda para igualar el espacio entre los tres controles.",
    "it": "• Il pulsante Aiuto del registro mantiene la sua posizione. Avvisi ed Errori si spostano di 6 px a sinistra per uniformare lo spazio tra i tre comandi.",
    "pt": "• O botão de ajuda do registo mantém a posição. Alertas e Erros deslocam-se 6 px para a esquerda para igualar o espaço entre os três controlos.",
    "ru": "• Кнопка справки журнала сохраняет положение. Кнопки предупреждений и ошибок сдвинуты на 6 px влево, чтобы интервалы между тремя элементами были одинаковыми.",
    "ja": "• 処理ログのヘルプボタン位置は維持します。3つの操作間隔を揃えるため、警告とエラーを6 px左へ移動しました。",
    "hi": "• प्रसंस्करण लॉग का सहायता बटन अपनी जगह रहता है। तीनों नियंत्रणों के बीच समान दूरी के लिए चेतावनी और त्रुटि को 6 px बाएँ किया गया है।",
    "zh": "• 处理日志帮助按钮保持原位。警告和错误按钮向左移动6 px，使三个控件之间的间距一致。",
    "ko": "• 처리 로그 도움말 버튼은 제자리를 유지합니다. 세 컨트롤의 간격을 같게 하기 위해 경고와 오류를 6 px 왼쪽으로 옮겼습니다.",
    "id": "• Tombol bantuan log tetap pada posisinya. Peringatan dan Kesalahan digeser 6 px ke kiri agar jarak ketiga kontrol sama.",
    "tr": "• İşlem günlüğü Yardım düğmesi konumunu korur. Üç denetim arasındaki boşluğu eşitlemek için Uyarılar ve Hatalar 6 px sola kaydırılmıştır.",
}


TRANSLATION_UPDATES_201700 = {
    language: {
        **TRANSLATION_UPDATES_201600[language],
        "version_changes": _VERSION_CHANGES[language],
    }
    for language in TRANSLATION_UPDATES_201600
}


__all__ = ["TRANSLATION_UPDATES_201700"]
