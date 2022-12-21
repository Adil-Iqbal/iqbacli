import os
from pathlib import Path
import logging
import sqlite3
from typing import Any
from contextlib import contextmanager


BASE_DIR: Path = Path(__file__).parent.resolve()
DB_PATH: Path = BASE_DIR / "db" / "database.sqlite3"
SQL_DIR: Path = BASE_DIR / "sql"


@contextmanager
def open_db(commit: bool = True) -> sqlite3.Cursor:
    db_path = str(DB_PATH.absolute())
    connection = sqlite3.connect(db_path)
    try:
        yield connection.cursor()
    except sqlite3.DatabaseError as err:
        logging.error(err)
    finally:
        if commit:
            connection.commit()
        connection.close()


def file(filename: str, commit: bool = True) -> Any:
    """Execute an SQL file."""

    # Add file extension, if needed.
    ext = ".sql"
    if not filename.endswith(ext):
        filename += ext

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


def query(query_str: str) -> Any:
    with open_db() as cursor:
        cursor.execute(query_str)
        return cursor.fetchall()


def initialize_database() -> None:
    file("initialize_tables", commit=False)