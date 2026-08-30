"""Self-contained macOS release text for LUFScale 2.1.10."""

from .translations_201700 import TRANSLATION_UPDATES_201700
from .translations_201000 import TRANSLATION_UPDATES_201000
from .translations_201500 import TRANSLATION_UPDATES_201500


_AUTONOMOUS_FEATURE = {
    "fr": "• L’application macOS contient déjà Python, PySide6/Qt, FFmpeg, les codecs, les guides et les licences : l’utilisateur final n’installe aucun outil supplémentaire.",
    "en": "• The macOS application already contains Python, PySide6/Qt, FFmpeg, codecs, guides and licences: end users install no additional tool.",
    "es": "• La aplicación macOS ya contiene Python, PySide6/Qt, FFmpeg, códecs, guías y licencias: el usuario final no instala ninguna herramienta adicional.",
    "it": "• L’applicazione macOS contiene già Python, PySide6/Qt, FFmpeg, codec, guide e licenze: l’utente finale non installa strumenti aggiuntivi.",
    "pt": "• A aplicação macOS já contém Python, PySide6/Qt, FFmpeg, codecs, guias e licenças: o utilizador final não instala ferramentas adicionais.",
    "ru": "• Приложение macOS уже содержит Python, PySide6/Qt, FFmpeg, кодеки, руководства и лицензии: пользователю не нужно устанавливать дополнительные средства.",
    "ja": "• macOSアプリにはPython、PySide6/Qt、FFmpeg、コーデック、ガイド、ライセンスが含まれ、利用者が追加ツールをインストールする必要はありません。",
    "hi": "• macOS अनुप्रयोग में Python, PySide6/Qt, FFmpeg, कोडेक, मार्गदर्शिकाएँ और लाइसेंस पहले से शामिल हैं; अंतिम उपयोगकर्ता को कोई अतिरिक्त साधन स्थापित नहीं करना पड़ता।",
    "zh": "• macOS应用已内置Python、PySide6/Qt、FFmpeg、编解码器、指南和许可证；最终用户无需安装任何额外工具。",
    "ko": "• macOS 앱에는 Python, PySide6/Qt, FFmpeg, 코덱, 안내서와 라이선스가 이미 포함되어 있어 사용자가 추가 도구를 설치할 필요가 없습니다.",
    "id": "• Aplikasi macOS sudah memuat Python, PySide6/Qt, FFmpeg, codec, panduan, dan lisensi; pengguna akhir tidak perlu memasang alat tambahan.",
    "tr": "• macOS uygulaması Python, PySide6/Qt, FFmpeg, codec bileşenleri, kılavuzlar ve lisansları içerir; son kullanıcı ek araç kurmaz.",
}

