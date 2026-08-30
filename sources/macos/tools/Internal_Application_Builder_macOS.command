#!/bin/zsh

set -eu
script_dir="$(cd -- "$(dirname -- "$0")" && /bin/pwd)"
project_root="$(cd -- "$script_dir/.." && /bin/pwd)"
cd -- "$project_root"

show_error() {
    print -u2 -- "ERROR — $1"
    if [[ "${LUFSCALE_NONINTERACTIVE:-0}" != "1" ]]; then
        /usr/bin/osascript -e "display alert \"LUFScale build\" message \"$1\" as critical"
    fi
}

ensure_command_line_tools() {
    if /usr/bin/xcrun --find clang >/dev/null 2>&1; then
        return
    fi

    echo "The Xcode Command Line Tools are required. macOS will now open its installer."
    /usr/bin/xcode-select --install >/dev/null 2>&1 || true
    echo "Waiting for the Xcode Command Line Tools installation to finish…"
    echo "The LUFScale build will continue automatically; do not close this window."
    echo "Press Control-C only if you want to cancel the build."

    local elapsed=0
    local poll_seconds=10
    local timeout_seconds=14400
    while ! /usr/bin/xcrun --find clang >/dev/null 2>&1; do
        if (( elapsed >= timeout_seconds )); then
            show_error "The Xcode Command Line Tools are still unavailable after four hours. Restart the Mac, then run this builder again."
            exit 1
        fi
        /bin/sleep "$poll_seconds"
        (( elapsed += poll_seconds ))
        if (( elapsed % 60 == 0 )); then
            echo "Still waiting for the Apple installation… ${elapsed} seconds elapsed."
        fi
    done
    echo "The Xcode Command Line Tools are ready. Continuing the LUFScale build automatically…"
}

tree_bytes() {
    local target="$1"
    if [[ ! -d "$target" ]]; then
        print -- "0"
        return
    fi
    /usr/bin/find "$target" -type f -exec /usr/bin/stat -f '%z' {} + \
        | /usr/bin/awk '{ total += $1 } END { print total + 0 }'
}

format_bytes() {
    /usr/bin/awk -v bytes="$1" 'BEGIN { printf "%.1f MiB", bytes / 1048576 }'
}

python_version="3.13.15"
uv_version="0.12.5"
uv_release_base="https://releases.astral.sh/github/uv/releases/download/${uv_version}"
build_tools_dir="$project_root/.build-tools"
download_dir="$build_tools_dir/downloads"
uv_python_dir="$build_tools_dir/python"
uv_cache_dir="$build_tools_dir/uv-cache"
uv_python_bin_dir="$build_tools_dir/python-bin"
bootstrap_python=""
uv_binary=""

sha256_file() {
    /usr/bin/shasum -a 256 "$1" | /usr/bin/awk '{print $1}'
}

download_verified_archive() {
    local url="$1"
    local destination="$2"
    local expected_sha256="$3"
    local description="$4"
    local partial="$destination.partial"
    /bin/mkdir -p "$download_dir"
    if [[ -f "$destination" ]] \
        && [[ "$(sha256_file "$destination")" == "$expected_sha256" ]]; then
        return
    fi
    /bin/rm -f -- "$destination" "$partial"
    echo "Downloading ${description}…"
    /usr/bin/curl \
        --fail \
        --location \
        --proto '=https' \
        --tlsv1.2 \
        --retry 3 \
        --output "$partial" \
        "$url" || {
        /bin/rm -f -- "$partial"
        show_error "${description} could not be downloaded. Check the Internet connection and run the builder again."
        exit 1
    }
    if [[ "$(sha256_file "$partial")" != "$expected_sha256" ]]; then
        /bin/rm -f -- "$partial"
        show_error "${description} failed SHA-256 verification."
        exit 1
    fi
    /bin/mv -f -- "$partial" "$destination"
}

