from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from enum import Enum


class DataBaseType(Enum):
    ml = "ml"
    main = "main"


class TableName(Enum):
    Users = "Users"


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


class DbConnector():
    base = None

    def __init__(self):
        self._engine = None
        self.Session = None
        self.tables = {}

    def new_session(self):
        return self.Session()

    def _reflect_table(self):
        pass

    def get_table(self, table_name):
        print("getting table name from tables:", table_name, self.tables)
        try:
            table = self.tables[table_name]
        except KeyError:
            raise Exception("INVALID_TABLE_NAME")
        return table


class MainDbConnector(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)
        self._engine = engine(DataBaseType.main)
        self.Session = sessionmaker(bind=self._engine)
        # Add other tables that need to be accessed
        self.tables = {
            TableName.Users.value: None
        }
        self._reflect_table()

    def _reflect_table(self):
        if not MainDbConnector.base:
            MainDbConnector.base = automap_base()
            MainDbConnector.base.prepare(self._engine, reflect=True)
        tables = {}
        for table in self.tables:
            try:
                t = MainDbConnector.base.classes.__getattr__(table)
            except KeyError:
                print("No table in classes:", table)
            except Exception as e:
                print("Unknown exception:", e)
            else:
                print("got table:", t)
                tables[table] = t
        self.tables = tables
        return None


class MLDbConnector(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)
        self._engine = engine(DataBaseType.ml)
        self.Session = sessionmaker(bind=self._engine)
        # Add other tables that need to be accessed
        self.tables = {
            TableName.Users.value: None
        }
        self._reflect_table()

    def _reflect_table(self):
        if not MainDbConnector.base:
            MainDbConnector.base = automap_base()
            MainDbConnector.base.prepare(self._engine, reflect=True)
        tables = {}
        for table in self.tables:
            try:
                t = MainDbConnector.base.classes.__getattr__(table)
            except KeyError:
                print("No table in classes:", table)
            except Exception as e:
                print("Unknown exception:", e)
            else:
                print("got table:", t)
                tables[table] = t
        self.tables = tables
        return None
