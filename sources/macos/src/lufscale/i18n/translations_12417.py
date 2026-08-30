from __future__ import annotations


# Analyse-only graph feedback, explicit chart/QC scales, ReplayGain wording,
# and release notes for the 1.24.17 interface refinements.
TRANSLATION_UPDATES_12417: dict[str, dict[str, str]] = {
    "fr": {
        "loudness_comparison_analysis_only": "Aucune sortie en mode Analyser seulement",
        "loudness_comparison_scale": "Vue ±{scale} LU · tol. QC ±{tolerance} LU",
        "loudness_comparison_tooltip": "Chaque point représente la sonie intégrée d’un fichier. Avant et Après utilisent la même échelle fixe de ±6 LU autour de la cible ; la tolérance réelle du contrôle qualité est ±0,60 LU. En mode Analyser seulement, seul Avant se met à jour.",
        "loudness_comparison_help_text": "Chaque nouveau fichier ajoute un point à droite et fait glisser les mesures précédentes vers la gauche. Avant et Après utilisent exactement la même échelle verticale fixe de ±6 LU autour de la cible : il s’agit de l’étendue d’affichage, et non de la marge d’acceptation. La bande verte étroite d’Après représente la tolérance réelle du contrôle qualité, soit ±0,60 LU. Une source située hors de la vue reste bloquée au bord du graphique. En mode Uniformiser, Avant montre la sonie intégrée de la source et Après la sortie réellement remesurée. En mode Analyser seulement, Avant se met à jour dès que chaque fichier est mesuré et Après reste immobile, car aucun fichier de sortie n’est créé. Chaque point est une mesure intégrée par fichier, et non une mesure instantanée pendant la lecture.",
        "operation_tooltip": "Uniformiser modifie réellement les échantillons audio puis encode une sortie afin de la rapprocher de la cible dans tous les lecteurs. ReplayGain ne modifie pas les échantillons et ne réencode pas l’audio : il copie le flux et ajoute des balises de gain et de crête ; seul un lecteur compatible qui applique ces balises change le volume à la lecture. ReplayGain ne garantit donc ni un LUFS physique identique, ni le respect du plafond True Peak par modification du signal. Analyser seulement mesure les sources et simule les résultats sans créer de fichiers audio.",
        "version_changes": "• En mode Analyser seulement, le graphique Avant reçoit la mesure LUFS de chaque fichier dès qu’elle est disponible ; le graphique Après reste immobile puisqu’aucune sortie n’est créée.\n• Le libellé distingue maintenant l’échelle d’affichage fixe ±6 LU de la tolérance réelle du contrôle qualité ±0,60 LU ; cette tolérance est matérialisée par une bande étroite.\n• Les trois boutons de traitement et le panneau Évolution de la sonie sont légèrement abaissés ; le bas du panneau s’aligne sur celui du journal.\n• Le repère vert des onglets Audio et Options est supprimé. Le cadre actif reprend le rebord neutre et en retrait du journal de traitement.\n• L’aide précise ce que ReplayGain modifie, ce qu’il ne modifie pas et sa différence avec Uniformiser.\n• Le moteur audio et les seuils de traitement restent inchangés.",
    },
    "en": {
        "loudness_comparison_analysis_only": "No output in Analyze-only mode",
        "loudness_comparison_scale": "View ±{scale} LU · QC tol. ±{tolerance} LU",
        "loudness_comparison_tooltip": "Each point is one file’s integrated loudness. Before and After use the same fixed ±6 LU range around target; the actual quality-control tolerance is ±0.60 LU. In Analyze-only mode, only Before updates.",
        "loudness_comparison_help_text": "Each new file adds a point on the right and moves previous measurements left. Before and After use exactly the same fixed vertical range of ±6 LU around the target: this is the display range, not the acceptance margin. The narrow green band in After represents the actual quality-control tolerance of ±0.60 LU. A source outside the view remains pinned to the graph edge. In Normalize mode, Before shows the source’s integrated loudness and After the remeasured output. In Analyze-only mode, Before updates as soon as each file is measured and After stays still because no output file is created. Each point is one integrated measurement per file, not an instantaneous playback reading.",
        "operation_tooltip": "Normalize changes the audio samples and encodes an output so it approaches the target in every player. ReplayGain does not change samples or re-encode audio: it copies the stream and adds gain and peak tags; playback volume changes only in a compatible player that applies those tags. ReplayGain therefore does not guarantee physically identical LUFS or enforce the True Peak ceiling by modifying the signal. Analyze-only measures sources and simulates results without creating audio files.",
        "version_changes": "• In Analyze-only mode, the Before graph receives each file’s LUFS measurement as soon as it is available; After stays still because no output is created.\n• The label now distinguishes the fixed ±6 LU display range from the actual ±0.60 LU quality-control tolerance, which is shown as a narrow band.\n• The three processing buttons and Loudness change panel are lowered slightly; the panel bottom aligns with the journal.\n• The green Audio/Options tab marker is removed. The active frame now uses the journal’s neutral recessed edge.\n• Help now states what ReplayGain changes, what it does not change, and how it differs from Normalize.\n• The audio engine and processing thresholds are unchanged.",
    },
    "es": {
        "loudness_comparison_analysis_only": "Sin salida en el modo Solo analizar",
        "loudness_comparison_scale": "Vista ±{scale} LU · tol. QC ±{tolerance} LU",
        "loudness_comparison_tooltip": "Cada punto es la sonoridad integrada de un archivo. Antes y Después usan la misma vista fija de ±6 LU; la tolerancia real de calidad es ±0,60 LU. En Solo analizar, solo se actualiza Antes.",
        "loudness_comparison_help_text": "Cada archivo añade un punto a la derecha y desplaza los anteriores a la izquierda. Antes y Después comparten exactamente la misma escala vertical fija de ±6 LU alrededor del objetivo: es el rango visual, no la tolerancia. La banda verde estrecha de Después muestra la tolerancia real del control de calidad, ±0,60 LU. En Normalizar se muestran la fuente y la salida medida de nuevo. En Solo analizar, Antes se actualiza al medir cada archivo y Después permanece inmóvil porque no se crea ninguna salida. Cada punto es una medición integrada por archivo.",
        "operation_tooltip": "Normalizar modifica las muestras y codifica una salida cercana al objetivo en todos los reproductores. ReplayGain no modifica las muestras ni recodifica: copia el flujo y añade etiquetas de ganancia y pico, que solo aplica un reproductor compatible. No garantiza LUFS físicos idénticos ni impone el límite True Peak modificando la señal. Solo analizar mide y simula sin crear audio.",
        "version_changes": "• Solo analizar actualiza Antes con cada LUFS y deja Después inmóvil.\n• La interfaz distingue la vista fija ±6 LU de la tolerancia de calidad ±0,60 LU y muestra esta última como una banda.\n• Los botones y el panel de sonoridad bajan ligeramente; su borde inferior se alinea con el registro.\n• Se elimina la marca verde de las pestañas y el marco activo adopta el reborde neutro del registro.\n• La ayuda aclara ReplayGain frente a Normalizar.\n• El motor de audio y los umbrales no cambian.",
    },
    "it": {
        "loudness_comparison_analysis_only": "Nessuna uscita in modalità Solo analisi",
        "loudness_comparison_scale": "Vista ±{scale} LU · toll. QC ±{tolerance} LU",
        "loudness_comparison_tooltip": "Ogni punto è la sonorità integrata di un file. Prima e Dopo usano la stessa vista fissa ±6 LU; la tolleranza QC reale è ±0,60 LU. In Solo analisi si aggiorna solo Prima.",
        "loudness_comparison_help_text": "Ogni file aggiunge un punto a destra e sposta i precedenti a sinistra. Prima e Dopo condividono la stessa scala verticale fissa ±6 LU attorno all’obiettivo: è l’intervallo visivo, non la tolleranza. La stretta banda verde in Dopo mostra la tolleranza QC reale di ±0,60 LU. Con Normalizza si vedono sorgente e uscita rimisurata. Con Solo analisi, Prima si aggiorna a ogni misura e Dopo resta fermo perché non viene creata un’uscita. Ogni punto è una misura integrata per file.",
        "operation_tooltip": "Normalizza modifica i campioni e codifica un’uscita vicina all’obiettivo in ogni lettore. ReplayGain non modifica i campioni e non ricodifica: copia il flusso e aggiunge tag di guadagno e picco, applicati solo da lettori compatibili. Non garantisce LUFS fisicamente identici né impone il limite True Peak modificando il segnale. Solo analisi misura e simula senza creare audio.",
        "version_changes": "• Solo analisi aggiorna Prima con ogni misura LUFS e lascia Dopo fermo.\n• L’interfaccia distingue la vista fissa ±6 LU dalla tolleranza QC ±0,60 LU, mostrata come banda.\n• Pulsanti e pannello sonorità sono leggermente abbassati e il fondo si allinea al registro.\n• Il segno verde delle schede è rimosso; la cornice attiva riprende il bordo neutro del registro.\n• La guida chiarisce ReplayGain rispetto a Normalizza.\n• Motore audio e soglie non cambiano.",
    },
    "pt": {
        "loudness_comparison_analysis_only": "Sem saída no modo Apenas analisar",
        "loudness_comparison_scale": "Vista ±{scale} LU · tol. QC ±{tolerance} LU",
        "loudness_comparison_tooltip": "Cada ponto é a sonoridade integrada de um ficheiro. Antes e Depois usam a mesma vista fixa ±6 LU; a tolerância QC real é ±0,60 LU. Em Apenas analisar, só Antes é atualizado.",
        "loudness_comparison_help_text": "Cada ficheiro acrescenta um ponto à direita e desloca os anteriores para a esquerda. Antes e Depois partilham a mesma escala vertical fixa ±6 LU em torno do alvo: é a faixa visual, não a tolerância. A faixa verde estreita em Depois mostra a tolerância QC real de ±0,60 LU. Em Uniformizar veem-se a origem e a saída novamente medida. Em Apenas analisar, Antes é atualizado após cada medição e Depois fica imóvel porque não é criada uma saída. Cada ponto é uma medição integrada por ficheiro.",
        "operation_tooltip": "Uniformizar altera as amostras e codifica uma saída próxima do alvo em todos os leitores. ReplayGain não altera amostras nem recodifica: copia o fluxo e adiciona etiquetas de ganho e pico, aplicadas apenas por leitores compatíveis. Não garante LUFS físicos idênticos nem impõe o teto True Peak ao sinal. Apenas analisar mede e simula sem criar áudio.",
        "version_changes": "• Apenas analisar atualiza Antes com cada LUFS e mantém Depois imóvel.\n• A interface distingue a vista fixa ±6 LU da tolerância QC ±0,60 LU, apresentada como faixa.\n• Os botões e o painel de sonoridade descem ligeiramente; o fundo alinha-se com o registo.\n• A marca verde dos separadores é removida e a moldura ativa usa o rebordo neutro do registo.\n• A ajuda esclarece ReplayGain face a Uniformizar.\n• O motor áudio e os limites não mudam.",
    },
    "ru": {
        "loudness_comparison_analysis_only": "В режиме анализа выходной файл не создаётся",
        "loudness_comparison_scale": "Шкала ±{scale} LU · допуск QC ±{tolerance} LU",
        "loudness_comparison_tooltip": "Каждая точка — интегральная громкость файла. Оба графика имеют одинаковый фиксированный диапазон ±6 LU; реальный допуск QC — ±0,60 LU. В режиме анализа обновляется только «До».",
        "loudness_comparison_help_text": "Каждый файл добавляет точку справа и сдвигает предыдущие влево. Оба графика используют одинаковую фиксированную шкалу ±6 LU относительно цели: это диапазон отображения, а не допуск. Узкая зелёная полоса «После» показывает реальный допуск QC ±0,60 LU. При нормализации показаны источник и повторно измеренный результат. При одном анализе обновляется только «До», а «После» остаётся неподвижным, поскольку выходной файл не создаётся. Каждая точка — интегральное измерение файла.",
        "operation_tooltip": "Нормализация изменяет аудиосэмплы и кодирует результат, близкий к цели в любом проигрывателе. ReplayGain не изменяет сэмплы и не перекодирует звук: он копирует поток и добавляет теги усиления и пика, которые применяет только совместимый проигрыватель. Он не гарантирует физически одинаковые LUFS и не ограничивает True Peak изменением сигнала. Анализ измеряет и моделирует без создания аудио.",
        "version_changes": "• В режиме анализа график «До» обновляется для каждого файла, а «После» не движется.\n• Диапазон отображения ±6 LU теперь явно отделён от допуска QC ±0,60 LU, показанного полосой.\n• Кнопки и панель громкости немного опущены; низ панели выровнен с журналом.\n• Зелёная метка вкладок удалена; активная рамка повторяет нейтральный край журнала.\n• Справка уточняет отличие ReplayGain от нормализации.\n• Аудиодвижок и пороги не изменены.",
    },
    "ja": {
        "loudness_comparison_analysis_only": "解析のみでは出力を作成しません",
        "loudness_comparison_scale": "表示 ±{scale} LU・QC許容 ±{tolerance} LU",
        "loudness_comparison_tooltip": "各点は1ファイルの統合ラウドネスです。処理前後は同じ固定表示範囲±6 LUを使い、実際のQC許容差は±0.60 LUです。解析のみでは処理前だけ更新します。",
        "loudness_comparison_help_text": "ファイルごとに右へ点を追加し、以前の点を左へ送ります。処理前と処理後は目標を中心とする同じ固定縦軸±6 LUを使います。これは表示範囲で、許容差ではありません。処理後の細い緑帯が実際のQC許容差±0.60 LUです。ノーマライズでは元音源と再測定した出力を表示します。解析のみでは測定のたびに処理前を更新し、出力を作らないため処理後は動きません。各点はファイル単位の統合測定値です。",
        "operation_tooltip": "ノーマライズは音声サンプルを変更し、どのプレーヤーでも目標に近い出力をエンコードします。ReplayGainはサンプルを変更・再エンコードせず、ストリームをコピーしてゲインとピークのタグを追加します。音量が変わるのは対応プレーヤーがタグを適用した場合だけです。物理的に同じLUFSや信号変更によるTrue Peak制限は保証しません。解析のみは音声を作らず測定・予測します。",
        "version_changes": "• 解析のみでは各LUFSを処理前へ表示し、処理後は動きません。\n• 固定表示範囲±6 LUとQC許容差±0.60 LUを区別し、許容帯を表示します。\n• ボタンとラウドネスパネルを少し下げ、下端をログに揃えました。\n• タブの緑印を削除し、選択枠をログと同じ中立的な縁にしました。\n• ReplayGainとノーマライズの違いをヘルプに明記しました。\n• 音声処理としきい値は変更していません。",
    },
    "hi": {
        "loudness_comparison_analysis_only": "केवल विश्लेषण में कोई आउटपुट नहीं",
        "loudness_comparison_scale": "दृश्य ±{scale} LU · QC सीमा ±{tolerance} LU",
        "loudness_comparison_tooltip": "हर बिंदु एक फ़ाइल की integrated loudness है। पहले और बाद एक ही स्थिर ±6 LU दृश्य रखते हैं; वास्तविक QC tolerance ±0.60 LU है। केवल विश्लेषण में सिर्फ पहले अपडेट होता है।",
        "loudness_comparison_help_text": "हर फ़ाइल दाईं ओर बिंदु जोड़ती है और पुराने बिंदु बाईं ओर खिसकते हैं। पहले और बाद लक्ष्य के आसपास एक ही स्थिर ±6 LU पैमाना उपयोग करते हैं; यह display range है, tolerance नहीं। बाद में पतली हरी पट्टी वास्तविक QC tolerance ±0.60 LU दिखाती है। Normalize में source और दोबारा मापा output दिखता है। केवल विश्लेषण में हर माप पर पहले अपडेट होता है और output न बनने के कारण बाद स्थिर रहता है। हर बिंदु प्रति फ़ाइल integrated माप है।",
        "operation_tooltip": "Normalize audio samples बदलकर हर player में लक्ष्य के पास output encode करता है। ReplayGain samples नहीं बदलता और re-encode नहीं करता; वह stream copy करके gain व peak tags जोड़ता है, जिन्हें केवल compatible player लागू करता है। इसलिए वह समान physical LUFS या signal बदलकर True Peak सीमा की गारंटी नहीं देता। केवल विश्लेषण बिना audio बनाए माप और अनुमान करता है।",
        "version_changes": "• केवल विश्लेषण हर फ़ाइल का LUFS पहले में दिखाता है और बाद को स्थिर रखता है।\n• स्थिर ±6 LU दृश्य और वास्तविक ±0.60 LU QC tolerance अलग दिखाए गए हैं।\n• बटन व loudness panel थोड़ा नीचे और journal के नीचे से aligned हैं।\n• tabs की हरी पट्टी हटाकर journal जैसा neutral border लगाया गया है।\n• Help ReplayGain और Normalize का अंतर स्पष्ट करती है।\n• Audio engine और thresholds नहीं बदले हैं।",
    },
    "zh": {
        "loudness_comparison_analysis_only": "仅分析模式不生成输出",
        "loudness_comparison_scale": "显示 ±{scale} LU · QC容差 ±{tolerance} LU",
        "loudness_comparison_tooltip": "每个点是一个文件的综合响度。处理前后使用相同的固定±6 LU显示范围；实际质检容差为±0.60 LU。仅分析时只更新处理前。",
        "loudness_comparison_help_text": "每个文件在右侧增加一个点，旧点向左移动。处理前和处理后使用以目标为中心的相同固定±6 LU纵轴；这是显示范围，不是容差。处理后图中的窄绿色带表示实际质检容差±0.60 LU。标准化时显示源文件和复测输出；仅分析时每完成一个文件测量就更新处理前，而处理后保持不动，因为不会创建输出文件。每个点都是单个文件的综合测量。",
        "operation_tooltip": "标准化会改变音频采样并编码输出，使其在所有播放器中接近目标。ReplayGain不改变采样也不重新编码；它复制音频流并添加增益和峰值标签，只有兼容播放器应用标签时播放音量才变化。因此它不保证物理LUFS完全一致，也不会通过修改信号来执行True Peak上限。仅分析只测量和模拟，不创建音频。",
        "version_changes": "• 仅分析时，处理前图逐个显示文件LUFS，处理后图保持不动。\n• 明确区分固定±6 LU显示范围和实际±0.60 LU质检容差，并以窄带显示容差。\n• 处理按钮和响度面板略微下移，面板底部与日志对齐。\n• 移除标签页绿色标记，活动边框改为日志式中性内凹边缘。\n• 帮助说明ReplayGain与标准化的区别。\n• 音频引擎和阈值未更改。",
    },
    "ko": {
        "loudness_comparison_analysis_only": "분석 전용 모드에서는 출력 없음",
        "loudness_comparison_scale": "보기 ±{scale} LU · QC 허용 ±{tolerance} LU",
        "loudness_comparison_tooltip": "각 점은 파일 하나의 통합 라우드니스입니다. 처리 전후는 같은 고정 ±6 LU 표시 범위를 쓰며 실제 QC 허용치는 ±0.60 LU입니다. 분석 전용에서는 처리 전만 갱신됩니다.",
        "loudness_comparison_help_text": "파일마다 오른쪽에 점을 추가하고 이전 점을 왼쪽으로 이동합니다. 처리 전과 처리 후는 목표 중심의 동일한 고정 ±6 LU 세로 범위를 사용합니다. 이는 표시 범위이며 허용치가 아닙니다. 처리 후의 좁은 녹색 띠가 실제 QC 허용치 ±0.60 LU입니다. 정규화에서는 원본과 재측정한 출력을 표시합니다. 분석 전용에서는 파일 측정 때마다 처리 전을 갱신하고 출력 파일이 없으므로 처리 후는 움직이지 않습니다. 각 점은 파일 단위의 통합 측정입니다.",
        "operation_tooltip": "정규화는 오디오 샘플을 변경하고 모든 플레이어에서 목표에 가까운 출력을 인코딩합니다. ReplayGain은 샘플을 바꾸거나 재인코딩하지 않고 스트림을 복사해 게인과 피크 태그를 추가합니다. 호환 플레이어가 태그를 적용할 때만 재생 음량이 바뀝니다. 따라서 물리적으로 같은 LUFS나 신호 변경에 의한 True Peak 제한을 보장하지 않습니다. 분석 전용은 오디오를 만들지 않고 측정·예측합니다.",
        "version_changes": "• 분석 전용에서 각 LUFS를 처리 전에 표시하고 처리 후는 고정합니다.\n• 고정 ±6 LU 표시 범위와 실제 ±0.60 LU QC 허용치를 구분하고 허용 띠를 표시합니다.\n• 버튼과 패널을 조금 내리고 패널 아래를 로그와 맞췄습니다.\n• 탭의 녹색 표시를 없애고 로그와 같은 중립 테두리를 사용합니다.\n• ReplayGain과 정규화 차이를 도움말에 명시했습니다.\n• 오디오 엔진과 임계값은 변경하지 않았습니다.",
    },
    "id": {
        "loudness_comparison_analysis_only": "Tidak ada keluaran dalam Hanya analisis",
        "loudness_comparison_scale": "Tampilan ±{scale} LU · tol. QC ±{tolerance} LU",
        "loudness_comparison_tooltip": "Setiap titik adalah kenyaringan terintegrasi satu berkas. Sebelum dan Sesudah memakai tampilan tetap ±6 LU yang sama; toleransi QC sebenarnya ±0,60 LU. Dalam Hanya analisis, hanya Sebelum yang diperbarui.",
        "loudness_comparison_help_text": "Setiap berkas menambah titik di kanan dan menggeser titik lama ke kiri. Sebelum dan Sesudah memakai skala vertikal tetap ±6 LU yang sama di sekitar target; ini rentang tampilan, bukan toleransi. Pita hijau sempit pada Sesudah menunjukkan toleransi QC sebenarnya ±0,60 LU. Normalisasi menampilkan sumber dan keluaran yang diukur ulang. Hanya analisis memperbarui Sebelum pada setiap pengukuran dan membiarkan Sesudah diam karena tidak membuat keluaran. Setiap titik adalah pengukuran terintegrasi per berkas.",
        "operation_tooltip": "Normalisasi mengubah sampel dan mengodekan keluaran yang mendekati target di semua pemutar. ReplayGain tidak mengubah sampel atau mengodekan ulang; ia menyalin stream dan menambah tag gain serta peak, yang hanya diterapkan pemutar kompatibel. Ia tidak menjamin LUFS fisik identik atau menerapkan batas True Peak dengan mengubah sinyal. Hanya analisis mengukur dan menyimulasikan tanpa membuat audio.",
        "version_changes": "• Hanya analisis memperbarui Sebelum dengan setiap LUFS dan membiarkan Sesudah diam.\n• Tampilan tetap ±6 LU dibedakan dari toleransi QC ±0,60 LU yang ditampilkan sebagai pita.\n• Tombol dan panel diturunkan sedikit; bagian bawah panel sejajar dengan log.\n• Tanda hijau tab dihapus dan bingkai aktif memakai tepi netral log.\n• Bantuan menjelaskan ReplayGain dibanding Normalisasi.\n• Mesin audio dan ambang tidak berubah.",
    },
    "tr": {
        "loudness_comparison_analysis_only": "Yalnızca analiz modunda çıkış yok",
        "loudness_comparison_scale": "Görünüm ±{scale} LU · QC tol. ±{tolerance} LU",
        "loudness_comparison_tooltip": "Her nokta bir dosyanın tümleşik ses yüksekliğidir. Önce ve Sonra aynı sabit ±6 LU görünümü kullanır; gerçek QC toleransı ±0,60 LU’dur. Yalnızca analizde sadece Önce güncellenir.",
        "loudness_comparison_help_text": "Her dosya sağa bir nokta ekler ve eskileri sola kaydırır. Önce ve Sonra hedef çevresinde aynı sabit ±6 LU dikey ölçeği kullanır; bu görüntü aralığıdır, tolerans değildir. Sonra’daki dar yeşil bant gerçek QC toleransı ±0,60 LU’yu gösterir. Normalleştirmede kaynak ve yeniden ölçülen çıkış gösterilir. Yalnızca analizde her ölçümle Önce güncellenir, çıkış oluşturulmadığı için Sonra hareket etmez. Her nokta dosya başına tümleşik ölçümdür.",
        "operation_tooltip": "Normalleştirme ses örneklerini değiştirir ve her oynatıcıda hedefe yakın bir çıkış kodlar. ReplayGain örnekleri değiştirmez ve yeniden kodlamaz; akışı kopyalayıp gain ve peak etiketleri ekler, ses yalnızca uyumlu oynatıcı bu etiketleri uyguladığında değişir. Fiziksel olarak aynı LUFS’u veya sinyali değiştirerek True Peak sınırını garanti etmez. Yalnızca analiz ses oluşturmadan ölçer ve simüle eder.",
        "version_changes": "• Yalnızca analiz her dosyanın LUFS’unu Önce’ye ekler, Sonra’yı sabit tutar.\n• Sabit ±6 LU görüntü ile gerçek ±0,60 LU QC toleransı ayrılır ve tolerans bantla gösterilir.\n• Düğmeler ve panel biraz indirilmiş, panel altı günlükle hizalanmıştır.\n• Sekmelerdeki yeşil işaret kaldırılmış, etkin çerçeve günlükteki nötr kenarı kullanmıştır.\n• Yardım ReplayGain ile Normalleştirme farkını açıklar.\n• Ses motoru ve eşikler değişmemiştir.",
    },
}


