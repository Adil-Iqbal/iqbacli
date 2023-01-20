import humps
import typer

app = typer.Typer(short_help="Get configuration settings.")


@app.callback(invoke_without_command=True)
def get(
    param: str = typer.Option(
        default=None, show_default=False, help="Get a specific parameter."
    )
):
    """
    Get entire configuration. / Get a specific parameter.\n
    (entire config) iqba config get\n
    (just a param)  iqba config get --param flat\n
    """
    print(f"get (with param?) {param}")