prepare_uv() {
    local uv_target
    local uv_sha256
    case "$target_arch" in
        arm64)
            uv_target="aarch64-apple-darwin"
            uv_sha256="5bb0e5fe008a773c3dbcb97ff79cd89e1241464fe9d2f986d52ad8f1b037bd62"
            ;;
        x86_64)
            uv_target="x86_64-apple-darwin"
            uv_sha256="b3b2137477cf96c9686ebfb71524614cec780c673fd73e59bce099aef02e70e8"
            ;;
    esac

    local uv_archive="$download_dir/uv-${uv_version}-${uv_target}.tar.gz"
    local uv_dir="$build_tools_dir/uv-${uv_version}-${uv_target}"
    uv_binary="$uv_dir/uv"
    if [[ -x "$uv_binary" ]] \
        && [[ "$("$uv_binary" --version | /usr/bin/awk '{print $2}')" == "$uv_version" ]]; then
        return
    fi

    download_verified_archive \
        "$uv_release_base/uv-${uv_target}.tar.gz" \
        "$uv_archive" \
        "$uv_sha256" \
        "the pinned uv ${uv_version} bootstrap"

    local extract_dir
    extract_dir="$(/usr/bin/mktemp -d -t lufscale-uv)"
    /bin/rm -rf -- "$uv_dir"
    /bin/mkdir -p "$uv_dir"
    if ! /usr/bin/tar -xzf "$uv_archive" -C "$extract_dir"; then
        /bin/rm -rf -- "$extract_dir" "$uv_dir"
        show_error "The verified uv archive could not be extracted."
        exit 1
    fi
    local extracted_uv
    extracted_uv="$(/usr/bin/find "$extract_dir" -type f -name uv -print -quit)"
    if [[ -z "$extracted_uv" ]]; then
        /bin/rm -rf -- "$extract_dir" "$uv_dir"
        show_error "The verified uv archive does not contain the expected executable."
        exit 1
    fi
    /bin/cp -f -- "$extracted_uv" "$uv_binary"
    /bin/chmod 755 "$uv_binary"
    /bin/rm -rf -- "$extract_dir"
    if [[ "$("$uv_binary" --version | /usr/bin/awk '{print $2}')" != "$uv_version" ]]; then
        show_error "The private uv bootstrap failed its version check."
        exit 1
    fi
}

python_is_usable() {
    local candidate="$1"
    [[ -x "$candidate" ]] || return 1
    "$candidate" - "$python_version" "$target_arch" <<'PY'
import platform
import sys

expected_version = tuple(int(part) for part in sys.argv[1].split("."))
expected_arch = sys.argv[2]
raise SystemExit(
    0
    if sys.version_info[:3] == expected_version
    and platform.machine() == expected_arch
    else 1
)
PY
}

