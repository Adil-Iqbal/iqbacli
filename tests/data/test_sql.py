from iqbacli.data import sql
from . import util


@util.delete_db
def test_open_db_creates_file_at_base_path():
    assert not sql.DB_PATH.exists()
    with sql.open_db() as _:
        ...
    assert sql.DB_PATH.exists()


@util.delete_db
def test_open_db_commit_on_close(monkeypatch):
    db_conn = util.FakeSQLite3Connection()
    util.monkeypatch_sqlite3(monkeypatch, db_conn)
    with sql.open_db():
        ...
    assert db_conn.commit_called


@util.delete_db
def test_open_db_commit_override(monkeypatch):
    db_conn = util.FakeSQLite3Connection()
    util.monkeypatch_sqlite3(monkeypatch, db_conn)
    with sql.open_db(commit=False):
        ...
    assert not db_conn.commit_called


@util.delete_db
def test_open_db_resource_closed(monkeypatch):
    db_conn = util.FakeSQLite3Connection()
    util.monkeypatch_sqlite3(monkeypatch, db_conn)
    with sql.open_db():
        ...
    assert db_conn.close_called


@util.delete_db
def test_open_db_resource_closed_on_error(monkeypatch):
    db_conn = util.FakeSQLite3Connection()
    util.monkeypatch_sqlite3(monkeypatch, db_conn)
    try:
        with sql.open_db():
            raise ValueError()
    except ValueError:
        assert db_conn.close_called


@util.delete_db
def test_open_db_uses_correct_path(monkeypatch):
    expected_path = str(sql.DB_PATH.absolute())
    db_conn = util.FakeSQLite3Connection()
    util.monkeypatch_sqlite3(monkeypatch, db_conn)
    with sql.open_db(commit=True):
        ...
    assert db_conn.db_path == expected_path


@util.delete_db
def test_open_db_cursor_called_and_returned(monkeypatch):

    db_conn = util.FakeSQLite3Connection()
    util.monkeypatch_sqlite3(monkeypatch, db_conn)
    with sql.open_db(commit=True) as cursor:
        assert db_conn.cursor_object == cursor
    assert db_conn.cursor_called
