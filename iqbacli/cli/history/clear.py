import typer

app = typer.Typer(short_help="Clear all search queries.")


@app.callback(invoke_without_command=True)
def clear():
    print("clear")
