from __future__ import annotations

import typer

app = typer.Typer(short_help="Undo most recent search query.")


@app.callback(invoke_without_command=True)
def undo():
    """
    Delete the most recent search query.\n
    (example) iqba history undo
    """
    print("undo")
