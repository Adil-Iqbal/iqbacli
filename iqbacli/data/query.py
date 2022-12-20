from . import util


class Query:
    @staticmethod
    def initialize_table() -> None:
        util.execute_sql_file("init_query_table")
