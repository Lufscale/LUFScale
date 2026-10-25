"""Documentation-only clarification of format scope, translated in all guide languages."""
SCOPE_COPY = {
 'fr': {
  'title':'Formats concernés', 'revision':'Documentation révisée - doc-r1. Application : 2.2.3.', 'mp3':'MP3 uniquement : traitement dynamique',
  'body':'LUFScale prend en charge MP3, FLAC, WAV, AIFF, M4A, OGG et Opus. La mesure de sonie, la cible LUFS, le plafond True Peak en mode Uniformiser, les réglages de traitement et le contrôle qualité concernent les formats compatibles, pas seulement le MP3. Le codec et certaines corrections dépendent du format de sortie. Les exemples MP3 illustrent un cas particulier ; ils ne limitent pas les fonctions générales au MP3.',
  'qc':'Le contrôle qualité concerne tous les formats pris en charge. M4A, OGG et Opus sont également vérifiés, mais ne bénéficient pas des boucles correctives propres au MP3 dynamique ou à FLAC/WAV/AIFF. En mode ReplayGain, le contrôle vérifie la préservation du signal et les balises ; il ne garantit pas un niveau audio physiquement normalisé.',
  'peak':'Le plafond True Peak concerne tous les formats en mode Uniformiser. Les exemples citant le MP3 sont aussi utiles pour comprendre les précautions liées aux autres formats avec pertes, comme M4A/AAC, OGG/Vorbis et Opus. La marge interne supplémentaire de 1 dB décrite dans l’annexe est, elle, réservée au traitement dynamique des sorties MP3.',
  'formulas':'Les mesures et les seuils de contrôle concernent les formats pris en charge. Les formules de cible interne et de correction marquées « MP3 uniquement » décrivent la boucle MP3 dynamique. Les limites de correction précisent séparément le cas FLAC/WAV/AIFF ; elles ne doivent pas être généralisées à M4A, OGG ou Opus.'},
 'en': {
  'title':'Format scope', 'revision':'Revised documentation - doc-r1. Application: 2.2.3.', 'mp3':'MP3 only: dynamic processing',
  'body':'LUFScale supports MP3, FLAC, WAV, AIFF, M4A, OGG and Opus. Loudness measurement, the LUFS target, the True Peak ceiling in Normalize mode, processing settings and quality control apply to supported formats, not only MP3. The codec and some corrections depend on the output format. MP3 examples illustrate a particular case; they do not restrict general features to MP3.',
  'qc':'Quality control covers all supported formats. M4A, OGG and Opus are also checked, but do not use the corrective loops specific to dynamic MP3 or FLAC/WAV/AIFF. In ReplayGain mode, checks concern signal preservation and tags; they do not guarantee physically normalized audio.',
  'peak':'The True Peak ceiling applies to all formats in Normalize mode. MP3 examples also help explain precautions for other lossy formats such as M4A/AAC, OGG/Vorbis and Opus. The additional internal 1 dB margin described in the appendix is specific to dynamic processing of MP3 output.',
  'formulas':'Measurements and quality thresholds cover supported formats. Internal-target and feedback formulas marked “MP3 only” describe the dynamic MP3 loop. Correction limits separately identify FLAC/WAV/AIFF; they must not be generalized to M4A, OGG or Opus.'},
 'es': {
  'title':'Formatos a los que se aplica', 'revision':'Documentación revisada - doc-r1. Aplicación: 2.2.3.', 'mp3':'Solo MP3: procesamiento dinámico',
  'body':'LUFScale admite MP3, FLAC, WAV, AIFF, M4A, OGG y Opus. La medición de sonoridad, el objetivo LUFS, el límite True Peak en el modo Normalizar, los ajustes y el control de calidad se aplican a los formatos compatibles, no solo a MP3. El códec y algunas correcciones dependen del formato de salida. Los ejemplos MP3 ilustran un caso particular, no una limitación de las funciones generales.',
  'qc':'El control de calidad abarca todos los formatos compatibles. M4A, OGG y Opus también se verifican, pero no utilizan los ciclos correctivos específicos de MP3 dinámico o FLAC/WAV/AIFF. En ReplayGain se comprueban la conservación de la señal y las etiquetas, no una normalización física del audio.',
  'peak':'El límite True Peak se aplica a todos los formatos al normalizar. Los ejemplos MP3 también ayudan a entender las precauciones para M4A/AAC, OGG/Vorbis y Opus. El margen interno adicional de 1 dB del anexo es exclusivo del procesamiento dinámico de salidas MP3.',
  'formulas':'Las mediciones y los umbrales abarcan los formatos compatibles. Las fórmulas de objetivo interno y corrección marcadas «Solo MP3» describen el ciclo MP3 dinámico. Los límites distinguen FLAC/WAV/AIFF y no se deben generalizar a M4A, OGG u Opus.'},
 'it': {
  'title':'Formati interessati', 'revision':'Documentazione revisionata - doc-r1. Applicazione: 2.2.3.', 'mp3':'Solo MP3: elaborazione dinamica',
  'body':'LUFScale supporta MP3, FLAC, WAV, AIFF, M4A, OGG e Opus. La misura della sonorità, il valore LUFS, il limite True Peak in modalità Normalizza, le impostazioni e il controllo qualità riguardano i formati supportati, non soltanto MP3. Il codec e alcune correzioni dipendono dal formato di uscita. Gli esempi MP3 illustrano un caso particolare e non limitano le funzioni generali.',
  'qc':'Il controllo qualità riguarda tutti i formati supportati. Anche M4A, OGG e Opus vengono verificati, ma non usano i cicli correttivi specifici di MP3 dinamico o FLAC/WAV/AIFF. In ReplayGain si verificano la conservazione del segnale e i tag, non una normalizzazione fisica dell’audio.',
  'peak':'Il limite True Peak riguarda tutti i formati durante la normalizzazione. Gli esempi MP3 chiariscono anche le precauzioni per M4A/AAC, OGG/Vorbis e Opus. Il margine interno aggiuntivo di 1 dB nell’appendice è specifico delle uscite MP3 elaborate dinamicamente.',
  'formulas':'Misure e soglie riguardano i formati supportati. Le formule di obiettivo interno e correzione contrassegnate «Solo MP3» descrivono il ciclo MP3 dinamico. I limiti distinguono FLAC/WAV/AIFF e non vanno estesi a M4A, OGG o Opus.'},
 'pt': {
  'title':'Formatos abrangidos', 'revision':'Documentação revista - doc-r1. Aplicação: 2.2.3.', 'mp3':'Apenas MP3: processamento dinâmico',
  'body':'O LUFScale suporta MP3, FLAC, WAV, AIFF, M4A, OGG e Opus. A medição de sonoridade, o alvo LUFS, o limite True Peak no modo Normalizar, os ajustes e o controlo de qualidade abrangem os formatos compatíveis, não apenas MP3. O codec e algumas correções dependem do formato de saída. Os exemplos MP3 ilustram um caso particular, não uma limitação das funções gerais.',
  'qc':'O controlo de qualidade abrange todos os formatos compatíveis. M4A, OGG e Opus também são verificados, mas não usam os ciclos corretivos próprios do MP3 dinâmico ou de FLAC/WAV/AIFF. Em ReplayGain, verificam-se a preservação do sinal e as etiquetas, não uma normalização física do áudio.',
  'peak':'O limite True Peak aplica-se a todos os formatos ao normalizar. Os exemplos MP3 também explicam precauções para M4A/AAC, OGG/Vorbis e Opus. A margem interna adicional de 1 dB do anexo é específica das saídas MP3 com processamento dinâmico.',
  'formulas':'As medições e os limiares abrangem os formatos compatíveis. As fórmulas de alvo interno e correção assinaladas «Apenas MP3» descrevem o ciclo MP3 dinâmico. Os limites distinguem FLAC/WAV/AIFF e não se generalizam a M4A, OGG ou Opus.'},
 'ru': {
  'title':'Применимость к форматам', 'revision':'Исправленная документация - doc-r1. Приложение: 2.2.3.', 'mp3':'Только MP3: динамическая обработка',
  'body':'LUFScale поддерживает MP3, FLAC, WAV, AIFF, M4A, OGG и Opus. Измерение громкости, цель LUFS, предел True Peak при нормализации, настройки обработки и контроль качества относятся ко всем поддерживаемым форматам, а не только к MP3. Кодек и отдельные коррекции зависят от выходного формата. Примеры MP3 показывают частный случай, не ограничивая общие функции.',
  'qc':'Контроль качества охватывает все поддерживаемые форматы. M4A, OGG и Opus также проверяются, но не используют циклы коррекции для динамического MP3 или FLAC/WAV/AIFF. В режиме ReplayGain проверяются сохранность сигнала и теги, а не физическая нормализация аудио.',
  'peak':'Предел True Peak действует для всех форматов при нормализации. Примеры MP3 также поясняют меры предосторожности для M4A/AAC, OGG/Vorbis и Opus. Дополнительный внутренний запас 1 дБ из приложения относится только к динамической обработке выходных MP3.',
  'formulas':'Измерения и пороги относятся к поддерживаемым форматам. Формулы внутренней цели и коррекции с пометкой «Только MP3» описывают динамический цикл MP3. Пределы отдельно указывают FLAC/WAV/AIFF и не распространяются на M4A, OGG или Opus.'},
 'ja': {
  'title':'対象となる形式', 'revision':'改訂ドキュメント - doc-r1。アプリケーション：2.2.3。', 'mp3':'MP3のみ：動的処理',
  'body':'LUFScaleはMP3、FLAC、WAV、AIFF、M4A、OGG、Opusに対応しています。ラウドネス測定、LUFS目標、ノーマライズ時のTrue Peak上限、処理設定、品質チェックは、MP3だけでなく対応形式全般に適用されます。コーデックと一部の補正は出力形式によって異なります。MP3の例は個別のケースを示すもので、一般機能をMP3に限定するものではありません。',
  'qc':'品質チェックはすべての対応形式が対象です。M4A、OGG、Opusも検証されますが、動的MP3やFLAC/WAV/AIFF専用の補正ループは使いません。ReplayGainでは信号の保持とタグを確認し、音声自体のノーマライズを保証するものではありません。',
  'peak':'ノーマライズ時のTrue Peak上限は全形式に適用されます。MP3の例はM4A/AAC、OGG/Vorbis、Opusの注意点を理解する際にも役立ちます。付録の追加内部マージン1 dBは、MP3出力の動的処理専用です。',
  'formulas':'測定と品質しきい値は対応形式全般に適用されます。「MP3のみ」と記された内部目標と補正式は動的MP3ループを示します。補正回数の上限ではFLAC/WAV/AIFFを別に示しており、M4A、OGG、Opusに一般化できません。'},
 'hi': {
  'title':'किन प्रारूपों पर लागू होता है', 'revision':'संशोधित दस्तावेज़ - doc-r1। एप्लिकेशन: 2.2.3।', 'mp3':'केवल MP3: डायनेमिक प्रोसेसिंग',
  'body':'LUFScale MP3, FLAC, WAV, AIFF, M4A, OGG और Opus का समर्थन करता है। लाउडनेस मापन, LUFS लक्ष्य, नॉर्मलाइज़ मोड में True Peak सीमा, प्रोसेसिंग सेटिंग और गुणवत्ता जाँच केवल MP3 नहीं, सभी समर्थित प्रारूपों पर लागू हैं। कोडेक और कुछ सुधार आउटपुट प्रारूप पर निर्भर हैं। MP3 के उदाहरण एक विशेष स्थिति दिखाते हैं; वे सामान्य सुविधाओं को MP3 तक सीमित नहीं करते।',
  'qc':'गुणवत्ता जाँच सभी समर्थित प्रारूपों पर लागू है। M4A, OGG और Opus भी जाँचे जाते हैं, पर डायनेमिक MP3 या FLAC/WAV/AIFF के विशेष सुधार चक्र इस्तेमाल नहीं करते। ReplayGain में सिग्नल के संरक्षण और टैग की जाँच होती है; ऑडियो के वास्तविक स्तर का नॉर्मलाइज़ होना सुनिश्चित नहीं होता।',
  'peak':'नॉर्मलाइज़ करते समय True Peak सीमा सभी प्रारूपों पर लागू है। MP3 के उदाहरण M4A/AAC, OGG/Vorbis और Opus की सावधानियाँ भी समझाते हैं। परिशिष्ट में दिया अतिरिक्त आंतरिक 1 dB मार्जिन केवल MP3 आउटपुट की डायनेमिक प्रोसेसिंग के लिए है।',
  'formulas':'मापन और गुणवत्ता सीमाएँ समर्थित प्रारूपों पर लागू हैं। «केवल MP3» वाले आंतरिक लक्ष्य और सुधार सूत्र डायनेमिक MP3 चक्र के हैं। सुधार की सीमाओं में FLAC/WAV/AIFF अलग हैं; उन्हें M4A, OGG या Opus पर लागू न करें।'},
 'zh': {
  'title':'适用格式', 'revision':'修订文档 - doc-r1。应用版本：2.2.3。', 'mp3':'仅限 MP3：动态处理',
  'body':'LUFScale 支持 MP3、FLAC、WAV、AIFF、M4A、OGG 和 Opus。响度测量、LUFS 目标、均衡模式下的 True Peak 上限、处理设置和质量检查适用于支持的格式，而非仅限 MP3。编码器及部分修正取决于输出格式。MP3 示例只是特定案例，并不表示通用功能仅支持 MP3。',
  'qc':'质量检查适用于所有支持的格式。M4A、OGG 和 Opus 也会接受检查，但不使用动态 MP3 或 FLAC/WAV/AIFF 专用的修正循环。ReplayGain 模式检查信号保留情况和标签，并不保证实际音频已被均衡到目标响度。',
  'peak':'均衡时的 True Peak 上限适用于所有格式。MP3 示例也有助于理解 M4A/AAC、OGG/Vorbis 和 Opus 的注意事项。附录中的额外 1 dB 内部余量仅用于 MP3 输出的动态处理。',
  'formulas':'测量和质量阈值适用于支持的格式。标注“仅限 MP3”的内部目标与反馈修正公式描述动态 MP3 循环。修正次数上限单独说明 FLAC/WAV/AIFF，不应套用于 M4A、OGG 或 Opus。'},
 'ko': {
  'title':'적용 형식', 'revision':'수정된 문서 - doc-r1. 애플리케이션: 2.2.3.', 'mp3':'MP3 전용: 동적 처리',
  'body':'LUFScale은 MP3, FLAC, WAV, AIFF, M4A, OGG, Opus를 지원합니다. 라우드니스 측정, LUFS 목표, 정규화 모드의 True Peak 상한, 처리 설정과 품질 검사는 MP3뿐 아니라 지원 형식 전반에 적용됩니다. 코덱과 일부 보정은 출력 형식에 따라 달라집니다. MP3 예시는 특정 사례이며 일반 기능을 MP3로 제한하지 않습니다.',
  'qc':'품질 검사는 모든 지원 형식에 적용됩니다. M4A, OGG, Opus도 검사하지만 동적 MP3 또는 FLAC/WAV/AIFF 전용 보정 루프는 사용하지 않습니다. ReplayGain에서는 신호 보존과 태그를 확인하며 오디오 자체의 정규화를 보장하지 않습니다.',
  'peak':'정규화 시 True Peak 상한은 모든 형식에 적용됩니다. MP3 예시는 M4A/AAC, OGG/Vorbis, Opus의 주의점에도 도움이 됩니다. 부록의 추가 내부 여유 1 dB는 MP3 출력의 동적 처리 전용입니다.',
  'formulas':'측정과 품질 기준은 지원 형식에 적용됩니다. «MP3 전용»으로 표시된 내부 목표와 피드백 보정 수식은 동적 MP3 루프를 설명합니다. 보정 횟수 제한은 FLAC/WAV/AIFF를 별도로 명시하며 M4A, OGG, Opus에 일반화할 수 없습니다.'},
 'id': {
  'title':'Cakupan format', 'revision':'Dokumentasi diperbarui - doc-r1. Aplikasi: 2.2.3.', 'mp3':'Khusus MP3: pemrosesan dinamis',
  'body':'LUFScale mendukung MP3, FLAC, WAV, AIFF, M4A, OGG, dan Opus. Pengukuran kenyaringan, target LUFS, batas True Peak dalam mode Normalisasi, pengaturan, dan pemeriksaan kualitas berlaku untuk format yang didukung, bukan hanya MP3. Codec dan beberapa koreksi bergantung pada format keluaran. Contoh MP3 menunjukkan kasus khusus, bukan batasan fitur umum.',
  'qc':'Pemeriksaan kualitas mencakup semua format yang didukung. M4A, OGG, dan Opus juga diperiksa, tetapi tidak menggunakan siklus koreksi khusus MP3 dinamis atau FLAC/WAV/AIFF. Dalam ReplayGain, pemeriksaan mencakup keutuhan sinyal dan tag, bukan jaminan normalisasi fisik audio.',
  'peak':'Batas True Peak berlaku untuk semua format saat normalisasi. Contoh MP3 juga menjelaskan langkah kehati-hatian untuk M4A/AAC, OGG/Vorbis, dan Opus. Margin internal tambahan 1 dB dalam lampiran khusus untuk pemrosesan dinamis keluaran MP3.',
  'formulas':'Pengukuran dan ambang kualitas berlaku untuk format yang didukung. Rumus target internal dan koreksi bertanda «Khusus MP3» menjelaskan siklus MP3 dinamis. Batas koreksi membedakan FLAC/WAV/AIFF dan tidak boleh digeneralisasi ke M4A, OGG, atau Opus.'},
 'tr': {
  'title':'Kapsanan biçimler', 'revision':'Gözden geçirilmiş belge - doc-r1. Uygulama: 2.2.3.', 'mp3':'Yalnızca MP3: dinamik işleme',
  'body':'LUFScale MP3, FLAC, WAV, AIFF, M4A, OGG ve Opus biçimlerini destekler. Ses yüksekliği ölçümü, LUFS hedefi, Normalleştir modunda True Peak sınırı, işleme ayarları ve kalite kontrolü yalnızca MP3 için değil, desteklenen biçimler için geçerlidir. Codec ve bazı düzeltmeler çıkış biçimine bağlıdır. MP3 örnekleri özel bir durumu gösterir; genel özellikleri MP3 ile sınırlamaz.',
  'qc':'Kalite kontrolü desteklenen tüm biçimleri kapsar. M4A, OGG ve Opus da denetlenir ancak dinamik MP3 veya FLAC/WAV/AIFF için özel düzeltme döngülerini kullanmaz. ReplayGain modunda sinyalin korunması ve etiketler denetlenir; sesin fiziksel olarak normalleştirildiği garanti edilmez.',
  'peak':'Normalleştirme sırasında True Peak sınırı tüm biçimlere uygulanır. MP3 örnekleri M4A/AAC, OGG/Vorbis ve Opus için önlemleri de açıklar. Ekteki ek 1 dB iç pay, MP3 çıkışlarının dinamik işlenmesine özeldir.',
  'formulas':'Ölçümler ve kalite eşikleri desteklenen biçimler için geçerlidir. «Yalnızca MP3» işaretli iç hedef ve geri besleme formülleri dinamik MP3 döngüsünü açıklar. Düzeltme sınırları FLAC/WAV/AIFF için ayrıca belirtilir; M4A, OGG veya Opus için genellenmemelidir.'},
}

