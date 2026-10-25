"""Verify the OS-facing application icon before distributing a build."""
from pathlib import Path
import argparse
import plistlib
import struct


def verify_mac(bundle, source):
    contents = Path(bundle) / "Contents"
    with (contents / "Info.plist").open("rb") as stream:
        info = plistlib.load(stream)
    name = info.get("CFBundleIconFile", "")
    if not name or Path(name).name != name:
        raise ValueError("Missing or invalid CFBundleIconFile")
    if not name.endswith(".icns"):
        name += ".icns"
    data = (contents / "Resources" / name).read_bytes()
    if len(data) < 8 or data[:4] != b"icns" or struct.unpack(">I", data[4:8])[0] != len(data):
        raise ValueError("Invalid bundled ICNS icon")
    if data != Path(source).read_bytes():
        raise ValueError("The bundle icon differs from the generated LUFScale icon")


def ico_images(source):
    data = Path(source).read_bytes()
    reserved, kind, count = struct.unpack_from("<HHH", data)
    if reserved or kind != 1 or not count:
        raise ValueError("Invalid ICO header")
    images = set()
    for i in range(count):
        size, offset = struct.unpack_from("<II", data, 6 + 16*i + 8)
        if not size or offset < 6 + 16*count or offset + size > len(data):
            raise ValueError("Invalid ICO image range")
        images.add(data[offset:offset+size])
    return images


def verify_windows(executable, source):
    import pefile  # Installed by PyInstaller on Windows.
    images = set()
    groups = False
    with pefile.PE(str(executable)) as pe:
        root = getattr(pe, "DIRECTORY_ENTRY_RESOURCE", None)
        if root is None:
            raise ValueError("Executable has no icon resources")
        for resource in root.entries:
            if resource.id == 14:
                groups = True
            if resource.id != 3:
                continue
            for entry in resource.directory.entries:
                for language in entry.directory.entries:
                    item = language.data.struct
                    images.add(pe.get_data(item.OffsetToData, item.Size))
    if not groups or not ico_images(source).issubset(images):
        raise ValueError("Executable does not contain all LUFScale icon sizes")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("platform", choices=("mac", "windows"))
    parser.add_argument("application", type=Path)
    parser.add_argument("icon", type=Path)
    args = parser.parse_args()
    (verify_mac if args.platform == "mac" else verify_windows)(args.application, args.icon)
    print(f"Application icon verified: {args.application}")
