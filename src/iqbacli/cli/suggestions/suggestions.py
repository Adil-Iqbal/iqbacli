from __future__ import annotations
from pathlib import Path
from typing import Iterator, Optional

from iqbacli.cli.suggestions.suggestion import Suggestion
from iqbacli.driver.config import get_config
from iqbacli.logging import create_logger
from iqbacli.params import builtins
from iqbacli.paths import CONFIG_PATH
from iqbacli.params.env import get_env, is_env


logger = create_logger(__file__)


def _resolve_no_suggest_param(
    no_suggest_flag: Optional[bool], config_path: Path
) -> bool:
    if no_suggest_flag is not None:
        return no_suggest_flag

    if get_env("SUGGESTIONS") is not None:
        return is_env("SUGGESTIONS", "0")

    try:
        return not get_config(config_path=config_path).suggestions

    except OSError:
        logger.exception("Could not access config file. Investigate data.config file.")
        return not builtins.SUGGESTIONS


class Suggestions:
    def __init__(
        self: Suggestions,
        no_suggest: Optional[bool] = None,
        config_path: Path = CONFIG_PATH,
    ) -> None:
        self.no_suggest: bool = _resolve_no_suggest_param(no_suggest, config_path)
        self.collection: list[Suggestion] = []
        self.max_len = 0

    def __len__(self: Suggestions) -> int:
        return len(self.collection)

    def __iter__(self: Suggestions) -> Iterator[Suggestion]:
        return iter(self.collection)

    def add(self: Suggestions, description: str, command: str) -> None:
        if self.no_suggest:
            return

        description = " ".join(description.split()).lower()
        command = " ".join(command.split()).lower()

        if not description or not command:
            raise ValueError(
                f"Invalid command or description. {command=} {description=}"
            )

        self.max_len = max(self.max_len, len(description))
        self.collection.append(Suggestion(description=description, command=command))

    def _pre_print(self: Suggestions) -> None:
        self.add("turn off suggestions", "iqba config set suggestions off")
