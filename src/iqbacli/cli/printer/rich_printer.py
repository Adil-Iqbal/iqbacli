from __future__ import annotations

import humps
from ...paths import CONFIG_PATH
from ...driver import config
from pathlib import Path
from typing import Optional, Type
from rich.console import Console
from rich.table import Table
from .printer import Printer


class RichPrinter(Printer):
    def __init__(self, console: Console, color: bool):
        super().__init__(console=console, color=color)

    def print_config(
        self: RichPrinter,
        config_path: Path = CONFIG_PATH,
        highlight_keys: Optional[tuple[str, ...]] = None,
    ) -> None:
        """Print representation of application configuration file."""
        config_dict = config.get_config_dict(config_path)
        table = Table(title="User Configuration")
        table.add_column("Name")
        table.add_column("Value")

        for key, value in config_dict.items():
            k, v = humps.kebabize(key), str(value)
            if highlight_keys is not None and key in highlight_keys and self.color:
                table.add_row(f"[green]{k}[/green]", f"[green]{v}[/green]")
                continue
            table.add_row(k, v)

        self.console.print(table, highlight=self.color)