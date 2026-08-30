#!/usr/bin/env python3
"""Build the redistributable FFmpeg runtime embedded in LUFScale for macOS.

The script deliberately builds the codec libraries from pinned upstream source
archives.  It does not copy a Homebrew or imageio-ffmpeg executable into the
application.  Homebrew may provide the *build-only* ``pkg-config`` utility,
but no Homebrew library is allowed to remain linked to the resulting binary.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import shlex
import shutil
import subprocess
import sys
import tarfile
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from runpy import run_path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEPLOYMENT_TARGET = "12.0"
APP_VERSION = str(
    run_path(PROJECT_ROOT / "src" / "lufscale" / "version.py")["APP_VERSION"]
)


@dataclass(frozen=True)
class SourceArchive:
    name: str
    version: str
    filename: str
    url: str
    sha256: str
    source_directory: str
    license_files: tuple[str, ...]


SOURCES = (
    SourceArchive(
        name="FFmpeg",
        version="7.1.5",
        filename="ffmpeg-7.1.5.tar.xz",
        url="https://ffmpeg.org/releases/ffmpeg-7.1.5.tar.xz",
        sha256="de668509caf9e35e3cd162473441fdb29538c6d96ed080292b3cf9e6fc5d558f",
        source_directory="ffmpeg-7.1.5",
        license_files=("COPYING.LGPLv2.1", "COPYING.LGPLv3", "LICENSE.md"),
    ),
    SourceArchive(
        name="LAME",
        version="4.0",
        filename="lame-4.0.tar.gz",
        url="https://downloads.sourceforge.net/project/lame/lame/4.0/lame-4.0.tar.gz",
        sha256="3df5124d5ad3a98312ffd7ba6a9b36230e4f8a3e66d3ce0f425e336c32d216eb",
        source_directory="lame-4.0",
        license_files=("COPYING", "LICENSE"),
    ),
    SourceArchive(
        name="libogg",
        version="1.3.6",
        filename="libogg-1.3.6.tar.gz",
        url="https://ftp.osuosl.org/pub/xiph/releases/ogg/libogg-1.3.6.tar.gz",
        sha256="83e6704730683d004d20e21b8f7f55dcb3383cdf84c0daedf30bde175f774638",
        source_directory="libogg-1.3.6",
        license_files=("COPYING",),
    ),
    SourceArchive(
        name="libvorbis",
        version="1.3.7",
        filename="libvorbis-1.3.7.tar.xz",
        url="https://ftp.osuosl.org/pub/xiph/releases/vorbis/libvorbis-1.3.7.tar.xz",
        sha256="b33cc4934322bcbf6efcbacf49e3ca01aadbea4114ec9589d1b1e9d20f72954b",
        source_directory="libvorbis-1.3.7",
        license_files=("COPYING",),
    ),
    SourceArchive(
        name="Opus",
        version="1.6.1",
        filename="opus-1.6.1.tar.gz",
        url="https://ftp.osuosl.org/pub/xiph/releases/opus/opus-1.6.1.tar.gz",
        sha256="6ffcb593207be92584df15b32466ed64bbec99109f007c82205f0194572411a1",
        source_directory="opus-1.6.1",
        license_files=("COPYING",),
    ),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run(command: list[str], *, cwd: Path | None = None, env: dict[str, str] | None = None) -> str:
    print("+", " ".join(command), flush=True)
    completed = subprocess.run(
        command,
        cwd=cwd,
        env=env,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if completed.stdout:
        print(completed.stdout, end="" if completed.stdout.endswith("\n") else "\n")
    if completed.returncode != 0:
        raise subprocess.CalledProcessError(
            completed.returncode,
            command,
            output=completed.stdout,
        )
    return completed.stdout


def download(source: SourceArchive, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.is_file() and sha256(destination) == source.sha256:
        print(f"Verified source already present: {destination.name}")
        return
    temporary = destination.with_suffix(destination.suffix + ".download")
    curl = shutil.which("curl")
    if curl is None:
        raise RuntimeError("The system curl tool was not found.")
    # Use macOS' system curl and trust store.  Python.org installations can
    # otherwise lack a configured CA bundle and fail with
    # CERTIFICATE_VERIFY_FAILED.  TLS verification remains mandatory: the
    # script never uses --insecure and still verifies the pinned SHA-256.
    run(
        [
            curl,
            "--proto",
            "=https",
            "--tlsv1.2",
            "--location",
            "--fail",
            "--show-error",
            "--silent",
            "--retry",
            "3",
            "--retry-all-errors",
            "--connect-timeout",
            "30",
            "--max-time",
            "600",
            "--user-agent",
            f"LUFScale-{APP_VERSION}-source-builder",
            "--output",
            str(temporary),
            source.url,
        ]
    )
    actual = sha256(temporary)
    if actual != source.sha256:
        raise RuntimeError(
            f"Incorrect checksum for {source.filename}: {actual} instead of {source.sha256}"
        )
    temporary.replace(destination)


def safe_extract(archive: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    root = destination.resolve()
    with tarfile.open(archive, "r:*") as package:
        for member in package.getmembers():
            target = (destination / member.name).resolve()
            if target != root and root not in target.parents:
                raise RuntimeError(f"Unsafe path in {archive.name}: {member.name}")
        package.extractall(destination)


def configure_and_make(
    source: Path,
    build: Path,
    prefix: Path,
    options: list[str],
    env: dict[str, str],
    *,
    preserve_make_flags: bool = False,
) -> None:
    marker = build / ".lufscale-built"
    if marker.is_file():
        print(f"Component already built: {build.name}")
        return
    build.mkdir(parents=True, exist_ok=True)
    try:
        run([str(source / "configure"), f"--prefix={prefix}", *options], cwd=build, env=env)
    except subprocess.CalledProcessError:
        config_log = build / "config.log"
        if config_log.is_file():
            diagnostic_directory = (
                PROJECT_ROOT / "packaging" / "generated" / "build-diagnostics"
            )
            diagnostic_directory.mkdir(parents=True, exist_ok=True)
            persistent_log = diagnostic_directory / f"{build.name}-config.log"
            shutil.copy2(config_log, persistent_log)
            lines = config_log.read_text(encoding="utf-8", errors="replace").splitlines()
            error_lines = [
                index
                for index, line in enumerate(lines)
                if re.search(
                    r"(?:error:|failed|cannot|not found|invalid|problem determining)",
                    line,
                    re.I,
                )
            ]
            if error_lines:
                print(f"\n--- Errors found in {config_log} ---")
                displayed: set[int] = set()
                for index in error_lines[-6:]:
                    for context_index in range(max(0, index - 4), min(len(lines), index + 6)):
                        if context_index not in displayed:
                            print(f"{context_index + 1}: {lines[context_index]}")
                            displayed.add(context_index)
                print("--- End of detected errors ---\n")
            print(f"\n--- Diagnostic {config_log} (last 160 lines) ---")
            print("\n".join(lines[-160:]))
            print("--- End of diagnostic ---\n")
            print(f"Persistent diagnostic copy: {persistent_log}\n")
        raise
    make_overrides: list[str] = []
    if preserve_make_flags:
        # libvorbis 1.3.7's macOS configure branch unconditionally replaces
        # CFLAGS with a legacy set containing -force_cpusubtype_ALL.  Modern
        # Apple Silicon linkers reject that option when the self-test program
        # is linked.  Command-line make variables take precedence over the
        # generated Makefile and restore the already validated SDK/arch flags
        # without patching or skipping any Vorbis source or self-test.
        make_overrides = [
            f"CFLAGS={env['CFLAGS']}",
            f"CXXFLAGS={env['CXXFLAGS']}",
            f"LDFLAGS={env['LDFLAGS']}",
        ]
    run(
        ["make", f"-j{max(1, os.cpu_count() or 1)}", *make_overrides],
        cwd=build,
        env=env,
    )
    run(["make", "install", *make_overrides], cwd=build, env=env)
    marker.write_text(f"built by LUFScale {APP_VERSION}\n", encoding="utf-8")


def validated_lame_configure_env(
    build_root: Path,
    env: dict[str, str],
    compiler_flags: list[str],
) -> dict[str, str]:
    """Validate the native macOS ABI and seed LAME's fragile size probes.

    LAME 4.0 exits directly with status 1 if any Autoconf ``sizeof`` probe
    returns zero.  The supported macOS targets are both 64-bit LP64.  We do
    not assume those values silently: clang must first compile and run static
    assertions with the exact SDK, architecture and deployment flags used by
    the real build.  Only then are the equivalent Autoconf cache values passed
    to LAME's unmodified configure script.
    """

    probe_directory = build_root / "lame-abi-check"
    probe_directory.mkdir(parents=True, exist_ok=True)
    probe_source = probe_directory / "lame-abi-check.c"
    probe_binary = probe_directory / "lame-abi-check"
    probe_source.write_text(
        """#include <limits.h>\n
