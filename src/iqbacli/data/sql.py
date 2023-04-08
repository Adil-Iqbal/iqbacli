from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from typing import Any
from typing import Final
from typing import Generator

from ..logging import create_logger
from ..paths import DB_PATH
from ..paths import SQL_DIR

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
    sql_file = SQL_DIR / filename

    # Read SQL file.
    script = sql_file.read_text()

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
    logger.info("initializing database")
    file("initialize_tables")
