from typing import Optional
import typer
from pathlib import Path
from ..params import builtins

app = typer.Typer(
    short_help="Perform a search through files for `keywords` in a given `directory`.",
)


def _resolve_keywords(keywords: Optional[str], regex: bool) -> str:
    if keywords is None and not regex:
        kw = typer.prompt("Please enter a comma-seperated list of keywords: ")
    elif keywords is None and regex:
        kw = typer.prompt("Please enter a regular expression: ")
    if type(kw) != str:
        raise typer.Abort()
    return kw


@app.callback(invoke_without_command=True)
def search(
    directory: Path = typer.Argument(
        ...,
        help="The directory to be searched.",
        file_okay=False,
        dir_okay=True,
        exists=True,
    ),
    keywords: Optional[str] = typer.Argument(
        default=None, help="A comma-seperated list of keywords to look for."
    ),
    output_dir: Optional[Path] = typer.Option(
        default=builtins.OUTPUT_DIR,
        envvar="IQBA_OUTPUT_DIR",
        show_envvar=False,
        show_default=False,
        file_okay=False,
        dir_okay=True,
        exists=True,
        help="Copy matching files into this directory.",
    ),
    params: Optional[Path] = typer.Option(
        default=builtins.PARAMS,
        show_default=False,
        file_okay=True,
        dir_okay=False,
        exists=True,
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
    keywords = _resolve_keywords(keywords=keywords, regex=regex)
    print("search")
