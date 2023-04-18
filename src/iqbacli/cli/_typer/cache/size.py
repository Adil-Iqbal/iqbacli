from __future__ import annotations

import typer

app = typer.Typer(short_help="Display size of file cache.")


@app.callback(invoke_without_command=True)
def size():
    """
    Display size of file cache in megabytes. \n
    (Example) iqba cache size
    """
    print("size")
