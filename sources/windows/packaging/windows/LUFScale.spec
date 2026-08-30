# -*- mode: python ; coding: utf-8 -*-

import os
from pathlib import Path


PROJECT_ROOT = Path(SPECPATH).resolve().parents[1]
ICON = PROJECT_ROOT / "assets" / "branding" / "LUFScale.ico"
BUNDLED_FFMPEG = Path(os.environ["LUFSCALE_BUNDLED_FFMPEG"]).resolve()
GUIDES_DIR = Path(
    os.environ.get(
        "LUFSCALE_GUIDES_DIR",
        str(PROJECT_ROOT / "output" / "pdf"),
    )
).resolve()
GENERATED = PROJECT_ROOT / "packaging" / "generated" / "windows-x86_64"

for required in (ICON, BUNDLED_FFMPEG, GUIDES_DIR):
    if not required.exists():
        raise FileNotFoundError(f"Required Windows build input not found: {required}")

a = Analysis(
    [str(PROJECT_ROOT / "app.py")],
    pathex=[str(PROJECT_ROOT / "src")],
    binaries=[(str(BUNDLED_FFMPEG), ".")],
    datas=[
        (str(GUIDES_DIR), "output/pdf"),
        (str(PROJECT_ROOT / "assets" / "fonts"), "assets/fonts"),
        (str(PROJECT_ROOT / "assets" / "branding"), "assets/branding"),
        (str(PROJECT_ROOT / "LICENSE"), "."),
        (str(PROJECT_ROOT / "COPYRIGHT"), "."),
        (str(PROJECT_ROOT / "README.md"), "."),
        (str(PROJECT_ROOT / "OPEN_LUFSCALE_ON_WINDOWS.md"), "."),
        (str(PROJECT_ROOT / "THIRD_PARTY_NOTICES.md"), "."),
        (str(PROJECT_ROOT / "SBOM.cdx.json"), "."),
        (str(PROJECT_ROOT / "RELEASE_2.1.12.md"), "."),
        (str(PROJECT_ROOT / "VALIDATION_2.1.12.md"), "."),
        (str(PROJECT_ROOT / "third_party_licenses"), "third_party_licenses"),
        (str(GENERATED / "FFMPEG_WINDOWS_DISTRIBUTION_NOTICE.txt"), "."),
        (str(GENERATED / "FFMPEG_WINDOWS_BUILD_MANIFEST.json"), "."),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    # The native executable is copied explicitly after validation.  Excluding
    # the Python package prevents a second hidden FFmpeg binary.
    excludes=["imageio_ffmpeg"],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="LUFScale",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    icon=str(ICON),
    version=str(PROJECT_ROOT / "packaging" / "windows" / "version_info.txt"),
    uac_admin=False,
    contents_directory=".",
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="LUFScale",
)
