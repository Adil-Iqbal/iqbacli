from pathlib import Path
import typer

app = typer.Typer(short_help="Set configuration using JSON file.")


@app.callback(invoke_without_command=True)
def set_file(
    path: Path = typer.Argument(..., file_okay=True, dir_okay=False, exists=True)
):
    """
    Set configuration using JSON file.\n
    (example) iqba config file "C:\\\\path\\\\to\\\\file.json"
    (example) iqba config file --path "C:\\\\path\\\\to\\\\file.json"
    """
    print(f"file path: {path}")