_VERSION_CHANGES = {
    "fr": "• Distribution macOS autonome : Python, PySide6/Qt et un FFmpeg natif vérifié sont intégrés à LUFScale.app.\n• Aucun environnement d’exécution externe n’est requis pour l’utilisateur final ; le paquet contrôle son contenu avant publication.\n• Le moteur audio et les seuils du contrôle qualité sont inchangés.",
    "en": "• Self-contained macOS distribution: Python, PySide6/Qt and one verified native FFmpeg are embedded in LUFScale.app.\n• End users need no external runtime; the package verifies its contents before publication.\n• The audio engine and quality-control thresholds are unchanged.",
    "es": "• Distribución macOS autónoma: Python, PySide6/Qt y un FFmpeg nativo verificado están integrados en LUFScale.app.\n• El usuario final no necesita un entorno externo; el paquete comprueba su contenido antes de publicarse.\n• El motor de audio y los umbrales de calidad no cambian.",
    "it": "• Distribuzione macOS autonoma: Python, PySide6/Qt e un FFmpeg nativo verificato sono integrati in LUFScale.app.\n• L’utente finale non necessita di runtime esterni; il pacchetto verifica il contenuto prima della pubblicazione.\n• Motore audio e soglie di qualità restano invariati.",
    "pt": "• Distribuição macOS autónoma: Python, PySide6/Qt e um FFmpeg nativo verificado estão integrados em LUFScale.app.\n• O utilizador final não precisa de runtime externo; o pacote verifica o conteúdo antes da publicação.\n• O motor de áudio e os limites de qualidade não mudam.",
    "ru": "• Автономная сборка macOS: Python, PySide6/Qt и проверенный нативный FFmpeg встроены в LUFScale.app.\n• Пользователю не нужна внешняя среда; перед публикацией состав пакета проверяется.\n• Аудиодвижок и пороги контроля качества не изменены.",
    "ja": "• 自己完結型macOS版として、Python、PySide6/Qt、検証済みのネイティブFFmpegをLUFScale.appに同梱しました。\n• 利用者側の外部ランタイムは不要で、公開前にパッケージ内容を検証します。\n• 音声エンジンと品質管理しきい値は変更していません。",
    "hi": "• स्व-संपूर्ण macOS वितरण: Python, PySide6/Qt और सत्यापित मूल FFmpeg LUFScale.app में शामिल हैं।\n• अंतिम उपयोगकर्ता को बाहरी कार्यपरिवेश की आवश्यकता नहीं; प्रकाशन से पहले पैकेज की सामग्री जाँची जाती है।\n• ध्वनि इंजन और गुणवत्ता-जाँच की सीमाएँ अपरिवर्तित हैं।",
    "zh": "• 自包含macOS发行版：Python、PySide6/Qt和经验证的原生FFmpeg均内置于LUFScale.app。\n• 最终用户无需外部运行环境；发布前会验证软件包内容。\n• 音频引擎和质量控制阈值未改变。",
    "ko": "• 자체 포함 macOS 배포판으로 Python, PySide6/Qt와 검증된 네이티브 FFmpeg를 LUFScale.app에 내장했습니다.\n• 사용자는 외부 런타임이 필요 없으며 게시 전에 패키지 내용을 검증합니다.\n• 오디오 엔진과 품질 관리 임계값은 변경되지 않았습니다.",
    "id": "• Distribusi macOS mandiri: Python, PySide6/Qt, dan FFmpeg native terverifikasi tertanam di LUFScale.app.\n• Pengguna akhir tidak memerlukan runtime eksternal; isi paket diverifikasi sebelum diterbitkan.\n• Mesin audio dan ambang kontrol mutu tidak berubah.",
    "tr": "• Bağımsız macOS dağıtımı: Python, PySide6/Qt ve doğrulanmış yerel FFmpeg LUFScale.app içine gömülüdür.\n• Son kullanıcı haricî çalışma zamanı kurmaz; paket yayımdan önce içeriğini doğrular.\n• Ses motoru ve kalite denetimi eşikleri değişmedi.",
}

