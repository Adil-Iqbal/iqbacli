import typer

app = typer.Typer(short_help="Set configuration parameter.")


@app.callback(invoke_without_command=True)
def set(param: str, value: str):
    """
    Set a specific parameter value.\n
    (example) iqba config set cache false
    (example) iqba config set --param cache --value false
    """
    print(f"get id: {param} {value}")
