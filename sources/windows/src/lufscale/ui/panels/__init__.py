"""Panneaux composant la fenêtre principale."""

from .header import HeaderPanel
from .progress import ProgressPanel
from .results import ResultsPanel
from .settings import SettingsPanel
from .sources import SourcesPanel

__all__ = [
    "HeaderPanel",
    "ProgressPanel",
    "ResultsPanel",
    "SettingsPanel",
    "SourcesPanel",
]
