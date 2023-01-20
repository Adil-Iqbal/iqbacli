from typing import Any
import json
import dataclasses
from pathlib import Path
from ..paths import CONFIG_PATH
from ..data.config import Config, is_cfg_field_name


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
    "Path": Path,
}


def get_path(config_path: Path = CONFIG_PATH) -> str:
    return str(config_path.absolute())


def get_config_dict(config_path: Path = CONFIG_PATH) -> dict[str, Any]:
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
            setattr(config, key, value)
            config.save()
            return

    raise KeyError(f"Unknown key: {key}")
