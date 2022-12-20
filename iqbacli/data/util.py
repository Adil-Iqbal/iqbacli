import os
from pathlib import Path
import logging
import sqlite3
import dotenv
from contextlib import contextmanager

dotenv.load_dotenv()

BASE_DIR: Path = Path(__file__).parent.resolve()
db_path: Path = BASE_DIR / "db" / "data.db"
SQL_DIR: Path = BASE_DIR / "sql"


def check_env_var(varname: str, value: str) -> bool:
    return varname in os.environ and os.getenv(varname) == value


def resolve_db_file() -> str:
    """Create database file and return path."""
    if not db_path.exists():
        db_path.touch()
    logging.info(f"Database path: {db_path}")
    return str(db_path.absolute())


@contextmanager
def open_db() -> sqlite3.Cursor:
    db_file = resolve_db_file()
    connection = sqlite3.connect(db_file)
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
    if not filepath.exists() or not filepath.is_file():
        raise FileNotFoundError(f"{filepath.absolute()}")

    # Read SQL file.
    filepath_str = str(filepath.absolute())
    with open(filepath_str, "r") as sql_file:
        script = SQL_DIR.read()

    # Execute file and return results.
    with open_db() as cursor:
        cursor.executescript(script)
        return cursor.fetchall()
