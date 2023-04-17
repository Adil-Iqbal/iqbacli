from __future__ import annotations

from io import UnsupportedOperation
from pathlib import Path

from rich.console import Console

from iqbacli.cli.printer.printer import Printer
from iqbacli.cli.suggestions.suggestions import Suggestions
from iqbacli.paths import CONFIG_PATH


class QuietPrinter(Printer):
    def __init__(self, console: Console, color: bool):
        super().__init__(console=console, color=color)

    def print_config(
        self: Printer,
        config_path: Path = CONFIG_PATH,
        highlight_keys: list[str] | None = None,
    ) -> None:
        pass

    def success(self: Printer, message: str) -> None:
        pass

    def info(self: Printer, message: str) -> None:
        pass

    def warn(self: Printer, message: str) -> None:
        pass

    def error(self: Printer, message: str, argv: str | None = None) -> None:
        pass

    def print_suggestions(self: Printer, suggests: Suggestions) -> None:
        pass

    def _print_suggestions_impl(self: Printer, suggests: Suggestions) -> None:
        raise UnsupportedOperation()
