from __future__ import annotations

import sqlite3
from typing import Any, Generator, Final
from contextlib import contextmanager
from ..logging import create_logger
from ..paths import SQL_DIR, DB_PATH

logger = create_logger(__file__)

SQL_EXT: Final[str] = ".sql"


@contextmanager
def open_db(commit: bool = True) -> Generator[sqlite3.Cursor, None, None]:
    db_path = str(DB_PATH.absolute())
    logger.debug(f"{db_path=}")
    connection = sqlite3.connect(db_path)
    try:
        yield connection.cursor()
    except sqlite3.Error as err:
        logger.error(err)
    finally:
        if commit:
            connection.commit()
        connection.close()


def file(filename: str, commit: bool = True) -> list[Any]:
    """Execute an SQL file."""

    # Add file extension, if needed.
    if not filename.endswith(SQL_EXT):
        filename += SQL_EXT

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


def query(query_str: str, *args, commit: bool = True) -> list[Any]:
    """Execute an SQL query."""
    logger.debug(f"running query: {query_str} with args {args}")
    with open_db(commit=commit) as cursor:
        cursor.execute(query_str, args)
        return cursor.fetchall()


def initialize_database() -> None:
    logger.debug(f"Initializing with database path: {DB_PATH}")
    logger.debug(f"Initializing with SQL directory: {SQL_DIR}")
    file("initialize_tables")
