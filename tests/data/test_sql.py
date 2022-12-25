from iqbacli.data import sql
from . import util
import pytest


@pytest.fixture
def db_conn(monkeypatch):
    conn = util.FakeSQLite3Connection()
    util.monkeypatch_sqlite3(monkeypatch, conn)
    return conn


@util.delete_db
def test_open_db_creates_file_at_base_path():
    assert not sql.DB_PATH.exists()
    with sql.open_db() as _:
        ...
    assert sql.DB_PATH.exists()


@util.delete_db
def test_open_db_commit_on_close(db_conn):
    with sql.open_db():
        ...
    assert db_conn.commit_called


@util.delete_db
def test_open_db_commit_override(db_conn: util.FakeSQLite3Connection):
    with sql.open_db(commit=False):
        ...
    assert not db_conn.commit_called


@util.delete_db
def test_open_db_resource_closed(db_conn: util.FakeSQLite3Connection):
    with sql.open_db():
        ...
    assert db_conn.close_called


@util.delete_db
def test_open_db_resource_closed_on_error(db_conn: util.FakeSQLite3Connection):
    try:
        with sql.open_db():
            raise ValueError()
    except ValueError:
        assert db_conn.close_called


@util.delete_db
def test_open_db_uses_correct_path(db_conn: util.FakeSQLite3Connection):
    expected_path = str(sql.DB_PATH.absolute())
    with sql.open_db(commit=True):
        ...
    assert db_conn.db_path == expected_path


@util.delete_db
def test_open_db_cursor_called_and_cursor_returned(db_conn: util.FakeSQLite3Connection):
    with sql.open_db(commit=True) as cursor:
        assert db_conn.cursor_object == cursor
    assert db_conn.cursor_called


@util.reset_db
def test_query_success(db_conn: util.FakeSQLite3Connection):
    query_str = "select * from ?"
    sql.query(query_str, "foo")
    assert db_conn.cursor_object.execute_called
    assert db_conn.cursor_object.fetchall_called
    assert db_conn.cursor_object.execute_query_str == query_str
    assert db_conn.cursor_object.execute_args == (("foo",),)
