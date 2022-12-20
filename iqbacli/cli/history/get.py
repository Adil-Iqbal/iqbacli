import typer

app = typer.Typer(short_help="Get the details of a specific search query.")


@app.callback(invoke_without_command=True)
def get(id: int):
    """
    Get the details of the search query with the provided ID.
    """
    print(f"get id:{id}")
