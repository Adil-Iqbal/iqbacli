import typer

app = typer.Typer(short_help="Display path to configuration file.")


@app.callback(invoke_without_command=True)
def path():
    """
    Display path to configuration file.\n
    (example) iqba config path
    """
    print("path")