prepare_python() {
    prepare_uv
    export UV_PYTHON_INSTALL_DIR="$uv_python_dir"
    export UV_CACHE_DIR="$uv_cache_dir"
    export UV_PYTHON_BIN_DIR="$uv_python_bin_dir"
    export UV_NO_MODIFY_PATH=1
    export UV_MANAGED_PYTHON=1

    echo "Preparing private Python ${python_version} without administrator access…"
    "$uv_binary" python install "$python_version" \
        --managed-python \
        --no-config \
        --no-progress || {
        show_error "The private Python runtime could not be downloaded or installed."
        exit 1
    }
    bootstrap_python="$(
        "$uv_binary" python find "$python_version" \
            --managed-python \
            --no-config
    )" || {
        show_error "The private Python runtime could not be located."
        exit 1
    }
    case "$bootstrap_python" in
        "$uv_python_dir"/*) ;;
        *)
            show_error "The selected Python runtime is not inside the private build directory."
            exit 1
            ;;
    esac
    if ! python_is_usable "$bootstrap_python"; then
        show_error "The private Python ${python_version} runtime failed its version or architecture check."
        exit 1
    fi
}

if [[ "$(/usr/bin/uname -s)" != "Darwin" ]]; then
    show_error "A macOS application must be built on a Mac."
    exit 1
fi

host_arch="$(/usr/bin/uname -m)"
target_arch="${LUFSCALE_TARGET_ARCH:-$host_arch}"
case "$target_arch" in
    arm64|x86_64) ;;
    *)
        show_error "Unsupported macOS architecture: $target_arch. Expected arm64 or x86_64. The self-contained application must be built natively for each architecture."
        exit 1
        ;;
esac
if [[ "$target_arch" != "$host_arch" ]]; then
    show_error "The self-contained application must be built on the target architecture. This Mac is $host_arch, but the requested target is $target_arch."
    exit 1
fi
export LUFSCALE_TARGET_ARCH="$target_arch"

ensure_command_line_tools

prepare_python

interface_fonts=(
    "DejaVuSans.ttf"
    "DejaVuSans-Bold.ttf"
    "DejaVuSerif.ttf"
    "NotoSansDevanagari-Regular.ttf"
    "NotoSansDevanagari-Bold.ttf"
    "NotoSansJP-Regular.ttf"
    "NotoSansJP-Bold.ttf"
    "NotoSansSC-Regular.ttf"
    "NotoSansSC-Bold.ttf"
    "NotoSansKR-Regular.ttf"
    "NotoSansKR-Bold.ttf"
)

for font in "${interface_fonts[@]}"; do
    if [[ ! -f "assets/fonts/$font" ]]; then
        show_error "The assets/fonts/$font font is missing. It is required by the multilingual interface."
        exit 1
    fi
done

icon_source="assets/branding/LUFScale_logo.png"
iconset_dir=".construction-macos/LUFScale.iconset"
icon_file=".construction-macos/LUFScale.icns"
if [[ ! -f "$icon_source" ]]; then
    show_error "The $icon_source icon is missing. It is required by the application."
    exit 1
fi

echo "Preparing the build environment…"
build_environment_is_usable() {
    python_is_usable ".construction-macos/bin/python" \
        && [[ -f ".construction-macos/pyvenv.cfg" ]] \
        && /usr/bin/grep -Fq "$uv_python_dir" ".construction-macos/pyvenv.cfg"
}
if [[ -d ".construction-macos" ]] && ! build_environment_is_usable; then
    /bin/rm -rf -- ".construction-macos"
fi
if [[ ! -x ".construction-macos/bin/python" ]]; then
    "$uv_binary" venv ".construction-macos" \
        --python "$bootstrap_python" \
        --managed-python \
        --no-config \
        --no-progress || {
        show_error "The build environment could not be created."
        exit 1
    }
fi

"$uv_binary" pip install \
    --python ".construction-macos/bin/python" \
    --managed-python \
    --no-config \
    --no-progress \
    -r requirements.txt "pyinstaller==6.21.0" "reportlab==4.4.3" || {
    show_error "Build-tool installation failed."
    exit 1
}

/bin/chmod 755 "tools/pkg-config"
export PATH="$project_root/tools:$PATH"
if [[ "$(command -v pkg-config)" != "$project_root/tools/pkg-config" ]]; then
    show_error "The private pkg-config helper could not be activated."
    exit 1
fi

build_version="$(PYTHONPATH=src .construction-macos/bin/python - <<'PY'
from lufscale.version import APP_VERSION

print(APP_VERSION)
PY
)"
if [[ "$build_version" != "2.1.12" ]]; then
    show_error "Unexpected application version: $build_version"
    exit 1
fi

echo "Generating the twelve macOS PDF guides…"
/bin/rm -rf -- "output/pdf"
/bin/mkdir -p "output/pdf"
.construction-macos/bin/python tools/generate_guides.py \
    --output-dir "output/pdf" || {
    show_error "PDF guide generation failed. Review the Terminal messages."
    exit 1
}
pdf_guide_manifest=$(
    PYTHONPATH="src" .construction-macos/bin/python - <<'PY'
from lufscale.resources import PDF_GUIDES

print("\n".join(PDF_GUIDES.values()))
PY
) || {
    show_error "The list of supported PDF guides could not be read."
    exit 1
}
pdf_guides=("${(@f)pdf_guide_manifest}")
if (( ${#pdf_guides[@]} != 12 )); then
    show_error "The macOS build requires exactly twelve PDF guides."
    exit 1
fi
for guide in "${pdf_guides[@]}"; do
    if [[ ! -s "output/pdf/$guide" ]]; then
        show_error "The generated output/pdf/$guide guide is missing or empty."
        exit 1
    fi
done

echo "Building the self-contained FFmpeg engine from verified sources…"
.construction-macos/bin/python tools/build_bundled_ffmpeg_macos.py \
    --target-arch "$target_arch" || {
    show_error "The self-contained FFmpeg engine build failed. Review the Terminal messages."
    exit 1
}
bundled_ffmpeg_path="packaging/generated/ffmpeg/$target_arch/ffmpeg"
if [[ ! -x "$bundled_ffmpeg_path" ]]; then
    show_error "The expected self-contained FFmpeg engine is missing: $bundled_ffmpeg_path"
    exit 1
fi
export LUFSCALE_BUNDLED_FFMPEG="$PWD/$bundled_ffmpeg_path"

for release_file in LICENSE COPYRIGHT README.md OPEN_LUFSCALE_ON_MACOS.md THIRD_PARTY_NOTICES.md SBOM.cdx.json RELEASE_2.1.12.md VALIDATION_2.1.12.md; do
    if [[ ! -f "$release_file" ]]; then
        show_error "The $release_file distribution file is missing."
        exit 1
    fi
done
if [[ ! -d "third_party_licenses" ]]; then
    show_error "The third_party_licenses folder is missing."
    exit 1
fi

echo "Checking the FFmpeg engine manifest…"
for generated_file in FFMPEG_DISTRIBUTION_NOTICE.txt FFMPEG_BUILD_MANIFEST.json; do
    if [[ ! -f "packaging/generated/$generated_file" ]]; then
        show_error "The generated packaging/generated/$generated_file file is missing."
        exit 1
    fi
done
if ! /usr/bin/grep -Fq "LUFScale $build_version" "packaging/generated/FFMPEG_DISTRIBUTION_NOTICE.txt"; then
    show_error "The FFmpeg notice does not match LUFScale $build_version."
    exit 1
fi
if [[ ! -d "packaging/generated/third_party_licenses_ffmpeg" ]]; then
    show_error "The self-contained FFmpeg engine licenses are missing."
    exit 1
fi

echo "Recording the complete embedded runtime…"
.construction-macos/bin/python tools/generate_runtime_manifest.py \
    --ffmpeg "$bundled_ffmpeg_path" \
    --target-arch "$target_arch" \
    --output "packaging/generated/LUFSCALE_RUNTIME_MANIFEST.json" || {
    show_error "The autonomous runtime manifest could not be generated."
    exit 1
}

echo "Creating the macOS icon…"
/bin/mkdir -p "$iconset_dir"
for size in 16 32 128 256 512; do
    /usr/bin/sips -z "$size" "$size" "$icon_source" \
        --out "$iconset_dir/icon_${size}x${size}.png" >/dev/null
    double_size=$((size * 2))
    /usr/bin/sips -z "$double_size" "$double_size" "$icon_source" \
        --out "$iconset_dir/icon_${size}x${size}@2x.png" >/dev/null
done
/usr/bin/iconutil -c icns "$iconset_dir" -o "$icon_file" || {
    show_error "The macOS icon could not be created."
    exit 1
}

echo "Building LUFScale.app…"
.construction-macos/bin/python -m PyInstaller \
    --noconfirm \
    --clean \
    "packaging/macos/LUFScale.spec" || {
    show_error "The application build failed. Review the Terminal messages."
    exit 1
}

if [[ ! -d "dist/LUFScale.app" ]]; then
    show_error "The LUFScale.app bundle was not found after the build."
    exit 1
fi

bundled_ffmpeg=$(
    /usr/bin/find "dist/LUFScale.app" \
        -type f \
        \( -name "ffmpeg" -o -name "ffmpeg.exe" -o -name "ffmpeg-macos-*" \) \
        -print \
        -quit
)
if [[ -z "$bundled_ffmpeg" ]]; then
    show_error "The self-contained FFmpeg executable was not included in LUFScale.app."
    exit 1
fi

bundled_python=$(
    /usr/bin/find "dist/LUFScale.app" -type f \
        \( -name "Python" -o -name "libpython*.dylib" \) \
        -print -quit
)
if [[ -z "$bundled_python" ]]; then
    show_error "The Python runtime was not included in LUFScale.app."
    exit 1
fi
bundled_qt_core=$(
    /usr/bin/find "dist/LUFScale.app" -type f \
        \( -name "QtCore" -o -name "libQt6Core*.dylib" \) \
        -print -quit
)
if [[ -z "$bundled_qt_core" ]]; then
    show_error "The PySide6/Qt runtime was not included in LUFScale.app."
    exit 1
fi
main_executable="dist/LUFScale.app/Contents/MacOS/LUFScale"
if /usr/bin/otool -L "$main_executable" | /usr/bin/tail -n +2 \
    | /usr/bin/awk '{print $1}' \
    | /usr/bin/grep -E '^(/Library/|/opt/|/usr/local/)' \
    | /usr/bin/grep -q .; then
    show_error "The application executable still depends on a non-system external runtime."
    exit 1
fi
if [[ "$(/usr/bin/find "dist/LUFScale.app" -type f -name ffmpeg | /usr/bin/wc -l | /usr/bin/tr -d ' ')" != "1" ]]; then
    show_error "The package must contain exactly one FFmpeg executable."
    exit 1
fi
if ! "$bundled_ffmpeg" -hide_banner -filters 2>/dev/null | /usr/bin/grep -q " loudnorm "; then
    show_error "The bundled FFmpeg does not contain the loudnorm filter."
    exit 1
fi

for release_file in LICENSE COPYRIGHT README.md OPEN_LUFSCALE_ON_MACOS.md THIRD_PARTY_NOTICES.md SBOM.cdx.json RELEASE_2.1.12.md VALIDATION_2.1.12.md FFMPEG_DISTRIBUTION_NOTICE.txt FFMPEG_BUILD_MANIFEST.json LUFSCALE_RUNTIME_MANIFEST.json; do
    integrated_release_file=$(
        /usr/bin/find "dist/LUFScale.app" \
            -type f \
            -name "$release_file" \
            -print \
            -quit
    )
    if [[ -z "$integrated_release_file" ]]; then
        show_error "The $release_file file was not included in LUFScale.app."
        exit 1
    fi
done

integrated_runtime_manifest=$(
    /usr/bin/find "dist/LUFScale.app" -type f \
        -name "LUFSCALE_RUNTIME_MANIFEST.json" -print -quit
)
if [[ -z "$integrated_runtime_manifest" ]] \
    || ! /usr/bin/cmp -s \
        "packaging/generated/LUFSCALE_RUNTIME_MANIFEST.json" \
        "$integrated_runtime_manifest"; then
    show_error "The embedded runtime manifest is missing or does not match the build record."
    exit 1
fi

for font in "${interface_fonts[@]}"; do
    integrated_font=$(
        /usr/bin/find "dist/LUFScale.app" \
            -type f \
            -path "*/assets/fonts/$font" \
            -print \
            -quit
    )
    if [[ -z "$integrated_font" ]]; then
        show_error "The $font font was not included in LUFScale.app."
        exit 1
    fi
    if ! /usr/bin/cmp -s "assets/fonts/$font" "$integrated_font"; then
        show_error "The $font font in LUFScale.app does not match the source file."
        exit 1
    fi
