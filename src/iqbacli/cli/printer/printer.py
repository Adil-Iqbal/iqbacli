from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from pathlib import Path
from typing import Optional

from rich.console import Console

from iqbacli.cli.suggestions.suggestions import Suggestions
from iqbacli.paths import CONFIG_PATH


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
    def success(self: Printer, message: str) -> None:
        """Print representation of success message."""

    @abstractmethod
    def info(self: Printer, message: str) -> None:
        """Print representation of info message."""

    @abstractmethod
    def warn(self: Printer, message: str) -> None:
        """Print representation of warn message."""

    @abstractmethod
    def error(self: Printer, message: str, argv: Optional[str] = None) -> None:
        """Print representation of error message."""

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
