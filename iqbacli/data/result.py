from . import util


class Result:
    @staticmethod
    def initialize_table() -> None:
        util.execute_sql_file("init_result_table")