done

integrated_logo=$(
    /usr/bin/find "dist/LUFScale.app" \
        -type f \
        -path "*/assets/branding/LUFScale_logo.png" \
        -print \
        -quit
)
if [[ -z "$integrated_logo" ]]; then
    show_error "The LUFScale logo was not included in LUFScale.app."
    exit 1
fi
if ! /usr/bin/cmp -s "$icon_source" "$integrated_logo"; then
    show_error "The logo in LUFScale.app does not match the source file."
    exit 1
fi

for guide in "${pdf_guides[@]}"; do
    integrated_guide=$(
        /usr/bin/find "dist/LUFScale.app" \
            -type f \
            -path "*/output/pdf/$guide" \
            -print \
            -quit
    )
    if [[ -z "$integrated_guide" ]]; then
        show_error "The $guide guide was not included in LUFScale.app."
        exit 1
    fi
    if ! /usr/bin/cmp -s "output/pdf/$guide" "$integrated_guide"; then
        show_error "The $guide guide in LUFScale.app does not match the generated PDF."
        exit 1
    fi
done

app_logical_bytes="$(tree_bytes "dist/LUFScale.app")"
frameworks_logical_bytes="$(tree_bytes "dist/LUFScale.app/Contents/Frameworks")"
resources_logical_bytes="$(tree_bytes "dist/LUFScale.app/Contents/Resources")"
ffmpeg_logical_bytes="$(/usr/bin/stat -f '%z' "$bundled_ffmpeg")"
app_disk_kib="$(/usr/bin/du -sk "dist/LUFScale.app" | /usr/bin/awk '{ print $1 }')"
app_file_count="$(/usr/bin/find "dist/LUFScale.app" -type f | /usr/bin/wc -l | /usr/bin/tr -d ' ')"

