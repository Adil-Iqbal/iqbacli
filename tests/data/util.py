from __future__ import annotations

import functools
import sqlite3
from pathlib import Path
from typing import Any
from typing import Optional

from iqbacli.data import sql

sql.DB_PATH = Path(__file__).parent.resolve() / "test.sqlite3"
sql.SQL_DIR = Path(__file__).parent.resolve() / "sql"
FakeReturnData = Optional[list[Any]]


def delete_db(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if sql.DB_PATH.exists() and sql.DB_PATH.is_file():
            sql.DB_PATH.unlink()
        func(*args, **kwargs)

    return wrapper


def reset_db(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sql.file("reset_db")
        func(*args, **kwargs)

    return wrapper


class FakeSQLite3Connection:
    def __init__(self):
        self.return_data = None
        self.cursor_object = None
        self.db_path = None
        self.commit_called = False
        self.close_called = False
        self.cursor_called = False

    def __call__(self, db_path: str, return_data: FakeReturnData = None):
        self.db_path = db_path
        self.return_data = return_data
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
    def __init__(self, return_data: FakeReturnData = None):
        self.return_data = return_data
        self.executescript_called = False
        self.excutescript_script_arg = None
        self.execute_called = False
        self.execute_query_str = None
        self.execute_args = None
        self.fetchall_called = False

    def execute(self, query_str: str, *args):
        self.execute_called = True
        self.execute_query_str = query_str
        self.execute_args = args

    def executescript(self, script: str):
        self.executescript_called = True
        self.excutescript_script_arg = script

    def fetchall(self):
        self.fetchall_called = True
        return self.return_data


def monkeypatch_sqlite3(
    monkeypatch,
    fake_connection: FakeSQLite3Connection,
    /,
    return_data: FakeReturnData = None,
):
    def fake_connect_func(db_path):
        return fake_connection(db_path=db_path, return_data=return_data)

    monkeypatch.setattr(sqlite3, "connect", fake_connect_func)
