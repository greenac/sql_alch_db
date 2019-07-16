from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from enum import Enum


class DataBaseType(Enum):
    ml = "ml"
    main = "main"


def ml_db_params():
    return {
        "drivername": "postgres",
        "host": "localhost",
        "port": "5432",
        "username": "andre",
        "password": "",
        "database": "ml"
    }


def db_params(db_type):
    params = {
        "drivername": "postgres",
        "host": "localhost",
        "port": "5432",
        "username": "andre",
        "password": "",
    }

    if db_type == DataBaseType.ml:
        params["database"] = "ml"
    elif db_type == DataBaseType.main:
        params["database"] = "local"
    else:
        raise Exception("MISSED_DB_PARAM_BROSEF")

    return params


def db_url(db_type):
    return URL(**db_params(db_type=db_type))


def engine(db_type):
    return create_engine(db_url(db_type=db_type))


class MainDbConnector():
    def __init__(self):
        self.Session = sessionmaker(bind=engine(DataBaseType.main))

    def new_session(self):
        return self.Session()
