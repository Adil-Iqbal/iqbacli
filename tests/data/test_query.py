"""
TODO: Test the Query module. The utilities built will also help with test_result.py
TODO: Start working on result.py & test_result.py. That's secondary to testing query.
"""

import pytest
from iqbacli.data import sql
from iqbacli.data.query import Query
from pathlib import Path
from .util import reset_db


@pytest.fixture
def query():
    return Query(
        qid=-1,
        keywords_raw="test",
        keywords_pattern="test",
        directory=Path(__file__).parent.resolve(),
        output_dir=Path(__file__).parent.parent.resolve(),
        cache=True,
        flat=False,
        regex=False,
        only_ext="abc,def",
        only_filename="bingo",
        only_dirname="bongo",
        ignore_ext="lmnop,xyz",
        ignore_filename="honky",
        ignore_dirname="chonky",
    )


@pytest.fixture
def query_repr():
    return (
        -1,
        "test",
        "raw_test",
        "C:\\\\a\\b\\c",
        "C:\\\\x\\y\\z",
        True,
        False,
        True,
        "abc,def",
        "bingo",
        "bongo",
        "xyz,lmnop",
        "honky",
        "chonky",
    )


@reset_db
def test_query_save(query: Query) -> None:
    first_len = sql.query("SELECT COUNT(*) FROM queries")[0][0]
    query.save()
    second_len = sql.query("SELECT COUNT(*) FROM queries")[0][0]
    assert second_len - first_len == 1


@reset_db
def test_query_delete():
    query = Query.get(qid=1)
    first_len = sql.query("SELECT COUNT(*) FROM queries")[0][0]
    query.delete()
    second_len = sql.query("SELECT COUNT(*) FROM queries")[0][0]
    assert second_len - first_len == -1


def test_query_get_result():
    ...


def test_query_get_result_empty():
    ...


def test_query_from_sqlite3():
    ...


@reset_db
def test_query_get_success():
    query = Query.get(qid=5)
    assert query.qid == 5
    assert query.keywords_raw == "fasten7556"


@reset_db
def test_query_get_fail():
    query = Query.get(qid=100)
    assert query is None


@reset_db
def test_query_get_max_qid_success():
    filepath = sql.SQL_DIR / "sample_query_data.sql"
    with open(str(filepath), "r") as file:
        expected_max_qid = file.read().count("queries")
    max_qid = Query.get_max_qid()
    assert max_qid == expected_max_qid


@reset_db
def test_query_get_max_qid_fail():
    sql.query("DELETE FROM queries")
    max_qid = Query.get_max_qid()
    assert max_qid is None


@reset_db
def test_query_last_success():
    filepath = sql.SQL_DIR / "sample_query_data.sql"
    with open(str(filepath), "r") as file:
        expected_qid = file.read().count("queries")
    query = Query.last()
    assert query.qid == expected_qid


@reset_db
def test_query_last_fail():
    sql.query("DELETE FROM queries")
    query = Query.last()
    assert query is None


def test_query_list():
    ...
