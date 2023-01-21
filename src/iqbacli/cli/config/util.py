import humps
import typer
from typing import NoReturn, Optional
from ...driver import config


def _handle_key_error(key: str, default_keys: Optional[list[str]] = None) -> NoReturn:
    if default_keys is None:
        default_keys = [humps.kebabize(k) for k in config.get_valid_config_keys()]
    typer.secho(
        f"""
Unknown key: {key}

Key must be one of these: {', '.join(default_keys)}
        """,
        fg="red",
    )
    raise typer.Abort()
