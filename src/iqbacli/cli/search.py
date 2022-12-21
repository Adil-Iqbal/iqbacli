from typing import Optional
import typer
from pathlib import Path
from ..params import builtins

app = typer.Typer(
    short_help="Perform a search through files for `keywords` in a given `directory`.",
)


@app.callback(invoke_without_command=True)
def search(
    directory: Path,
    keywords: str,
    output_dir: Optional[Path] = typer.Option(
        default=builtins.OUTPUT_DIR,
        show_default=False,
        help="Copy matching files into this directory.",
    ),
    params: Optional[Path] = typer.Option(
        default=builtins.PARAMS,
        show_default=False,
        help="Pass in command arguments from a JSON file.",
    ),
    id: Optional[int] = typer.Option(
        default=builtins.ID,
        show_default=False,
        help="Perform a specific previous search again.",
    ),
    again: bool = typer.Option(
        default=builtins.AGAIN,
        show_default=False,
        help="Perform the most recent search again.",
    ),
    cache: bool = typer.Option(
        default=builtins.CACHE,
        show_default=False,
        help="Save a back-up copy of matching files.",
    ),
    flat: bool = typer.Option(
        default=builtins.FLAT,
        show_default=False,
        help="Only search in the top-level of search directory.",
    ),
    regex: bool = typer.Option(
        default=builtins.REGEX,
        show_default=False,
        help="Treat `keywords` argument as a regular expression.",
    ),
    ignore_ext: str = typer.Option(
        default=builtins.IGNORE_EXT,
        show_default=False,
        help="Ignore files with these extensions. (comma-seperated)",
    ),
    ignore_filename: str = typer.Option(
        default=builtins.IGNORE_FILENAME,
        show_default=False,
        help="Ignore filenames containing these words. (comma-seperated)",
    ),
    ignore_dirname: str = typer.Option(
        default=builtins.IGNORE_DIRNAME,
        show_default=False,
        help="Ignore sub-directories containing these words. (comma-seperated)",
    ),
    only_ext: str = typer.Option(
        default=builtins.ONLY_EXT,
        show_default=False,
        help="Search only files with these extensions. (comma-seperated)",
    ),
    only_filename: str = typer.Option(
        default=builtins.ONLY_FILENAME,
        show_default=False,
        help="Search only filenames containing these words. (comma-seperated)",
    ),
    only_dirname: str = typer.Option(
        default=builtins.ONLY_DIRNAME,
        show_default=False,
        help="Search only sub-directories containing these words. (comma-seperated)",
    ),
):
    """
    Search all files in `directory` for the keywords `keywords`.\n
    (Example) iqba search "C:\\\\path\\\\to\\\\directory" "foo,bar,baz"
    """
    print("search")
