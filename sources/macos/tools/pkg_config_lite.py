#!/usr/bin/env python3
"""Small build-local pkg-config implementation used by the macOS builder.

It intentionally implements only the stable query surface used by the
Autoconf projects and FFmpeg in LUFScale's pinned audio dependency graph.
The implementation uses only the Python standard library and reads ordinary
``.pc`` files from ``PKG_CONFIG_PATH`` / ``PKG_CONFIG_LIBDIR``.
"""

from __future__ import annotations

import os
import re
import shlex
import sys
from dataclasses import dataclass
from pathlib import Path


_REQUIREMENT = re.compile(
    r"^\s*([A-Za-z0-9_.+\-]+)\s*(?:(>=|<=|=|>|<)\s*([^\s,]+))?\s*$"
)


def _version_key(value: str) -> tuple[tuple[int, object], ...]:
    parts = re.findall(r"\d+|[A-Za-z]+", value)
    return tuple((0, int(part)) if part.isdigit() else (1, part.lower()) for part in parts)


def _version_matches(actual: str, operator: str | None, requested: str | None) -> bool:
    if not operator or requested is None:
        return True
    left = _version_key(actual)
    right = _version_key(requested)
    return {
        "=": left == right,
        ">=": left >= right,
        "<=": left <= right,
        ">": left > right,
        "<": left < right,
    }[operator]


