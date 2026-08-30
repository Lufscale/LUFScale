"""Corrections de présentation et clarification ReplayGain de LUFScale 1.24.19."""

from __future__ import annotations


TRANSLATION_UPDATES_12419: dict[str, dict[str, str]] = {
    "fr": {
        "replaygain_levels_log": "audio inchangé : {before} LUFS · gain ReplayGain {gain} dB en métadonnées · cible réglée {target} LUFS (lecteur compatible requis)",
        "replaygain_usefulness_text": "Intérêt de ReplayGain : harmoniser le volume à la lecture, sans perte de réencodage et de façon réversible, pour une bibliothèque utilisée avec un lecteur compatible. Pour livrer un fichier qui mesure physiquement la cible dans tous les lecteurs, utilisez Uniformiser.",
        "replaygain_log_help_text": "En ReplayGain, le journal indique la sonie physique inchangée, le gain inscrit dans les métadonnées et la cible réglée. Ce gain ne devient audible que si le lecteur applique les balises ; il ne s’agit pas d’une sortie audio normalisée.",
        "version_changes": "• Les lignes ReplayGain distinguent maintenant la sonie physique inchangée, le gain en métadonnées et la cible réglée.\n• L’aide et les guides expliquent l’intérêt réversible de ReplayGain et quand préférer Uniformiser.\n• Le panneau de sonie reste ancré sous les boutons lors d’un agrandissement ; seul le journal absorbe la hauteur.\n• L’en-tête du journal est compacté pour agrandir sa zone utile vers le haut.\n• Les voyants et leurs sigles sont centrés verticalement.\n• Le cadre Réglages utilise un trait uniforme dans les thèmes sombre et clair.\n• Le moteur audio et les seuils sont inchangés.",
    },
    "en": {
        "replaygain_levels_log": "audio unchanged: {before} LUFS · ReplayGain {gain} dB in metadata · configured target {target} LUFS (compatible player required)",
        "replaygain_usefulness_text": "ReplayGain is useful for reversible, no-re-encode playback leveling in a library used with a compatible player. To deliver a file that physically measures at the target in every player, use Normalize.",
        "replaygain_log_help_text": "For ReplayGain, the log states the unchanged physical loudness, the gain written to metadata, and the configured target. That gain is audible only when a player applies the tags; this is not a normalized audio output.",
        "version_changes": "• ReplayGain lines now distinguish unchanged physical loudness, metadata gain, and configured target.\n• Help and guides explain ReplayGain’s reversible use and when to choose Normalize.\n• The loudness panel stays anchored below the buttons when the window grows; only the log takes the extra height.\n• The log header is compacted to extend its useful area upward.\n• Option lamps and abbreviations are vertically centered.\n• The Settings frame uses one uniform stroke in dark and light themes.\n• The audio engine and thresholds are unchanged.",
    },
    "es": {
        "replaygain_levels_log": "audio sin cambios: {before} LUFS · ReplayGain {gain} dB en metadatos · objetivo configurado {target} LUFS (requiere reproductor compatible)",
        "replaygain_usefulness_text": "ReplayGain sirve para igualar el volumen de reproducción de forma reversible y sin recodificación en una biblioteca usada con un reproductor compatible. Para entregar un archivo que mida físicamente el objetivo en todos los reproductores, use Normalizar.",
        "replaygain_log_help_text": "Con ReplayGain, el registro indica la sonoridad física sin cambios, la ganancia escrita en los metadatos y el objetivo configurado. La ganancia solo se oye si el reproductor aplica las etiquetas; no es una salida de audio normalizada.",
        "version_changes": "• Las líneas ReplayGain separan la sonoridad física sin cambios, la ganancia de metadatos y el objetivo configurado.\n• La ayuda y las guías explican el uso reversible de ReplayGain y cuándo elegir Normalizar.\n• El panel de sonoridad permanece bajo los botones al ampliar la ventana; solo crece el registro.\n• El encabezado del registro es más compacto y amplía el área útil hacia arriba.\n• Las luces y sus siglas quedan centradas verticalmente.\n• El marco de Ajustes usa un trazo uniforme en ambos temas.\n• El motor de audio y los umbrales no cambian.",
    },
    "it": {
        "replaygain_levels_log": "audio invariato: {before} LUFS · ReplayGain {gain} dB nei metadati · obiettivo impostato {target} LUFS (serve un lettore compatibile)",
        "replaygain_usefulness_text": "ReplayGain è utile per uniformare la riproduzione in modo reversibile e senza ricodifica in una libreria usata con un lettore compatibile. Per consegnare un file che misuri fisicamente l’obiettivo in ogni lettore, usare Normalizza.",
        "replaygain_log_help_text": "Con ReplayGain, il registro indica la sonorità fisica invariata, il guadagno scritto nei metadati e l’obiettivo impostato. Il guadagno è udibile solo se il lettore applica i tag; non è un’uscita audio normalizzata.",
        "version_changes": "• Le righe ReplayGain distinguono sonorità fisica invariata, guadagno nei metadati e obiettivo impostato.\n• Aiuto e guide spiegano l’uso reversibile di ReplayGain e quando scegliere Normalizza.\n• Il pannello della sonorità resta sotto i pulsanti quando la finestra cresce; solo il registro usa l’altezza aggiuntiva.\n• L’intestazione del registro è più compatta e ne amplia l’area utile verso l’alto.\n• Spie e sigle sono centrate verticalmente.\n• La cornice Impostazioni usa un tratto uniforme nei due temi.\n• Motore audio e soglie sono invariati.",
    },
    "pt": {
        "replaygain_levels_log": "áudio inalterado: {before} LUFS · ReplayGain {gain} dB nos metadados · alvo configurado {target} LUFS (requer leitor compatível)",
        "replaygain_usefulness_text": "ReplayGain é útil para uniformizar a reprodução de forma reversível e sem recodificação numa biblioteca usada com um leitor compatível. Para entregar um ficheiro que meça fisicamente o alvo em todos os leitores, use Uniformizar.",
        "replaygain_log_help_text": "Com ReplayGain, o registo indica a sonoridade física inalterada, o ganho escrito nos metadados e o alvo configurado. O ganho só é audível se o leitor aplicar as etiquetas; não é uma saída de áudio normalizada.",
        "version_changes": "• As linhas ReplayGain distinguem sonoridade física inalterada, ganho nos metadados e alvo configurado.\n• A ajuda e os guias explicam o uso reversível de ReplayGain e quando escolher Uniformizar.\n• O painel de sonoridade permanece sob os botões ao ampliar a janela; só o registo recebe a altura extra.\n• O cabeçalho do registo fica mais compacto e aumenta a área útil para cima.\n• Luzes e siglas ficam centradas verticalmente.\n• A moldura Definições usa um traço uniforme nos dois temas.\n• O motor de áudio e os limiares não mudam.",
    },
    "ru": {
        "replaygain_levels_log": "аудио без изменений: {before} LUFS · ReplayGain {gain} дБ в метаданных · заданная цель {target} LUFS (нужен совместимый проигрыватель)",
        "replaygain_usefulness_text": "ReplayGain полезен для обратимого выравнивания громкости при воспроизведении без перекодирования, если библиотека используется в совместимом проигрывателе. Для файла, физически измеряемого на цели в любом проигрывателе, выберите Нормализацию.",
        "replaygain_log_help_text": "Для ReplayGain журнал показывает неизменную физическую громкость, усиление в метаданных и заданную цель. Усиление слышно только в проигрывателе, применяющем теги; это не нормализованный аудиовыход.",
        "version_changes": "• Строки ReplayGain разделяют неизменную физическую громкость, усиление в метаданных и заданную цель.\n• Справка и руководства объясняют обратимое применение ReplayGain и выбор Нормализации.\n• Панель громкости остаётся под кнопками при увеличении окна; дополнительную высоту получает только журнал.\n• Заголовок журнала стал компактнее, полезная область поднята вверх.\n• Индикаторы и сокращения центрированы по вертикали.\n• Рамка настроек имеет одинаковую линию в обеих темах.\n• Аудиодвижок и пороги не изменены.",
    },
    "ja": {
        "replaygain_levels_log": "音声は変更なし: {before} LUFS · メタデータのReplayGain {gain} dB · 設定目標 {target} LUFS（対応プレーヤーが必要）",
        "replaygain_usefulness_text": "ReplayGainは、対応プレーヤーで使うライブラリの再生音量を、再エンコードせず可逆的に揃える用途に適しています。すべてのプレーヤーで物理的に目標値を測定できるファイルを納品する場合は、ノーマライズを使用してください。",
        "replaygain_log_help_text": "ReplayGainのログは、物理的な音量が変わらないこと、メタデータに書いたゲイン、設定目標を示します。タグを適用するプレーヤーでのみゲインが聞こえ、音声出力自体の正規化ではありません。",
        "version_changes": "• ReplayGain行で、変わらない物理音量、メタデータのゲイン、設定目標を区別します。\n• ヘルプとガイドにReplayGainの可逆的な用途とノーマライズを選ぶ場合を説明しました。\n• ウィンドウを拡大しても音量パネルはボタン直下に固定され、ログだけが高くなります。\n• ログ見出しを小さくして有効領域を上へ広げました。\n• オプションランプと略称を縦方向に中央揃えしました。\n• 設定枠を両テーマで均一な線にしました。\n• 音声エンジンとしきい値は変更していません。",
    },
    "hi": {
        "replaygain_levels_log": "audio unchanged: {before} LUFS · metadata में ReplayGain {gain} dB · configured target {target} LUFS (compatible player आवश्यक)",
        "replaygain_usefulness_text": "ReplayGain compatible player वाली library में बिना re-encoding, reversible playback leveling के लिए उपयोगी है। हर player में file को target पर physically measure कराने के लिए Normalize उपयोग करें।",
        "replaygain_log_help_text": "ReplayGain में log unchanged physical loudness, metadata में लिखा gain और configured target दिखाता है। Gain तभी सुनाई देता है जब player tags लागू करे; यह normalized audio output नहीं है।",
        "version_changes": "• ReplayGain lines unchanged physical loudness, metadata gain और configured target अलग दिखाती हैं।\n• Help और guides ReplayGain का reversible उपयोग और Normalize चुनने का समय बताते हैं।\n• Window बढ़ाने पर loudness panel buttons के नीचे स्थिर रहता है; केवल log अतिरिक्त height लेता है।\n• Log header compact करके usable area ऊपर बढ़ाया गया है।\n• Option lights और abbreviations vertically centered हैं।\n• Settings frame दोनों themes में uniform stroke उपयोग करता है।\n• Audio engine और thresholds unchanged हैं।",
    },
    "zh": {
        "replaygain_levels_log": "音频不变：{before} LUFS · 元数据ReplayGain {gain} dB · 设置目标 {target} LUFS（需要兼容播放器）",
        "replaygain_usefulness_text": "ReplayGain适合在兼容播放器中对资料库进行可逆、无重编码的播放音量统一。若要交付在所有播放器中都能实际测得目标值的文件，请使用标准化。",
        "replaygain_log_help_text": "ReplayGain日志会显示未改变的物理响度、写入元数据的增益和设置目标。只有播放器应用标签时才能听到该增益；这不是经过标准化的音频输出。",
        "version_changes": "• ReplayGain行现在区分未改变的物理响度、元数据增益和设置目标。\n• 帮助和指南说明ReplayGain的可逆用途以及何时选择标准化。\n• 放大窗口时响度面板固定在按钮下方，只有日志获得额外高度。\n• 日志标题栏更紧凑，可用区域向上扩展。\n• 选项灯和缩写已垂直居中。\n• 设置框在深浅主题中使用一致的线条。\n• 音频引擎和阈值未更改。",
    },
    "ko": {
        "replaygain_levels_log": "오디오 변경 없음: {before} LUFS · 메타데이터 ReplayGain {gain} dB · 설정 목표 {target} LUFS(호환 플레이어 필요)",
        "replaygain_usefulness_text": "ReplayGain은 호환 플레이어에서 사용하는 라이브러리의 재생 음량을 재인코딩 없이 가역적으로 맞출 때 유용합니다. 모든 플레이어에서 물리적으로 목표값이 측정되는 파일을 제공하려면 정규화를 사용하십시오.",
        "replaygain_log_help_text": "ReplayGain 로그는 변경되지 않은 물리적 음량, 메타데이터에 기록한 게인, 설정 목표를 표시합니다. 태그를 적용하는 플레이어에서만 게인이 들리며 정규화된 오디오 출력은 아닙니다.",
        "version_changes": "• ReplayGain 줄에서 변경되지 않은 물리 음량, 메타데이터 게인, 설정 목표를 구분합니다.\n• 도움말과 안내서에 ReplayGain의 가역적 용도와 정규화를 선택할 경우를 설명했습니다.\n• 창을 키워도 음량 패널은 버튼 아래에 고정되고 로그만 높아집니다.\n• 로그 헤더를 줄여 유효 영역을 위로 넓혔습니다.\n• 옵션 표시등과 약어를 세로로 중앙 정렬했습니다.\n• 설정 프레임은 두 테마에서 균일한 선을 사용합니다.\n• 오디오 엔진과 임계값은 변경하지 않았습니다.",
    },
    "id": {
        "replaygain_levels_log": "audio tidak berubah: {before} LUFS · ReplayGain {gain} dB dalam metadata · target pengaturan {target} LUFS (perlu pemutar kompatibel)",
        "replaygain_usefulness_text": "ReplayGain berguna untuk meratakan volume pemutaran secara reversibel tanpa enkode ulang pada pustaka yang memakai pemutar kompatibel. Untuk menghasilkan berkas yang secara fisik terukur pada target di semua pemutar, gunakan Normalisasi.",
        "replaygain_log_help_text": "Untuk ReplayGain, log menunjukkan kenyaringan fisik yang tidak berubah, gain yang ditulis ke metadata, dan target pengaturan. Gain hanya terdengar bila pemutar menerapkan tag; ini bukan keluaran audio yang dinormalisasi.",
        "version_changes": "• Baris ReplayGain membedakan kenyaringan fisik yang tidak berubah, gain metadata, dan target pengaturan.\n• Bantuan dan panduan menjelaskan kegunaan reversibel ReplayGain dan kapan memilih Normalisasi.\n• Panel kenyaringan tetap di bawah tombol saat jendela diperbesar; hanya log yang menerima tinggi tambahan.\n• Header log dipadatkan agar area berguna meluas ke atas.\n• Lampu opsi dan singkatan dipusatkan secara vertikal.\n• Bingkai Pengaturan memakai garis seragam pada kedua tema.\n• Mesin audio dan ambang tidak berubah.",
    },
    "tr": {
        "replaygain_levels_log": "ses değişmedi: {before} LUFS · meta veride ReplayGain {gain} dB · ayarlanan hedef {target} LUFS (uyumlu oynatıcı gerekir)",
        "replaygain_usefulness_text": "ReplayGain, uyumlu bir oynatıcıyla kullanılan arşivde yeniden kodlama olmadan, geri alınabilir çalma düzeyi eşitlemesi için yararlıdır. Her oynatıcıda fiziksel olarak hedefte ölçülen bir dosya teslim etmek için Normalleştirme kullanın.",
        "replaygain_log_help_text": "ReplayGain için günlük değişmeyen fiziksel ses yüksekliğini, meta veriye yazılan gain’i ve ayarlanan hedefi gösterir. Gain yalnızca oynatıcı etiketleri uygularsa duyulur; bu normalleştirilmiş bir ses çıkışı değildir.",
        "version_changes": "• ReplayGain satırları değişmeyen fiziksel ses yüksekliğini, meta veri gain’ini ve ayarlanan hedefi ayırır.\n• Yardım ve kılavuzlar ReplayGain’in geri alınabilir kullanımını ve Normalleştirme seçimini açıklar.\n• Pencere büyüdüğünde ses yüksekliği paneli düğmelerin altında sabit kalır; ek yüksekliği yalnızca günlük alır.\n• Günlük başlığı sıkıştırılarak kullanılabilir alan yukarı doğru büyütüldü.\n• Seçenek ışıkları ve kısaltmalar dikey ortalandı.\n• Ayarlar çerçevesi iki temada da tek tip çizgi kullanır.\n• Ses motoru ve eşikler değişmedi.",
    },
}


__all__ = ["TRANSLATION_UPDATES_12419"]
