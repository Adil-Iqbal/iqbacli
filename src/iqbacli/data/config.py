from __future__ import annotations

import dataclasses
import json
from pathlib import Path
from typing import Any

from iqbacli.logging import create_logger
from iqbacli.params import builtins

logger = create_logger(__file__)
_OMITTED_FNAME_PREFIX = ("_", "config_path")


def is_cfg_field_name(name: str) -> bool:
    return not name.startswith(_OMITTED_FNAME_PREFIX)


@dataclasses.dataclass
class Config:
    config_path: Path
    cache: bool
    flat: bool
    regex: bool
    suggestions: bool
    only_ext: str
    only_filename: str
    only_dirname: str
    ignore_ext: str
    ignore_filename: str
    ignore_dirname: str
    max_cached: int
    max_cache_size: int

    def _to_dict(self: Config) -> dict[str, Any]:
        config_dict = {k: v for k, v in self.__dict__.items() if is_cfg_field_name(k)}
        logger.debug(f"converting to dict: {config_dict=}")
        return config_dict

    def save(self) -> None:
        logger.info("saving config file.")
        config = self._to_dict()
        with self.config_path.open("w") as config_file:
            json.dump(config, config_file)

    @staticmethod
    def get(config_path: Path) -> Config:
        logger.info(f"getting config json file at {config_path=}")
        try:
            return Config.get_from_file(config_path)
        except (TypeError, OSError):
            return Config.create_new(config_path)

    @staticmethod
    def get_from_file(config_path: Path) -> Config:
        with config_path.open("r") as config_file:
            config_dict = {k: v for k, v in json.load(config_file).items()}
            logger.debug(f"get config, created {config_dict=}")
            return Config(config_path=config_path, **config_dict)

    @staticmethod
    def create_new(config_path: Path) -> Config:
        logger.info("creating new default config")

        default_config = Config(
            config_path=config_path,
            cache=builtins.CACHE,
            flat=builtins.FLAT,
            regex=builtins.REGEX,
            suggestions=builtins.SUGGESTIONS,
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

    @staticmethod
    def is_valid_key(key: str) -> bool:
        for field in dataclasses.fields(Config):
            if is_cfg_field_name(field.name) and key == field.name:
                return True
        return False
