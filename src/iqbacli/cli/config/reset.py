import typer
import humps
from iqbacli.cli.printer import printer_factory
from iqbacli.driver.config import reset_config, reset_config_key, get_valid_config_keys
from iqbacli.cli.config.util import _handle_key_error


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
    Reset entire configuration. / Reset a specific key.\n
    (entire config)               iqba config reset\n
    (just a key)                  iqba config reset ignore-filename\n
    (output json)                 iqba config reset --json\n
    (without color)               iqba config reset --no-color\n
    (json without color)          iqba config reset --json --no-color\n
    (json with key)               iqba config reset --json only-ext\n
    (json without color with key) iqba config reset --json --no-color max-cached
    """
    if key is None:
        reset_config()
        printer = printer_factory(json, no_color)
        printer.print_config(highlight_keys=get_valid_config_keys())
        raise typer.Exit()

    if humps.is_kebabcase(key):
        key = humps.dekebabize(key)

    try:
        reset_config_key(key)
    except KeyError:
        _handle_key_error(key)

    printer = printer_factory(json, no_color)
    printer.print_config(highlight_keys=[key])
