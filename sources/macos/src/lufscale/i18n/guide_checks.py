"""Localized troubleshooting checks for page 4 of every PDF guide."""


USEFUL_CHECKS_COPY = {
    "fr": {
        "heading": "Trois vérifications utiles",
        "cards": (
            ("Aucun traitement", "Vérifiez qu’au moins une source audio compatible et une destination différente sont sélectionnées."),
            ("FFmpeg introuvable", "Relancez le créateur de l’application ou installez FFmpeg, puis redémarrez."),
            ("Alertes de crête", "Choisissez une crête plus négative ou une cible moins forte, puis relancez le fichier."),
        ),
    },
    "en": {
        "heading": "Three useful checks",
        "cards": (
            ("No processing", "Check that at least one compatible audio source and a different destination are selected."),
            ("FFmpeg not found", "Run the application builder again or install FFmpeg, then restart."),
            ("Peak warnings", "Choose a more negative true-peak ceiling or a lower loudness target, then process the file again."),
        ),
    },
    "es": {
        "heading": "Tres comprobaciones útiles",
        "cards": (
            ("Ningún procesamiento", "Compruebe que estén seleccionados al menos un origen de audio compatible y un destino diferente."),
            ("FFmpeg no encontrado", "Vuelva a ejecutar el creador de la aplicación o instale FFmpeg y reinicie."),
            ("Alertas de pico", "Elija un límite de pico real más negativo o un objetivo de sonoridad más bajo y vuelva a procesar el archivo."),
        ),
    },
    "it": {
        "heading": "Tre verifiche utili",
        "cards": (
            ("Nessuna elaborazione", "Verificare che siano selezionati almeno una sorgente audio compatibile e una destinazione diversa."),
            ("FFmpeg non trovato", "Eseguire di nuovo il generatore dell’applicazione oppure installare FFmpeg, quindi riavviare."),
            ("Avvisi di picco", "Scegliere un limite di picco reale più negativo o un obiettivo di sonorità più basso, quindi elaborare di nuovo il file."),
        ),
    },
    "pt": {
        "heading": "Três verificações úteis",
        "cards": (
            ("Sem processamento", "Verifique se estão selecionados pelo menos uma fonte de áudio compatível e um destino diferente."),
            ("FFmpeg não encontrado", "Execute novamente o criador da aplicação ou instale o FFmpeg e reinicie."),
            ("Avisos de pico", "Escolha um limite de pico real mais negativo ou um alvo de sonoridade mais baixo e processe novamente o ficheiro."),
        ),
    },
    "ru": {
        "heading": "Три полезные проверки",
        "cards": (
            ("Обработка не запускается", "Убедитесь, что выбран хотя бы один совместимый аудиоисточник и другая папка назначения."),
            ("FFmpeg не найден", "Снова запустите сборщик приложения или установите FFmpeg, затем перезапустите программу."),
            ("Предупреждения о пиках", "Выберите более отрицательный предел истинного пика или более низкую целевую громкость, затем обработайте файл снова."),
        ),
    },
    "ja": {
        "heading": "3つの確認ポイント",
        "cards": (
            ("処理されない", "対応する音声ソースが1つ以上選択され、別の保存先が指定されていることを確認してください。"),
            ("FFmpegが見つからない", "アプリケーションビルダーを再実行するかFFmpegをインストールし、再起動してください。"),
            ("ピーク警告", "より低いトゥルーピーク上限または低いラウドネス目標を選び、ファイルを再処理してください。"),
        ),
    },
    "hi": {
        "heading": "तीन उपयोगी जाँच",
        "cards": (
            ("प्रोसेसिंग नहीं हुई", "जाँचें कि कम-से-कम एक समर्थित ऑडियो स्रोत और उससे अलग गंतव्य चुना गया है।"),
            ("FFmpeg नहीं मिला", "एप्लिकेशन बिल्डर फिर चलाएँ या FFmpeg इंस्टॉल करें, फिर पुनः आरंभ करें।"),
            ("पीक चेतावनियाँ", "अधिक ऋणात्मक ट्रू-पीक सीमा या कम लाउडनेस लक्ष्य चुनें, फिर फ़ाइल को दोबारा प्रोसेस करें।"),
        ),
    },
    "zh": {
        "heading": "三项实用检查",
        "cards": (
            ("未开始处理", "请确认已选择至少一个受支持的音频源以及不同的输出位置。"),
            ("未找到 FFmpeg", "请重新运行应用程序构建器或安装 FFmpeg，然后重新启动。"),
            ("峰值警告", "请选择更低的真峰值上限或更低的响度目标，然后重新处理文件。"),
        ),
    },
    "ko": {
        "heading": "세 가지 유용한 확인",
        "cards": (
            ("처리되지 않음", "지원되는 오디오 원본을 하나 이상 선택하고 원본과 다른 대상 위치를 지정했는지 확인하십시오."),
            ("FFmpeg를 찾을 수 없음", "애플리케이션 빌더를 다시 실행하거나 FFmpeg를 설치한 뒤 다시 시작하십시오."),
            ("피크 경고", "더 낮은 트루 피크 상한 또는 더 낮은 라우드니스 목표를 선택한 뒤 파일을 다시 처리하십시오."),
        ),
    },
    "id": {
        "heading": "Tiga pemeriksaan penting",
        "cards": (
            ("Tidak ada pemrosesan", "Pastikan setidaknya satu sumber audio yang didukung dan tujuan yang berbeda telah dipilih."),
            ("FFmpeg tidak ditemukan", "Jalankan kembali pembuat aplikasi atau pasang FFmpeg, lalu mulai ulang."),
            ("Peringatan puncak", "Pilih batas true peak yang lebih negatif atau target kenyaringan yang lebih rendah, lalu proses ulang berkas."),
        ),
    },
    "tr": {
        "heading": "Üç yararlı kontrol",
        "cards": (
            ("İşlem yapılmadı", "En az bir uyumlu ses kaynağının ve farklı bir hedefin seçildiğini doğrulayın."),
            ("FFmpeg bulunamadı", "Uygulama oluşturucuyu yeniden çalıştırın veya FFmpeg’i kurup yeniden başlatın."),
            ("Tepe uyarıları", "Daha negatif bir gerçek tepe sınırı veya daha düşük bir ses yüksekliği hedefi seçip dosyayı yeniden işleyin."),
        ),
    },
}


__all__ = ["USEFUL_CHECKS_COPY"]