MAC_DISTRIBUTIONS = {'fr': 'Deux distributions macOS sont proposées : Apple Silicon (arm64) et Intel (x86_64). Utilisez celle qui '
       'correspond au processeur de votre Mac.',
 'en': 'Two macOS distributions are available: Apple Silicon (arm64) and Intel (x86_64). Use the one matching your Mac '
       'processor.',
 'es': 'Hay dos distribuciones para macOS: Apple Silicon (arm64) e Intel (x86_64). Utilice la que corresponda al '
       'procesador de su Mac.',
 'it': 'Sono disponibili due distribuzioni macOS: Apple Silicon (arm64) e Intel (x86_64). Usare quella corrispondente '
       'al processore del Mac.',
 'pt': 'Existem duas distribuições para macOS: Apple Silicon (arm64) e Intel (x86_64). Utilize a correspondente ao '
       'processador do seu Mac.',
 'ru': 'Доступны две сборки macOS: Apple Silicon (arm64) и Intel (x86_64). Выберите сборку для процессора вашего Mac.',
 'ja': 'macOS版にはApple Silicon（arm64）とIntel（x86_64）の2種類があります。Macのプロセッサに合うものを使用してください。',
 'hi': 'macOS के दो वितरण हैं: Apple Silicon (arm64) और Intel (x86_64)। अपने Mac के प्रोसेसर से मेल खाने वाला वितरण '
       'चुनें।',
 'zh': 'macOS 提供 Apple Silicon（arm64）和 Intel（x86_64）两个发行版。请选择与您的 Mac 处理器匹配的版本。',
 'ko': 'macOS 배포본은 Apple Silicon(arm64)과 Intel(x86_64) 두 종류입니다. Mac 프로세서에 맞는 버전을 사용하십시오.',
 'id': 'Tersedia dua distribusi macOS: Apple Silicon (arm64) dan Intel (x86_64). Gunakan yang sesuai dengan prosesor '
       'Mac Anda.',
 'tr': 'İki macOS dağıtımı vardır: Apple Silicon (arm64) ve Intel (x86_64). Mac işlemcinize uygun olanı kullanın.'}

