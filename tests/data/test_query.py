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


def test_query_get_success():
    ...


def test_query_get_fail():
    ...


def test_query_get_max_qid_success():
    ...


def test_query_get_max_qid_fail():
    ...


def test_query_last_success():
    ...


def test_query_last_fail():
    ...


def test_query_list():
    ...
