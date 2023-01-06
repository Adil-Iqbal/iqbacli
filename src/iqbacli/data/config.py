from __future__ import annotations

import json
import dataclasses
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

    def save(self) -> None:
        logger.info("saving config file.")
        config = {
            "cache": self.cache,
            "flat": self.flat,
            "regex": self.regex,
            "only_ext": self.only_ext,
            "only_filename": self.only_filename,
            "only_dirname": self.only_dirname,
            "ignore_ext": self.ignore_ext,
            "ignore_filename": self.ignore_filename,
            "ignore_dirname": self.ignore_dirname,
            "max_cached": self.max_cached,
            "max_cache_size": self.max_cache_size,
        }
        logger.debug(f"saving config file with {config=}")
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
