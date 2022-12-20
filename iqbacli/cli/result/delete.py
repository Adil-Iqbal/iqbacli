import typer

app = typer.Typer(short_help="Delete a specific search result.")


@app.callback(invoke_without_command=True)
def get(
    id: int,
    cache_only: bool = typer.Option(
        default=False, help="Delete cached files without removing records."
    ),
):
    """
    Delete the search result with the provided ID.
    """
    print(f"delete id: {id}")
