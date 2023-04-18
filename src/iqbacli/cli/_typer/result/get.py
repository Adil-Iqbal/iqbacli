from __future__ import annotations

import typer

app = typer.Typer(short_help="Get details of a specific search result.")


@app.callback(invoke_without_command=True)
def get(id: int):
    """
    Get the details of the search result with the provided ID.
    """
    print(f"get id:{id}")
