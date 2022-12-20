import typer

app = typer.Typer(short_help="Get details of most recent search query.")


@app.callback(invoke_without_command=True)
def last():
    print("last")
