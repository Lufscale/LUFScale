"""Compatibility exports for earlier LUFScale translation imports."""

from __future__ import annotations

import sys
from pathlib import Path


_SRC = Path(__file__).resolve().parent / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from lufscale.i18n.catalog_windows import *  # noqa: E402,F403
from lufscale.i18n.loader import translate  # noqa: E402,F401
