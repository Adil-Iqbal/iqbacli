from __future__ import annotations

from . import sql
import dataclasses
import functools
from pathlib import Path
from typing import Optional, Any
from .datatypes import SQLiteReprResult


@dataclasses.dataclass
class Result:
    rid: int
    qid: int
    search_count: int = 0
    match_count: int = 0
    unsupported_count: int = 0
    fail_to_parse_count: int = 0
    fail_to_copy_count: int = 0
    cache_dir_size: int = 0
    cache_dir: Optional[Path] = None

    def __hash__(self: Result):
        return self.rid if self.rid else -1

    def save(self: Result) -> None:
        sql.query(
            """
            INSERT INTO results (
                qid,
                search_count,
                match_count,
                unsupported_count,
                fail_to_parse_count,
                fail_to_copy_count,
                cache_dir_size,
                cache_dir
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
            self.qid,
            self.search_count,
            self.match_count,
            self.unsupported_count,
            self.fail_to_parse_count,
            self.fail_to_copy_count,
            self.cache_dir_size,
            str(self.cache_dir.absolute()) if self.cache_dir else "",
        )

    def delete(self: Result) -> None:
        sql.query("DELETE FROM results WHERE rid = ?", self.rid)

    def cached(self: Result, cache_dir: Path, cache_dir_size: int) -> None:
        self.cache_dir = cache_dir
        self.cache_dir_size = cache_dir_size
        sql.query(
            "UPDATE results SET cache_dir = ?, cache_dir_size = ? WHERE rid = ?",
            str(self.cache_dir.absolute()),
            self.cache_dir_size,
            self.rid,
        )

    def cache_removed(self: Result) -> None:
        self.cache_dir = None
        self.cache_dir_size = 0
        sql.query(
            "UPDATE results SET cache_dir = NULL, cache_dir_size = 0 WHERE rid = ?",
            self.rid,
        )

    @staticmethod
    def _from_sqlite3(sql_repr: SQLiteReprResult) -> Result:
        return Result(
            rid=sql_repr[0],
            qid=sql_repr[1],
            search_count=sql_repr[2],
            match_count=sql_repr[3],
            unsupported_count=sql_repr[4],
            fail_to_parse_count=sql_repr[5],
            fail_to_copy_count=sql_repr[6],
            cache_dir_size=sql_repr[7],
            cache_dir=Path(sql_repr[8]) if sql_repr[8] else None,
        )

    @staticmethod
    def get(rid: int) -> Optional[Result]:
        if result_reprs := sql.query("SELECT * FROM results WHERE rid = ?", rid):
            return Result._from_sqlite3(result_reprs[0])
        return None

    @staticmethod
    @functools.cache
    def get_max_rid() -> Any:
        if rid_reprs := sql.query("SELECT MAX(rid) FROM results"):
            return rid_reprs[0][0]
        return None

    @staticmethod
    def last() -> Optional[Result]:
        if (max_rid := Result.get_max_rid()) is not None:
            return Result.get(rid=max_rid)
        return None

    @staticmethod
    def list() -> list[Result]:
        result_reprs = sql.query("SELECT * FROM results")
        return [Result._from_sqlite3(result_repr) for result_repr in result_reprs]
