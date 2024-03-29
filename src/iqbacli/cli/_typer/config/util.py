from __future__ import annotations

from typing import NoReturn

import humps
import typer

from ...driver import config


def _handle_key_error(key: str, default_keys: list[str] | None = None) -> NoReturn:
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
