"""Localized Windows build instructions for the PDF technical appendix."""


BUILD_COMMAND = r".\Create_Offline_Installer_Windows.cmd"
WINDOWS_SETUP_PATH = r"dist\LUFScale-2.1.12-Setup-x64.exe"
WINDOWS_PORTABLE_PATH = r"dist\LUFScale-2.1.12-Portable-x64.exe"
WINDOWS_SETUP_CHECKSUM_PATH = f"{WINDOWS_SETUP_PATH}.sha256"
WINDOWS_PORTABLE_CHECKSUM_PATH = f"{WINDOWS_PORTABLE_PATH}.sha256"
SPACER_LINE = " "


def _body(
    intro: str,
    windows_instruction: str,
    created_label: str,
    setup_description: str,
    portable_description: str,
    checksum_description: str,
) -> str:
    """Keep the command and generated Windows paths on dedicated guide lines."""
    return (
        f"{intro}\n{SPACER_LINE}\n"
        f"{windows_instruction}\n{SPACER_LINE}\n"
        f"\t**{BUILD_COMMAND}**\n{SPACER_LINE}\n"
        f"{created_label}\n{SPACER_LINE}\n"
        f"\t**{WINDOWS_SETUP_PATH}**\n"
        f"\t**{WINDOWS_SETUP_CHECKSUM_PATH}**\n"
        f"\t**{WINDOWS_PORTABLE_PATH}**\n"
        f"\t**{WINDOWS_PORTABLE_CHECKSUM_PATH}**\n{SPACER_LINE}\n"
        f"{setup_description}\n"
        f"{portable_description}\n"
        f"{checksum_description}"
    )


