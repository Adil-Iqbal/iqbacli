from typing import Any
import humps
import dataclasses
from pathlib import Path
from ..paths import CONFIG_PATH
from ..data.config import Config, is_cfg_field_name


name_to_type: dict[Any, Any] = {
    "str": str,
    "bool": bool,
    "int": int,
    "Path": Path,
}

str_true: set[str] = {"ok", "1", "yes", "true"}


def str_to_bool(string: str) -> bool:
    if string.lower() in str_true:
        return True
    if string.isdigit() and int(string) != 0:
        return True
    if string.startswith(("t", "T", "y", "Y")):
        return True
    return False


def get_path() -> str:
    return str(CONFIG_PATH.absolute())


# def get_config_param(key: str) -> Any:
#     key = humps.dekebabize(_key)


def set_config_param(_key: str, _value: str) -> Config:
    key = humps.dekebabize(_key)
    for field in dataclasses.fields(Config):
        if is_cfg_field_name(field.name) and field.name == key:
            if field.type is bool:
                value = str_to_bool(_value)
            else:
                type_callable = name_to_type[field.type]
                value = type_callable(_value)
            config = Config.get(CONFIG_PATH)
            setattr(config, key, value)
            config.save()
            return config

    raise ValueError(f"Unknown key: {key}")
