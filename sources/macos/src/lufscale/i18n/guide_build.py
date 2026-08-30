"""Localized macOS build instructions for the PDF technical appendix."""


BUILD_COMMAND = "./Create_Community_Distribution_macOS.command"
APP_PATH = "dist/LUFScale.app"
ARM64_ARCHIVE_PATH = "dist/LUFScale-2.1.12-macOS-arm64-community.zip"
INTEL_ARCHIVE_PATH = "dist/LUFScale-2.1.12-macOS-x86_64-community.zip"
ARM64_CHECKSUM_PATH = f"{ARM64_ARCHIVE_PATH}.sha256"
INTEL_CHECKSUM_PATH = f"{INTEL_ARCHIVE_PATH}.sha256"
SPACER_LINE = " "


def _body(
    intro: str,
    app_description: str,
    archive_description: str,
    checksum_description: str,
    apple_instruction: str,
    created_label: str,
    intel_instruction: str,
    intel_note: str,
) -> str:
    """Keep commands and generated macOS paths on dedicated guide lines."""
    return (
        f"{intro}\n{SPACER_LINE}\n"
        f"{apple_instruction}\n{SPACER_LINE}\n"
        f"\t**{BUILD_COMMAND}**\n{SPACER_LINE}\n"
        f"{created_label}\n{SPACER_LINE}\n"
        f"\t**{APP_PATH}**\n"
        f"\t**{ARM64_ARCHIVE_PATH}**\n"
        f"\t**{ARM64_CHECKSUM_PATH}**\n{SPACER_LINE}\n"
        f"{intel_instruction}\n{SPACER_LINE}\n"
        f"\t**{BUILD_COMMAND}**\n{SPACER_LINE}\n"
        f"{intel_note}\n{SPACER_LINE}\n"
        f"{created_label}\n{SPACER_LINE}\n"
        f"\t**{APP_PATH}**\n"
        f"\t**{INTEL_ARCHIVE_PATH}**\n"
        f"\t**{INTEL_CHECKSUM_PATH}**\n{SPACER_LINE}\n"
        f"{app_description}\n"
        f"{archive_description}\n"
        f"{checksum_description}"
    )


