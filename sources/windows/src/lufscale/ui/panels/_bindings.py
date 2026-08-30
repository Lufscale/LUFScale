from __future__ import annotations

from dataclasses import fields
from typing import Any


# Shared, translation-independent height for the two upper workspace panels.
# Keeping this value explicit prevents taller CJK/Devanagari font metrics from
# pushing the progress and results rows down when the saved language changes.
COMPACT_WORKSPACE_HEIGHT = 322


class PanelBindings:
    """Bind a panel's public Qt objects to the historical window attributes."""

    def bind_to(self, owner: Any) -> None:
        for field in fields(self):
            setattr(owner, field.name, getattr(self, field.name))
