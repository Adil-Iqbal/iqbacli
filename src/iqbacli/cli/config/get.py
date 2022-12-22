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
    (Entire config) iqba config get\n
    (Just a param) iqba config get flat
    """
    print(f"get id: {param}")
