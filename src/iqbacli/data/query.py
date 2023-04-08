from __future__ import annotations

import dataclasses
import functools
from pathlib import Path
from typing import Any
from typing import Optional

from ..logging import create_logger
from . import sql
from .datatypes import SQLiteReprQuery
from .result import Result

logger = create_logger(__file__)


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

    def __hash__(self):
        hash_value = self.qid if self.qid else -1
        logger.debug(f"query hashed to {hash_value=}")
        return hash_value

    def save(self: Query) -> None:
        logger.info(f"saving query to db {self}")
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

    def delete(self: Query) -> None:
        logger.info(f"deleting query from db {self.qid=}")
        sql.query("DELETE FROM queries WHERE qid = ?", self.qid)

    @functools.lru_cache(maxsize=5)
    def get_results(self: Query) -> list[Result]:
        logger.info(f"getting results for query from db {self.qid=}")
        result_reprs = sql.query(
            "SELECT * FROM results WHERE qid = ? ORDER BY rid",
            self.qid,
        )
        return [Result._from_sqlite3(repr) for repr in result_reprs]

    @staticmethod
    def _from_sqlite3(sql_repr: SQLiteReprQuery) -> Query:
        query = Query(
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
        logger.debug(f"new query object created {query=} from sqlite repr {sql_repr=}")
        return query

    @staticmethod
    def get(qid: int) -> Optional[Query]:
        logger.info(f"getting query from db with {qid=}")
        if query_reprs := sql.query("SELECT * FROM queries WHERE qid = ?", qid):
            return Query._from_sqlite3(query_reprs[0])
        logger.info(f"query with {qid=} not found in db")
        return None

    @staticmethod
    @functools.lru_cache(maxsize=1)
    def get_max_qid() -> Any:
        if qid_reprs := sql.query("SELECT MAX(qid) FROM queries"):
            logger.info(f"got max qid from db {qid_reprs[0][0]}")
            return qid_reprs[0][0]
        logger.info("max qid not found in db")
        return None

    @staticmethod
    def last() -> Optional[Query]:
        logger.info("getting last query from db")
        if (max_qid := Query.get_max_qid()) is not None:
            return Query.get(qid=max_qid)
        return None

    @staticmethod
    def list() -> list[Query]:
        logger.info("getting list of queries from db")
        query_reprs = sql.query("SELECT * FROM queries")
        return [Query._from_sqlite3(query_repr) for query_repr in query_reprs]
