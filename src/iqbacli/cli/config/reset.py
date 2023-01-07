import typer

app = typer.Typer(short_help="Reset configuration or reset specific param.")


@app.callback(invoke_without_command=True)
def reset(
    param: str = typer.Option(
        default=None, show_default=False, help="Reset a specific parameter to default."
    )
):
    """
    Reset entire configuration. / Reset a specific parameter.
    (entire config) iqba config reset
    (just a param)  iqba config reset ignore-filename
    (just a param)  iqba config reset ==param ignore-filename
    """
    print(f"reset id: {param}")
