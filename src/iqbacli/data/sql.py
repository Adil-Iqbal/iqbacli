from pathlib import Path
import logging
import sqlite3
from typing import Any, Generator
from contextlib import contextmanager


sql_ext = ".sql"
BASE_DIR: Path = Path(__file__).parent.resolve()
SQL_DIR: Path = BASE_DIR / "sql"
DB_PATH: Path = SQL_DIR / "database.sqlite3"


@contextmanager
def open_db(commit: bool = True) -> Generator[sqlite3.Cursor, None, None]:
    db_path = str(DB_PATH.absolute())
    connection = sqlite3.connect(db_path)
    try:
        yield connection.cursor()
    except sqlite3.Error as err:
        logging.error(err)
    finally:
        if commit:
            connection.commit()
        connection.close()


def file(filename: str, commit: bool = True) -> list[tuple[Any, ...]]:
    """Execute an SQL file."""

    # Add file extension, if needed.
    if not filename.endswith(sql_ext):
        filename += sql_ext

    # Determine absolute path to the file.
    filepath = SQL_DIR / filename

    # Read SQL file.
    filepath_str = str(filepath.absolute())
    with open(filepath_str, "r") as sql_file:
        script = sql_file.read()

    # Execute file and return results.
    with open_db(commit=commit) as cursor:
        cursor.executescript(script)
        return cursor.fetchall()


def query(query_str: str, *args, commit: bool = True) -> Any:
    """Execute an SQL query."""
    with open_db(commit=commit) as cursor:
        cursor.execute(query_str, args)
        return cursor.fetchall()


def initialize_database() -> None:
    file("initialize_tables", commit=False)
