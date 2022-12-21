import typer

app = typer.Typer(short_help="Undo most recent search query.")


@app.callback(invoke_without_command=True)
def undo():
    print("undo")
