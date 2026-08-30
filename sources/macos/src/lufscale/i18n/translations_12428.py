"""PDF hierarchy, formula typography and active-tab alignment 1.24.28."""

from __future__ import annotations


TRANSLATION_UPDATES_12428: dict[str, dict[str, str]] = {
    "fr": {
        "guide_quality_priority_body": "LUFScale privilégie la mesure complète, la normalisation vers la cible et la remesure finale. Il ne cherche pas l’encodage le plus rapide : il vise un niveau perçu cohérent et stable entre les fichiers et signale toute sortie hors tolérance.",
        "guide_analysis_method": "LUFScale utilise automatiquement la mesure historique complète, seule méthode validée sur le corpus de référence. Les variantes Rapide et Adaptatif ne sont plus proposées.",
        "guide_level_mode_body": "Piste règle chaque fichier audio séparément. Album calcule un gain commun par dossier afin de conserver les écarts de volume entre ses pistes.\nMesure Album : chaque album est parcouru entièrement avant encodage pour calculer ce gain commun.",
        "version_changes": "• La première page aligne l’icône à gauche du titre et affiche clairement LUFScale pour macOS avec sa version.\n• Les textes Mode de niveau et Traitement sont plus lisibles et les repères de couleur du journal ont un titre.\n• Les formules des pages techniques sont isolées dans une zone typographique distincte des explications.\n• Le coin et le trait gauche de l’onglet Audio utilisent le même axe.\n• Le traitement audio, les calculs et les seuils sont inchangés.",
    },
    "en": {
        "guide_quality_priority_body": "LUFScale prioritizes full measurement, normalization toward the target, and final remeasurement. It does not seek the fastest encode: it aims for consistent, stable perceived loudness across files and flags any output outside tolerance.",
        "guide_analysis_method": "LUFScale automatically uses the full historical measurement, the only method validated on the reference corpus. Fast and Adaptive are no longer offered.",
        "guide_level_mode_body": "Track processes each audio file separately. Album calculates one shared gain per folder to preserve level differences between its tracks.\nAlbum measurement: each album is scanned in full before encoding to calculate that shared gain.",
        "version_changes": "• Page one aligns the icon to the left of the title and clearly identifies LUFScale for macOS and its version.\n• Level-mode and Processing text is more readable, and the processing-log colour key has a title.\n• Technical formulas are separated typographically from their explanations.\n• The Audio tab's corner and left side now share the same axis.\n• Audio processing, calculations, and thresholds are unchanged.",
    },
    "es": {
        "guide_analysis_method": "LUFScale utiliza automáticamente la medición histórica completa, la única validada en el corpus de referencia. Rápido y Adaptativo ya no se ofrecen.",
        "guide_level_mode_body": "Pista procesa cada archivo por separado. Álbum calcula una ganancia común por carpeta para conservar las diferencias entre pistas.\nMedición de álbum: cada álbum se recorre por completo antes de codificar.",
        "version_changes": "• La primera página alinea el icono a la izquierda e identifica LUFScale para macOS y su versión.\n• Los textos son más legibles y la leyenda de colores tiene título.\n• Las fórmulas se separan visualmente de sus explicaciones.\n• La esquina y el lado izquierdo de Audio comparten el mismo eje.\n• El procesamiento de audio no cambia.",
    },
    "it": {
        "guide_analysis_method": "LUFScale usa automaticamente la misura storica completa, l’unico metodo convalidato sul corpus di riferimento. Rapido e Adattivo non sono più proposti.",
        "guide_level_mode_body": "Traccia elabora separatamente ogni file. Album calcola un guadagno comune per cartella e conserva le differenze fra le tracce.\nMisura Album: ogni album viene analizzato per intero prima della codifica.",
        "version_changes": "• La prima pagina allinea l’icona a sinistra e identifica LUFScale per macOS con la versione.\n• I testi sono più leggibili e la legenda colori ha un titolo.\n• Le formule sono separate visivamente dalle spiegazioni.\n• L’angolo e il lato sinistro di Audio condividono lo stesso asse.\n• L’elaborazione audio non cambia.",
    },
    "pt": {
        "guide_analysis_method": "O LUFScale utiliza automaticamente a medição histórica completa, o único método validado no corpus de referência. Rápido e Adaptativo deixaram de ser propostos.",
        "guide_level_mode_body": "Faixa processa cada ficheiro separadamente. Álbum calcula um ganho comum por pasta e conserva as diferenças entre faixas.\nMedição de álbum: cada álbum é analisado por completo antes da codificação.",
        "version_changes": "• A primeira página alinha o ícone à esquerda e identifica o LUFScale para macOS e a versão.\n• Os textos são mais legíveis e a legenda de cores tem título.\n• As fórmulas ficam visualmente separadas das explicações.\n• O canto e o lado esquerdo de Áudio partilham o mesmo eixo.\n• O processamento áudio não muda.",
    },
    "ru": {
        "guide_analysis_method": "LUFScale автоматически использует полный исторический эталонный замер - единственный метод, проверенный на эталонном наборе. Быстрый и адаптивный варианты не предлагаются.",
        "guide_level_mode_body": "Режим дорожки обрабатывает каждый файл отдельно. Альбом рассчитывает общее усиление для папки и сохраняет разницу между дорожками.\nАльбом полностью измеряется до кодирования.",
        "version_changes": "• На первой странице значок выровнен слева, а версия показана явно.\n• Текст и цветовая легенда стали понятнее.\n• Формулы отделены от пояснений.\n• Левый край вкладки Audio выровнен.\n• Обработка звука не изменена.",
    },
    "ja": {
        "guide_analysis_method": "LUFScaleは、基準コーパスで検証済みの完全な履歴方式を自動的に使用します。高速方式と適応方式は提供しません。",
        "guide_level_mode_body": "トラックは各ファイルを個別に処理します。アルバムはフォルダごとに共通ゲインを計算し、曲間の差を保ちます。\nアルバム全体をエンコード前に測定します。",
        "version_changes": "• 1ページ目でアイコンを左に揃え、macOS版とバージョンを明記しました。\n• 文字と処理ログの色分けを読みやすくしました。\n• 式と説明を視覚的に分けました。\n• Audioタブ左端を同じ軸に揃えました。\n• 音声処理は変更していません。",
    },
    "hi": {
        "guide_analysis_method": "LUFScale reference corpus पर सत्यापित पूर्ण historical measurement का स्वतः उपयोग करता है। Fast और Adaptive विकल्प उपलब्ध नहीं हैं।",
        "guide_level_mode_body": "Track हर file को अलग process करता है। Album हर folder के लिए common gain गणना करके tracks का अंतर बचाता है।\nEncoding से पहले पूरे album को measure किया जाता है।",
        "version_changes": "• पहले page पर icon बाएं है और macOS version स्पष्ट है।\n• Text और processing-log colour key अधिक पठनीय हैं।\n• Formulas और explanations अलग दिखते हैं।\n• Audio tab का बायां किनारा aligned है।\n• Audio processing नहीं बदली।",
    },
    "zh": {
        "guide_analysis_method": "LUFScale自动使用已通过参考语料验证的完整历史测量方法。不再提供快速和自适应方法。",
        "guide_level_mode_body": "单曲模式分别处理每个文件。专辑模式按文件夹计算共同增益，保留曲目间的音量差。\n编码前会完整测量每张专辑。",
        "version_changes": "• 首页图标左对齐，并明确显示macOS版本。\n• 文字和处理日志颜色说明更易阅读。\n• 公式与解释在视觉上分开。\n• Audio标签左侧已对齐。\n• 音频处理未更改。",
    },
    "ko": {
        "guide_analysis_method": "LUFScale는 기준 자료에서 검증된 전체 길이 분석 방식을 자동으로 사용합니다. 빠른 분석과 적응형 분석은 제공하지 않습니다.",
        "guide_level_mode_body": "트랙은 각 파일을 별도로 처리합니다. 앨범은 폴더별 공통 게인을 계산해 곡 사이의 차이를 유지합니다.\n인코딩 전에 앨범 전체를 측정합니다.",
        "version_changes": "• 첫 페이지에서 아이콘을 왼쪽에 맞추고 macOS 버전을 명시합니다.\n• 글자와 처리 로그 색상 안내를 더 읽기 쉽게 했습니다.\n• 수식과 설명을 시각적으로 분리했습니다.\n• Audio 탭 왼쪽을 정렬했습니다.\n• 오디오 처리는 변경되지 않았습니다.",
    },
    "id": {
        "guide_analysis_method": "LUFScale secara otomatis memakai pengukuran historis penuh yang telah divalidasi pada korpus acuan. Metode Cepat dan Adaptif tidak ditawarkan.",
        "guide_level_mode_body": "Trek memproses setiap berkas secara terpisah. Album menghitung gain bersama per folder dan mempertahankan perbedaan antar trek.\nSetiap album diukur sepenuhnya sebelum pengodean.",
        "version_changes": "• Halaman pertama meratakan ikon ke kiri dan menyebut versi macOS dengan jelas.\n• Teks dan keterangan warna log lebih mudah dibaca.\n• Rumus dipisahkan secara visual dari penjelasannya.\n• Sisi kiri tab Audio kini sejajar.\n• Pemrosesan audio tidak berubah.",
    },
    "tr": {
        "guide_analysis_method": "LUFScale, referans derlem üzerinde doğrulanan tam tarihsel ölçümü otomatik olarak kullanır. Hızlı ve Uyarlanabilir yöntemler sunulmaz.",
        "guide_level_mode_body": "Parça her dosyayı ayrı işler. Albüm, klasör başına ortak kazanç hesaplar ve parçalar arasındaki farkları korur.\nHer albüm kodlamadan önce tamamen ölçülür.",
        "version_changes": "• İlk sayfada simge sola hizalanır ve macOS sürümü açıkça belirtilir.\n• Metin ve işlem günlüğü renk anahtarı daha okunaklıdır.\n• Formüller açıklamalardan görsel olarak ayrılır.\n• Audio sekmesinin sol kenarı hizalanmıştır.\n• Ses işleme değişmemiştir.",
    },
}


__all__ = ["TRANSLATION_UPDATES_12428"]
