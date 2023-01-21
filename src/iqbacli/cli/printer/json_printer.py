from __future__ import annotations

from ...paths import CONFIG_PATH
from ...driver import config
from pathlib import Path
from typing import Optional
from rich.console import Console
from rich import print_json
from .printer import Printer


class JsonPrinter(Printer):
    def __init__(self, console: Console, color: bool):
        super().__init__(console=console, color=color)

    def print_config(
        self: JsonPrinter,
        config_path: Path = CONFIG_PATH,
        highlight_keys: Optional[list[str]] = None,
    ) -> None:
        """Print representation of application configuration file."""
        config_dict = config.get_config_dict(config_path)
        print_json(data=config_dict, highlight=self.color)
