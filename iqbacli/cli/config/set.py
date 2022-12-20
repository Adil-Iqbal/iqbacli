import typer

app = typer.Typer(short_help="Set configuration parameter.")


@app.callback(invoke_without_command=True)
def set(param: str, value: str):
    """
    Set a specific parameter value.\n
    (Example) iqba config set "cache" "false"
    """
    print(f"get id: {param} {value}")
