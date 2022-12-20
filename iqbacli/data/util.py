import os
from pathlib import Path
import logging
import sqlite3
import dotenv
from contextlib import contextmanager

dotenv.load_dotenv()

BASE_DIR: Path = Path(__file__).parent.resolve()
DB_PATH: Path = BASE_DIR / "db" / "database.db"
SQL_DIR: Path = BASE_DIR / "sql"


def check_env_var(varname: str, value: str) -> bool:
    return varname in os.environ and os.getenv(varname) == value


@contextmanager
def open_db() -> sqlite3.Cursor:
    db_path = str(DB_PATH.absolute())
    connection = sqlite3.connect(db_path)
    try:
        yield connection.cursor()
    except sqlite3.DatabaseError as err:
        logging.error(err)
    finally:
        connection.commit()
        connection.close()


def execute_sql_file(filename: str):
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
    with open_db() as cursor:
        cursor.executescript(script)
        return cursor.fetchall()
