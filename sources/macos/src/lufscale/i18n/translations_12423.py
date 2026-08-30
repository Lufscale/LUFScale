"""Corrections d’interface, analyse seule et guides 1.24.23."""

from __future__ import annotations


TRANSLATION_UPDATES_12423: dict[str, dict[str, str]] = {
    "fr": {
        "analyze_only_fresh_help_text": "Analyser seulement décode chaque source et parcourt tout le signal avec FFmpeg loudnorm afin de mesurer la sonie intégrée, la plage LRA, le seuil et la crête vraie. C’est pourquoi l’analyse peut rester longue même sans encodage ni fichier produit. Chaque lancement effectue une nouvelle mesure et ne réutilise pas le cache d’une uniformisation précédente. Comme aucune sortie n’existe, il n’y a pas de contrôle qualité de sortie : Après reste immobile et le journal n’affiche plus « contrôle qualité : RÉUSSI ».",
        "version_changes": "• Les boutons Version et tous les boutons ? ouvrent de nouveau leur fenêtre commune d’information.\n• Les aides conservent des paragraphes et listes aérés sans modifier directement le document Qt natif.\n• Le bas d’Évolution de la sonie gagne 2 px et rejoint exactement celui du journal, sans déplacer le haut.\n• La courbe Avant devient violette afin de se distinguer clairement du graphe CPU bleu.\n• Le cadre Audio/Options est plus visible, arrondi et ne laisse plus de trait parasite sur l’onglet inactif.\n• Analyser seulement ne présente plus une mesure source comme un contrôle qualité réussi.\n• Les douze guides reprennent la maquette 1.23.2 : fenêtre principale en page 1, organisation validée et deux pages complètes de formules mises à jour.",
    },
    "en": {
        "analyze_only_fresh_help_text": "Analyze-only decodes every source and scans the complete signal with FFmpeg loudnorm to measure integrated loudness, LRA, threshold and true peak. It can therefore remain time-consuming even though no encoding or output file is produced. Every run performs a fresh measurement and does not reuse the cache from an earlier normalization. Because no output exists, no output quality check occurs: After stays still and the log no longer says ‘quality control: SUCCESS’.",
        "version_changes": "• Version and every ? button open their shared information window again.\n• Help keeps readable paragraphs and lists without directly rewriting the native Qt document.\n• The Loudness change panel gains 2 px at the bottom and now exactly meets the processing log without moving its top.\n• The Before curve is purple so it is clearly distinct from the blue CPU graph.\n• The Audio/Options frame is stronger, rounded, and leaves no stray line on the inactive tab.\n• Analyze-only no longer presents a source measurement as a successful quality check.\n• All twelve guides return to the validated 1.23.2 layout: main window on page 1, familiar organization, and two complete updated formula pages.",
    },
    "es": {
        "version_changes": "• Los botones Versión y ? vuelven a abrir la ventana de información.\n• El panel de sonoridad queda alineado con el registro.\n• La curva Antes pasa a violeta y se distingue del gráfico azul de CPU.\n• El marco Audio/Opciones es más visible, redondeado y sin línea parásita.\n• Solo analizar ya no anuncia un control de calidad superado.\n• Las doce guías recuperan el diseño 1.23.2, la ventana principal y dos páginas completas de fórmulas actualizadas.",
    },
    "it": {
        "version_changes": "• I pulsanti Versione e ? aprono di nuovo la finestra informativa.\n• Il pannello della sonorità è allineato al registro.\n• La curva Prima diventa viola e si distingue dal grafico CPU blu.\n• Il bordo Audio/Opzioni è più visibile, arrotondato e senza linea residua.\n• Solo analisi non indica più un controllo qualità superato.\n• Le dodici guide riprendono il layout 1.23.2, la finestra principale e due pagine complete di formule aggiornate.",
    },
    "pt": {
        "version_changes": "• Os botões Versão e ? voltam a abrir a janela de informação.\n• O painel de sonoridade fica alinhado com o registo.\n• A curva Antes passa a violeta e distingue-se do gráfico azul da CPU.\n• O contorno Áudio/Opções fica mais visível, arredondado e sem linha residual.\n• Apenas analisar deixa de indicar um controlo de qualidade aprovado.\n• Os doze guias retomam o desenho 1.23.2, a janela principal e duas páginas completas de fórmulas atualizadas.",
    },
    "ru": {
        "version_changes": "• Кнопки версии и ? снова открывают информационное окно.\n• Панель громкости выровнена по журналу.\n• График «До» стал фиолетовым и отличается от синего графика ЦП.\n• Рамка Аудио/Параметры стала заметнее, получила скругления и не оставляет лишней линии.\n• Анализ больше не сообщает об успешном контроле качества.\n• Все двенадцать руководств возвращают макет 1.23.2, главное окно и две полные обновлённые страницы формул.",
    },
    "ja": {
        "version_changes": "• バージョンボタンとすべての？ボタンで情報画面が再び開きます。\n• ラウドネスパネル下端を処理ログに揃えました。\n• 処理前の線を紫にして青いCPUグラフと区別しました。\n• オーディオ／オプション枠を見やすく丸め、不要な線を除去しました。\n• 解析のみでは品質管理成功と表示しません。\n• 12言語のガイドを1.23.2の構成に戻し、メイン画面と更新済み数式2ページを収録しました。",
    },
    "hi": {
        "version_changes": "• Version और सभी ? buttons फिर से information window खोलते हैं।\n• Loudness panel का निचला किनारा processing log से align है।\n• Before curve बैंगनी है और नीले CPU graph से स्पष्ट अलग है।\n• Audio/Options frame अधिक स्पष्ट, rounded और stray line से मुक्त है।\n• Analyze-only अब successful quality check नहीं बताता।\n• सभी 12 guides में 1.23.2 layout, main window और दो updated formula pages लौट आए हैं।",
    },
    "zh": {
        "version_changes": "• 版本和所有？按钮恢复打开信息窗口。\n• 响度变化面板底边与处理日志对齐。\n• 处理前曲线改为紫色，与蓝色CPU图清楚区分。\n• 音频/选项边框更明显、圆润且没有多余线条。\n• 仅分析不再显示质量控制成功。\n• 十二种语言的指南恢复1.23.2版式、首页主窗口和两页完整的更新公式。",
    },
    "ko": {
        "version_changes": "• 버전 및 모든 ? 버튼이 다시 정보 창을 엽니다.\n• 라우드니스 패널 아래쪽을 처리 로그와 맞췄습니다.\n• 처리 전 곡선을 보라색으로 바꿔 파란 CPU 그래프와 구분했습니다.\n• 오디오/옵션 테두리를 더 선명하고 둥글게 만들고 불필요한 선을 제거했습니다.\n• 분석 전용은 더 이상 품질 검사 성공으로 표시하지 않습니다.\n• 12개 언어 안내서에 1.23.2 레이아웃, 첫 페이지의 메인 창, 업데이트된 공식 두 페이지를 복원했습니다.",
    },
    "id": {
        "version_changes": "• Tombol Versi dan semua tombol ? kembali membuka jendela informasi.\n• Batas bawah panel kenyaringan sejajar dengan log pemrosesan.\n• Kurva Sebelum menjadi ungu agar berbeda dari grafik CPU biru.\n• Bingkai Audio/Opsi lebih jelas, membulat, dan tanpa garis sisa.\n• Hanya analisis tidak lagi menyatakan pemeriksaan mutu berhasil.\n• Kedua belas panduan kembali memakai tata letak 1.23.2, jendela utama, dan dua halaman rumus lengkap yang diperbarui.",
    },
    "tr": {
        "version_changes": "• Sürüm ve tüm ? düğmeleri bilgi penceresini yeniden açar.\n• Ses yüksekliği panelinin alt kenarı işlem günlüğüyle hizalandı.\n• Önce eğrisi mor oldu ve mavi CPU grafiğinden ayrıldı.\n• Ses/Seçenekler çerçevesi daha görünür, yuvarlak ve artık gereksiz çizgi bırakmıyor.\n• Yalnızca analiz artık başarılı kalite kontrolü bildirmiyor.\n• On iki kılavuz 1.23.2 düzenine, ana pencere görseline ve güncellenmiş iki tam formül sayfasına döndü.",
    },
}


__all__ = ["TRANSLATION_UPDATES_12423"]
