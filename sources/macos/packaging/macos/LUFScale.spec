# -*- mode: python ; coding: utf-8 -*-

import os
from pathlib import Path
from runpy import run_path

PROJECT_ROOT = Path(SPECPATH).resolve().parents[1]
VERSION = run_path(PROJECT_ROOT / "src" / "lufscale" / "version.py")[
    "APP_VERSION"
]
ICON = PROJECT_ROOT / ".construction-macos" / "LUFScale.icns"
TARGET_ARCH = os.environ.get("LUFSCALE_TARGET_ARCH") or None
CODESIGN_IDENTITY = os.environ.get("LUFSCALE_CODESIGN_IDENTITY") or None
ENTITLEMENTS_FILE = os.environ.get("LUFSCALE_ENTITLEMENTS_FILE") or None
BUNDLED_FFMPEG = Path(os.environ["LUFSCALE_BUNDLED_FFMPEG"]).resolve()
if not BUNDLED_FFMPEG.is_file():
    raise FileNotFoundError(f"Bundled FFmpeg not found: {BUNDLED_FFMPEG}")
MACOS_GUIDES = sorted((PROJECT_ROOT / "output" / "pdf").glob("*.pdf"))
if len(MACOS_GUIDES) != 12:
    raise FileNotFoundError(
        f"Expected 12 top-level macOS PDF guides, found {len(MACOS_GUIDES)}"
    )
a = Analysis(
    [str(PROJECT_ROOT / "app.py")],
    pathex=[str(PROJECT_ROOT / "src")],
    # LUFScale 2.1.12 ships the verified native FFmpeg built by
    # tools/build_bundled_ffmpeg_macos.py.  imageio-ffmpeg remains excluded so
    # PyInstaller cannot silently add a second, unrelated platform binary.
    binaries=[(str(BUNDLED_FFMPEG), ".")],
    datas=[
        *((str(guide), "output/pdf") for guide in MACOS_GUIDES),
        (str(PROJECT_ROOT / "assets" / "fonts"), "assets/fonts"),
        (str(PROJECT_ROOT / "assets" / "branding"), "assets/branding"),
        (str(PROJECT_ROOT / "LICENSE"), "."),
        (str(PROJECT_ROOT / "COPYRIGHT"), "."),
        (str(PROJECT_ROOT / "README.md"), "."),
        (str(PROJECT_ROOT / "OPEN_LUFSCALE_ON_MACOS.md"), "."),
        (str(PROJECT_ROOT / "THIRD_PARTY_NOTICES.md"), "."),
        (str(PROJECT_ROOT / "SBOM.cdx.json"), "."),
        (str(PROJECT_ROOT / "RELEASE_2.1.12.md"), "."),
        (str(PROJECT_ROOT / "VALIDATION_2.1.12.md"), "."),
        (str(PROJECT_ROOT / "third_party_licenses"), "third_party_licenses"),
        (
            str(
                PROJECT_ROOT
                / "packaging"
                / "generated"
                / "third_party_licenses_ffmpeg"
            ),
            "third_party_licenses/ffmpeg",
        ),
        (
            str(
                PROJECT_ROOT
                / "packaging"
                / "generated"
                / "FFMPEG_DISTRIBUTION_NOTICE.txt"
            ),
            ".",
        ),
        (
            str(
                PROJECT_ROOT
                / "packaging"
                / "generated"
                / "FFMPEG_BUILD_MANIFEST.json"
            ),
            ".",
        ),
        (
            str(
                PROJECT_ROOT
                / "packaging"
                / "generated"
                / "LUFSCALE_RUNTIME_MANIFEST.json"
            ),
            ".",
        ),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    # Do not redistribute the unrelated binary from the development-only
    # imageio-ffmpeg wheel.
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
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=TARGET_ARCH,
    codesign_identity=CODESIGN_IDENTITY,
    entitlements_file=ENTITLEMENTS_FILE,
    icon=str(ICON),
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="LUFScale",
)
app = BUNDLE(
    coll,
    name="LUFScale.app",
    icon=str(ICON),
    bundle_identifier="com.perezphilippe.lufscale",
    version=VERSION,
    info_plist={
        "CFBundleDisplayName": "LUFScale",
        "CFBundleVersion": VERSION,
        "LSMinimumSystemVersion": "12.0",
        "NSHighResolutionCapable": True,
        "NSPrincipalClass": "NSApplication",
    },
)
