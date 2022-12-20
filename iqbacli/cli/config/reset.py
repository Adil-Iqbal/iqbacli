import typer

app = typer.Typer(short_help="Reset configuration or reset specific param.")


@app.callback(invoke_without_command=True)
def reset(
    param: str = typer.Option(
        default=None, show_default=None, help="Reset a specific parameter to default."
    )
):
    """
    Reset entire configuration. / Reset a specific parameter.
    (Entire config) iqba config reset
    (Just a param) iqba config reset "ignore-filename"
    """
    print(f"reset id: {param}")