_AUTOMATIC_BUILD_BODY = {
    "fr": "Version publiée : Apple Silicon. La variante Intel x86_64 n’est ni validée ni garantie. Sur un Mac Intel avec macOS 12 ou ultérieur :\n\n1. Décompressez complètement le paquet source.\n2. Connectez le Mac à Internet.\n3. Lancez “./Create_Community_Distribution_macOS.command”.\n4. Si macOS demande les outils de ligne de commande Xcode, terminez leur installation et gardez la fenêtre Terminal ouverte : le constructeur détecte les outils puis reprend automatiquement, sans être relancé.\n\nLe constructeur télécharge Python 3.13.15 depuis python.org, vérifie son SHA-256 et sa signature Developer ID, l’installe pour la construction et utilise son propre outil pkg-config. Il compile ensuite FFmpeg et embarque Python avec PySide6/Qt dans LUFScale.app.\n\nContrôle : commande “file” sur “dist/LUFScale.app/Contents/MacOS/LUFScale”, puis sur “dist/LUFScale.app/Contents/Frameworks/ffmpeg”. Les deux doivent indiquer x86_64 ; cela ne remplace pas un essai fonctionnel sur Mac Intel.",
    "en": "Published version: Apple Silicon. The Intel x86_64 variant is unvalidated and not guaranteed. On an Intel Mac running macOS 12 or later:\n\n1. Extract the complete source package.\n2. Connect the Mac to the Internet.\n3. Run “./Create_Community_Distribution_macOS.command”.\n4. If macOS requests the Xcode Command Line Tools, finish their installation and keep the Terminal window open: the builder detects the tools and resumes automatically, without being restarted.\n\nThe builder downloads Python 3.13.15 from python.org, verifies its SHA-256 and Developer ID signature, installs it for the build, and uses its own pkg-config helper. It then builds FFmpeg and embeds Python with PySide6/Qt in LUFScale.app.\n\nCheck with “file” on “dist/LUFScale.app/Contents/MacOS/LUFScale”, then on “dist/LUFScale.app/Contents/Frameworks/ffmpeg”. Both must report x86_64; this does not replace functional testing on an Intel Mac.",
    "es": "Versión publicada: Apple Silicon. La variante Intel x86_64 no está validada ni garantizada. En un Mac Intel con macOS 12 o posterior:\n\n1. Extraiga por completo el paquete fuente.\n2. Conecte el Mac a Internet.\n3. Ejecute “./Create_Community_Distribution_macOS.command”.\n4. Si macOS solicita las herramientas de línea de comandos de Xcode, finalice la instalación y mantenga abierta la ventana de Terminal: el constructor detecta las herramientas y continúa automáticamente, sin reiniciarlo.\n\nEl constructor descarga Python 3.13.15 desde python.org, verifica su SHA-256 y la firma Developer ID, lo instala para la compilación y utiliza su propio auxiliar pkg-config. Después compila FFmpeg e integra Python con PySide6/Qt en LUFScale.app.\n\nCompruebe con “file” sobre “dist/LUFScale.app/Contents/MacOS/LUFScale” y luego sobre “dist/LUFScale.app/Contents/Frameworks/ffmpeg”. Ambos deben indicar x86_64; esto no sustituye las pruebas funcionales en un Mac Intel.",
    "it": "Versione pubblicata: Apple Silicon. La variante Intel x86_64 non è convalidata né garantita. Su un Mac Intel con macOS 12 o successivo:\n\n1. Estrarre completamente il pacchetto sorgente.\n2. Collegare il Mac a Internet.\n3. Eseguire “./Create_Community_Distribution_macOS.command”.\n4. Se macOS richiede gli strumenti da riga di comando Xcode, completarne l’installazione e lasciare aperta la finestra Terminale: il costruttore rileva gli strumenti e riprende automaticamente, senza essere riavviato.\n\nIl costruttore scarica Python 3.13.15 da python.org, ne verifica SHA-256 e firma Developer ID, lo installa per la compilazione e usa il proprio strumento pkg-config. Compila quindi FFmpeg e integra Python con PySide6/Qt in LUFScale.app.\n\nControllare con “file” su “dist/LUFScale.app/Contents/MacOS/LUFScale” e poi su “dist/LUFScale.app/Contents/Frameworks/ffmpeg”. Entrambi devono indicare x86_64; ciò non sostituisce i test funzionali su un Mac Intel.",
    "pt": "Versão publicada: Apple Silicon. A variante Intel x86_64 não está validada nem garantida. Num Mac Intel com macOS 12 ou posterior:\n\n1. Extraia completamente o pacote fonte.\n2. Ligue o Mac à Internet.\n3. Execute “./Create_Community_Distribution_macOS.command”.\n4. Se o macOS pedir as ferramentas de linha de comandos Xcode, conclua a instalação e mantenha a janela do Terminal aberta: o construtor deteta as ferramentas e continua automaticamente, sem ser reiniciado.\n\nO construtor transfere Python 3.13.15 de python.org, verifica o SHA-256 e a assinatura Developer ID, instala-o para a compilação e utiliza o seu próprio auxiliar pkg-config. Depois compila o FFmpeg e integra Python com PySide6/Qt em LUFScale.app.\n\nVerifique com “file” em “dist/LUFScale.app/Contents/MacOS/LUFScale” e depois em “dist/LUFScale.app/Contents/Frameworks/ffmpeg”. Ambos devem indicar x86_64; isto não substitui testes funcionais num Mac Intel.",
    "ru": "Опубликованная версия предназначена для Apple Silicon. Вариант Intel x86_64 не проверен и не гарантируется. На Mac Intel с macOS 12 или новее:\n\n1. Полностью распакуйте пакет исходного кода.\n2. Подключите Mac к Интернету.\n3. Запустите «./Create_Community_Distribution_macOS.command».\n4. Если macOS запросит Xcode Command Line Tools, установите их, не закрывая Terminal: сборка продолжится сама.\n\nСборщик загружает Python 3.13.15 с python.org, проверяет SHA-256 и подпись Developer ID, устанавливает его для сборки и использует собственный помощник pkg-config. Затем он собирает FFmpeg и встраивает Python с PySide6/Qt в LUFScale.app.\n\nПроверьте командой «file» файлы «dist/LUFScale.app/Contents/MacOS/LUFScale» и «dist/LUFScale.app/Contents/Frameworks/ffmpeg». Оба результата должны содержать x86_64; это не заменяет функциональные испытания на Mac Intel.",
    "ja": "公開版はApple Silicon向けです。Intel x86_64版は未検証で、動作保証はありません。macOS 12以降のIntel Macでは次の手順を行います。\n\n1. ソースパッケージを完全に展開します。\n2. Macをインターネットに接続します。\n3. 「./Create_Community_Distribution_macOS.command」を実行します。\n4. macOSからXcode Command Line Toolsを求められた場合は、インストールを完了しTerminalウインドウを開いたままにします。ビルダーがツールを検出して自動的に再開するため、再実行は不要です。\n\nビルダーはpython.orgからPython 3.13.15をダウンロードし、SHA-256とDeveloper ID署名を検証してビルド用にインストールし、内蔵のpkg-config補助ツールを使用します。その後FFmpegをビルドし、PythonとPySide6/QtをLUFScale.appに組み込みます。\n\n「file」で「dist/LUFScale.app/Contents/MacOS/LUFScale」と「dist/LUFScale.app/Contents/Frameworks/ffmpeg」を確認します。両方にx86_64が表示される必要がありますが、Intel Macでの機能試験の代わりにはなりません。",
    "hi": "प्रकाशित संस्करण Apple Silicon के लिए है। Intel x86_64 संस्करण सत्यापित या सुनिश्चित नहीं है। macOS 12 या बाद वाले Intel Mac पर:\n\n1. पूरा स्रोत पैकेज निकालें।\n2. Mac को इंटरनेट से जोड़ें।\n3. “./Create_Community_Distribution_macOS.command” चलाएँ।\n4. यदि macOS Xcode Command Line Tools माँगे, तो स्थापना पूरी करें और Terminal विंडो खुली रखें: बिल्डर साधनों का पता लगाकर अपने-आप आगे बढ़ेगा; उसे फिर चलाने की आवश्यकता नहीं है।\n\nबिल्डर python.org से Python 3.13.15 डाउनलोड करता है, उसके SHA-256 और Developer ID हस्ताक्षर की जाँच करता है, उसे निर्माण के लिए स्थापित करता है और अपना pkg-config सहायक उपयोग करता है। फिर वह FFmpeg बनाकर Python और PySide6/Qt को LUFScale.app में शामिल करता है।\n\n“file” से “dist/LUFScale.app/Contents/MacOS/LUFScale” और फिर “dist/LUFScale.app/Contents/Frameworks/ffmpeg” जाँचें। दोनों में x86_64 होना चाहिए; यह Intel Mac पर वास्तविक परीक्षण का विकल्प नहीं है।",
    "zh": "发布版面向Apple Silicon。Intel x86_64版本未经验证，也不保证运行。在装有macOS 12或更高版本的Intel Mac上：\n\n1. 完整解压源代码包。\n2. 将Mac连接到互联网。\n3. 运行“./Create_Community_Distribution_macOS.command”。\n4. 如果macOS要求安装Xcode命令行工具，请完成安装并保持Terminal窗口打开：构建器会检测到这些工具并自动继续，无需重新运行。\n\n构建器从python.org下载Python 3.13.15，验证其SHA-256和Developer ID签名，将其安装用于构建，并使用内置的pkg-config辅助工具。随后它会构建FFmpeg，并把Python和PySide6/Qt嵌入LUFScale.app。\n\n使用“file”检查“dist/LUFScale.app/Contents/MacOS/LUFScale”和“dist/LUFScale.app/Contents/Frameworks/ffmpeg”。两者都必须显示x86_64；这不能替代Intel Mac上的功能测试。",
    "ko": "배포 버전은 Apple Silicon용입니다. Intel x86_64 버전은 검증되지 않았으며 동작을 보장하지 않습니다. macOS 12 이상 Intel Mac에서:\n\n1. 전체 소스 패키지의 압축을 풉니다.\n2. Mac을 인터넷에 연결합니다.\n3. “./Create_Community_Distribution_macOS.command”를 실행합니다.\n4. macOS에서 Xcode Command Line Tools를 요청하면 설치를 완료하고 Terminal 창을 열어 둡니다. 빌더가 도구를 감지해 자동으로 계속하므로 다시 실행할 필요가 없습니다.\n\n빌더는 python.org에서 Python 3.13.15를 다운로드하고 SHA-256과 Developer ID 서명을 확인한 뒤 빌드용으로 설치하며 내장 pkg-config 도우미를 사용합니다. 그런 다음 FFmpeg를 빌드하고 Python과 PySide6/Qt를 LUFScale.app에 포함합니다.\n\n“file”로 “dist/LUFScale.app/Contents/MacOS/LUFScale”과 “dist/LUFScale.app/Contents/Frameworks/ffmpeg”를 확인합니다. 둘 다 x86_64를 표시해야 하며 Intel Mac 기능 시험을 대신하지 않습니다.",
    "id": "Versi terbitan ditujukan untuk Apple Silicon. Varian Intel x86_64 belum divalidasi dan tidak dijamin. Pada Mac Intel dengan macOS 12 atau lebih baru:\n\n1. Ekstrak seluruh paket sumber.\n2. Sambungkan Mac ke Internet.\n3. Jalankan “./Create_Community_Distribution_macOS.command”.\n4. Jika macOS meminta Xcode Command Line Tools, selesaikan pemasangannya dan biarkan jendela Terminal terbuka: pembangun mendeteksi alat tersebut lalu melanjutkan otomatis tanpa dijalankan ulang.\n\nPembangun mengunduh Python 3.13.15 dari python.org, memverifikasi SHA-256 dan tanda tangan Developer ID, memasangnya untuk proses pembangunan, serta memakai pembantu pkg-config miliknya sendiri. Setelah itu pembangun menyusun FFmpeg dan menyertakan Python dengan PySide6/Qt ke dalam LUFScale.app.\n\nPeriksa dengan “file” pada “dist/LUFScale.app/Contents/MacOS/LUFScale”, lalu “dist/LUFScale.app/Contents/Frameworks/ffmpeg”. Keduanya harus menampilkan x86_64; hal ini tidak menggantikan pengujian fungsi pada Mac Intel.",
    "tr": "Yayımlanan sürüm Apple Silicon içindir. Intel x86_64 çeşidi doğrulanmamıştır ve garanti edilmez. macOS 12 veya üzeri Intel Mac’te:\n\n1. Kaynak paketinin tamamını açın.\n2. Mac’i internete bağlayın.\n3. “./Create_Community_Distribution_macOS.command” dosyasını çalıştırın.\n4. macOS Xcode Komut Satırı Araçlarını isterse kurulumu tamamlayın ve Terminal penceresini açık tutun: oluşturucu araçları algılayıp otomatik olarak devam eder; yeniden çalıştırılması gerekmez.\n\nOluşturucu Python 3.13.15’i python.org’dan indirir, SHA-256 ve Developer ID imzasını doğrular, derleme için kurar ve kendi pkg-config yardımcısını kullanır. Ardından FFmpeg’i derler ve Python ile PySide6/Qt’yi LUFScale.app içine gömer.\n\n“file” ile “dist/LUFScale.app/Contents/MacOS/LUFScale” ve ardından “dist/LUFScale.app/Contents/Frameworks/ffmpeg” dosyalarını denetleyin. İkisi de x86_64 göstermelidir; bu, Intel Mac işlev testinin yerini tutmaz.",
}

