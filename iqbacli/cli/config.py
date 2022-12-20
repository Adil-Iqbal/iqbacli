import typer

app = typer.Typer(short_help="Review and update configuration settings.")


@app.command()
def config():
    print("config")
