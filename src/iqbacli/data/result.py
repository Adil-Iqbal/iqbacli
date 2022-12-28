from __future__ import annotations

from .datatypes import SQLiteReprResult


class Result:
    @staticmethod
    def _from_sqlite3(sql_repr: SQLiteReprResult) -> Result:
        return Result()
