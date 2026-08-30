"""ReplayGain comparison and fail-safe resume fixes for 1.24.34."""

TRANSLATION_UPDATES_12434 = {
    "fr": {
        "loudness_comparison_tooltip": "Avant montre la source ; Après montre la sonie physique livrée. Avec ReplayGain, les deux courbes doivent normalement coïncider.",
        "loudness_comparison_help_text": "Chaque fichier ajoute un point à droite et décale l’historique vers la gauche. Avant affiche la source mesurée ; Après affiche la sortie réellement remesurée. Les deux graphiques partagent la même échelle fixe de ±6 LU autour de la cible, et la bande verte représente la tolérance QC de ±0,60 LU. Avec ReplayGain, Après représente la sonie physique du fichier copié : puisque les échantillons ne changent pas, sa courbe doit normalement reprendre Avant. Cela ne signifie pas que la cible est physiquement atteinte. Analyser seulement n’a pas de sortie Après.",
        "version_changes": "• ReplayGain affiche désormais la sonie physique livrée dans Après ; elle doit normalement coïncider avec Avant, car les échantillons sont inchangés.\n• La reprise d’une sortie déjà terminée ne bloque plus le worker ni l’interface.\n• Toute erreur interne inattendue libère désormais le traitement, l’annulation et la fermeture.",
    },
    "en": {
        "loudness_comparison_tooltip": "Before shows the source; After shows delivered physical loudness. With ReplayGain, both curves should normally overlap.",
        "loudness_comparison_help_text": "Each file adds a point on the right and moves history left. Before shows the measured source; After shows the actually remeasured output. Both graphs share the same fixed ±6 LU scale around target, and the green band is the ±0.60 LU QC tolerance. With ReplayGain, After represents the physical loudness of the copied file: because samples do not change, its curve should normally match Before. This does not mean that target loudness was physically reached. Analyze-only has no After output.",
        "version_changes": "• ReplayGain now shows delivered physical loudness in After; it should normally match Before because samples are unchanged.\n• Resuming an already completed output no longer locks the worker or interface.\n• Any unexpected internal error now releases processing, cancellation and closing.",
    },
    "es": {
        "loudness_comparison_tooltip": "Antes muestra la fuente; Después, la sonoridad física entregada. Con ReplayGain, ambas curvas deberían coincidir.",
        "loudness_comparison_help_text": "Cada archivo añade un punto a la derecha. Antes muestra la fuente medida y Después la salida realmente medida de nuevo. Ambos gráficos comparten la escala fija de ±6 LU alrededor del objetivo; la banda verde es la tolerancia QC de ±0,60 LU. Con ReplayGain, Después representa la sonoridad física del archivo copiado: como las muestras no cambian, normalmente coincide con Antes. Esto no significa que se alcance físicamente el objetivo. Solo analizar no tiene salida Después.",
        "version_changes": "• ReplayGain muestra ahora la sonoridad física entregada en Después.\n• Reanudar una salida terminada ya no bloquea el proceso ni la interfaz.\n• Un error interno inesperado libera el procesamiento, la cancelación y el cierre.",
    },
    "it": {
        "loudness_comparison_tooltip": "Prima mostra la sorgente; Dopo la sonorità fisica consegnata. Con ReplayGain le curve dovrebbero coincidere.",
        "loudness_comparison_help_text": "Ogni file aggiunge un punto a destra. Prima mostra la sorgente misurata e Dopo l’uscita realmente rimisurata. I grafici condividono la scala fissa ±6 LU intorno all’obiettivo; la fascia verde è la tolleranza QC ±0,60 LU. Con ReplayGain, Dopo rappresenta la sonorità fisica del file copiato: poiché i campioni non cambiano, normalmente coincide con Prima. Ciò non significa che l’obiettivo sia raggiunto fisicamente. Solo analisi non ha un’uscita Dopo.",
        "version_changes": "• ReplayGain mostra ora in Dopo la sonorità fisica consegnata.\n• La ripresa di un’uscita completata non blocca più worker e interfaccia.\n• Un errore interno inatteso libera elaborazione, annullamento e chiusura.",
    },
    "pt": {
        "loudness_comparison_tooltip": "Antes mostra a origem; Depois, a sonoridade física entregue. Com ReplayGain, as curvas devem normalmente coincidir.",
        "loudness_comparison_help_text": "Cada ficheiro acrescenta um ponto à direita. Antes mostra a origem medida e Depois a saída realmente medida de novo. Os gráficos partilham a escala fixa ±6 LU em torno do alvo; a faixa verde é a tolerância QC ±0,60 LU. Com ReplayGain, Depois representa a sonoridade física do ficheiro copiado: como as amostras não mudam, normalmente coincide com Antes. Isto não significa que o alvo foi fisicamente atingido. Apenas analisar não tem saída Depois.",
        "version_changes": "• ReplayGain mostra agora em Depois a sonoridade física entregue.\n• Retomar uma saída concluída já não bloqueia o processo nem a interface.\n• Um erro interno inesperado liberta o processamento, o cancelamento e o fecho.",
    },
    "ru": {
        "loudness_comparison_tooltip": "«До» показывает источник, «После» — физическую громкость результата. Для ReplayGain кривые обычно совпадают.",
        "loudness_comparison_help_text": "Каждый файл добавляет точку справа. «До» показывает измеренный источник, «После» — повторно измеренный результат. Оба графика используют фиксированную шкалу ±6 LU вокруг цели; зелёная полоса — допуск QC ±0,60 LU. Для ReplayGain «После» показывает физическую громкость скопированного файла: поскольку сэмплы не меняются, кривая обычно совпадает с «До». Это не означает физическое достижение цели. У режима анализа нет выхода «После».",
        "version_changes": "• ReplayGain теперь показывает физическую громкость результата на графике «После».\n• Возобновление готового результата больше не блокирует обработчик и интерфейс.\n• Неожиданная внутренняя ошибка теперь освобождает обработку, отмену и закрытие.",
    },
    "ja": {
        "loudness_comparison_tooltip": "「前」は入力、「後」は出力の物理ラウドネスです。ReplayGainでは通常、2本の曲線は重なります。",
        "loudness_comparison_help_text": "各ファイルは右側に点を追加します。「前」は測定した入力、「後」は実際に再測定した出力です。両グラフは目標を中心とする固定±6 LUスケールを共有し、緑の帯はQC許容差±0.60 LUです。ReplayGainの「後」はコピーされたファイルの物理ラウドネスを示します。サンプルは変わらないため、通常は「前」と重なります。これは目標を物理的に達成した意味ではありません。解析のみには「後」の出力がありません。",
        "version_changes": "• ReplayGainの物理出力ラウドネスを「後」に表示します。\n• 完了済み出力の再開で処理と画面がロックしなくなりました。\n• 予期しない内部エラーでも処理、キャンセル、終了を解放します。",
    },
    "hi": {
        "loudness_comparison_tooltip": "पहले source दिखाता है; बाद में delivered physical loudness। ReplayGain में दोनों curves सामान्यतः समान होती हैं।",
        "loudness_comparison_help_text": "हर file दाईं ओर एक point जोड़ती है। पहले measured source और बाद में वास्तव में दोबारा मापा output दिखता है। दोनों graph लक्ष्य के चारों ओर समान fixed ±6 LU scale उपयोग करते हैं; हरी पट्टी QC tolerance ±0.60 LU है। ReplayGain में बाद वाला graph copied file की physical loudness दिखाता है। Samples नहीं बदलते, इसलिए वह सामान्यतः पहले वाले से मिलता है। इसका अर्थ यह नहीं कि लक्ष्य physically प्राप्त हुआ। Analyze-only में बाद वाला output नहीं है।",
        "version_changes": "• ReplayGain अब बाद वाले graph में delivered physical loudness दिखाता है।\n• पूर्ण output को resume करने पर worker और interface lock नहीं होते।\n• Unexpected internal error अब processing, cancel और close को release करता है।",
    },
    "zh": {
        "loudness_comparison_tooltip": "“之前”显示源文件，“之后”显示交付文件的物理响度。ReplayGain 下两条曲线通常应重合。",
        "loudness_comparison_help_text": "每个文件都会在右侧添加一个点。“之前”显示测得的源文件，“之后”显示实际复测的输出。两个图表共用以目标为中心的固定 ±6 LU 标尺；绿色区域表示 ±0.60 LU 的 QC 容差。ReplayGain 的“之后”表示复制文件的物理响度：样本没有改变，因此曲线通常与“之前”重合。这并不表示物理响度达到了目标。仅分析模式没有“之后”输出。",
        "version_changes": "• ReplayGain 现在会在“之后”显示交付文件的物理响度。\n• 恢复已完成的输出不再锁死工作线程或界面。\n• 意外内部错误也会释放处理、取消和关闭操作。",
    },
    "ko": {
        "loudness_comparison_tooltip": "이전은 원본, 이후는 전달 파일의 물리적 음량입니다. ReplayGain에서는 두 곡선이 보통 겹칩니다.",
        "loudness_comparison_help_text": "파일마다 오른쪽에 점이 추가됩니다. 이전은 측정한 원본, 이후는 실제로 다시 측정한 출력을 표시합니다. 두 그래프는 목표 중심의 고정 ±6 LU 눈금을 공유하며 녹색 띠는 QC 허용치 ±0.60 LU입니다. ReplayGain의 이후는 복사된 파일의 물리적 음량입니다. 샘플이 바뀌지 않으므로 보통 이전과 겹칩니다. 이는 목표 음량을 물리적으로 달성했다는 뜻이 아닙니다. 분석 전용에는 이후 출력이 없습니다.",
        "version_changes": "• ReplayGain의 전달 물리 음량을 이후 그래프에 표시합니다.\n• 완료된 출력을 재개해도 작업자와 화면이 잠기지 않습니다.\n• 예기치 않은 내부 오류도 처리, 취소, 종료를 해제합니다.",
    },
    "id": {
        "loudness_comparison_tooltip": "Sebelum menampilkan sumber; Sesudah menampilkan loudness fisik hasil. Pada ReplayGain, kedua kurva biasanya bertumpuk.",
        "loudness_comparison_help_text": "Setiap berkas menambah satu titik di kanan. Sebelum menampilkan sumber terukur dan Sesudah menampilkan hasil yang benar-benar diukur ulang. Kedua grafik memakai skala tetap ±6 LU di sekitar target; pita hijau adalah toleransi QC ±0,60 LU. Pada ReplayGain, Sesudah menunjukkan loudness fisik berkas salinan. Karena sampel tidak berubah, kurvanya biasanya sama dengan Sebelum. Ini tidak berarti target tercapai secara fisik. Analisis saja tidak memiliki keluaran Sesudah.",
        "version_changes": "• ReplayGain kini menampilkan loudness fisik hasil pada grafik Sesudah.\n• Melanjutkan keluaran yang sudah selesai tidak lagi mengunci worker atau antarmuka.\n• Galat internal tak terduga kini melepaskan proses, pembatalan, dan penutupan.",
    },
    "tr": {
        "loudness_comparison_tooltip": "Önce kaynağı, Sonra teslim edilen fiziksel ses düzeyini gösterir. ReplayGain’de eğriler normalde çakışır.",
        "loudness_comparison_help_text": "Her dosya sağa bir nokta ekler. Önce ölçülen kaynağı, Sonra gerçekten yeniden ölçülen çıktıyı gösterir. İki grafik hedef çevresinde aynı sabit ±6 LU ölçeğini kullanır; yeşil bant ±0,60 LU QC toleransıdır. ReplayGain’de Sonra, kopyalanan dosyanın fiziksel ses düzeyini gösterir. Örnekler değişmediği için eğri normalde Önce ile çakışır. Bu, hedefe fiziksel olarak ulaşıldığı anlamına gelmez. Yalnızca Analiz modunda Sonra çıktısı yoktur.",
        "version_changes": "• ReplayGain artık Sonra grafiğinde teslim edilen fiziksel ses düzeyini gösterir.\n• Tamamlanmış çıktıyı sürdürmek worker veya arayüzü kilitlemez.\n• Beklenmeyen iç hata artık işlem, iptal ve kapatmayı serbest bırakır.",
    },
}