_PRIVATE_BUILD_PARAGRAPH = {
    "fr": "Le constructeur télécharge uv 0.12.5, vérifie son SHA-256, puis place un CPython 3.13.15 portable uniquement dans .build-tools. Il ne lance pas sudo, ne modifie ni /Library ni le PATH et utilise aussi son propre outil pkg-config. Il compile ensuite FFmpeg et embarque Python avec PySide6/Qt dans LUFScale.app.",
    "en": "The builder downloads uv 0.12.5, verifies its SHA-256, then places portable CPython 3.13.15 only inside .build-tools. It does not run sudo or modify /Library or PATH, and it also uses its own pkg-config helper. It then builds FFmpeg and embeds Python with PySide6/Qt in LUFScale.app.",
    "es": "El constructor descarga uv 0.12.5, verifica su SHA-256 y coloca CPython 3.13.15 portátil únicamente en .build-tools. No ejecuta sudo ni modifica /Library o PATH, y también utiliza su propio auxiliar pkg-config. Después compila FFmpeg e integra Python con PySide6/Qt en LUFScale.app.",
    "it": "Il costruttore scarica uv 0.12.5, ne verifica lo SHA-256 e colloca CPython 3.13.15 portatile solo in .build-tools. Non esegue sudo né modifica /Library o PATH e usa anche il proprio strumento pkg-config. Compila quindi FFmpeg e integra Python con PySide6/Qt in LUFScale.app.",
    "pt": "O construtor transfere uv 0.12.5, verifica o SHA-256 e coloca o CPython 3.13.15 portátil apenas em .build-tools. Não executa sudo nem altera /Library ou PATH e utiliza também o seu próprio auxiliar pkg-config. Depois compila o FFmpeg e integra Python com PySide6/Qt em LUFScale.app.",
    "ru": "Сборщик загружает uv 0.12.5, проверяет SHA-256 и размещает переносимый CPython 3.13.15 только в .build-tools. Он не запускает sudo, не изменяет /Library или PATH и использует собственный помощник pkg-config. Затем он собирает FFmpeg и встраивает Python с PySide6/Qt в LUFScale.app.",
    "ja": "ビルダーはuv 0.12.5をダウンロードしてSHA-256を検証し、ポータブルCPython 3.13.15を.build-tools内だけに配置します。sudoを実行せず、/LibraryやPATHを変更せず、内蔵のpkg-config補助ツールも使用します。その後FFmpegをビルドし、PythonとPySide6/QtをLUFScale.appに組み込みます。",
    "hi": "बिल्डर uv 0.12.5 डाउनलोड करके उसका SHA-256 जाँचता है और पोर्टेबल CPython 3.13.15 को केवल .build-tools में रखता है। यह sudo नहीं चलाता, /Library या PATH नहीं बदलता और अपना pkg-config सहायक भी उपयोग करता है। फिर FFmpeg बनाकर Python और PySide6/Qt को LUFScale.app में शामिल करता है।",
    "zh": "构建器下载uv 0.12.5并验证其SHA-256，然后只在.build-tools中放置便携式CPython 3.13.15。它不运行sudo，不修改/Library或PATH，并使用内置的pkg-config辅助工具。随后构建FFmpeg，并把Python和PySide6/Qt嵌入LUFScale.app。",
    "ko": "빌더는 uv 0.12.5를 다운로드해 SHA-256을 확인하고 휴대형 CPython 3.13.15를 .build-tools 안에만 둡니다. sudo를 실행하거나 /Library 또는 PATH를 변경하지 않으며 내장 pkg-config 도우미도 사용합니다. 그런 다음 FFmpeg를 빌드하고 Python과 PySide6/Qt를 LUFScale.app에 포함합니다.",
    "id": "Pembangun mengunduh uv 0.12.5, memverifikasi SHA-256, lalu menempatkan CPython 3.13.15 portabel hanya di .build-tools. Pembangun tidak menjalankan sudo atau mengubah /Library maupun PATH, serta memakai pembantu pkg-config miliknya sendiri. Setelah itu FFmpeg disusun dan Python beserta PySide6/Qt dimasukkan ke LUFScale.app.",
    "tr": "Oluşturucu uv 0.12.5’i indirip SHA-256 değerini doğrular ve taşınabilir CPython 3.13.15’i yalnızca .build-tools içine yerleştirir. sudo çalıştırmaz, /Library veya PATH’i değiştirmez ve kendi pkg-config yardımcısını kullanır. Ardından FFmpeg’i derler ve Python ile PySide6/Qt’yi LUFScale.app içine gömer.",
}

