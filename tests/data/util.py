import sqlite3
import functools
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
    def __init__(self):
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
        self.cursor_object = FakeSQLite3Cursor()
        return self.cursor_object

    def commit(self):
        self.commit_called = True

    def close(self):
        self.close_called = True


class FakeSQLite3Cursor:
    ...


def monkeypatch_sqlite3(mp, fake_connection: FakeSQLite3Connection):
    mp.setattr(sqlite3, "connect", lambda db_path: fake_connection(db_path))
