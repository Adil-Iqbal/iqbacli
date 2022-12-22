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
    def __init__(self, db_path):
        self.db_path = db_path
        self.commit_called = False
        self.close_called = False

    def cursor(self):
        ...

    def commit(self):
        self.commit_called = True

    def close(self):
        self.close_called = True


def monkeypatch_sqlite3(mp, fake_connection: FakeSQLite3Connection):
    mp.setattr(sqlite3, "connect", lambda _: fake_connection)
