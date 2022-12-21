from iqbacli import cli
from iqbacli.data import initialize_database


def main():
    initialize_database()
    cli.app()


if __name__ == "__main__":
    main()
