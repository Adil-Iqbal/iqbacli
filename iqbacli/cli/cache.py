import typer

app = typer.Typer(short_help="Review and manage file cache.")


@app.command()
def cache():
    print("cache")
