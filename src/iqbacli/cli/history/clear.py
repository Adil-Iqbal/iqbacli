import typer

app = typer.Typer(short_help="Clear all search queries.")


@app.callback(invoke_without_command=True)
def clear():
    """
    Clear entire history.\n
    (example) iqba history clear
    """
    print("clear")
