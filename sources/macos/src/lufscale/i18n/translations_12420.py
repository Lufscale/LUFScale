"""Analyse explicite et géométrie du panneau de sonie pour LUFScale 1.24.20."""

from __future__ import annotations


TRANSLATION_UPDATES_12420: dict[str, dict[str, str]] = {
    "fr": {
        "analysis_measurement_progress": "Analyse {current}/{total} — {file} — {value}",
        "analyze_only_fresh_help_text": "En mode Analyser seulement, chaque lancement effectue une nouvelle mesure FFmpeg de tous les fichiers. Le cache créé par une uniformisation précédente n’est pas réutilisé.",
        "analysis_progress_help_text": "En mode Analyser seulement, le graphique Avant, le journal et la barre de progression avancent fichier par fichier dès qu’une mesure est terminée ; Après reste immobile.",
        "version_changes": "• L’en-tête du journal revient à sa hauteur précédente de 32 px.\n• Les marges supérieure et inférieure des graphiques et leur séparation utilisent toutes 8 px.\n• Analyser seulement relance systématiquement FFmpeg sans réutiliser le cache d’une uniformisation précédente.\n• Le graphique Avant, le journal et la barre progressent maintenant fichier par fichier pendant cette analyse.\n• Après reste immobile, puisqu’aucune sortie audio n’est créée.\n• Le cache reste disponible pour Uniformiser et ReplayGain.\n• Les calculs audio et les seuils sont inchangés.",
    },
    "en": {
        "analysis_measurement_progress": "Analysis {current}/{total} — {file} — {value}",
        "analyze_only_fresh_help_text": "In Analyze-only mode, every run performs a new FFmpeg measurement of every file. It does not reuse the cache created by an earlier normalization run.",
        "analysis_progress_help_text": "In Analyze-only mode, the Before graph, log, and progress bar advance file by file as each measurement finishes; After stays still.",
        "version_changes": "• The log header returns to its previous 32 px height.\n• The graph’s top margin, inter-graph gap, and bottom margin are all 8 px.\n• Analyze-only always runs FFmpeg again instead of reusing a previous normalization cache.\n• The Before graph, log, and progress bar now advance file by file during analysis.\n• After stays still because no audio output is created.\n• Caching remains available for Normalize and ReplayGain.\n• Audio calculations and thresholds are unchanged.",
    },
    "es": {
        "analysis_measurement_progress": "Análisis {current}/{total} — {file} — {value}",
        "analyze_only_fresh_help_text": "En Solo analizar, cada ejecución realiza una nueva medición FFmpeg de todos los archivos. No reutiliza la caché creada por una normalización anterior.",
        "analysis_progress_help_text": "En Solo analizar, el gráfico Antes, el registro y la barra avanzan archivo por archivo al terminar cada medición; Después permanece inmóvil.",
        "version_changes": "• El encabezado del registro vuelve a su altura anterior de 32 px.\n• El margen superior, la separación entre gráficos y el margen inferior son de 8 px.\n• Solo analizar siempre vuelve a ejecutar FFmpeg y no reutiliza la caché de una normalización anterior.\n• Antes, el registro y la barra avanzan ahora archivo por archivo durante el análisis.\n• Después permanece inmóvil porque no se crea audio.\n• La caché sigue disponible para Normalizar y ReplayGain.\n• Los cálculos y umbrales de audio no cambian.",
    },
    "it": {
        "analysis_measurement_progress": "Analisi {current}/{total} — {file} — {value}",
        "analyze_only_fresh_help_text": "In Solo analisi, ogni avvio esegue una nuova misura FFmpeg di tutti i file. Non riutilizza la cache creata da una normalizzazione precedente.",
        "analysis_progress_help_text": "In Solo analisi, il grafico Prima, il registro e la barra avanzano file per file al termine di ogni misura; Dopo resta fermo.",
        "version_changes": "• L’intestazione del registro torna all’altezza precedente di 32 px.\n• Margine superiore, separazione dei grafici e margine inferiore sono tutti di 8 px.\n• Solo analisi esegue sempre di nuovo FFmpeg senza riutilizzare la cache di una normalizzazione precedente.\n• Prima, registro e barra avanzano ora file per file durante l’analisi.\n• Dopo resta fermo perché non viene creato audio.\n• La cache resta disponibile per Normalizza e ReplayGain.\n• Calcoli e soglie audio sono invariati.",
    },
    "pt": {
        "analysis_measurement_progress": "Análise {current}/{total} — {file} — {value}",
        "analyze_only_fresh_help_text": "Em Apenas analisar, cada execução faz uma nova medição FFmpeg de todos os ficheiros. Não reutiliza a cache criada por uma uniformização anterior.",
        "analysis_progress_help_text": "Em Apenas analisar, o gráfico Antes, o registo e a barra avançam ficheiro a ficheiro após cada medição; Depois permanece imóvel.",
        "version_changes": "• O cabeçalho do registo volta à altura anterior de 32 px.\n• A margem superior, a separação dos gráficos e a margem inferior são todas de 8 px.\n• Apenas analisar volta sempre a executar FFmpeg e não reutiliza a cache de uma uniformização anterior.\n• Antes, o registo e a barra avançam agora ficheiro a ficheiro durante a análise.\n• Depois permanece imóvel porque não é criado áudio.\n• A cache continua disponível para Uniformizar e ReplayGain.\n• Os cálculos e limiares de áudio não mudam.",
    },
    "ru": {
        "analysis_measurement_progress": "Анализ {current}/{total} — {file} — {value}",
        "analyze_only_fresh_help_text": "В режиме анализа каждый запуск заново измеряет все файлы через FFmpeg. Кэш предыдущей нормализации не используется.",
        "analysis_progress_help_text": "При анализе график «До», журнал и индикатор выполнения обновляются после каждого файла; «После» остаётся неподвижным.",
        "version_changes": "• Заголовок журнала возвращён к прежней высоте 32 px.\n• Верхний отступ, промежуток между графиками и нижний отступ равны 8 px.\n• Анализ всегда заново запускает FFmpeg без кэша предыдущей нормализации.\n• График «До», журнал и индикатор теперь обновляются после каждого файла.\n• «После» остаётся неподвижным, поскольку аудиовыход не создаётся.\n• Кэш остаётся доступным для Нормализации и ReplayGain.\n• Аудиорасчёты и пороги не изменены.",
    },
    "ja": {
        "analysis_measurement_progress": "解析 {current}/{total} — {file} — {value}",
        "analyze_only_fresh_help_text": "解析のみでは、実行するたびに全ファイルをFFmpegで新しく測定します。以前のノーマライズで作成したキャッシュは再利用しません。",
        "analysis_progress_help_text": "解析のみでは、各測定の完了時に処理前グラフ、ログ、進行バーがファイル単位で進みます。処理後は動きません。",
        "version_changes": "• ログ見出しを以前の32 pxの高さに戻しました。\n• グラフ上部、グラフ間、下部の余白をすべて8 pxにしました。\n• 解析のみは以前のノーマライズキャッシュを使わず、毎回FFmpegを実行します。\n• 処理前グラフ、ログ、進行バーがファイルごとに更新されます。\n• 音声を出力しないため処理後は動きません。\n• ノーマライズとReplayGainではキャッシュを引き続き利用できます。\n• 音声計算としきい値は変更していません。",
    },
    "hi": {
        "analysis_measurement_progress": "विश्लेषण {current}/{total} — {file} — {value}",
        "analyze_only_fresh_help_text": "केवल विश्लेषण में हर run सभी files की नई FFmpeg measurement करता है। पिछली normalization की cache reuse नहीं होती।",
        "analysis_progress_help_text": "केवल विश्लेषण में हर measurement पूरी होने पर पहले graph, log और progress bar file-by-file आगे बढ़ते हैं; बाद स्थिर रहता है।",
        "version_changes": "• Log header पिछली 32 px height पर वापस है।\n• Graph का top margin, बीच का gap और bottom margin सभी 8 px हैं।\n• केवल विश्लेषण पिछली normalization cache के बिना हर बार FFmpeg चलाता है।\n• पहले graph, log और progress bar अब file-by-file update होते हैं।\n• Audio output न बनने के कारण बाद स्थिर रहता है।\n• Normalize और ReplayGain में cache उपलब्ध रहती है।\n• Audio calculations और thresholds unchanged हैं।",
    },
    "zh": {
        "analysis_measurement_progress": "分析 {current}/{total} — {file} — {value}",
        "analyze_only_fresh_help_text": "仅分析模式每次都会使用FFmpeg重新测量所有文件，不会复用先前标准化生成的缓存。",
        "analysis_progress_help_text": "仅分析时，每完成一个文件，处理前图表、日志和进度条都会更新；处理后图表保持不动。",
        "version_changes": "• 日志标题栏恢复到以前的32 px高度。\n• 图表顶部、图表之间和底部的间距均为8 px。\n• 仅分析每次都会重新运行FFmpeg，不复用先前标准化的缓存。\n• 处理前图表、日志和进度条现在逐文件更新。\n• 因为不创建音频输出，处理后图表保持不动。\n• 标准化和ReplayGain仍可使用缓存。\n• 音频计算和阈值未更改。",
    },
    "ko": {
        "analysis_measurement_progress": "분석 {current}/{total} — {file} — {value}",
        "analyze_only_fresh_help_text": "분석 전용은 실행할 때마다 모든 파일을 FFmpeg로 새로 측정하며 이전 정규화의 캐시를 재사용하지 않습니다.",
        "analysis_progress_help_text": "분석 전용에서는 각 측정이 끝날 때마다 처리 전 그래프, 로그, 진행률이 파일별로 갱신되고 처리 후는 움직이지 않습니다.",
        "version_changes": "• 로그 헤더를 이전 32 px 높이로 되돌렸습니다.\n• 그래프 위, 그래프 사이, 아래 간격을 모두 8 px로 맞췄습니다.\n• 분석 전용은 이전 정규화 캐시를 쓰지 않고 매번 FFmpeg를 실행합니다.\n• 처리 전 그래프, 로그, 진행률이 파일별로 갱신됩니다.\n• 오디오 출력을 만들지 않으므로 처리 후는 움직이지 않습니다.\n• 정규화와 ReplayGain에서는 캐시를 계속 사용할 수 있습니다.\n• 오디오 계산과 임계값은 변경하지 않았습니다.",
    },
    "id": {
        "analysis_measurement_progress": "Analisis {current}/{total} — {file} — {value}",
        "analyze_only_fresh_help_text": "Dalam Hanya analisis, setiap proses melakukan pengukuran FFmpeg baru untuk semua berkas. Cache dari normalisasi sebelumnya tidak digunakan kembali.",
        "analysis_progress_help_text": "Dalam Hanya analisis, grafik Sebelum, log, dan bilah progres bergerak per berkas setelah setiap pengukuran; Sesudah tetap diam.",
        "version_changes": "• Header log kembali ke tinggi sebelumnya, 32 px.\n• Margin atas, jarak antargrafik, dan margin bawah semuanya 8 px.\n• Hanya analisis selalu menjalankan FFmpeg lagi tanpa cache normalisasi sebelumnya.\n• Grafik Sebelum, log, dan bilah progres kini diperbarui per berkas.\n• Sesudah tetap diam karena tidak ada keluaran audio.\n• Cache tetap tersedia untuk Normalisasi dan ReplayGain.\n• Perhitungan audio dan ambang tidak berubah.",
    },
    "tr": {
        "analysis_measurement_progress": "Analiz {current}/{total} — {file} — {value}",
        "analyze_only_fresh_help_text": "Yalnızca analizde her çalıştırma tüm dosyaları FFmpeg ile yeniden ölçer. Önceki normalleştirmenin önbelleği kullanılmaz.",
        "analysis_progress_help_text": "Yalnızca analizde her ölçüm bittiğinde Önce grafiği, günlük ve ilerleme çubuğu dosya dosya ilerler; Sonra sabit kalır.",
        "version_changes": "• Günlük başlığı önceki 32 px yüksekliğine döndürüldü.\n• Grafik üst boşluğu, grafikler arası boşluk ve alt boşluk 8 px’tir.\n• Yalnızca analiz önceki normalleştirme önbelleğini kullanmadan FFmpeg’i her seferinde çalıştırır.\n• Önce grafiği, günlük ve ilerleme çubuğu artık dosya dosya güncellenir.\n• Ses çıkışı oluşturulmadığı için Sonra sabit kalır.\n• Önbellek Normalleştirme ve ReplayGain için kullanılabilir.\n• Ses hesapları ve eşikler değişmedi.",
    },
}


__all__ = ["TRANSLATION_UPDATES_12420"]
