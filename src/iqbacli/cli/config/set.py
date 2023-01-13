import humps
import typer
from ...driver import config

app = typer.Typer(short_help="Set configuration parameter.")


@app.callback(invoke_without_command=True)
def set(param: str, value: str):
    """
    Set a specific parameter value.\n
    (example) iqba config set --param cache --value false
    """
    _param = humps.dekebabize(param)
    try:
        config.set_config_param(_param, value)
        typer.echo("Success")
    except ValueError:
        typer.echo(f"Could not recognize input: {value}")
        raise typer.Abort()
