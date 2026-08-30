from __future__ import annotations


# Release notes for the visual refinements and rebuilt documentation in 1.24.15.
TRANSLATION_UPDATES_12415: dict[str, dict[str, str]] = {
    "fr": {
        "version_changes": "• Le bas du panneau Évolution de la sonie est aminci jusqu’à la même marge que les côtés ; les deux graphiques gagnent en hauteur et en lisibilité.\n• Avant et Après conservent la même échelle verticale fixe de ±6 LU autour de la cible et restent directement comparables.\n• Les angles supérieurs des onglets Audio et Options sont arrondis ; chaque contour reste tracé une seule fois.\n• Les douze guides PDF reprennent la structure graphique détaillée de la version 1.24.6 et documentent les fonctions et seuils actuels.\n• Le moteur audio et les calculs de normalisation sont inchangés.",
    },
    "en": {
        "version_changes": "• The bottom of the Loudness change panel now matches the side margins; both graphs gain height and detail.\n• Before and After keep the same fixed ±6 LU vertical scale around the target and remain directly comparable.\n• The upper corners of the Audio and Options tabs are rounded, while each outline is still drawn only once.\n• All twelve PDF guides reuse the detailed visual structure of version 1.24.6 and document the current functions and thresholds.\n• The audio engine and normalization calculations are unchanged.",
    },
    "es": {
        "version_changes": "• El margen inferior del panel Evolución de sonoridad ahora coincide con los laterales; ambos gráficos ganan altura y detalle.\n• Antes y Después mantienen la misma escala vertical fija de ±6 LU alrededor del objetivo y siguen siendo directamente comparables.\n• Las esquinas superiores de las pestañas Audio y Opciones están redondeadas y cada contorno se dibuja una sola vez.\n• Las doce guías PDF recuperan la estructura visual detallada de la versión 1.24.6 y documentan las funciones y umbrales actuales.\n• El motor de audio y los cálculos de normalización no cambian.",
    },
    "it": {
        "version_changes": "• Il margine inferiore del pannello Evoluzione della sonorità ora coincide con quelli laterali; entrambi i grafici guadagnano altezza e dettaglio.\n• Prima e Dopo mantengono la stessa scala verticale fissa di ±6 LU attorno all’obiettivo e restano direttamente confrontabili.\n• Gli angoli superiori delle schede Audio e Opzioni sono arrotondati e ogni contorno viene tracciato una sola volta.\n• Le dodici guide PDF riprendono la struttura grafica dettagliata della versione 1.24.6 e documentano funzioni e soglie attuali.\n• Il motore audio e i calcoli di normalizzazione non cambiano.",
    },
    "pt": {
        "version_changes": "• A margem inferior do painel Evolução da sonoridade passa a ser igual às margens laterais; os dois gráficos ganham altura e detalhe.\n• Antes e Depois mantêm a mesma escala vertical fixa de ±6 LU em torno do alvo e continuam diretamente comparáveis.\n• Os cantos superiores dos separadores Áudio e Opções estão arredondados e cada contorno continua a ser desenhado uma única vez.\n• Os doze guias PDF retomam a estrutura gráfica detalhada da versão 1.24.6 e documentam as funções e os limites atuais.\n• O motor de áudio e os cálculos de normalização não mudam.",
    },
    "ru": {
        "version_changes": "• Нижнее поле панели изменения громкости теперь совпадает с боковыми; оба графика стали выше и подробнее.\n• Графики «До» и «После» сохраняют одинаковую фиксированную шкалу ±6 LU относительно цели и остаются напрямую сопоставимыми.\n• Верхние углы вкладок «Аудио» и «Параметры» закруглены, а каждый контур по-прежнему рисуется только один раз.\n• Все двенадцать PDF-руководств используют подробную графическую структуру версии 1.24.6 и описывают текущие функции и пороги.\n• Аудиодвижок и расчёты нормализации не изменены.",
    },
    "ja": {
        "version_changes": "• ラウドネス変化パネルの下余白を左右と同じ幅にし、2つのグラフの高さと見やすさを向上しました。\n• 処理前と処理後は、目標値を中心とする同じ固定縦軸±6 LUを維持し、直接比較できます。\n• オーディオとオプションのタブ上部を丸め、各輪郭は引き続き1回だけ描画します。\n• 12言語のPDFガイドは、バージョン1.24.6の詳しい図解構成を引き継ぎ、現在の機能としきい値を説明します。\n• オーディオエンジンと正規化計算は変更していません。",
    },
    "hi": {
        "version_changes": "• Loudness change पैनल का नीचे का अंतर अब किनारों के बराबर है; दोनों ग्राफ़ अधिक ऊँचे और स्पष्ट हैं।\n• पहले और बाद, लक्ष्य के आसपास समान स्थिर ±6 LU ऊर्ध्व पैमाना रखते हैं और उनकी सीधी तुलना की जा सकती है।\n• ऑडियो और विकल्प टैब के ऊपरी कोने गोल हैं और हर बॉर्डर केवल एक बार बनाया जाता है।\n• सभी बारह PDF गाइड संस्करण 1.24.6 की विस्तृत दृश्य संरचना अपनाते हैं और मौजूदा फ़ंक्शन व सीमाएँ बताते हैं।\n• ऑडियो इंजन और normalization गणनाएँ नहीं बदली हैं।",
    },
    "zh": {
        "version_changes": "• 响度变化面板的底部留白现已与两侧一致，两个图表更高、细节更清楚。\n• 处理前和处理后继续使用以目标为中心的同一固定±6 LU纵向刻度，可直接比较。\n• 音频和选项标签页的上角已圆润处理，每条边框仍只绘制一次。\n• 十二种语言的PDF指南沿用1.24.6版的详细图文结构，并说明当前功能和阈值。\n• 音频引擎和响度标准化计算没有变化。",
    },
    "ko": {
        "add_source_files": "오디오 파일 추가",
        "analysis_method_tooltip": "안정 버전은 기준 자료에서 검증된 전체 길이 분석 방식을 자동으로 사용합니다. 빠른 분석과 적응형 분석은 제공하지 않습니다.",
        "mode_track_label": "트랙",
        "mode_album_label": "앨범",
        "version_changes": "• 라우드니스 변화 패널의 아래 여백을 좌우와 같게 맞춰 두 그래프가 더 높고 자세하게 표시됩니다.\n• 처리 전과 처리 후는 목표를 중심으로 한 동일한 고정 ±6 LU 세로 눈금을 유지하므로 직접 비교할 수 있습니다.\n• 오디오와 옵션 탭의 위쪽 모서리를 둥글게 했으며 각 테두리는 계속 한 번만 그립니다.\n• 12개 언어 PDF 안내서는 1.24.6의 자세한 시각 구조를 이어받아 현재 기능과 기준값을 설명합니다.\n• 오디오 엔진과 정규화 계산은 변경되지 않았습니다.",
    },
    "id": {
        "add_source_files": "Tambahkan berkas audio",
        "analysis_method_tooltip": "Versi stabil otomatis memakai pengukuran penuh historis, yaitu satu-satunya metode yang telah divalidasi pada korpus acuan. Metode Cepat dan Adaptif tidak ditawarkan.",
        "mode_track_label": "Trek",
        "mode_album_label": "Album",
        "version_changes": "• Ruang bawah panel Perubahan kenyaringan kini sama dengan sisi kiri dan kanan; kedua grafik menjadi lebih tinggi dan terperinci.\n• Sebelum dan Sesudah tetap memakai skala vertikal tetap ±6 LU yang sama di sekitar target sehingga dapat dibandingkan langsung.\n• Sudut atas tab Audio dan Opsi dibulatkan, sementara setiap garis tepi tetap digambar satu kali.\n• Kedua belas panduan PDF memakai kembali struktur visual terperinci versi 1.24.6 dan menjelaskan fungsi serta ambang saat ini.\n• Mesin audio dan perhitungan normalisasi tidak berubah.",
    },
    "tr": {
        "add_source_files": "Ses dosyaları ekle",
        "analysis_method_tooltip": "Kararlı sürüm, referans derlem üzerinde doğrulanan tek yöntem olan tam tarihsel ölçümü otomatik olarak kullanır. Hızlı ve Uyarlanabilir yöntemler sunulmaz.",
        "mode_track_label": "Parça",
        "mode_album_label": "Albüm",
        "version_changes": "• Ses yüksekliği değişimi panelinin alt boşluğu artık yan boşluklarla aynıdır; iki grafik daha yüksek ve ayrıntılıdır.\n• Önce ve Sonra, hedefin çevresinde aynı sabit ±6 LU dikey ölçeği korur ve doğrudan karşılaştırılabilir.\n• Ses ve Seçenekler sekmelerinin üst köşeleri yuvarlatılmıştır; her kenarlık yine yalnızca bir kez çizilir.\n• On iki PDF kılavuzu, 1.24.6 sürümünün ayrıntılı görsel yapısını temel alır ve güncel işlevlerle eşikleri açıklar.\n• Ses motoru ve normalleştirme hesaplamaları değişmemiştir.",
    },
}


__all__ = ["TRANSLATION_UPDATES_12415"]