BEST_ATTEMPT_COPY = {'fr': 'Parmi les essais disponibles, le score privilégie le respect du plafond de crête, puis la tolérance de sonie, '
       'puis l’écart absolu à la cible. Ce choix s’applique aux reprises MP3 dynamiques et FLAC/WAV/AIFF.',
 'en': 'Among available attempts, the score prioritizes the peak ceiling, then loudness tolerance, then absolute '
       'distance from the target. This selection applies to dynamic MP3 and FLAC/WAV/AIFF corrections.',
 'es': 'Entre los intentos disponibles, la puntuación prioriza el límite de pico, la tolerancia de sonoridad y la '
       'distancia absoluta al objetivo. Se aplica a las correcciones MP3 dinámicas y FLAC/WAV/AIFF.',
 'it': 'Tra i tentativi disponibili, il punteggio privilegia il limite di picco, la tolleranza di sonorità e la '
       'distanza assoluta dall’obiettivo. Vale per le correzioni MP3 dinamiche e FLAC/WAV/AIFF.',
 'pt': 'Entre as tentativas disponíveis, a pontuação privilegia o limite de pico, a tolerância de sonoridade e a '
       'distância absoluta ao alvo. Aplica-se às correções MP3 dinâmicas e FLAC/WAV/AIFF.',
 'ru': 'Среди доступных попыток оценка отдаёт приоритет пределу пика, допуску громкости и абсолютному отклонению от '
       'цели. Это относится к коррекциям динамического MP3 и FLAC/WAV/AIFF.',
 'ja': '利用できる試行の中で、ピーク上限、ラウドネス許容範囲、目標との差の絶対値の順に評価します。動的MP3とFLAC/WAV/AIFFの補正に適用されます。',
 'hi': 'उपलब्ध प्रयासों में स्कोर पहले पीक सीमा, फिर लाउडनेस सहनशीलता और फिर लक्ष्य से निरपेक्ष अंतर को प्राथमिकता '
       'देता है। यह डायनेमिक MP3 और FLAC/WAV/AIFF सुधारों पर लागू है।',
 'zh': '在可用尝试中，评分依次优先考虑峰值上限、响度容差以及与目标的绝对差值。这适用于动态 MP3 和 FLAC/WAV/AIFF 的修正。',
 'ko': '사용 가능한 시도 중 피크 상한, 라우드니스 허용 오차, 목표와의 절대 차이 순으로 평가합니다. 동적 MP3 및 FLAC/WAV/AIFF 보정에 적용됩니다.',
 'id': 'Di antara percobaan yang tersedia, skor memprioritaskan batas puncak, toleransi kenyaringan, lalu selisih '
       'absolut dari target. Ini berlaku untuk koreksi MP3 dinamis dan FLAC/WAV/AIFF.',
 'tr': 'Mevcut denemeler arasında puan sırasıyla tepe sınırına, ses yüksekliği toleransına ve hedefe mutlak uzaklığa '
       'öncelik verir. Dinamik MP3 ve FLAC/WAV/AIFF düzeltmelerine uygulanır.'}
