from typing import Optional
from . import sql
import dataclasses
from pathlib import Path
from re import Pattern


@dataclasses.dataclass
class Query:
    id: int
    keywords_raw: str
    keywords_pattern: Pattern
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
            INSERT INTO query (
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
            self.directory,
            self.output_dir,
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


def delete_query(id: int) -> None:
    sql.query("DELETE FROM query WHERE id = ?", id)


def get_query(id: int) -> Optional[Query]:
    ret = sql.query("SELECT * FROM query WHERE id = ?", id)
    if len(ret) == 0:
        return None
    return Query(*ret[0])
