"""Résolution centralisée des ressources source et PyInstaller."""

from __future__ import annotations

import sys
from pathlib import Path


PDF_GUIDES = {
    "fr": "Guide_LUFScale_FR.pdf",
    "en": "Guide_LUFScale_EN.pdf",
    "es": "Guia_LUFScale_ES.pdf",
    "it": "Guida_LUFScale_IT.pdf",
    "pt": "Guia_LUFScale_PT.pdf",
    "ru": "Rukovodstvo_LUFScale_RU.pdf",
    "ja": "Guide_LUFScale_JA.pdf",
    "hi": "Guide_LUFScale_HI.pdf",
    "zh": "Guide_LUFScale_ZH.pdf",
    "ko": "Guide_LUFScale_KO.pdf",
    "id": "Panduan_LUFScale_ID.pdf",
    "tr": "Kilavuz_LUFScale_TR.pdf",
}


def project_root() -> Path:
    """Retourne la racine du projet lors d'un lancement depuis les sources."""
    return Path(__file__).resolve().parents[2]


def application_folder() -> Path:
    """Retourne le dossier de l'exécutable ou la racine du projet."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return project_root()


def application_resource_folder() -> Path:
    """Retourne la racine contenant les ressources intégrées ou locales."""
    bundled_root = getattr(sys, "_MEIPASS", None)
    if bundled_root:
        return Path(bundled_root).resolve()
    return project_root()


def application_logo_path(resource_root: Path | None = None) -> Path:
    root = resource_root or application_resource_folder()
    return root / "assets" / "branding" / "LUFScale_logo.png"


def localized_guide_path(
    language: str,
    resource_root: Path | None = None,
) -> Path:
    guide_name = PDF_GUIDES.get(language, PDF_GUIDES["en"])
    root = resource_root or application_resource_folder()
    return root / "output" / "pdf" / guide_name
