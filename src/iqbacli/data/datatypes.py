from __future__ import annotations
from typing import Union


SQLiteReprQuery = tuple[
    int, str, str, str, str, bool, bool, bool, str, str, str, str, str, str
]
SQLiteReprResult = tuple[int, int, int, int, int, int, int, int, str]
SQLiteFetchAllQuery = list[SQLiteReprQuery]
SQLiteFetchAllResult = list[SQLiteReprResult]

SQLiteRepr = Union[SQLiteReprQuery, SQLiteReprResult]
SQLiteFetchAll = Union[SQLiteFetchAllQuery, SQLiteFetchAllResult]
