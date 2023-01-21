from typing import Union, Optional
import typer
import humps
from iqbacli.cli.printer import printer_factory
from iqbacli.driver import config
from iqbacli.params import builtins
from iqbacli.cli.config.util import _handle_key_error
from iqbacli.driver.config import get_valid_config_keys


app = typer.Typer(short_help="Reset configuration or reset specific param.")


@app.callback(invoke_without_command=True)
def reset(
    key: str = typer.Argument(
        default=None, show_default=False, help="Reset a specific key to default value."
    ),
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
    Reset entire configuration. / Reset a specific key.
    (entire config) iqba config reset
    (just a key)    iqba config reset ignore-filename
    """
    if key is None:
        ...
        raise typer.Exit()

    if humps.is_kebabcase(key):
        key = humps.dekebabize(key)

    try:
        config.reset_config_key(key)
    except KeyError:
        _handle_key_error(key)

    printer = printer_factory(json, no_color)
    printer.print_config(highlight_keys=[key])

    print(f"reset id: {key}")
