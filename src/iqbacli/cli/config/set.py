from __future__ import annotations

import json
from typing import NoReturn
import rich
import humps
import typer

from iqbacli.cli.config.util import print_config_table
from ...paths import CONFIG_PATH
from ...driver import config
from ..printer import printer_factory


app = typer.Typer(short_help="Set configuration parameter.")


def _handle_key_error(key: str) -> NoReturn:
    valid_field_names = [humps.kebabize(k) for k in config.get_valid_config_keys()]
    typer.secho(
        f"""
Unknown key: {key}
            
Key must be one of these: {', '.join(valid_field_names)}
        """,
        fg="red",
    )
    raise typer.Abort()


def _handle_value_error(key: str, value: str) -> NoReturn:
    typer.secho(
        f"""
Unrecognized value: {value}

Maybe the data type is incorrect for the key `{key}`.
Try running `iqba config get --json` for a hint.

(boolean example) iqba config set cache false
(string example)  iqba config set ignore-ext js,css,ico
(integer example) iqba config set max-cached 30
        """,
        fg="red",
    )
    raise typer.Abort()


@app.callback(invoke_without_command=True)
def set(
    key: str = typer.Argument(..., show_default=False),
    value: str = typer.Argument(..., show_default=False),
    json: bool = typer.Option(
        False,
        "--json/",
        show_default=False,
        help="Output json.",
        rich_help_panel="Formatting",
    ),
    no_color: bool = typer.Option(
        False,
        "--no-color/",
        show_default=False,
        help="Remove color.",
        rich_help_panel="Formatting",
    ),
):
    """
    Set a specific configuration KEY to a VALUE.\n
    (boolean example)      iqba config set cache false\n
    (string example)       iqba config set ignore-ext js,css,ico\n
    (integer example)      iqba config set max-cached 30\n
    (with json output)     iqba config set --json cache false\n
    (output without color) iqba config set --no-color cache false\n
    (json without color)   iqba config set --json --no-color cache false

    """
    if humps.is_kebabcase(key):
        key = humps.dekebabize(key)

    try:
        config.set_config_key(key, value)
        printer = printer_factory(json, no_color)
        printer.print_config(highlight_keys=[key])

    except KeyError:
        _handle_key_error(key)
    except ValueError:
        _handle_value_error(key, value)
