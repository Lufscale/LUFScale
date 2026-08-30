"""Interface corrections introduced by LUFScale 2.1.12."""

from .translations_211000 import TRANSLATION_UPDATES_211000


_LOG_SPACING_CHANGE = {
    "fr": "• L’interligne du journal de traitement est maintenant uniforme dans toutes les langues ; les polices japonaises, chinoises, coréennes et devanagari n’ajoutent plus d’espace vertical excessif.",
    "en": "• Processing-log line spacing is now uniform in every language; Japanese, Chinese, Korean and Devanagari fonts no longer add excessive vertical space.",
    "es": "• El interlineado del registro de procesamiento ahora es uniforme en todos los idiomas; las fuentes de japonés, chino, coreano y devanagari ya no añaden un espacio vertical excesivo.",
    "it": "• L’interlinea del registro di elaborazione è ora uniforme in tutte le lingue; i caratteri giapponesi, cinesi, coreani e devanagari non aggiungono più uno spazio verticale eccessivo.",
    "pt": "• O espaçamento entre linhas do registo de processamento é agora uniforme em todos os idiomas; as fontes japonesas, chinesas, coreanas e devanágari já não acrescentam espaço vertical excessivo.",
    "ru": "• Межстрочный интервал журнала обработки теперь одинаков для всех языков; японские, китайские, корейские шрифты и деванагари больше не добавляют избыточное вертикальное пространство.",
    "ja": "• 処理ログの行間を全言語で統一し、日本語・中国語・韓国語・デーヴァナーガリー文字のフォントで過剰な縦方向の余白が生じないようにしました。",
    "hi": "• प्रसंस्करण लॉग की पंक्ति-दूरी अब सभी भाषाओं में समान है; जापानी, चीनी, कोरियाई और देवनागरी फ़ॉन्ट अब अतिरिक्त ऊर्ध्वाधर खाली स्थान नहीं जोड़ते।",
    "zh": "• 处理日志的行距现在在所有语言中保持一致；日文、中文、韩文和天城文字体不再产生过大的垂直间距。",
    "ko": "• 처리 로그의 줄 간격을 모든 언어에서 동일하게 맞췄으며 일본어, 중국어, 한국어 및 데바나가리 글꼴이 더 이상 과도한 세로 여백을 추가하지 않습니다.",
    "id": "• Jarak baris log pemrosesan kini seragam dalam semua bahasa; font Jepang, Tionghoa, Korea, dan Dewanagari tidak lagi menambahkan ruang vertikal berlebihan.",
    "tr": "• İşlem günlüğünün satır aralığı artık tüm dillerde aynıdır; Japonca, Çince, Korece ve Devanagari yazı tipleri artık aşırı dikey boşluk eklemez.",
}


TRANSLATION_UPDATES_211100 = {
    language: {
        "version_changes": (
            _LOG_SPACING_CHANGE[language]
            + "\n"
            + TRANSLATION_UPDATES_211000[language]["version_changes"]
        ),
    }
    for language in TRANSLATION_UPDATES_211000
}


__all__ = ["TRANSLATION_UPDATES_211100"]
