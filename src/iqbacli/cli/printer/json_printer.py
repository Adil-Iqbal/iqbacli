from __future__ import annotations
from collections import defaultdict
from enum import Enum

from iqbacli.cli.suggestions.suggestions import Suggestions
import dataclasses
from iqbacli.paths import CONFIG_PATH
from iqbacli.driver import config
from pathlib import Path
from typing import Any, Optional
from rich.console import Console
from rich import print_json
from iqbacli.cli.printer.printer import Printer
from typing import Protocol, DefaultDict
import atexit


class JsonPrintable(Protocol):
    def to_dict(self: JsonPrintable) -> dict[str, Any]:
        ...


class MessageType(Enum):
    SUCCESS = "success"


@dataclasses.dataclass
class Message:
    message: str
    type: MessageType

    def to_dict(self: Message) -> dict[str, Any]:
        return self.__dict__


@dataclasses.dataclass
class HighlightedConfigKey:
    key: str
    value: Any

    def to_dict(self: HighlightedConfigKey) -> dict[str, Any]:
        return self.__dict__


class JsonPrinter(Printer):
    def __init__(self, console: Console, color: bool):
        super().__init__(console=console, color=color)
        self.data: DefaultDict[str, Any] = defaultdict(list)
        atexit.register(self._print_impl)

    def _print_impl(self: JsonPrinter):
        if not self.data:
            return
        print_json(data=self.data, highlight=self.color)

    def _register_entity(self: JsonPrinter, key: str, entity: JsonPrintable) -> None:
        self.data[key].append(entity.to_dict())

    def _message(self: JsonPrinter, message: str, type: MessageType) -> None:
        self._register_entity("messages", Message(message=message, type=type))

    def success_message(self: JsonPrinter, message: str) -> None:
        self._message(message=message, type=MessageType.SUCCESS)

    def print_config(
        self: JsonPrinter,
        config_path: Path = CONFIG_PATH,
        highlight_keys: Optional[list[str]] = None,
    ) -> None:
        """Print representation of application configuration file."""
        config_dict = config.get_config_dict(config_path)
        self.data["config"] = config_dict

        if highlight_keys is None:
            return
        for key in highlight_keys:
            if key not in config_dict:
                continue
            self._register_entity(
                "highlighted_keys",
                HighlightedConfigKey(key=key, value=config_dict[key]),
            )

    def _print_suggestions_impl(self: JsonPrinter, suggests: Suggestions) -> None:
        for suggest in suggests:
            self._register_entity("suggestions", suggest)
