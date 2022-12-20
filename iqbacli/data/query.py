from . import util


class Query:
    def initialize_table() -> None:
        with util.open_db() as cursor:
            query = util.SQL_DIR / "init_query_table.sql"
            cursor.executescript()
