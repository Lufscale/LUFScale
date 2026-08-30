from __future__ import annotations


# Text changed with the identical fixed-scale loudness graphs in 1.24.14.
TRANSLATION_UPDATES_12414: dict[str, dict[str, str]] = {
    "fr": {
        "loudness_comparison_help_text": "Chaque point représente la mesure intégrée d’un fichier traité. Avant et Après utilisent exactement la même échelle verticale fixe de ±6 LU autour de la cible ; la ligne médiane représente donc la cible dans les deux graphiques et une même distance verticale correspond toujours au même écart de sonie. Les valeurs situées hors de cette plage restent bloquées sur le bord supérieur ou inférieur. Les variations des sources sont ainsi directement comparables au regroupement des sorties après uniformisation. Le graphique reste inactif sans contrôle qualité.",
        "version_changes": "• Avant et Après partagent désormais une échelle fixe identique de ±6 LU autour de la cible, sans recalcul automatique.\n• La ligne médiane représente la cible dans les deux graphiques : les écarts avant traitement et la stabilité après traitement sont directement comparables.\n• Les valeurs hors plage restent visibles sur le bord du graphique.\n• La règle de copie à l’identique reste ±0,10 LU et la tolérance finale du contrôle qualité reste ±0,60 LU.",
    },
    "en": {
        "loudness_comparison_help_text": "Each point is the integrated measurement of one processed file. Before and After use exactly the same fixed vertical scale of ±6 LU around the target; the centre line therefore represents the target in both graphs, and the same vertical distance always means the same loudness difference. Values outside this range remain pinned to the upper or lower edge. Source variation can therefore be compared directly with the clustering of the normalized outputs. The graph remains inactive without quality control.",
        "version_changes": "• Before and After now share the same fixed ±6 LU scale around the target, with no automatic rescaling.\n• The centre line represents the target in both graphs, so pre-processing variation and post-processing stability are directly comparable.\n• Out-of-range values remain visible at the graph edge.\n• Unchanged copying remains at ±0.10 LU and final quality-control tolerance remains at ±0.60 LU.",
    },
    "es": {
        "loudness_comparison_help_text": "Cada punto es la medición integrada de un archivo procesado. Antes y Después usan exactamente la misma escala vertical fija de ±6 LU alrededor del objetivo; por tanto, la línea central representa el objetivo en ambos gráficos y una misma distancia vertical siempre equivale al mismo desvío de sonoridad. Los valores fuera del intervalo permanecen en el borde superior o inferior. Así, la variación de las fuentes se compara directamente con la agrupación de las salidas uniformizadas. El gráfico queda inactivo sin control de calidad.",
        "version_changes": "• Antes y Después comparten ahora la misma escala fija de ±6 LU alrededor del objetivo, sin reajuste automático.\n• La línea central representa el objetivo en ambos gráficos, por lo que la variación previa y la estabilidad posterior son directamente comparables.\n• Los valores fuera del intervalo permanecen visibles en el borde.\n• La copia sin recodificación sigue en ±0,10 LU y la tolerancia final de calidad en ±0,60 LU.",
    },
    "it": {
        "loudness_comparison_help_text": "Ogni punto è la misura integrata di un file elaborato. Prima e Dopo usano esattamente la stessa scala verticale fissa di ±6 LU attorno all’obiettivo; la linea centrale rappresenta quindi l’obiettivo in entrambi i grafici e la stessa distanza verticale indica sempre lo stesso scarto di sonorità. I valori fuori intervallo restano bloccati sul bordo superiore o inferiore. La variazione delle sorgenti è così direttamente confrontabile con il raggruppamento delle uscite uniformate. Il grafico resta inattivo senza controllo qualità.",
        "version_changes": "• Prima e Dopo condividono ora la stessa scala fissa di ±6 LU attorno all’obiettivo, senza ridimensionamento automatico.\n• La linea centrale rappresenta l’obiettivo in entrambi i grafici: variazione iniziale e stabilità finale sono direttamente confrontabili.\n• I valori fuori intervallo restano visibili sul bordo.\n• La copia senza ricodifica resta a ±0,10 LU e la tolleranza finale di qualità a ±0,60 LU.",
    },
    "pt": {
        "loudness_comparison_help_text": "Cada ponto é a medição integrada de um ficheiro processado. Antes e Depois usam exatamente a mesma escala vertical fixa de ±6 LU em torno do alvo; a linha central representa o alvo nos dois gráficos e a mesma distância vertical corresponde sempre ao mesmo desvio de sonoridade. Os valores fora desta faixa ficam presos ao bordo superior ou inferior. A variação das origens pode assim ser comparada diretamente com o agrupamento das saídas uniformizadas. O gráfico fica inativo sem controlo de qualidade.",
        "version_changes": "• Antes e Depois partilham agora a mesma escala fixa de ±6 LU em torno do alvo, sem reajuste automático.\n• A linha central representa o alvo nos dois gráficos, tornando diretamente comparáveis a variação inicial e a estabilidade final.\n• Os valores fora da faixa permanecem visíveis no bordo.\n• A cópia sem recodificação mantém ±0,10 LU e a tolerância final de qualidade mantém ±0,60 LU.",
    },
    "ru": {
        "loudness_comparison_help_text": "Каждая точка — интегральное измерение одного обработанного файла. Графики «До» и «После» используют одну и ту же фиксированную вертикальную шкалу ±6 LU относительно цели; средняя линия означает цель на обоих графиках, а одинаковое расстояние по вертикали всегда соответствует одинаковому отклонению громкости. Значения за пределами диапазона остаются у верхнего или нижнего края. Поэтому разброс источников можно напрямую сравнить с группировкой результатов после выравнивания. Без контроля качества график неактивен.",
        "version_changes": "• Графики «До» и «После» теперь используют одинаковую фиксированную шкалу ±6 LU относительно цели без автоматического изменения масштаба.\n• Средняя линия означает цель на обоих графиках, поэтому начальный разброс и итоговая стабильность напрямую сопоставимы.\n• Значения вне диапазона остаются видимыми у края.\n• Порог копирования без перекодирования остаётся ±0,10 LU, а итоговый допуск контроля качества — ±0,60 LU.",
    },
    "ja": {
        "loudness_comparison_help_text": "各点は処理した1ファイルの統合測定値です。処理前と処理後は、目標値を中心とする同じ固定縦軸±6 LUを使用します。そのため、両方の中央線が目標値を表し、同じ縦距離は常に同じラウドネス偏差を意味します。範囲外の値は上端または下端に固定して表示します。これにより、元ファイルのばらつきと均一化後の出力のまとまりを直接比較できます。品質管理を無効にするとグラフは動作しません。",
        "version_changes": "• 処理前と処理後は、目標値を中心とする同じ固定縦軸±6 LUを使用し、自動的に目盛りを変更しません。\n• 両グラフの中央線が目標値を表すため、処理前のばらつきと処理後の安定性を直接比較できます。\n• 範囲外の値はグラフ端に表示されます。\n• 無変換コピーの条件は±0.10 LU、最終品質管理の許容差は±0.60 LUのままです。",
    },
    "hi": {
        "loudness_comparison_help_text": "हर बिंदु एक प्रोसेस की गई फ़ाइल का एकीकृत माप है। पहले और बाद, लक्ष्य के आसपास ठीक वही स्थिर ±6 LU ऊर्ध्वाधर पैमाना उपयोग करते हैं; इसलिए दोनों ग्राफ़ की बीच वाली रेखा लक्ष्य है और समान ऊर्ध्व दूरी हमेशा समान loudness अंतर दिखाती है। सीमा से बाहर के मान ऊपर या नीचे के किनारे पर टिके रहते हैं। इससे स्रोतों के बदलाव की तुलना uniform किए गए outputs के समूह से सीधे की जा सकती है। गुणवत्ता नियंत्रण के बिना ग्राफ़ निष्क्रिय रहता है।",
        "version_changes": "• पहले और बाद अब लक्ष्य के आसपास एक ही स्थिर ±6 LU पैमाना उपयोग करते हैं; कोई स्वचालित rescaling नहीं होता।\n• दोनों ग्राफ़ की बीच वाली रेखा लक्ष्य है, इसलिए processing से पहले का बदलाव और बाद की स्थिरता सीधे तुलना योग्य हैं।\n• सीमा से बाहर के मान ग्राफ़ के किनारे पर दिखते रहते हैं।\n• बिना re-encoding copy की सीमा ±0.10 LU और अंतिम quality-control tolerance ±0.60 LU रहती है।",
    },
    "zh": {
        "loudness_comparison_help_text": "每个点都是一个已处理文件的综合测量值。处理前和处理后使用以目标值为中心、完全相同的固定垂直刻度±6 LU；因此两个图的中线都代表目标，相同的垂直距离始终表示相同的响度偏差。超出范围的值会固定显示在上边缘或下边缘。这样可以直接比较源文件的波动与均一化后输出的集中程度。关闭质量控制后图表不工作。",
        "version_changes": "• 处理前和处理后现在使用以目标为中心、完全相同的固定±6 LU刻度，不再自动缩放。\n• 两个图的中线都代表目标，因此处理前的波动和处理后的稳定性可以直接比较。\n• 超出范围的值仍显示在图表边缘。\n• 不重新编码的复制阈值仍为±0.10 LU，最终质量控制容差仍为±0.60 LU。",
    },
    "ko": {
        "loudness_comparison_help_text": "각 점은 처리된 파일 하나의 통합 측정값입니다. 처리 전과 처리 후는 목표값을 중심으로 한 동일한 고정 세로 눈금 ±6 LU를 사용합니다. 따라서 두 그래프의 중앙선은 모두 목표를 나타내고, 같은 세로 거리는 언제나 같은 라우드니스 편차를 뜻합니다. 범위를 벗어난 값은 위쪽 또는 아래쪽 가장자리에 고정해 표시합니다. 원본의 변동과 균일화된 출력의 밀집도를 직접 비교할 수 있습니다. 품질 관리를 끄면 그래프가 작동하지 않습니다.",
        "version_changes": "• 처리 전과 처리 후는 목표를 중심으로 한 동일한 고정 ±6 LU 눈금을 사용하며 자동으로 다시 조정되지 않습니다.\n• 두 그래프의 중앙선이 목표이므로 처리 전 변동과 처리 후 안정성을 직접 비교할 수 있습니다.\n• 범위를 벗어난 값은 그래프 가장자리에 표시됩니다.\n• 재인코딩 없는 복사 기준은 ±0.10 LU, 최종 품질 관리 허용치는 ±0.60 LU로 유지됩니다.",
    },
    "id": {
        "loudness_comparison_help_text": "Setiap titik adalah pengukuran terintegrasi dari satu berkas yang diproses. Sebelum dan Sesudah memakai skala vertikal tetap yang sama, yaitu ±6 LU di sekitar target; garis tengah pada kedua grafik berarti target dan jarak vertikal yang sama selalu berarti penyimpangan kenyaringan yang sama. Nilai di luar rentang tetap ditampilkan pada tepi atas atau bawah. Variasi sumber dapat langsung dibandingkan dengan pengelompokan keluaran setelah penyeragaman. Grafik tidak aktif tanpa kontrol mutu.",
        "version_changes": "• Sebelum dan Sesudah kini memakai skala tetap ±6 LU yang sama di sekitar target, tanpa penskalaan ulang otomatis.\n• Garis tengah adalah target pada kedua grafik sehingga variasi awal dan kestabilan akhir dapat dibandingkan langsung.\n• Nilai di luar rentang tetap terlihat pada tepi grafik.\n• Batas salin tanpa enkode ulang tetap ±0,10 LU dan toleransi akhir kontrol mutu tetap ±0,60 LU.",
    },
    "tr": {
        "loudness_comparison_help_text": "Her nokta işlenmiş bir dosyanın tümleşik ölçümüdür. Önce ve Sonra, hedefin çevresinde tamamen aynı sabit ±6 LU dikey ölçeği kullanır; bu nedenle iki grafikteki orta çizgi de hedefi gösterir ve aynı dikey uzaklık her zaman aynı ses yüksekliği sapması anlamına gelir. Aralık dışındaki değerler üst veya alt kenarda sabitlenir. Kaynaklardaki değişim, dengelenmiş çıktıların kümelenmesiyle doğrudan karşılaştırılabilir. Kalite kontrolü olmadan grafik etkin değildir.",
        "version_changes": "• Önce ve Sonra artık hedefin çevresinde aynı sabit ±6 LU ölçeği kullanır; otomatik yeniden ölçekleme yoktur.\n• İki grafikte de orta çizgi hedeftir; işlem öncesi değişim ile işlem sonrası kararlılık doğrudan karşılaştırılabilir.\n• Aralık dışındaki değerler grafik kenarında görünür kalır.\n• Yeniden kodlamadan kopyalama sınırı ±0,10 LU, son kalite kontrol toleransı ±0,60 LU olarak kalır.",
    },
}


__all__ = ["TRANSLATION_UPDATES_12414"]
