from pathlib import Path
import typer

app = typer.Typer(short_help="Set configuration using JSON file.")


@app.callback(invoke_without_command=True)
def set_file(file: Path):
    """
    Set configuration using JSON file.\n
    (Example) iqba config file "C:\\\\path\\\\to\\\\file.json"
    """
    print(f"file path: {file}")
