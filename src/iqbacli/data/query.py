from __future__ import annotations
import re

from typing import Any, Optional, TypeVar
from . import sql
import dataclasses
from pathlib import Path
from .datatypes import SQLiteReprQuery
from .result import Result


TQuery = TypeVar("TQuery", bound="Query")


@dataclasses.dataclass
class Query:
    qid: int
    keywords_raw: str
    keywords_pattern: str
    directory: Path
    output_dir: Path
    cache: bool
    flat: bool
    regex: bool
    only_ext: str
    only_filename: str
    only_dirname: str
    ignore_ext: str
    ignore_filename: str
    ignore_dirname: str

    def save(self):
        sql.query(
            """
            INSERT INTO queries (
                    keywords_raw,
                    keywords_pattern,
                    directory,
                    output_dir,
                    cache,
                    flat,
                    regex,
                    only_ext,
                    only_filename,
                    only_dirname,
                    ignore_ext,
                    ignore_filename,
                    ignore_dirname
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            self.keywords_raw,
            self.keywords_pattern,
            str(self.directory.absolute()),
            str(self.output_dir.absolute()),
            self.cache,
            self.flat,
            self.regex,
            self.only_ext,
            self.only_filename,
            self.only_dirname,
            self.ignore_ext,
            self.ignore_filename,
            self.ignore_dirname,
        )

    def delete(self):
        sql.query("DELETE FROM query WHERE qid = ?", self.qid)

    def get_results(self) -> Optional[list[Result]]:
        if result_reprs := sql.query(
            "SELECT * FROM results WHERE qid = ? ORDER BY rid",
            self.qid,
        ):
            return [Result._from_sqlite3(repr) for repr in result_reprs]
        return None

    @staticmethod
    def _from_sqlite3(sql_repr: SQLiteReprQuery) -> Query:
        return Query(
            qid=sql_repr[0],
            keywords_raw=sql_repr[1],
            keywords_pattern=sql_repr[2],
            directory=Path(sql_repr[3]),
            output_dir=Path(sql_repr[4]),
            cache=sql_repr[5],
            flat=sql_repr[6],
            regex=sql_repr[7],
            only_ext=sql_repr[8],
            only_filename=sql_repr[9],
            only_dirname=sql_repr[10],
            ignore_ext=sql_repr[11],
            ignore_filename=sql_repr[12],
            ignore_dirname=sql_repr[13],
        )

    @staticmethod
    def get(qid: int) -> Optional[Query]:
        if query_reprs := sql.query("SELECT * FROM queries WHERE qid = ?", qid):
            return Query._from_sqlite3(query_reprs[0])
        return None

    @staticmethod
    def get_max_qid() -> Any:
        if qid_reprs := sql.query("SELECT MAX(qid) FROM queries"):
            return qid_reprs[0][0]
        return None

    @staticmethod
    def last() -> Optional[Query]:
        if (max_qid := Query.get_max_qid()) is not None:
            return Query.get(qid=max_qid)
        return None

    @staticmethod
    def list() -> Optional[list[Query]]:
        if query_reprs := sql.query("SELECT * FROM queries"):
            return [Query._from_sqlite3(query_repr) for query_repr in query_reprs]
        return None