_PRIVATE_VERSION_CHANGE = {
    "fr": "• Le constructeur accepte maintenant la vérification de version demandée par LAME 4.0, contrôle l’ABI C native et conserve le journal complet en cas d’échec.",
    "en": "• The builder now accepts LAME 4.0's version probe, verifies the native C ABI and preserves the complete log if configuration fails.",
    "es": "• El constructor acepta ahora la comprobación de versión de LAME 4.0, verifica la ABI C nativa y conserva el registro completo si falla la configuración.",
    "it": "• Il costruttore ora accetta il controllo di versione richiesto da LAME 4.0, verifica l’ABI C nativa e conserva il registro completo in caso di errore.",
    "pt": "• O construtor aceita agora a verificação de versão do LAME 4.0, verifica a ABI C nativa e conserva o registo completo em caso de falha.",
    "ru": "• Сборщик теперь принимает проверку версии LAME 4.0, проверяет нативный ABI C и сохраняет полный журнал при сбое настройки.",
    "ja": "• ビルダーはLAME 4.0のバージョン確認に対応し、ネイティブC ABIを検証して、構成に失敗した場合は完全なログを保存します。",
    "hi": "• बिल्डर अब LAME 4.0 की संस्करण जाँच स्वीकार करता है, मूल C ABI की जाँच करता है और विफलता पर पूरा लॉग सुरक्षित रखता है।",
    "zh": "• 构建器现在支持LAME 4.0的版本检查，验证原生C ABI，并在配置失败时保存完整日志。",
    "ko": "• 빌더는 이제 LAME 4.0의 버전 확인을 지원하고 네이티브 C ABI를 검증하며 구성 실패 시 전체 로그를 보존합니다.",
    "id": "• Pembangun kini menerima pemeriksaan versi LAME 4.0, memverifikasi ABI C native, dan menyimpan log lengkap jika konfigurasi gagal.",
    "tr": "• Oluşturucu artık LAME 4.0’ın sürüm denetimini kabul eder, yerel C ABI’yi doğrular ve hata durumunda tam günlüğü saklar.",
}