_REPLAYGAIN_HELP_12417 = {
    "fr": "ReplayGain copie le flux audio sans modifier les échantillons et ajoute des balises de gain et de crête. Seul un lecteur compatible les applique. Il ne normalise donc pas physiquement le signal et n’impose pas le plafond True Peak.",
    "en": "ReplayGain copies the audio stream without changing samples and adds gain and peak tags. Only a compatible player applies them. It therefore does not physically normalize the signal or enforce the True Peak ceiling.",
    "es": "ReplayGain copia el flujo sin modificar las muestras y añade etiquetas de ganancia y pico. Solo las aplica un reproductor compatible. No normaliza físicamente la señal ni impone el límite True Peak.",
    "it": "ReplayGain copia il flusso senza modificare i campioni e aggiunge tag di guadagno e picco. Solo un lettore compatibile li applica. Non normalizza fisicamente il segnale né impone il limite True Peak.",
    "pt": "ReplayGain copia o fluxo sem alterar as amostras e adiciona etiquetas de ganho e pico. Só um leitor compatível as aplica. Não normaliza fisicamente o sinal nem impõe o teto True Peak.",
    "ru": "ReplayGain копирует поток без изменения сэмплов и добавляет теги усиления и пика. Их применяет только совместимый проигрыватель. Сигнал физически не нормализуется, а предел True Peak не задаётся.",
    "ja": "ReplayGainはサンプルを変更せずに音声ストリームをコピーし、ゲインとピークのタグを追加します。対応プレーヤーだけがタグを適用します。信号自体のノーマライズやTrue Peak制限は行いません。",
    "hi": "ReplayGain samples बदले बिना audio stream copy करके gain और peak tags जोड़ता है। केवल compatible player उन्हें लागू करता है। यह signal को physically normalize या True Peak सीमा लागू नहीं करता।",
    "zh": "ReplayGain复制音频流而不改变采样，并添加增益和峰值标签。只有兼容播放器会应用这些标签，因此它不会物理标准化信号，也不会执行True Peak上限。",
    "ko": "ReplayGain은 샘플을 바꾸지 않고 오디오 스트림을 복사해 게인과 피크 태그를 추가합니다. 호환 플레이어만 태그를 적용합니다. 신호 자체를 정규화하거나 True Peak 한계를 적용하지 않습니다.",
    "id": "ReplayGain menyalin stream tanpa mengubah sampel dan menambah tag gain serta peak. Hanya pemutar kompatibel yang menerapkannya. Sinyal tidak dinormalisasi secara fisik dan batas True Peak tidak diterapkan.",
    "tr": "ReplayGain örnekleri değiştirmeden ses akışını kopyalar ve gain ile peak etiketleri ekler. Bunları yalnızca uyumlu oynatıcı uygular. Sinyali fiziksel olarak normalleştirmez veya True Peak sınırını uygulamaz.",
}

for _language, _text in _REPLAYGAIN_HELP_12417.items():
    TRANSLATION_UPDATES_12417[_language]["replaygain_help_text"] = _text


__all__ = ["TRANSLATION_UPDATES_12417"]
