"""
TODO: START RESULT TESTING! PEACE!!!!
"""
import random
import pytest
import functools
from iqbacli.data.result import Result


@pytest.fixture
@functools.cache
def result() -> Result:
    return Result(rid=-1, qid=-1, cache_dir_size=100, cache_dir="C:\\\\a\\b\\c")


def test_result_hash_func(result: Result) -> None:
    test_rid = random.randint(1, 1000)
    result.rid = test_rid
    assert hash(result) == test_rid
