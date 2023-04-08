from __future__ import annotations

import typer

from iqbacli.driver import config

app = typer.Typer(short_help="Display path to configuration file.")


@app.callback(invoke_without_command=True)
def path():
    """
    Display path to configuration file.\n
    (example) iqba config path
    """
    print(config.get_path())
