from __future__ import annotations

import typer

app = typer.Typer(short_help="Get the details of a specific search query.")


@app.callback(invoke_without_command=True)
def get(
    id: int = typer.Argument(
        ..., min=1, show_default=False, help="The ID of search query to retrieve."
    ),
):
    """
    Get the details of the search query with the provided ID.\n
    (example) iqba history get 4\n
    (example) iqba history get --id 4
    """
    print(f"get id:{id}")