PLATFORM_BUILD_COPY = {
    "fr": {
        "title": "Compiler pour Mac Apple Silicon et Mac Intel",
        "body": _body(
            "Chemins relatifs à la racine du paquet source décompressé :",
            ".app (application autonome à tester ou utiliser localement)",
            ".zip (archive à partager ou publier, avec l’application, les sources, les licences et les notices)",
            ".sha256 (empreinte SHA-256 du fichier .zip)",
            "Mac Apple Silicon (arm64) - Sous macOS 12 ou une version ultérieure, lancez :",
            "Fichiers créés :",
            "Mac Intel (x86_64) - Sur un Mac Intel, lancez :",
            "Si macOS installe les outils Xcode, gardez le Terminal ouvert : le constructeur reprend automatiquement.",
        ),
    },
    "en": {
        "title": "Build for Apple Silicon Mac and Intel Mac",
        "body": _body(
            "Paths are relative to the extracted source-package root:",
            ".app (self-contained application for local testing or regular use)",
            ".zip (archive to share or publish, with the application, sources, licences and notices)",
            ".sha256 (SHA-256 fingerprint of the .zip file)",
            "Apple Silicon Mac (arm64) - On macOS 12 or later, run:",
            "Created files:",
            "Intel Mac (x86_64) - On an Intel Mac, run:",
            "If macOS installs the Xcode tools, keep Terminal open: the builder resumes automatically.",
        ),
    },
    "es": {
        "title": "Compilar para Mac Apple Silicon y Mac Intel",
        "body": _body(
            "Rutas relativas a la raíz del paquete fuente descomprimido:",
            ".app (aplicación autónoma para pruebas o uso local)",
            ".zip (archivo para compartir o publicar, con la aplicación, las fuentes, las licencias y los avisos)",
            ".sha256 (huella SHA-256 del archivo .zip)",
            "Mac Apple Silicon (arm64) - En macOS 12 o posterior, ejecute:",
            "Archivos creados:",
            "Mac Intel (x86_64) - En un Mac Intel, ejecute:",
            "Si macOS instala las herramientas Xcode, mantenga Terminal abierto: el constructor continúa automáticamente.",
        ),
    },
    "it": {
        "title": "Compilare per Mac Apple Silicon e Mac Intel",
        "body": _body(
            "Percorsi relativi alla radice del pacchetto sorgente estratto:",
            ".app (applicazione autonoma per test o uso locale)",
            ".zip (archivio da condividere o pubblicare, con applicazione, sorgenti, licenze e informative)",
            ".sha256 (impronta SHA-256 del file .zip)",
            "Mac Apple Silicon (arm64) - Su macOS 12 o successivo, eseguire:",
            "File creati:",
            "Mac Intel (x86_64) - Su un Mac Intel, eseguire:",
            "Se macOS installa gli strumenti Xcode, lasciare aperto Terminale: il costruttore riprende automaticamente.",
        ),
    },
    "pt": {
        "title": "Compilar para Mac Apple Silicon e Mac Intel",
        "body": _body(
            "Caminhos relativos à raiz do pacote-fonte descompactado:",
            ".app (aplicação autónoma para teste ou utilização local)",
            ".zip (arquivo para partilhar ou publicar, com aplicação, fontes, licenças e avisos)",
            ".sha256 (impressão digital SHA-256 do ficheiro .zip)",
            "Mac Apple Silicon (arm64) - No macOS 12 ou posterior, execute:",
            "Ficheiros criados:",
            "Mac Intel (x86_64) - Num Mac Intel, execute:",
            "Se o macOS instalar as ferramentas Xcode, mantenha o Terminal aberto: o construtor retoma automaticamente.",
        ),
    },
    "ru": {
        "title": "Сборка для Mac с Apple Silicon и Mac Intel",
        "body": _body(
            "Пути указаны от корня распакованного пакета:",
            ".app (автономное приложение для локального тестирования или использования)",
            ".zip (архив для публикации или передачи с приложением, исходниками, лицензиями и уведомлениями)",
            ".sha256 (отпечаток SHA-256 файла .zip)",
            "Mac с Apple Silicon (arm64) - В macOS 12 или новее запустите:",
            "Созданные файлы:",
            "Mac Intel (x86_64) - На Mac Intel запустите:",
            "Если macOS устанавливает инструменты Xcode, не закрывайте Terminal: сборщик продолжит работу автоматически.",
        ),
    },
    "ja": {
        "title": "Apple Silicon MacおよびIntel Mac向けのビルド",
        "body": _body(
            "パスは展開したソースパッケージのルート基準です:",
            ".app (ローカルテストまたは通常利用向けの自己完結型アプリ)",
            ".zip (共有・公開用アーカイブで、アプリ、ソース、ライセンス、通知を含む)",
            ".sha256 (.zipファイルのSHA-256フィンガープリント)",
            "Apple Silicon Mac (arm64) - macOS 12以降で次を実行します:",
            "作成されるファイル:",
            "Intel Mac (x86_64) - Intel Macで次を実行します:",
            "macOSがXcodeツールをインストールする場合はTerminalを開いたままにすると、ビルダーが自動再開します。",
        ),
    },
    "hi": {
        "title": "Apple Silicon Mac और Intel Mac के लिए build",
        "body": _body(
            "Paths extract किए गए source package के root से relative हैं:",
            ".app (local test या उपयोग के लिए self-contained application)",
            ".zip (share या publish करने का archive, जिसमें application, sources, licences और notices हैं)",
            ".sha256 (.zip file का SHA-256 fingerprint)",
            "Apple Silicon Mac (arm64) - macOS 12 या बाद में यह चलाएँ:",
            "बनाए गए files:",
            "Intel Mac (x86_64) - Intel Mac पर यह चलाएँ:",
            "यदि macOS Xcode tools install करे, तो Terminal खुला रखें: builder अपने आप जारी रहेगा।",
        ),
    },
    "zh": {
        "title": "为Apple Silicon Mac和Intel Mac编译",
        "body": _body(
            "路径均相对于已解压源代码包的根目录:",
            ".app (用于本地测试或日常使用的自包含应用程序)",
            ".zip (用于共享或发布的压缩包，包含应用程序、源代码、许可证和说明)",
            ".sha256 (.zip文件的SHA-256指纹)",
            "Apple Silicon Mac (arm64) - 在macOS 12或更高版本中运行:",
            "创建的文件:",
            "Intel Mac (x86_64) - 在Intel Mac上运行:",
            "如果macOS安装Xcode工具，请保持Terminal开启，构建器会自动继续。",
        ),
    },
    "ko": {
        "title": "Apple Silicon Mac 및 Intel Mac용 빌드",
        "body": _body(
            "모든 경로는 압축을 푼 소스 패키지 루트를 기준으로 합니다:",
            ".app (로컬 테스트 또는 일반 사용을 위한 독립 실행형 앱)",
            ".zip (공유·게시용 아카이브로 앱, 소스, 라이선스 및 고지 사항 포함)",
            ".sha256 (.zip 파일의 SHA-256 지문)",
            "Apple Silicon Mac (arm64) - macOS 12 이상에서 다음을 실행합니다:",
            "생성되는 파일:",
            "Intel Mac (x86_64) - Intel Mac에서 다음을 실행합니다:",
            "macOS가 Xcode 도구를 설치하면 Terminal을 열어 두십시오. 빌더가 자동으로 계속됩니다.",
        ),
    },
    "id": {
        "title": "Build untuk Mac Apple Silicon dan Mac Intel",
        "body": _body(
            "Semua path relatif terhadap root paket sumber yang diekstrak:",
            ".app (aplikasi mandiri untuk pengujian atau penggunaan lokal)",
            ".zip (arsip untuk dibagikan atau dipublikasikan, berisi aplikasi, sumber, lisensi, dan pemberitahuan)",
            ".sha256 (sidik SHA-256 dari berkas .zip)",
            "Mac Apple Silicon (arm64) - Pada macOS 12 atau lebih baru, jalankan:",
            "File yang dibuat:",
            "Mac Intel (x86_64) - Pada Mac Intel, jalankan:",
            "Jika macOS memasang alat Xcode, biarkan Terminal terbuka: builder melanjutkan secara otomatis.",
        ),
    },
    "tr": {
        "title": "Apple Silicon Mac ve Intel Mac için derleme",
        "body": _body(
            "Tüm yollar çıkarılmış kaynak paketinin köküne göredir:",
            ".app (yerel test veya kullanım için bağımsız uygulama)",
            ".zip (paylaşım veya yayımlama arşivi; uygulama, kaynaklar, lisanslar ve bildirimleri içerir)",
            ".sha256 (.zip dosyasının SHA-256 parmak izi)",
            "Apple Silicon Mac (arm64) - macOS 12 veya üzerinde şunu çalıştırın:",
            "Oluşturulan dosyalar:",
            "Intel Mac (x86_64) - Intel Mac'te şunu çalıştırın:",
            "macOS Xcode araçlarını kurarsa Terminal'i açık tutun: oluşturucu otomatik olarak devam eder.",
        ),
    },
}


__all__ = ["PLATFORM_BUILD_COPY"]
