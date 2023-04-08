from __future__ import annotations

import typer

app = typer.Typer(short_help="Open cached directory in file explorer (if any).")


@app.callback(invoke_without_command=True)
def show(id: int):
    """
    See all files that matched the associated search query (if we have them).
    """
    print(f"show id:{id}")
