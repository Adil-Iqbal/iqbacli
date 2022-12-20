import typer

app = typer.Typer(short_help="Display list of previous search queries.")


@app.callback(invoke_without_command=True)
def list():
    print("list")
