from typing import Any
import json
import dataclasses
from pathlib import Path

from iqbacli.logging import create_logger
from iqbacli.params import builtins
from iqbacli.paths import CONFIG_PATH
from iqbacli.data.config import Config, is_cfg_field_name

logger = create_logger(__file__)
str_true: set[str] = {"ok", "1", "yes", "true"}


def str_to_bool(string: str) -> bool:
    if string.lower() in str_true:
        return True
    if string.isdigit() and int(string) != 0:
        return True
    if string.startswith(("t", "T", "y", "Y")):
        return True
    return False


name_to_type: dict[Any, Any] = {
    "str": str,
    "bool": str_to_bool,
    "int": int,
}


def get_path(config_path: Path = CONFIG_PATH) -> str:
    return str(config_path.absolute())


def get_config_dict(config_path: Path = CONFIG_PATH) -> Any:
    return json.loads(config_path.read_text())


def get_valid_config_keys() -> list[str]:
    return [
        field.name
        for field in dataclasses.fields(Config)
        if is_cfg_field_name(field.name)
    ]


def set_config_key(key: str, _value: str, config_path: Path = CONFIG_PATH) -> None:
    for field in dataclasses.fields(Config):
        if is_cfg_field_name(field.name) and field.name == key:
            type_callable = name_to_type[field.type]
            value = type_callable(_value)
            config = Config.get(config_path)
            logger.info(f"setting config {key=} to {value=}")
            setattr(config, key, value)
            config.save()
            return

    raise KeyError(f"Unknown key: {key}")


def reset_config_key(_key: str, config_path: Path = CONFIG_PATH) -> None:
    try:
        key = _key.upper()
        default_value = getattr(builtins, key)
        logger.info(f"resetting config {key=}")
        set_config_key(key=_key, _value=str(default_value), config_path=config_path)
    except AttributeError:
        raise KeyError(f"Unknown key: {_key}")


def reset_config(config_path: Path = CONFIG_PATH) -> None:
    logger.info(f"resetting entire config at path: {str(config_path.absolute())}")
    config_path.unlink(missing_ok=True)
    Config.create_new(config_path=config_path)
