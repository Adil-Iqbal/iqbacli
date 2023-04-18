from __future__ import annotations

import humps
import typer

from iqbacli.cli.printer import printer_factory

from ...driver import config

app = typer.Typer(short_help="Get configuration settings.")


def _print_entire_config(json: bool, no_color: bool) -> None:
    printer = printer_factory(json, no_color)
    printer.print_config()


@app.callback(invoke_without_command=True)
def get(
    key: str
    | None = typer.Argument(
        default=None,
        show_default=False,
        help="Get value for a specific configuration key.",
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
    Get entire configuration. / Get a specific value.\n
    (entire config)      iqba config get\n
    (just a key)         iqba config get flat\n
    (config as json)     iqba config get --json\n
    (json without color) iqba config get --json --no-color\n
    """
    if key is None:
        _print_entire_config(json, no_color)
        raise typer.Exit()

    if humps.is_kebabcase(key):
        key = humps.dekebabize(key)

    config_dict = config.get_config_dict()
    if key not in config_dict:
        _print_entire_config(json, no_color)
        typer.secho(f"\nUnknown key: {key}", fg="red")
        raise typer.Abort()

    typer.echo(config_dict[key])
