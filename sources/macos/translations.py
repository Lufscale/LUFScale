"""Compatibilité des anciens imports de traductions LUFScale."""

from __future__ import annotations

import sys
from pathlib import Path


_SRC = Path(__file__).resolve().parent / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from lufscale.i18n.translations import *  # noqa: E402,F403
