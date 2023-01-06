from __future__ import annotations

import copy
import json
import dataclasses
from typing import Any
from pathlib import Path
from ..params import builtins
from ..logging import create_logger

logger = create_logger(__file__)


@dataclasses.dataclass
class Config:
    config_path: Path
    cache: bool
    flat: bool
    regex: bool
    only_ext: str
    only_filename: str
    only_dirname: str
    ignore_ext: str
    ignore_filename: str
    ignore_dirname: str
    max_cached: int
    max_cache_size: int

    def _to_dict(self: Config) -> dict[str, Any]:
        config = copy.deepcopy(self.__dict__)
        del config["config_path"]

        logger.debug(f"converting to dict: {config=}")
        return config

    def save(self) -> None:
        logger.info("saving config file.")
        config = self._to_dict()
        with open(str(self.config_path.absolute()), "w") as config_file:
            json.dump(config, config_file)

    @staticmethod
    def get_config(config_path: Path) -> Config:
        if not config_path.exists() or not config_path.is_file():
            return Config.create_new_config(config_path)
        logger.info(f"getting config json file at {config_path=}")
        with open(str(config_path.absolute()), "r") as config_file:
            return Config(config_path=config_path, **json.load(config_file))

    @staticmethod
    def create_new_config(config_path: Path) -> Config:
        logger.info("creating new default config")

        default_config = Config(
            config_path=config_path,
            cache=builtins.CACHE,
            flat=builtins.FLAT,
            regex=builtins.REGEX,
            only_ext=builtins.ONLY_EXT,
            only_filename=builtins.ONLY_FILENAME,
            only_dirname=builtins.ONLY_DIRNAME,
            ignore_ext=builtins.IGNORE_EXT,
            ignore_filename=builtins.IGNORE_FILENAME,
            ignore_dirname=builtins.IGNORE_DIRNAME,
            max_cached=builtins.MAX_CACHED,
            max_cache_size=builtins.MAX_CACHE_SIZE,
        )
        default_config.save()
        return default_config