echo "Bundle size report:"
echo "  Complete application (logical files): $(format_bytes "$app_logical_bytes")"
echo "  Complete application (disk footprint): $(/usr/bin/awk -v kib="$app_disk_kib" 'BEGIN { printf "%.1f MiB", kib / 1024 }')"
echo "  Bundled FFmpeg: $(format_bytes "$ffmpeg_logical_bytes")"
echo "  Bundled Python: $(format_bytes "$(/usr/bin/stat -f '%z' "$bundled_python")")"
echo "  Bundled QtCore: $(format_bytes "$(/usr/bin/stat -f '%z' "$bundled_qt_core")")"
echo "  Contents/Frameworks: $(format_bytes "$frameworks_logical_bytes")"
echo "  Contents/Resources: $(format_bytes "$resources_logical_bytes")"
echo "  Regular files: $app_file_count"

if [[ -n "${LUFSCALE_CODESIGN_IDENTITY:-}" ]]; then
    echo "Checking the Developer ID signature…"
    /usr/bin/codesign --verify --deep --strict --verbose=2 "dist/LUFScale.app" || {
        show_error "Developer ID signature verification failed."
        exit 1
    }
else
    print -u2 -- "WARNING — the application has no Developer ID identity and is not notarized. macOS will normally display a warning after download."
fi

print -u2 -- "INFORMATION — LUFScale.app includes Python, PySide6/Qt, its verified FFmpeg engine, guides and licences. End users do not need to install any runtime."

if [[ "${LUFSCALE_NONINTERACTIVE:-0}" != "1" ]]; then
    /usr/bin/open "dist"
    /usr/bin/osascript -e 'display dialog "LUFScale.app was created in the dist folder." buttons {"OK"} default button "OK" with title "Build complete"'
fi