def _unique(tokens: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for token in tokens:
        if token not in seen:
            seen.add(token)
            result.append(token)
    return result


@dataclass
class PcFile:
    path: Path
    variables: dict[str, str]
    fields: dict[str, str]

    @classmethod
    def load(cls, path: Path, overrides: dict[str, str]) -> "PcFile":
        logical_lines: list[str] = []
        pending = ""
        for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = pending + raw
            if line.endswith("\\"):
                pending = line[:-1]
                continue
            pending = ""
            logical_lines.append(line)
        if pending:
            logical_lines.append(pending)

        variables: dict[str, str] = {"pcfiledir": str(path.parent), **overrides}
        fields: dict[str, str] = {}
        for line in logical_lines:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            equals = line.find("=")
            colon = line.find(":")
            if equals >= 0 and (colon < 0 or equals < colon):
                name, value = line.split("=", 1)
                variables[name.strip()] = value.strip()
            elif colon >= 0:
                name, value = line.split(":", 1)
                fields[name.strip()] = value.strip()

        package = cls(path=path, variables=variables, fields=fields)
        package.variables = {
            name: package.expand(value) for name, value in package.variables.items()
        }
        package.fields = {
            name: package.expand(value) for name, value in package.fields.items()
        }
        return package

    def expand(self, value: str) -> str:
        pattern = re.compile(r"\$\{([^}]+)\}")
        for _ in range(32):
            expanded = pattern.sub(lambda match: self.variables.get(match.group(1), ""), value)
            if expanded == value:
                return expanded
            value = expanded
        raise ValueError(f"recursive variable expansion in {self.path}")

    @property
    def version(self) -> str:
        return self.fields.get("Version", "0")

    def requirements(self, private: bool) -> list[tuple[str, str | None, str | None]]:
        values = [self.fields.get("Requires", "")]
        if private:
            values.append(self.fields.get("Requires.private", ""))
        result: list[tuple[str, str | None, str | None]] = []
        for value in values:
            for item in value.split(","):
                if not item.strip():
                    continue
                match = _REQUIREMENT.match(item)
                if not match:
                    raise ValueError(f"unsupported requirement {item!r} in {self.path}")
                result.append((match.group(1), match.group(2), match.group(3)))
        return result


class Repository:
    def __init__(self, overrides: dict[str, str]) -> None:
        raw_paths = os.environ.get("PKG_CONFIG_LIBDIR") or os.environ.get(
            "PKG_CONFIG_PATH", ""
        )
        self.paths = [Path(item) for item in raw_paths.split(os.pathsep) if item]
        self.overrides = overrides
        self.cache: dict[str, PcFile] = {}

    def get(self, name: str) -> PcFile:
        if name in self.cache:
            return self.cache[name]
        for directory in self.paths:
            candidate = directory / f"{name}.pc"
            if candidate.is_file():
                package = PcFile.load(candidate, self.overrides)
                self.cache[name] = package
                return package
        raise FileNotFoundError(f"package {name!r} was not found in {self.paths}")

    def closure(self, names: list[str], private: bool) -> list[PcFile]:
        result: list[PcFile] = []
        visited: set[str] = set()

        def visit(name: str, operator: str | None = None, version: str | None = None) -> None:
            package = self.get(name)
            if not _version_matches(package.version, operator, version):
                raise ValueError(
                    f"{name} {package.version} does not satisfy {operator} {version}"
                )
            if name in visited:
                return
            visited.add(name)
            result.append(package)
            for dependency in package.requirements(private):
                visit(*dependency)

        for name in names:
            visit(name)
        return result


def _parse_arguments(argv: list[str]) -> tuple[dict[str, object], list[str]]:
    options: dict[str, object] = {
        "mode": "exists",
        "static": False,
        "variable": None,
        "defines": {},
    }
    packages: list[str] = []
    index = 0
    while index < len(argv):
        argument = argv[index]
        if argument == "--cflags" or argument.startswith("--cflags-"):
            options["mode"] = "cflags"
        elif argument == "--libs" or argument.startswith("--libs-"):
            options["mode"] = "libs"
        elif argument == "--modversion":
            options["mode"] = "modversion"
        elif argument == "--exists":
            options["mode"] = "exists"
        elif argument == "--static":
            options["static"] = True
        elif argument.startswith("--variable="):
            options["mode"] = "variable"
            options["variable"] = argument.split("=", 1)[1]
        elif argument.startswith("--define-variable="):
            definition = argument.split("=", 1)[1]
            name, value = definition.split("=", 1)
            options["defines"][name] = value  # type: ignore[index]
        elif argument in {
            "--print-errors",
            "--short-errors",
            "--silence-errors",
            "--errors-to-stdout",
            "--define-prefix",
            "--dont-define-prefix",
        }:
            # The indexed loop advances below.  Using ``continue`` here would
            # revisit the same informational option forever (Autoconf commonly
            # invokes ``pkg-config --exists --print-errors ...``).
            pass
        elif argument.startswith("--atleast-pkgconfig-version="):
            options["mode"] = "pkgconfig-version"
            options["requested_pkgconfig_version"] = argument.split("=", 1)[1]
        elif argument == "--atleast-pkgconfig-version":
            index += 1
            if index >= len(argv):
                raise ValueError(
                    "--atleast-pkgconfig-version requires a version argument"
                )
            options["mode"] = "pkgconfig-version"
            options["requested_pkgconfig_version"] = argv[index]
        elif argument == "--version":
            options["mode"] = "version"
        elif argument.startswith("-"):
            raise ValueError(f"unsupported pkg-config option: {argument}")
        else:
            packages.append(argument)
        index += 1
    return options, packages


def _package_names(arguments: list[str]) -> tuple[list[str], list[tuple[str, str, str]]]:
    names: list[str] = []
    constraints: list[tuple[str, str, str]] = []
    joined = " ".join(arguments)
    expression = re.compile(
        r"\s*,?\s*([A-Za-z0-9_.+\-]+)"
        r"(?:\s*(>=|<=|=|>|<)\s*([^\s,]+))?"
    )
    position = 0
    while position < len(joined):
        match = expression.match(joined, position)
        if not match or match.end() == position:
            raise ValueError(f"unsupported package expression: {joined[position:]!r}")
        names.append(match.group(1))
        if match.group(2) and match.group(3):
            constraints.append((match.group(1), match.group(2), match.group(3)))
        position = match.end()
    return names, constraints


def main(argv: list[str]) -> int:
    try:
        options, package_arguments = _parse_arguments(argv)
        mode = str(options["mode"])
        if mode == "version":
            print("1.9.5-lufscale")
            return 0
        if mode == "pkgconfig-version":
            return 0 if _version_matches(
                "1.9.5", ">=", str(options["requested_pkgconfig_version"])
            ) else 1
        names, constraints = _package_names(package_arguments)
        repository = Repository(options["defines"])  # type: ignore[arg-type]
        packages = repository.closure(names, bool(options["static"]))
        for name, operator, version in constraints:
            if not _version_matches(repository.get(name).version, operator, version):
                return 1
        if mode == "exists":
            return 0
        if mode == "modversion":
            print("\n".join(repository.get(name).version for name in names))
            return 0
        if mode == "variable":
            variable = str(options["variable"])
            print(repository.get(names[0]).variables.get(variable, ""))
            return 0
        field = "Cflags" if mode == "cflags" else "Libs"
        tokens: list[str] = []
        for package in packages:
            tokens.extend(shlex.split(package.fields.get(field, "")))
            if mode == "libs" and options["static"]:
                tokens.extend(shlex.split(package.fields.get("Libs.private", "")))
        print(" ".join(_unique(tokens)))
        return 0
    except (FileNotFoundError, OSError, ValueError) as error:
        print(f"pkg-config: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
