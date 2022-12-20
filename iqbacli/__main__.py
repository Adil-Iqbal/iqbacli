from iqbacli import cli
from iqbacli.data.query import Query
from iqbacli.data.result import Result


def main():
    Query.initialize_table()
    Result.initialize_table()
    cli.app()


if __name__ == "__main__":
    main()
