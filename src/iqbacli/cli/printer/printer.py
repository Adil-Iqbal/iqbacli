from ...paths import CONFIG_PATH
from pathlib import Path
from rich.console import Console
from typing import Optional
from abc import ABC, abstractmethod


class Printer(ABC):
    def __init__(self, console: Console, color: bool):
        self.console = console
        self.color = color

    @abstractmethod
    def print_config(
        config_path: Path = CONFIG_PATH,
        highlight_keys: Optional[list[str]] = None,
    ) -> None:
        """Print representation of application configuration file."""
