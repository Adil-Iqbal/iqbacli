from ..data import sql
from .filesystem import create_user_data


def init():
    create_user_data()
    sql.initialize_database()
