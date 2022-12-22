import functools
from iqbacli.data import sql


def delete_db(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if sql.DB_PATH.exists() and sql.DB_PATH.is_file():
            sql.DB_PATH.unlink()
        func(*args, **kwargs)

    return wrapper


def reset_db(func):
    @functools.wraps(func)
    @delete_db
    def wrapper(*args, **kwargs):
        sql.initialize_database()
        func(*args, **kwargs)

    return wrapper


@delete_db
def test_open_db_creates_file_at_base_path():
    assert not sql.DB_PATH.exists()
    with sql.open_db() as _:
        ...
    assert sql.DB_PATH.exists()
