from __future__ import annotations

from iqbacli.cli.suggestions.suggestions import Suggestions

from iqbacli.paths import CONFIG_PATH
from pathlib import Path
from rich.console import Console
from typing import Optional
from abc import ABC, abstractmethod


class Printer(ABC):
    def __init__(self: Printer, console: Console, color: bool):
        self.console = console
        self.color = color

    @abstractmethod
    def print_config(
        self: Printer,
        config_path: Path = CONFIG_PATH,
        highlight_keys: Optional[list[str]] = None,
    ) -> None:
        """Print representation of application configuration file."""

    @abstractmethod
    def success_message(self: Printer, message: str) -> None:
        """Print representation of success message."""

    def print_suggestions(self: Printer, suggests: Suggestions) -> None:
        """Print representation of suggestions."""
        if suggests.no_suggest:
            return
        if len(suggests) == 0:
            return
        suggests._pre_print()
        return self._print_suggestions_impl(suggests=suggests)

    @abstractmethod
    def _print_suggestions_impl(self: Printer, suggests: Suggestions) -> None:
        """Print representation of suggestions. (PRIVATE)"""
        ...
