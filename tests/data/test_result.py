"""
TODO: START RESULT TESTING! PEACE!!!!
"""
from pathlib import Path
import random
import pytest
import functools
from iqbacli.data.datatypes import SQLiteReprResult
from iqbacli.data.result import Result
from iqbacli.data import sql
from .util import reset_db


@pytest.fixture
@functools.cache
def result() -> Result:
    return Result(
        rid=-1, qid=-1, cache_dir_size=100, cache_dir=Path(__file__).parent.absolute()
    )


@pytest.fixture
@functools.cache
def result_repr() -> SQLiteReprResult:
    return (
        -1,
        -1,
        0,
        0,
        0,
        0,
        0,
        0,
        "C:\\a\\b\\c",
    )


@pytest.fixture
@functools.cache
def num_results():
    filepath = sql.SQL_DIR / "reset_db.sql"
    with open(str(filepath), "r") as file:
        return file.read().count("insert into results")


def test_result_hash_func(result: Result) -> None:
    test_rid = random.randint(1, 1000)
    result.rid = test_rid
    assert hash(result) == test_rid


@reset_db
def test_result_save(result: Result) -> None:
    first_len = sql.query("SELECT COUNT(*) FROM results")[0][0]
    result.save()
    second_len = sql.query("SELECT COUNT(*) FROM results")[0][0]
    assert second_len - first_len == 1


@reset_db
def test_result_delete() -> None:
    result = Result.get(rid=1)
    first_len = sql.query("SELECT COUNT(*) FROM results")[0][0]
    result.delete()
    second_len = sql.query("SELECT COUNT(*) FROM results")[0][0]
    assert second_len - first_len == -1


@reset_db
def test_result_cached() -> None:
    result = Result.get(rid=1)
    result.cache_removed()
    cache_dir = Path("C:\\\\a\\b\\c")
    cache_dir_size = random.randint(1, 1000)

    result.cached(cache_dir=cache_dir, cache_dir_size=cache_dir_size)

    assert result.cache_dir is not None
    assert result.cache_dir_size == cache_dir_size

    new_result = Result.get(rid=1)
    assert new_result.cache_dir is not None
    assert new_result.cache_dir_size == cache_dir_size


def test_result_cache_removed() -> None:
    result = Result.get(rid=1)
    result.cache_removed()
    assert result.cache_dir is None
    assert result.cache_dir_size == 0

    new_result = Result.get(rid=1)
    assert new_result.cache_dir is None
    assert new_result.cache_dir_size == 0


def test_result_from_sqlite3(result_repr: SQLiteReprResult) -> None:
    result = Result._from_sqlite3(result_repr)
    assert result.rid == result_repr[0]
    assert result.qid == result_repr[1]
    assert str(result.cache_dir.absolute()) == result_repr[8]


@reset_db
def test_result_get_success() -> None:
    result = Result.get(rid=1)
    assert result.rid == 1
    assert str(result.cache_dir.absolute()) == r"C:\uktv\ufy\dlip"


@reset_db
def test_result_get_fail(num_results: int) -> None:
    result = Result.get(rid=num_results + 1)
    assert result is None


@reset_db
def test_result_get_max_rid_success(num_results: int) -> None:
    max_rid = Result.get_max_rid()
    assert max_rid == num_results


@reset_db
def test_result_get_max_rid_fail() -> None:
    Result.get_max_rid.cache_clear()
    sql.query("DELETE FROM results")
    max_rid = Result.get_max_rid()
    assert max_rid is None


@reset_db
def test_result_last_success(num_results: int) -> None:
    Result.get_max_rid.cache_clear()
    result = Result.last()
    assert result.rid == num_results


@reset_db
def test_result_last_fail() -> None:
    Result.get_max_rid.cache_clear()
    sql.query("DELETE FROM results")
    result = Result.last()
    assert result is None


@reset_db
def test_result_list(num_results: int) -> None:
    result_list = Result.list()
    assert len(result_list) == num_results