_Static_assert(CHAR_BIT == 8, \"unsupported CHAR_BIT\");\n
_Static_assert(sizeof(short) == 2, \"unsupported short\");\n
_Static_assert(sizeof(unsigned short) == 2, \"unsupported unsigned short\");\n
_Static_assert(sizeof(int) == 4, \"unsupported int\");\n
_Static_assert(sizeof(unsigned int) == 4, \"unsupported unsigned int\");\n
_Static_assert(sizeof(long) == 8, \"unsupported long\");\n
_Static_assert(sizeof(unsigned long) == 8, \"unsupported unsigned long\");\n
_Static_assert(sizeof(long long) == 8, \"unsupported long long\");\n
_Static_assert(sizeof(unsigned long long) == 8, \"unsupported unsigned long long\");\n
_Static_assert(sizeof(float) == 4, \"unsupported float\");\n
_Static_assert(sizeof(double) == 8, \"unsupported double\");\n
int main(void) { return 0; }\n
""",
        encoding="utf-8",
    )
    run(
        [
            env["CC"],
            *compiler_flags,
            str(probe_source),
            "-o",
            str(probe_binary),
        ],
        env=env,
    )
    run([str(probe_binary)], env=env)

    lame_env = env.copy()
    lame_env.update(
        {
            "ac_cv_sizeof_short": "2",
            "ac_cv_sizeof_unsigned_short": "2",
            "ac_cv_sizeof_int": "4",
            "ac_cv_sizeof_unsigned_int": "4",
            "ac_cv_sizeof_long": "8",
            "ac_cv_sizeof_unsigned_long": "8",
            "ac_cv_sizeof_long_long": "8",
            "ac_cv_sizeof_unsigned_long_long": "8",
            "ac_cv_sizeof_float": "4",
            "ac_cv_sizeof_double": "8",
        }
    )
    return lame_env


def validate_runtime(ffmpeg: Path, target_arch: str) -> dict[str, str]:
    version_output = run([str(ffmpeg), "-hide_banner", "-version"])
    configuration = next(
        (line for line in version_output.splitlines() if line.startswith("configuration:")),
        "",
    )
    if "--enable-gpl" in configuration or "--enable-nonfree" in configuration:
        raise RuntimeError("The FFmpeg configuration unexpectedly enables GPL or nonfree.")

    filters = run([str(ffmpeg), "-hide_banner", "-filters"])
    if " loudnorm " not in filters:
        raise RuntimeError("The built FFmpeg is missing the loudnorm filter.")
    encoders = run([str(ffmpeg), "-hide_banner", "-encoders"])
    required = {
        "libmp3lame",
        "flac",
        "pcm_s16le",
        "pcm_s16be",
        "pcm_s24le",
        "pcm_s24be",
        "pcm_s32le",
        "pcm_s32be",
        "pcm_f32le",
        "aac",
        "libvorbis",
        "libopus",
    }
    missing = sorted(name for name in required if name not in encoders)
    if missing:
        raise RuntimeError("Missing FFmpeg encoders: " + ", ".join(missing))

    file_output = run(["file", str(ffmpeg)]).strip()
    expected = "arm64" if target_arch == "arm64" else "x86_64"
    if expected not in file_output:
        raise RuntimeError(f"Unexpected FFmpeg architecture: {file_output}")

    links = run(["otool", "-L", str(ffmpeg)])
    forbidden = []
    for line in links.splitlines()[1:]:
        dependency = line.strip().split(" ", 1)[0]
        if dependency and not dependency.startswith(("/usr/lib/", "/System/Library/")):
            forbidden.append(dependency)
    if forbidden:
        raise RuntimeError(
            "The self-contained FFmpeg still depends on external libraries: "
            + ", ".join(forbidden)
        )

    with tempfile.TemporaryDirectory(prefix="lufscale-ffmpeg-test-") as temporary:
        temp = Path(temporary)
        cases = (
            ("test.mp3", "libmp3lame"),
            ("test.flac", "flac"),
            ("test.wav", "pcm_s24le"),
            ("test.aiff", "pcm_s24be"),
            ("test.m4a", "aac"),
            ("test.ogg", "libvorbis"),
            ("test.opus", "libopus"),
        )
        for filename, codec in cases:
            run(
                [
                    str(ffmpeg),
                    "-hide_banner",
                    "-loglevel",
                    "error",
                    "-f",
                    "lavfi",
                    "-i",
                    "sine=frequency=1000:duration=0.2",
                    "-af",
                    "loudnorm=I=-14:TP=-2:LRA=11",
                    "-c:a",
                    codec,
                    "-y",
                    str(temp / filename),
                ]
            )

    return {
        "binary_sha256": sha256(ffmpeg),
        "configuration": configuration,
        "file": file_output,
        "dynamic_dependencies": links,
        "version_output": version_output,
    }


def copy_licences(extracted: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for source in SOURCES:
        source_root = extracted / source.source_directory
        for relative in source.license_files:
            candidate = source_root / relative
            if candidate.is_file():
                target = destination / f"{source.name}-{relative.replace('/', '_')}"
                shutil.copy2(candidate, target)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-arch", choices=("arm64", "x86_64"))
    parser.add_argument("--print-manifest", action="store_true")
    args = parser.parse_args()

    if args.print_manifest:
        print(json.dumps([asdict(source) for source in SOURCES], indent=2, ensure_ascii=False))
        return 0
    if platform.system() != "Darwin":
        parser.error("the bundled FFmpeg must be built on macOS")

    host_arch = platform.machine()
    target_arch = args.target_arch or host_arch
    if target_arch != host_arch:
        parser.error(
            "this self-contained build creates one native architecture at a time; "
            f"host={host_arch}, target={target_arch}"
        )
    pkg_config = shutil.which("pkg-config")
    if not pkg_config:
        parser.error(
            "the build-local pkg-config helper was not activated by the launcher"
        )
    for tool in ("curl", "make", "file", "otool", "xcrun"):
        if not shutil.which(tool):
            parser.error(f"macOS build tool not found: {tool}")

    generated = PROJECT_ROOT / "packaging" / "generated"
    corresponding_source = generated / "corresponding-source"
    # Autoconf/Automake projects in the audio stack do not all preserve paths
    # containing spaces or shell metacharacters.  The downloaded project may
    # legitimately be named e.g. "LUFScale-2.1.12-open-source (1)", so all
    # compilation inputs, outputs and prefixes live below a private, stable,
    # whitespace-free macOS temporary path instead of below PROJECT_ROOT.
    safe_build_base = Path("/private/tmp") / (
        f"lufscale-{APP_VERSION}-ffmpeg-{os.getuid()}"
    )
    safe_build_base.mkdir(mode=0o700, parents=True, exist_ok=True)
    if safe_build_base.stat().st_uid != os.getuid():
        parser.error(
            "the temporary build folder is not owned by the current user: "
            f"{safe_build_base}"
        )
    safe_build_base.chmod(0o700)
    build_root = safe_build_base / target_arch
    extracted = build_root / "sources"
    builds = build_root / "build"
    prefix = build_root / "prefix"
    corresponding_source.mkdir(parents=True, exist_ok=True)

    for source in SOURCES:
        archive = corresponding_source / source.filename
        download(source, archive)
        if not (extracted / source.source_directory).is_dir():
            safe_extract(archive, extracted)

    sdk_root = run(["xcrun", "--sdk", "macosx", "--show-sdk-path"]).strip()
    if not sdk_root or not Path(sdk_root).is_dir():
        parser.error(f"macOS SDK not found: {sdk_root or 'no path returned'}")
    common_flag_arguments = [
        "-O2",
        "-arch",
        target_arch,
        "-isysroot",
        sdk_root,
        f"-mmacosx-version-min={DEPLOYMENT_TARGET}",
    ]
    linker_flag_arguments = [
        "-arch",
        target_arch,
        "-isysroot",
        sdk_root,
        f"-mmacosx-version-min={DEPLOYMENT_TARGET}",
    ]
    common_flags = shlex.join(common_flag_arguments)
    linker_flags = shlex.join(linker_flag_arguments)
    env = os.environ.copy()
    # Do not let Homebrew, MacPorts, a previous SDK selection, a user
    # config.site or inherited make options alter this reproducible build.
    for inherited_name in (
        "CPATH",
        "C_INCLUDE_PATH",
        "CPLUS_INCLUDE_PATH",
        "LIBRARY_PATH",
        "DYLD_LIBRARY_PATH",
        "DYLD_FALLBACK_LIBRARY_PATH",
        "CONFIG_SITE",
        "MAKEFLAGS",
        "MFLAGS",
    ):
        env.pop(inherited_name, None)
    env.update(
        {
            "PATH": f"{PROJECT_ROOT / 'tools'}:/usr/bin:/bin:/usr/sbin:/sbin",
            "LC_ALL": "C",
            "LANG": "C",
            "CC": run(["xcrun", "--find", "clang"]).strip(),
            "AR": run(["xcrun", "--find", "ar"]).strip(),
            "RANLIB": run(["xcrun", "--find", "ranlib"]).strip(),
            "CFLAGS": common_flags,
            "CXXFLAGS": common_flags,
            "LDFLAGS": linker_flags,
            "MACOSX_DEPLOYMENT_TARGET": DEPLOYMENT_TARGET,
            "SDKROOT": sdk_root,
            "PKG_CONFIG_PATH": str(prefix / "lib" / "pkgconfig"),
            "PKG_CONFIG_LIBDIR": str(prefix / "lib" / "pkgconfig"),
            "PKG_CONFIG": pkg_config,
        }
    )

    # Compile and link with the exact compiler, SDK and flags that Autoconf
    # will receive.  Calling only the path returned by `xcrun --find clang`
    # can otherwise lose the SDK selection and fail later with
    # "ld: library 'System' not found".
    compiler_check = build_root / "compiler-check"
    compiler_check.mkdir(parents=True, exist_ok=True)
    compiler_source = compiler_check / "main.c"
    compiler_output = compiler_check / "lufscale-compiler-check"
    compiler_source.write_text("int main(void) { return 0; }\n", encoding="utf-8")
    run(
        [env["CC"], *common_flag_arguments, str(compiler_source), "-o", str(compiler_output)],
        env=env,
    )
    run([str(compiler_output)], env=env)

    lame_env = validated_lame_configure_env(
        build_root,
        env,
        common_flag_arguments,
    )

    configure_and_make(
        extracted / "lame-4.0",
        builds / "lame",
        prefix,
        [
            "--disable-shared",
            "--enable-static",
            "--disable-frontend",
            "--disable-decoder",
            "--disable-nasm",
        ],
        lame_env,
    )
    configure_and_make(
        extracted / "libogg-1.3.6",
        builds / "libogg",
        prefix,
        ["--disable-shared", "--enable-static"],
        env,
    )
    configure_and_make(
        extracted / "libvorbis-1.3.7",
        builds / "libvorbis",
        prefix,
        [
            "--disable-shared",
            "--enable-static",
            "--disable-docs",
            "--disable-examples",
            "--disable-oggtest",
        ],
        env,
        preserve_make_flags=True,
    )
    configure_and_make(
        extracted / "opus-1.6.1",
        builds / "opus",
        prefix,
        [
            "--disable-shared",
            "--enable-static",
            "--disable-extra-programs",
            "--disable-doc",
        ],
        env,
    )

    ffmpeg_prefix = prefix / "ffmpeg"
    ffmpeg_marker = ffmpeg_prefix / ".lufscale-built"
    if not ffmpeg_marker.is_file():
        ffmpeg_build = builds / "ffmpeg"
        ffmpeg_build.mkdir(parents=True, exist_ok=True)
        ffmpeg_options = [
            f"--prefix={ffmpeg_prefix}",
            f"--arch={'aarch64' if target_arch == 'arm64' else 'x86_64'}",
            "--target-os=darwin",
            "--disable-shared",
            "--enable-static",
            "--disable-debug",
            "--disable-doc",
            "--disable-ffplay",
            "--disable-ffprobe",
            "--disable-network",
            "--disable-autodetect",
            "--disable-x86asm" if target_arch == "x86_64" else "--enable-neon",
            "--enable-libmp3lame",
            "--enable-libvorbis",
            "--enable-libopus",
            "--pkg-config-flags=--static",
            f"--extra-cflags={common_flags} -I{prefix / 'include'}",
            f"--extra-ldflags={linker_flags} -L{prefix / 'lib'}",
        ]
        run([str(extracted / "ffmpeg-7.1.5" / "configure"), *ffmpeg_options], cwd=ffmpeg_build, env=env)
        run(["make", f"-j{max(1, os.cpu_count() or 1)}"], cwd=ffmpeg_build, env=env)
        run(["make", "install"], cwd=ffmpeg_build, env=env)
        ffmpeg_marker.write_text(f"built by LUFScale {APP_VERSION}\n", encoding="utf-8")

    built_ffmpeg = ffmpeg_prefix / "bin" / "ffmpeg"
    runtime_dir = generated / "ffmpeg" / target_arch
    runtime_dir.mkdir(parents=True, exist_ok=True)
    runtime_ffmpeg = runtime_dir / "ffmpeg"
    shutil.copy2(built_ffmpeg, runtime_ffmpeg)
    runtime_ffmpeg.chmod(0o755)
    validation = validate_runtime(runtime_ffmpeg, target_arch)

    licence_dir = generated / "third_party_licenses_ffmpeg"
    copy_licences(extracted, licence_dir)
    source_manifest = {
        "application": f"LUFScale {APP_VERSION}",
        "target_architecture": target_arch,
        "macos_deployment_target": DEPLOYMENT_TARGET,
        "sources": [asdict(source) for source in SOURCES],
        **validation,
    }
    (generated / "FFMPEG_BUILD_MANIFEST.json").write_text(
        json.dumps(source_manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (corresponding_source / "README.txt").write_text(
        f"Exact sources of the FFmpeg engine redistributed with LUFScale {APP_VERSION}.\n"
        "Checksums, versions, URLs, and build options are recorded in "
        "FFMPEG_BUILD_MANIFEST.json. No local source modification is applied.\n",
        encoding="utf-8",
    )
    (generated / "FFMPEG_DISTRIBUTION_NOTICE.txt").write_text(
        f"LUFScale {APP_VERSION} — self-contained FFmpeg engine\n"
        f"Architecture: {target_arch}\n"
        f"Minimum macOS target: {DEPLOYMENT_TARGET}\n"
        f"FFmpeg: 7.1.5, binary SHA-256: {validation['binary_sha256']}\n"
        "Statically linked libraries: LAME 4.0, libogg 1.3.6, "
        "libvorbis 1.3.7, Opus 1.6.1.\n"
        "LGPL build: neither --enable-gpl nor --enable-nonfree.\n"
        "The complete manifest, licenses, and exact source archives accompany "
        "the community distribution.\n\n"
        + validation["configuration"]
        + "\n",
        encoding="utf-8",
    )
    print(f"Self-contained FFmpeg ready: {runtime_ffmpeg}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
