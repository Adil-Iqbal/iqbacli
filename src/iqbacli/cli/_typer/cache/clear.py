from __future__ import annotations

import typer

app = typer.Typer(short_help="Delete all files in file cache.")


@app.callback(invoke_without_command=True)
def clear():
    print("clear")