_PRIVATE_AUTOMATIC_BUILD_BODY = {}
for _language, _body in _AUTOMATIC_BUILD_BODY.items():
    _sections = _body.split("\n\n")
    if len(_sections) != 4:
        raise ValueError(f"unexpected Intel build guide structure: {_language}")
    _PRIVATE_AUTOMATIC_BUILD_BODY[_language] = "\n\n".join(
        (_sections[0], _sections[1], _PRIVATE_BUILD_PARAGRAPH[_language], _sections[3])
    )

_BASE_FEATURE = {
    language: TRANSLATION_UPDATES_201000[language]["guide_license_feature"]
    for language in TRANSLATION_UPDATES_201000
}
_BASE_FEATURE["hi"] = TRANSLATION_UPDATES_201500["hi"][
    "guide_license_feature"
]


_WEBSITE_TEXTS = {
    "fr": {
        "official_website": "Site officiel",
        "official_website_tooltip": "Ouvrir le site officiel de LUFScale",
    },
    "en": {
        "official_website": "Official website",
        "official_website_tooltip": "Open the official LUFScale website",
    },
    "es": {
        "official_website": "Sitio web oficial",
        "official_website_tooltip": "Abrir el sitio web oficial de LUFScale",
    },
    "it": {
        "official_website": "Sito web ufficiale",
        "official_website_tooltip": "Apri il sito web ufficiale di LUFScale",
    },
    "pt": {
        "official_website": "Site oficial",
        "official_website_tooltip": "Abrir o site oficial do LUFScale",
    },
    "ru": {
        "official_website": "Официальный сайт",
        "official_website_tooltip": "Открыть официальный сайт LUFScale",
    },
    "ja": {
        "official_website": "公式サイト",
        "official_website_tooltip": "LUFScaleの公式サイトを開く",
    },
    "hi": {
        "official_website": "आधिकारिक वेबसाइट",
        "official_website_tooltip": "LUFScale की आधिकारिक वेबसाइट खोलें",
    },
    "zh": {
        "official_website": "官方网站",
        "official_website_tooltip": "打开 LUFScale 官方网站",
    },
    "ko": {
        "official_website": "공식 웹사이트",
        "official_website_tooltip": "LUFScale 공식 웹사이트 열기",
    },
    "id": {
        "official_website": "Situs web resmi",
        "official_website_tooltip": "Buka situs web resmi LUFScale",
    },
    "tr": {
        "official_website": "Resmî web sitesi",
        "official_website_tooltip": "LUFScale resmî web sitesini aç",
    },
}


TRANSLATION_UPDATES_211000 = {
    language: {
        **TRANSLATION_UPDATES_201700[language],
        **_WEBSITE_TEXTS[language],
        "guide_license_feature": (
            _BASE_FEATURE[language]
            + "\n"
            + _AUTONOMOUS_FEATURE[language]
        ),
        "guide_intel_build_body": _PRIVATE_AUTOMATIC_BUILD_BODY[language],
        "version_changes": (
            _PRIVATE_VERSION_CHANGE[language]
            + "\n"
            + _VERSION_CHANGES[language]
        ),
    }
    for language in TRANSLATION_UPDATES_201700
}


__all__ = ["TRANSLATION_UPDATES_211000"]
