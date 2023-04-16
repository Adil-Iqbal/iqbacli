from __future__ import annotations

from pathlib import Path

import humps
from rich.console import Console
from rich.table import Table

from iqbacli.cli.printer.printer import Printer
from iqbacli.driver.config import get_config_dict
from iqbacli.paths import CONFIG_PATH


class RichPrinter(Printer):
    def __init__(self, console: Console, color: bool):
        super().__init__(console=console, color=color)

    def _message(self: RichPrinter):
        ...

    def success(self: Printer, message: str) -> None:
        ...

    def info(self: Printer, message: str) -> None:
        ...

    def warn(self: Printer, message: str) -> None:
        ...

    def error(self: Printer, message: str, argv: str | None = None) -> None:
        ...

    def print_config(
        self: RichPrinter,
        config_path: Path = CONFIG_PATH,
        highlight_keys: list[str] | None = None,
    ) -> None:
        """Print representation of application configuration file."""
        if highlight_keys is None:
            highlight_keys = []
        config_dict = get_config_dict(config_path)
        table = Table(title="User Configuration")
        table.add_column("Key")
        table.add_column("Value")

        for key, value in config_dict.items():
            k, v = humps.kebabize(key), str(value)
            v = v if v else "[grey66][i]not used[/i][/grey66]"  # visualize empty string
            if self.color and key in highlight_keys:
                table.add_row(f"[green]{k}[/green]", f"[green]{v}[/green]")
                continue

            table.add_row(k, v)

        self.console.print()
        self.console.print(table, highlight=self.color)
