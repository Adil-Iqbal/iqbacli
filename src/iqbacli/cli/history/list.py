from __future__ import annotations

import typer

app = typer.Typer(short_help="Display list of previous search queries.")


@app.callback(invoke_without_command=True)
def list():
    """
    List out all search queries that have been saved.\n
    (example) iqba history list
    """
    print("list")
