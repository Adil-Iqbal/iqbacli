import typer

app = typer.Typer(short_help="Review size of back-up files and clear if desired.")


@app.command()
def cache():
    print("cache")