PLATFORM_BUILD_COPY = {
    "fr": {
        "title": "Compiler pour Windows",
        "body": _body(
            "Chemins relatifs à la racine du paquet source décompressé :",
            "Windows (x64) - Sous Windows 10 1809 ou une version ultérieure, ou sous Windows 11 64 bits, lancez :",
            "Fichiers créés :",
            ".exe Setup (recommandé pour installer normalement LUFScale et l’utiliser régulièrement)",
            ".exe Portable (sans installation, à lancer directement ou à transporter sur un autre ordinateur)",
            ".sha256 (empreinte SHA-256 du fichier .exe correspondant)",
        ),
    },
    "en": {
        "title": "Build for Windows",
        "body": _body(
            "Paths are relative to the extracted source-package root:",
            "Windows (x64) - On 64-bit Windows 10 1809 or later, or Windows 11, run:",
            "Created files:",
            ".exe Setup (recommended for installing LUFScale normally and using it regularly)",
            ".exe Portable (no installation, run directly or carry to another computer)",
            ".sha256 (SHA-256 fingerprint of the corresponding .exe file)",
        ),
    },
    "es": {
        "title": "Compilar para Windows",
        "body": _body(
            "Rutas relativas a la raíz del paquete fuente descomprimido:",
            "Windows (x64) - En Windows 10 1809 o posterior, o Windows 11 de 64 bits, ejecute:",
            "Archivos creados:",
            ".exe Setup (recomendado para instalar LUFScale normalmente y usarlo con regularidad)",
            ".exe Portable (sin instalación, para ejecutarlo directamente o llevarlo a otro ordenador)",
            ".sha256 (huella SHA-256 del archivo .exe correspondiente)",
        ),
    },
    "it": {
        "title": "Compilare per Windows",
        "body": _body(
            "Percorsi relativi alla radice del pacchetto sorgente estratto:",
            "Windows (x64) - Su Windows 10 1809 o successivo, oppure Windows 11 a 64 bit, eseguire:",
            "File creati:",
            ".exe Setup (consigliato per installare normalmente LUFScale e usarlo regolarmente)",
            ".exe Portable (senza installazione, da avviare direttamente o portare su un altro computer)",
            ".sha256 (impronta SHA-256 del file .exe corrispondente)",
        ),
    },
    "pt": {
        "title": "Compilar para Windows",
        "body": _body(
            "Caminhos relativos à raiz do pacote-fonte descompactado:",
            "Windows (x64) - No Windows 10 1809 ou posterior, ou Windows 11 de 64 bits, execute:",
            "Ficheiros criados:",
            ".exe Setup (recomendado para instalar normalmente o LUFScale e utilizá-lo regularmente)",
            ".exe Portable (sem instalação, para iniciar diretamente ou transportar para outro computador)",
            ".sha256 (impressão digital SHA-256 do ficheiro .exe correspondente)",
        ),
    },
    "ru": {
        "title": "Сборка для Windows",
        "body": _body(
            "Пути указаны от корня распакованного пакета с исходным кодом:",
            "Windows (x64) - В 64-разрядной Windows 10 1809 или новее либо Windows 11 запустите:",
            "Созданные файлы:",
            ".exe Setup (рекомендуется для обычной установки и постоянного использования LUFScale)",
            ".exe Portable (без установки, для прямого запуска или переноса на другой компьютер)",
            ".sha256 (отпечаток SHA-256 соответствующего файла .exe)",
        ),
    },
    "ja": {
        "title": "Windows向けのビルド",
        "body": _body(
            "パスは展開したソースパッケージのルート基準です:",
            "Windows (x64) - 64ビット版Windows 10 1809以降またはWindows 11で次を実行します:",
            "作成されるファイル:",
            ".exe Setup (LUFScaleを通常どおりインストールして継続利用する推奨版)",
            ".exe Portable (インストール不要で、直接起動または別のコンピューターへ持ち運び可能)",
            ".sha256 (対応する.exeファイルのSHA-256フィンガープリント)",
        ),
    },
    "hi": {
        "title": "Windows के लिए build",
        "body": _body(
            "Paths extract किए गए source package के root से relative हैं:",
            "Windows (x64) - 64-bit Windows 10 1809 या बाद में, या Windows 11 पर यह चलाएँ:",
            "बनाए गए files:",
            ".exe Setup (LUFScale को सामान्य रूप से install और नियमित उपयोग करने के लिए अनुशंसित)",
            ".exe Portable (बिना installation, सीधे चलाने या दूसरे computer पर ले जाने के लिए)",
            ".sha256 (संबंधित .exe file का SHA-256 fingerprint)",
        ),
    },
    "zh": {
        "title": "为Windows编译",
        "body": _body(
            "路径均相对于已解压源代码包的根目录:",
            "Windows (x64) - 在64位Windows 10 1809或更高版本，或Windows 11中运行:",
            "创建的文件:",
            ".exe Setup (推荐，用于正常安装LUFScale并日常使用)",
            ".exe Portable (无需安装，可直接运行或带到另一台电脑)",
            ".sha256 (对应.exe文件的SHA-256指纹)",
        ),
    },
    "ko": {
        "title": "Windows용 빌드",
        "body": _body(
            "모든 경로는 압축을 푼 소스 패키지 루트를 기준으로 합니다:",
            "Windows (x64) - 64비트 Windows 10 1809 이상 또는 Windows 11에서 다음을 실행합니다:",
            "생성되는 파일:",
            ".exe Setup (LUFScale을 일반 방식으로 설치해 정기적으로 사용할 때 권장)",
            ".exe Portable (설치 없이 바로 실행하거나 다른 컴퓨터로 옮길 수 있음)",
            ".sha256 (해당 .exe 파일의 SHA-256 지문)",
        ),
    },
    "id": {
        "title": "Build untuk Windows",
        "body": _body(
            "Semua path relatif terhadap root paket sumber yang diekstrak:",
            "Windows (x64) - Pada Windows 10 1809 atau lebih baru, atau Windows 11 64-bit, jalankan:",
            "File yang dibuat:",
            ".exe Setup (disarankan untuk memasang LUFScale secara normal dan menggunakannya secara rutin)",
            ".exe Portable (tanpa instalasi, dijalankan langsung atau dibawa ke komputer lain)",
            ".sha256 (sidik SHA-256 dari berkas .exe yang sesuai)",
        ),
    },
    "tr": {
        "title": "Windows için derleme",
        "body": _body(
            "Tüm yollar çıkarılmış kaynak paketinin kök dizinine göredir:",
            "Windows (x64) - 64 bit Windows 10 1809 veya üzeri ya da Windows 11'de şunu çalıştırın:",
            "Oluşturulan dosyalar:",
            ".exe Setup (LUFScale'i normal şekilde kurup düzenli kullanmak için önerilir)",
            ".exe Portable (kurulum gerektirmez, doğrudan çalıştırılır veya başka bir bilgisayara taşınır)",
            ".sha256 (ilgili .exe dosyasının SHA-256 parmak izi)",
        ),
    },
}


__all__ = ["PLATFORM_BUILD_COPY"]
