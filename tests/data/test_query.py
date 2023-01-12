import functools
import random
import pytest
from iqbacli.data import sql
from iqbacli.data.query import Query
from pathlib import Path
from .util import reset_db


@pytest.fixture
@functools.cache
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
@functools.cache
def query_repr():
    return (
        -1,
        "raw_test",
        "test",
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


@pytest.fixture
@functools.cache
def num_queries():
    filepath = sql.SQL_DIR / "reset_db.sql"
    return filepath.read_text().count("insert into queries")


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


@reset_db
def test_query_get_result():
    query = Query.get(qid=1)
    query.get_results.cache_clear()
    results = query.get_results()
    assert len(results) == 2


@reset_db
def test_query_get_result_empty():
    query = Query.get(qid=1)
    query.get_results.cache_clear()
    sql.query("DELETE FROM results")
    results = query.get_results()
    assert type(results) == list
    assert len(results) == 0


def test_query_from_sqlite3(query_repr):
    query = Query._from_sqlite3(query_repr)
    assert query.qid == query_repr[0]
    assert query.keywords_raw == query_repr[1]


@reset_db
def test_query_get_success():
    query = Query.get(qid=1)
    assert query.qid == 1
    assert query.keywords_raw == "motivate6129"


@reset_db
def test_query_get_fail():
    query = Query.get(qid=100)
    assert query is None


@reset_db
def test_query_get_max_qid_success(num_queries):
    max_qid = Query.get_max_qid()
    assert max_qid == num_queries


@reset_db
def test_query_get_max_qid_fail():
    Query.get_max_qid.cache_clear()
    sql.query("DELETE FROM queries")
    max_qid = Query.get_max_qid()
    assert max_qid is None


@reset_db
def test_query_last_success(num_queries):
    Query.get_max_qid.cache_clear()
    query = Query.last()
    assert query.qid == num_queries


@reset_db
def test_query_last_fail():
    Query.get_max_qid.cache_clear()
    sql.query("DELETE FROM queries")
    query = Query.last()
    assert query is None


@reset_db
def test_query_list(num_queries):
    query_list = Query.list()
    assert len(query_list) == num_queries


def test_query_hash_func(query):
    test_qid = random.randint(1, 1000)
    query.qid = test_qid
    assert hash(query) == test_qid
