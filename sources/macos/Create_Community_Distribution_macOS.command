#!/bin/zsh

set -eu
cd -- "$(dirname -- "$0")"

fail() {
    print -u2 -- "ERROR — $1"
    exit 1
}

[[ "$(/usr/bin/uname -s)" == "Darwin" ]] \
    || fail "The community distribution must be built on macOS."

unset LUFSCALE_CODESIGN_IDENTITY
unset LUFSCALE_NOTARY_PROFILE
export LUFSCALE_NONINTERACTIVE=1

./tools/Internal_Application_Builder_macOS.command

app_path="dist/LUFScale.app"
collect_path="dist/LUFScale"
[[ -d "$app_path" ]] \
    || fail "The $app_path bundle is missing after the build."
/usr/bin/codesign --verify --deep --strict --verbose=2 "$app_path" \
    || fail "The bundle's internal ad-hoc signature is invalid."
bundled_ffmpeg=$(
    /usr/bin/find "$app_path" -type f -name ffmpeg -print -quit
)
[[ -n "$bundled_ffmpeg" ]] \
    || fail "The self-contained FFmpeg engine is missing from the bundle."
[[ "$(/usr/bin/find "$app_path" -type f -name ffmpeg | /usr/bin/wc -l | /usr/bin/tr -d ' ')" == "1" ]] \
    || fail "The bundle must contain exactly one FFmpeg engine."
if /usr/bin/otool -L "$bundled_ffmpeg" | /usr/bin/tail -n +2 \
    | /usr/bin/awk '{print $1}' \
    | /usr/bin/grep -Ev '^(/usr/lib/|/System/Library/)' \
    | /usr/bin/grep -q .; then
    fail "The FFmpeg engine still depends on a non-system external library."
fi

version="$(PYTHONPATH=src .construction-macos/bin/python - <<'PY'
from lufscale.version import APP_VERSION

print(APP_VERSION)
PY
)"
target_arch="${LUFSCALE_TARGET_ARCH:-$(/usr/bin/uname -m)}"
release_name="LUFScale-${version}-macOS-${target_arch}-community"
release_tmp="$(/usr/bin/mktemp -d -t lufscale-community)"
trap '/bin/rm -rf -- "$release_tmp"' EXIT
release_folder="$release_tmp/$release_name"
/bin/mkdir -p "$release_folder"

/usr/bin/ditto "$app_path" "$release_folder/LUFScale.app"
for file in LICENSE COPYRIGHT README.md OPEN_LUFSCALE_ON_MACOS.md THIRD_PARTY_NOTICES.md SBOM.cdx.json RELEASE_2.1.12.md VALIDATION_2.1.12.md; do
    /usr/bin/ditto "$file" "$release_folder/$file"
done
/usr/bin/ditto "packaging/generated/FFMPEG_DISTRIBUTION_NOTICE.txt" \
    "$release_folder/FFMPEG_DISTRIBUTION_NOTICE.txt"
/usr/bin/ditto "packaging/generated/FFMPEG_BUILD_MANIFEST.json" \
    "$release_folder/FFMPEG_BUILD_MANIFEST.json"
/usr/bin/ditto "packaging/generated/LUFSCALE_RUNTIME_MANIFEST.json" \
    "$release_folder/LUFSCALE_RUNTIME_MANIFEST.json"
/usr/bin/ditto "third_party_licenses" "$release_folder/third_party_licenses"
/usr/bin/ditto "packaging/generated/third_party_licenses_ffmpeg" \
    "$release_folder/third_party_licenses/ffmpeg"
/usr/bin/ditto "packaging/generated/corresponding-source" \
    "$release_folder/corresponding-source"

release_zip="dist/$release_name.zip"
temporary_zip="$release_tmp/$release_name.zip"
/usr/bin/ditto -c -k --keepParent --rsrc --sequesterRsrc \
    "$release_folder" "$temporary_zip"
/bin/mv -f -- "$temporary_zip" "$release_zip"
/usr/bin/shasum -a 256 "$release_zip" > "$release_zip.sha256"

[[ -s "$release_zip" && -s "$release_zip.sha256" ]] \
    || fail "The community archive or its SHA-256 checksum is missing."

# Keep the finished application available for local testing. Only PyInstaller's
# redundant COLLECT directory is removed after the archive and checksum exist.
/bin/rm -rf -- "$collect_path"

echo "Community distribution created: $release_zip"
echo "SHA-256 checksum: $release_zip.sha256"
echo "LUFScale.app, the publishable ZIP, and its checksum are available in dist."
echo "This application is not identified with Developer ID or notarized by Apple."
echo "Python, PySide6/Qt, FFmpeg and the required codecs are included inside LUFScale.app."
echo "End users do not need to install Python, Qt, FFmpeg or a package manager."
echo "Exact sources, licenses, build options, and notices accompany the ZIP."
echo "Publish OPEN_LUFSCALE_ON_MACOS.md alongside the download."
