from __future__ import annotations

import pytest

from iqbacli.data import sql

from .util import FakeSQLite3Connection
from .util import delete_db
from .util import monkeypatch_sqlite3


@pytest.fixture
def conn(monkeypatch):
    conn = FakeSQLite3Connection()
    monkeypatch_sqlite3(monkeypatch, conn)
    return conn


@delete_db
def test_open_db_creates_file_at_base_path():
    assert not sql.DB_PATH.exists()
    with sql.open_db():
        ...
    assert sql.DB_PATH.exists()


@delete_db
def test_open_db_commit_on_close(conn):
    with sql.open_db():
        ...
    assert conn.commit_called


@delete_db
def test_open_db_commit_override(conn: FakeSQLite3Connection):
    with sql.open_db(commit=False):
        ...
    assert not conn.commit_called


def test_open_db_resource_closed(conn: FakeSQLite3Connection):
    with sql.open_db():
        ...
    assert conn.close_called


def test_open_db_resource_closed_on_error(conn: FakeSQLite3Connection):
    try:
        with sql.open_db():
            raise ValueError()
    except ValueError:
        assert conn.close_called


def test_open_db_uses_correct_path(conn: FakeSQLite3Connection):
    expected_path = str(sql.DB_PATH.absolute())
    with sql.open_db(commit=True):
        ...
    assert conn.db_path == expected_path


def test_open_db_cursor_called_and_cursor_returned(conn: FakeSQLite3Connection):
    with sql.open_db(commit=True) as cursor:
        assert conn.cursor_object == cursor
    assert conn.cursor_called


def test_query_success(conn: FakeSQLite3Connection):
    query_str = "select * from ?"
    sql.query(query_str, "foo")
    assert conn.commit_called
    assert conn.cursor_object.execute_called
    assert conn.cursor_object.fetchall_called
    assert conn.cursor_object.execute_query_str == query_str
    assert conn.cursor_object.execute_args == (("foo",),)


def test_query_success_with_commit_override(conn: FakeSQLite3Connection):
    query_str = "select * from ?"
    sql.query(query_str, "foo", commit=False)
    assert not conn.commit_called


def test_sql_file_can_read(conn: FakeSQLite3Connection):
    filename = "test_script.sql"
    filepath = sql.SQL_DIR / filename
    sql.file(filename)
    assert conn.commit_called
    assert conn.cursor_object.executescript_called
    assert conn.cursor_object.fetchall_called
    filepath.read_text() == conn.cursor_object.excutescript_script_arg


def test_sql_file_can_read_without_file_ext(conn: FakeSQLite3Connection):
    filename = "test_script"
    filepath = sql.SQL_DIR / f"{filename}.sql"
    sql.file(filename)
    assert conn.commit_called
    assert conn.cursor_object.executescript_called
    assert conn.cursor_object.fetchall_called
    filepath.read_text() == conn.cursor_object.excutescript_script_arg


def test_sql_file_with_commit_override(conn: FakeSQLite3Connection):
    filename = "test_script.sql"
    sql.file(filename, commit=False)
    assert not conn.commit_called


def test_initialize_database_func(conn: FakeSQLite3Connection):
    filename = "initialize_tables.sql"
    filepath = sql.SQL_DIR / filename
    sql.initialize_database()
    filepath.read_text() == conn.cursor_object.excutescript_script_arg
