"""
TODO: START RESULT TESTING! PEACE!!!!
"""
from pathlib import Path
import random
import pytest
import functools
from iqbacli.data.result import Result
from iqbacli.data import sql
from .util import reset_db


@pytest.fixture
@functools.cache
def result() -> Result:
    return Result(
        rid=-1, qid=-1, cache_dir_size=100, cache_dir=Path(__file__).parent.absolute()
    )


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
