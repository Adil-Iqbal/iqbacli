from __future__ import annotations

from typing import TypedDict, Union

SQLiteReprQuery = tuple[
    int, str, str, str, str, bool, bool, bool, str, str, str, str, str, str
]
SQLiteReprResult = tuple[int, int, int, int, int, int, int, int, str]
SQLiteFetchAllQuery = list[SQLiteReprQuery]
SQLiteFetchAllResult = list[SQLiteReprResult]

SQLiteRepr = Union[SQLiteReprQuery, SQLiteReprResult]
SQLiteFetchAll = Union[SQLiteFetchAllQuery, SQLiteFetchAllResult]


class ConfigDict(TypedDict):
    cache: bool
    flat: bool
    regex: bool
    only_ext: str
    only_filename: str
    only_dirname: str
    ignore_ext: str
    ignore_filename: str
    ignore_dirname: str
    max_cached: int
    max_cache_size: int
