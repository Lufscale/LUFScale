from __future__ import annotations


# Text changed with the stricter unchanged-copy rule and the final graph/tab
# presentation introduced in 1.24.13.
TRANSLATION_UPDATES_12413: dict[str, dict[str, str]] = {
    "fr": {
        "skip_compliant_tooltip": "Activé par défaut. Après l’analyse, un fichier dont la sonie est à ±0,10 LU de la cible et dont la crête vraie ne dépasse pas le plafond est copié à l’identique, sans réencodage. En mode Album, la conformité de la sonie est évaluée sur l’album entier. Cela préserve exactement sa qualité et sa taille ; le journal l’indique clairement.",
        "version_changes": "• Avant utilise une ligne médiane et une échelle automatique pour rendre les variations entre sources visibles ; Après garde la cible au milieu et fait défiler les écarts vers la gauche.\n• La copie sans réencodage exige désormais un écart maximal de ±0,10 LU : −14,39 LUFS n’est donc plus déclaré déjà conforme pour une cible de −14,00 LUFS.\n• Les bordures Audio et Options sont peintes une seule fois, avec des raccords continus à gauche et à droite.\n• La tolérance finale du contrôle qualité reste ±0,60 LU pour absorber les variations d’encodage.",
    },
    "en": {
        "skip_compliant_tooltip": "Enabled by default. After analysis, a file whose loudness is within ±0.10 LU of the target and whose true peak does not exceed the ceiling is copied unchanged, without re-encoding. In Album mode, loudness compliance is evaluated for the whole album. This preserves its exact quality and size; the log states it clearly.",
        "version_changes": "• Before uses a centre line and automatic scale to reveal variation among sources; After keeps the target in the middle and scrolls deviations to the left.\n• Unchanged copying now requires a maximum ±0.10 LU difference: −14.39 LUFS is therefore no longer already compliant with a −14.00 LUFS target.\n• Audio and Options borders are painted once, with continuous left and right joins.\n• The final quality-control tolerance remains ±0.60 LU to accommodate encoding variation.",
    },
    "es": {
        "skip_compliant_tooltip": "Activado por defecto. Tras el análisis, un archivo situado a ±0,10 LU del objetivo y cuyo pico real no supera el límite se copia sin cambios ni recodificación. En modo Álbum, la sonoridad se evalúa para el álbum completo. Así se conservan exactamente calidad y tamaño; el registro lo indica.",
        "version_changes": "• Antes usa una línea central y una escala automática para mostrar la variación de las fuentes; Después mantiene el objetivo en el centro y desplaza los desvíos hacia la izquierda.\n• La copia sin recodificación exige ahora un desvío máximo de ±0,10 LU: −14,39 LUFS ya no se considera conforme con un objetivo de −14,00 LUFS.\n• Los bordes de Audio y Opciones se dibujan una sola vez y se unen de forma continua a izquierda y derecha.\n• La tolerancia final del control de calidad sigue siendo ±0,60 LU para admitir variaciones de codificación.",
    },
    "it": {
        "skip_compliant_tooltip": "Attiva per impostazione predefinita. Dopo l’analisi, un file entro ±0,10 LU dall’obiettivo e con true peak non superiore al limite viene copiato identico, senza ricodifica. In modalità Album la conformità della sonorità è valutata sull’intero album. Qualità e dimensione restano identiche; il registro lo segnala.",
        "version_changes": "• Prima usa una linea centrale e una scala automatica per mostrare le variazioni tra le sorgenti; Dopo mantiene l’obiettivo al centro e fa scorrere gli scarti verso sinistra.\n• La copia senza ricodifica richiede ora uno scarto massimo di ±0,10 LU: −14,39 LUFS non è più considerato conforme a un obiettivo di −14,00 LUFS.\n• I bordi Audio e Opzioni vengono disegnati una sola volta, con raccordi continui a sinistra e a destra.\n• La tolleranza finale del controllo qualità resta ±0,60 LU per assorbire le variazioni di codifica.",
    },
    "pt": {
        "skip_compliant_tooltip": "Ativada por predefinição. Após a análise, um ficheiro a ±0,10 LU do alvo e cujo true peak não ultrapassa o limite é copiado sem alteração nem recodificação. No modo Álbum, a sonoridade é avaliada para o álbum inteiro. A qualidade e o tamanho ficam exatamente preservados; o registo indica-o.",
        "version_changes": "• Antes usa uma linha central e uma escala automática para mostrar as variações entre origens; Depois mantém o alvo no centro e desloca os desvios para a esquerda.\n• A cópia sem recodificação exige agora um desvio máximo de ±0,10 LU: −14,39 LUFS deixa de ser considerado conforme com um alvo de −14,00 LUFS.\n• Os contornos de Áudio e Opções são desenhados uma só vez, com ligações contínuas à esquerda e à direita.\n• A tolerância final do controlo de qualidade mantém-se em ±0,60 LU para admitir variações de codificação.",
    },
    "ru": {
        "skip_compliant_tooltip": "По умолчанию включено. После анализа файл копируется без изменений и перекодирования, если громкость отличается от цели не более чем на ±0,10 LU, а истинный пик не превышает предел. В режиме «Альбом» громкость оценивается для всего альбома. Качество и размер сохраняются точно; это указано в журнале.",
        "version_changes": "• График «До» использует среднюю линию и автоматический масштаб, чтобы показать разброс источников; график «После» удерживает цель в центре и сдвигает отклонения влево.\n• Копирование без перекодирования теперь требует отклонения не более ±0,10 LU: −14,39 LUFS больше не считается соответствующим цели −14,00 LUFS.\n• Рамки вкладок «Аудио» и «Параметры» рисуются один раз и непрерывно соединяются слева и справа.\n• Итоговый допуск контроля качества остаётся ±0,60 LU с учётом изменений при кодировании.",
    },
    "ja": {
        "skip_compliant_tooltip": "既定で有効です。解析後、ラウドネスが目標の±0.10 LU以内でトゥルーピークが上限以下なら、音声を再エンコードせず同一のままコピーします。アルバムモードではアルバム全体のラウドネスで判定します。品質とサイズを完全に維持し、ログにも表示します。",
        "version_changes": "• 処理前は中央線と自動目盛りでソース間の変動を表示し、処理後は目標を中央に固定して偏差を左へ流します。\n• 再エンコードしないコピーの条件を±0.10 LU以内に変更したため、目標−14.00 LUFSに対する−14.39 LUFSは適合済みと判定されません。\n• オーディオ／オプションの枠線を一度だけ描画し、左右の接続を連続させました。\n• エンコードによる変動を考慮し、最終品質管理の許容差は±0.60 LUのままです。",
    },
    "hi": {
        "skip_compliant_tooltip": "डिफ़ॉल्ट रूप से चालू। विश्लेषण के बाद लक्ष्य से ±0.10 LU के भीतर और true peak सीमा से नीचे वाली फ़ाइल बिना बदले और बिना पुनः एनकोड किए कॉपी होती है। एल्बम मोड में लाउडनेस पूरे एल्बम पर जाँची जाती है। गुणवत्ता और आकार बिल्कुल सुरक्षित रहते हैं; लॉग इसे बताता है।",
        "version_changes": "• पहले वाला ग्राफ़ स्रोतों का बदलाव दिखाने के लिए बीच की रेखा और स्वचालित पैमाना उपयोग करता है; बाद वाला लक्ष्य को बीच में रखकर अंतर को बाईं ओर खिसकाता है।\n• बिना पुनः एनकोड की कॉपी के लिए अब अधिकतम अंतर ±0.10 LU है; इसलिए −14.00 LUFS लक्ष्य पर −14.39 LUFS को पहले से अनुरूप नहीं माना जाता।\n• Audio और Options की सीमाएँ एक बार खींची जाती हैं और बाईं व दाईं ओर लगातार जुड़ती हैं।\n• एनकोडिंग बदलाव के लिए अंतिम गुणवत्ता नियंत्रण सहनशीलता ±0.60 LU रहती है।",
    },
    "zh": {
        "skip_compliant_tooltip": "默认启用。分析后，响度与目标相差不超过 ±0.10 LU 且真峰值不超过上限的文件会原样复制，不重新编码。专辑模式按整张专辑的响度判断。这样可完全保留质量和大小，日志会明确说明。",
        "version_changes": "• 处理前图使用中线和自动刻度显示源文件之间的变化；处理后图将目标保持在中央，并让偏差向左滚动。\n• 不重新编码的复制现在要求最大偏差为±0.10 LU；因此目标为−14.00 LUFS时，−14.39 LUFS不再判定为已经合规。\n• 音频和选项的边框只绘制一次，左右连接保持连续。\n• 为容纳编码变化，最终质量控制容差仍为±0.60 LU。",
    },
    "ko": {
        "skip_compliant_tooltip": "기본으로 켜집니다. 분석 후 라우드니스가 목표의 ±0.10 LU 이내이고 트루 피크가 상한을 넘지 않으면 재인코딩 없이 그대로 복사합니다. 앨범 모드에서는 앨범 전체의 라우드니스를 판정합니다.",
        "version_changes": "• 처리 전 그래프는 중앙선과 자동 눈금으로 원본 간 변화를 보여 주고, 처리 후 그래프는 목표를 가운데에 두고 편차를 왼쪽으로 이동시킵니다.\n• 재인코딩 없는 복사는 이제 최대 ±0.10 LU 차이만 허용하므로, 목표가 −14.00 LUFS일 때 −14.39 LUFS는 더 이상 이미 적합한 값으로 판정되지 않습니다.\n• 오디오/옵션 테두리를 한 번만 그려 왼쪽과 오른쪽 연결이 끊기지 않습니다.\n• 인코딩 변화를 고려해 최종 품질 관리 허용치는 ±0.60 LU로 유지됩니다.",
    },
    "id": {
        "skip_compliant_tooltip": "Aktif secara default. Setelah analisis, berkas disalin tanpa enkode ulang jika kenyaringannya berada dalam ±0,10 LU dari target dan true peak tidak melewati batas. Dalam mode Album, kesesuaian dinilai untuk seluruh album.",
        "version_changes": "• Grafik Sebelum memakai garis tengah dan skala otomatis untuk menunjukkan variasi sumber; grafik Sesudah mempertahankan target di tengah dan menggeser penyimpangan ke kiri.\n• Penyalinan tanpa enkode ulang kini mensyaratkan selisih maksimum ±0,10 LU; karena itu −14,39 LUFS tidak lagi dianggap sudah sesuai dengan target −14,00 LUFS.\n• Garis tepi Audio dan Opsi digambar satu kali, dengan sambungan kiri dan kanan yang berkelanjutan.\n• Toleransi akhir kontrol mutu tetap ±0,60 LU untuk menampung variasi enkode.",
    },
    "tr": {
        "skip_compliant_tooltip": "Varsayılan olarak etkindir. Analizden sonra ses yüksekliği hedefin ±0,10 LU aralığındaysa ve true peak sınırı aşmıyorsa dosya yeniden kodlanmadan aynen kopyalanır. Albüm modunda uygunluk albümün tamamı için değerlendirilir.",
        "version_changes": "• Önce grafiği kaynaklar arasındaki değişimi göstermek için orta çizgi ve otomatik ölçek kullanır; Sonra grafiği hedefi ortada tutup sapmaları sola kaydırır.\n• Yeniden kodlamadan kopyalama artık en fazla ±0,10 LU fark gerektirir; bu nedenle −14,00 LUFS hedefi için −14,39 LUFS artık önceden uygun sayılmaz.\n• Ses ve Seçenekler kenarlıkları bir kez çizilir ve sol ile sağ bağlantılar kesintisizdir.\n• Kodlama değişimlerini karşılamak için son kalite kontrol toleransı ±0,60 LU olarak kalır.",
    },
}


__all__ = ["TRANSLATION_UPDATES_12413"]
