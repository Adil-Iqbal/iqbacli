from __future__ import annotations


from typing import NoReturn
import humps
import typer


from iqbacli.cli.suggestions.suggestions import Suggestions
from iqbacli.cli.config.util import _handle_key_error
from iqbacli.driver import config
from iqbacli.cli.printer import printer_factory


app = typer.Typer(short_help="Set configuration parameter.")


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
    no_suggest: bool = typer.Option(
        False,
        "--no-suggest/",
        show_default=False,
        help="Remove suggestions.",
        rich_help_panel="Formatting",
    ),
):
    """
    Set a specific configuration KEY to a VALUE.\n
    (boolean example)      iqba config set cache false\n
    (string example)       iqba config set ignore-ext js,css,ico\n
    (integer example)      iqba config set max-cached 30\n

    """
    _key = key.lower()
    if humps.is_kebabcase(_key):
        _key = humps.dekebabize(_key)

    try:
        config.set_config_key(_key, value)
    except KeyError:
        _handle_key_error(_key)
    except ValueError:
        _handle_value_error(_key, value)

    printer = printer_factory(json, no_color)
    printer.success_message("Changes will be applied to next command.")

    _key = humps.kebabize(_key)
    suggests = Suggestions(no_suggest=no_suggest)
    suggests.add("view new config", "iqba config get")
    suggests.add("view new value only", f"iqba config get {_key}")
    suggests.add("reset value", f"iqba config reset {_key}")
    printer.print_suggestions(suggests)
