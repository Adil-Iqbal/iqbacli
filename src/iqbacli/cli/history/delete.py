import typer

app = typer.Typer(short_help="Delete a specific search query.")


@app.callback(invoke_without_command=True)
def delete(
    id: int = typer.Argument(
        ..., min=1, show_default=False, help="The ID of search query to be deleted."
    ),
    cache_only: bool = typer.Option(
        False,
        "--cache-only/",
        show_default=False,
        help="Delete cached files without removing records.",
    ),
):
    """
    Delete the search query with the provided ID.\n
    (delete entire query) iqba history delete 12\n
    (delete entire query) iqba history delete --id 12\n
    (delete only cache)   iqba history delete 12 --cache-only\n
    (delete only cache)   iqba history delete --id 12 --cache-only
    """
    print(f"delete id: {id}")
