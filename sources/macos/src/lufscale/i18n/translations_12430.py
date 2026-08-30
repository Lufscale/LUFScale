"""Concise Track-versus-Album guidance for application help and PDFs."""

from __future__ import annotations


TRANSLATION_UPDATES_12430: dict[str, dict[str, str]] = {
    "fr": {
        "mode_tooltip": "Piste rapproche chaque fichier de la cible. Album règle le niveau global d’un dossier avec un gain commun : les écarts entre pistes sont conservés.",
        "album_analysis_help_text": "Choisissez Album pour préserver l’équilibre voulu entre passages calmes et puissants lorsque l’album est écouté comme un ensemble. Pour un niveau régulier fichier par fichier ou en lecture aléatoire, choisissez Piste. En Album, la crête maximale peut limiter le gain et la mesure globale nécessite un second parcours, dont l’avancement est affiché.",
        "guide_level_mode_body": "Piste rapproche chaque fichier de la cible. Album applique un gain commun au dossier et préserve les écarts entre passages calmes et puissants. Utilisez Album pour écouter l’album comme un ensemble ; Piste pour un niveau régulier fichier par fichier ou en lecture aléatoire.",
        "version_changes": "• L’aide Mode de niveau explique clairement que Piste uniformise fichier par fichier, tandis qu’Album ajuste l’ensemble avec un gain commun.\n• Le guide précise quand choisir Album ou Piste et rappelle que les écarts artistiques sont conservés.\n• Les douze langues partagent la même explication concise.\n• Le traitement audio et les calculs sont inchangés.",
    },
    "en": {
        "mode_tooltip": "Track brings each file toward target. Album adjusts a folder’s overall level with one shared gain, preserving differences between tracks.",
        "album_analysis_help_text": "Choose Album to preserve the intended balance between quiet and powerful passages when listening to the complete work. For a consistent file-to-file level or shuffle playback, choose Track. In Album mode, the true-peak limit may restrict gain and the global measurement requires a second pass whose progress is displayed.",
        "guide_level_mode_body": "Track brings each file toward target. Album applies one shared gain to the folder and preserves the intended contrast between quiet and powerful passages. Use Album for a complete work; Track for consistent file-to-file or shuffle playback.",
        "version_changes": "• Level-mode help now clearly distinguishes per-file Track normalization from shared-gain Album adjustment.\n• The guide explains when to choose each mode and that artistic differences are preserved.\n• All twelve languages share the same concise explanation.\n• Audio processing and calculations are unchanged.",
    },
    "es": {
        "mode_tooltip": "Pista acerca cada archivo al objetivo. Álbum ajusta el nivel global de la carpeta con una ganancia común y conserva las diferencias entre pistas.",
        "album_analysis_help_text": "Elija Álbum para conservar el equilibrio entre pasajes tranquilos y potentes al escuchar la obra completa. Para un nivel regular entre archivos o reproducción aleatoria, elija Pista. La cresta máxima puede limitar la ganancia y la medición global necesita una segunda pasada cuyo progreso se muestra.",
        "guide_level_mode_body": "Pista acerca cada archivo al objetivo. Álbum aplica una ganancia común y conserva los contrastes. Use Álbum para una obra completa; Pista para un nivel regular entre archivos o reproducción aleatoria.",
        "version_changes": "• La ayuda distingue claramente Pista y Álbum.\n• La guía explica cuándo usar cada modo.\n• Las doce lenguas comparten la explicación.\n• El procesamiento no cambia.",
    },
    "it": {
        "mode_tooltip": "Traccia avvicina ogni file all’obiettivo. Album regola il livello globale della cartella con un guadagno comune, conservando le differenze fra tracce.",
        "album_analysis_help_text": "Scegliere Album per mantenere l’equilibrio fra passaggi calmi e potenti nell’ascolto completo. Per un livello regolare fra file o la riproduzione casuale, scegliere Traccia. Il limite di picco può ridurre il guadagno e la misura globale richiede una seconda passata, mostrata nell’avanzamento.",
        "guide_level_mode_body": "Traccia avvicina ogni file all’obiettivo. Album applica un guadagno comune e conserva i contrasti. Usare Album per un’opera completa; Traccia per un livello regolare o casuale.",
        "version_changes": "• L’aiuto distingue chiaramente Traccia e Album.\n• La guida spiega quando usare ogni modalità.\n• Le dodici lingue condividono la spiegazione.\n• L’elaborazione non cambia.",
    },
    "pt": {
        "mode_tooltip": "Faixa aproxima cada ficheiro do alvo. Álbum ajusta o nível global da pasta com um ganho comum, preservando as diferenças entre faixas.",
        "album_analysis_help_text": "Escolha Álbum para preservar o equilíbrio entre passagens calmas e fortes ao ouvir a obra completa. Para um nível regular entre ficheiros ou reprodução aleatória, escolha Faixa. O limite de pico pode restringir o ganho e a medição global exige uma segunda passagem, mostrada no progresso.",
        "guide_level_mode_body": "Faixa aproxima cada ficheiro do alvo. Álbum aplica um ganho comum e preserva os contrastes. Use Álbum para uma obra completa; Faixa para um nível regular ou aleatório.",
        "version_changes": "• A ajuda distingue claramente Faixa e Álbum.\n• O guia explica quando usar cada modo.\n• As doze línguas partilham a explicação.\n• O processamento não muda.",
    },
    "ru": {
        "mode_tooltip": "Режим трека ведёт каждый файл к цели. Альбом регулирует общий уровень папки единым усилением и сохраняет различия между треками.",
        "album_analysis_help_text": "Выбирайте Альбом, чтобы сохранить соотношение тихих и мощных частей при прослушивании произведения целиком. Для ровного уровня файлов или случайного воспроизведения выбирайте Трек. Ограничение пика может уменьшить усиление; общий замер требует второго прохода с отображением хода.",
        "guide_level_mode_body": "Трек ведёт каждый файл к цели. Альбом применяет к папке единое усиление и сохраняет контрасты. Альбом подходит для цельного произведения, Трек - для ровного уровня или случайного порядка.",
        "version_changes": "• Справка ясно различает режимы Трек и Альбом.\n• Руководство объясняет их назначение.\n• Текст обновлён во всех 12 языках.\n• Обработка не изменена.",
    },
    "ja": {
        "mode_tooltip": "トラックは各ファイルを目標へ近づけます。アルバムは共通ゲインでフォルダー全体を調整し、曲間差を保ちます。",
        "album_analysis_help_text": "静かな部分と力強い部分のバランスを保って作品全体を聴く場合はアルバムを選びます。ファイルごとの音量を揃える場合やシャッフル再生にはトラックを選びます。アルバムではピーク制限でゲインが抑えられることがあり、進捗表示付きの2回目の測定が必要です。",
        "guide_level_mode_body": "トラックは各ファイルを目標へ近づけます。アルバムは共通ゲインで全体を調整し曲間差を保ちます。作品全体にはアルバム、均一なファイルやシャッフルにはトラックを使います。",
        "version_changes": "• トラックとアルバムの違いを明確にしました。\n• ガイドに選択基準を追加しました。\n• 12言語を更新しました。\n• 音声処理は変更していません。",
    },
    "hi": {
        "mode_tooltip": "Track हर file को target के पास लाता है। Album पूरे folder पर एक common gain लगाकर tracks के differences बचाता है।",
        "album_analysis_help_text": "पूरे work को सुनते समय quiet और powerful passages का balance बचाने के लिए Album चुनें। Files के बीच regular level या shuffle playback के लिए Track चुनें। Album में peak limit gain को रोक सकती है और global measurement के दूसरे pass की progress दिखाई जाती है।",
        "guide_level_mode_body": "Track हर file को target के पास लाता है। Album common gain से पूरे folder को adjust करके contrasts बचाता है। Complete work के लिए Album; regular file level या shuffle के लिए Track चुनें।",
        "version_changes": "• Help Track और Album का अंतर साफ करती है।\n• Guide चुनाव समझाती है।\n• सभी 12 languages update हैं।\n• Audio processing unchanged है।",
    },
    "zh": {
        "mode_tooltip": "单曲模式让每个文件接近目标。专辑模式用共同增益调整整个文件夹，并保留曲目间差异。",
        "album_analysis_help_text": "完整聆听作品并保留安静与强烈段落的平衡时，请选择专辑。若要文件间音量稳定或随机播放，请选择单曲。专辑模式下峰值限制可能约束增益，且全局测量需要第二遍扫描，其进度会显示。",
        "guide_level_mode_body": "单曲模式让每个文件接近目标。专辑模式用共同增益调整整体并保留对比。完整作品用专辑；文件间稳定或随机播放用单曲。",
        "version_changes": "• 帮助明确区分单曲和专辑。\n• 指南说明选择场景。\n• 十二种语言同步更新。\n• 音频处理未更改。",
    },
    "ko": {
        "mode_tooltip": "트랙은 각 파일을 목표에 맞춥니다. 앨범은 하나의 공통 게인으로 폴더 전체를 조절하고 곡 사이 차이를 유지합니다.",
        "album_analysis_help_text": "조용한 부분과 강한 부분의 균형을 유지하며 전체 작품을 들을 때는 앨범을 선택합니다. 파일마다 일정한 음량이나 셔플 재생에는 트랙을 선택합니다. 앨범에서는 피크 제한이 게인을 줄일 수 있으며 진행률이 표시되는 두 번째 전체 측정이 필요합니다.",
        "guide_level_mode_body": "트랙은 각 파일을 목표에 맞춥니다. 앨범은 공통 게인으로 전체를 조절하고 대비를 보존합니다. 전체 작품에는 앨범, 일정한 파일 음량이나 셔플에는 트랙을 사용합니다.",
        "version_changes": "• 트랙과 앨범의 차이를 명확히 설명합니다.\n• 안내서에 선택 기준을 추가했습니다.\n• 12개 언어를 갱신했습니다.\n• 오디오 처리는 변경하지 않았습니다.",
    },
    "id": {
        "mode_tooltip": "Trek mendekatkan tiap berkas ke target. Album menyesuaikan tingkat keseluruhan folder dengan satu gain bersama dan mempertahankan perbedaan trek.",
        "album_analysis_help_text": "Pilih Album untuk menjaga keseimbangan bagian tenang dan kuat saat mendengarkan karya lengkap. Untuk tingkat yang konsisten antarberkas atau putar acak, pilih Trek. Batas puncak dapat membatasi gain dan pengukuran global memerlukan lintasan kedua yang kemajuannya ditampilkan.",
        "guide_level_mode_body": "Trek mendekatkan tiap berkas ke target. Album memakai gain bersama dan menjaga kontras. Gunakan Album untuk karya lengkap; Trek untuk tingkat berkas konsisten atau acak.",
        "version_changes": "• Bantuan membedakan Trek dan Album.\n• Panduan menjelaskan waktu pemakaiannya.\n• Dua belas bahasa diperbarui.\n• Pemrosesan tidak berubah.",
    },
    "tr": {
        "mode_tooltip": "Parça her dosyayı hedefe yaklaştırır. Albüm klasörün genel düzeyini tek ortak kazançla ayarlar ve parça farklarını korur.",
        "album_analysis_help_text": "Eserin tamamını dinlerken sakin ve güçlü bölümlerin dengesini korumak için Albüm seçin. Dosyalar arasında düzenli düzey veya karışık çalma için Parça seçin. Tepe sınırı kazancı kısıtlayabilir ve genel ölçüm, ilerlemesi gösterilen ikinci bir geçiş gerektirir.",
        "guide_level_mode_body": "Parça her dosyayı hedefe yaklaştırır. Albüm ortak kazançla bütünü ayarlar ve farkları korur. Tam eser için Albüm; düzenli dosya düzeyi veya karışık çalma için Parça kullanın.",
        "version_changes": "• Yardım Parça ve Albüm farkını açıklar.\n• Kılavuz seçim ölçütünü belirtir.\n• On iki dil güncellendi.\n• Ses işleme değişmedi.",
    },
}


__all__ = ["TRANSLATION_UPDATES_12430"]
