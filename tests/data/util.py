import sqlite3
import functools
from typing import Any, Optional
from iqbacli.data import sql


def delete_db(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if sql.DB_PATH.exists() and sql.DB_PATH.is_file():
            sql.DB_PATH.unlink()
        func(*args, **kwargs)

    return wrapper


def reset_db(func):
    @functools.wraps(func)
    @delete_db
    def wrapper(*args, **kwargs):
        sql.initialize_database()
        func(*args, **kwargs)

    return wrapper


class FakeSQLite3Connection:
    def __init__(self, return_data: Optional[list[tuple[Any, ...]]] = None):
        self.return_data = return_data
        self.cursor_object = None
        self.db_path = None
        self.commit_called = False
        self.close_called = False
        self.cursor_called = False

    def __call__(self, db_path: str):
        self.db_path = db_path
        return self

    def cursor(self):
        self.cursor_called = True
        self.cursor_object = FakeSQLite3Cursor(return_data=self.return_data)
        return self.cursor_object

    def commit(self):
        self.commit_called = True

    def close(self):
        self.close_called = True


class FakeSQLite3Cursor:
    def __init__(self, return_data: Optional[list[tuple[Any, ...]]] = None):
        self.return_data = return_data
        self.execute_called = False
        self.execute_query_str = None
        self.execute_args = None
        self.fetchall_called = False

    def execute(self, query_str: str, *args):
        self.execute_called = True
        self.execute_query_str = query_str
        self.execute_args = args
        return None

    def executescript(self, script: str):
        ...

    def fetchall(self):
        self.fetchall_called = True
        return self.return_data


def monkeypatch_sqlite3(mp, fake_connection: FakeSQLite3Connection):
    mp.setattr(sqlite3, "connect", lambda db_path: fake_connection(db_path))
