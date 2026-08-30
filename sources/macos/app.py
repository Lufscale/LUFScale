"""Lanceur historique de LUFScale.

Le code applicatif vit désormais dans le paquet ``lufscale``. Ce relais
conserve la compatibilité avec ``python app.py``, PyInstaller et les anciens
imports utilisés par les outils et extensions du projet.
"""

from __future__ import annotations

import sys
from pathlib import Path


_SRC = Path(__file__).resolve().parent / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from lufscale.application import *  # noqa: E402,F403
from lufscale.application import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
