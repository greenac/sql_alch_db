from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import src.db.database as database
from src.utils.system import clean_args
from src.bin import create_ml_db


#from db.database import db_url, DataBaseType
import sys

args = clean_args(sys.argv)
if len(args) > 0:
    for arg in args:
        if arg == "create-tables":
            create_ml_db.create_tables()
            break
        else:
            print("Unknown arguemnt:", arg)
            raise Exception("UNKNOWN_COMMAND_LINE_ARG")
else:
    app = Flask(__name__)

    app.config.update({
        "SQLALCHEMY_DATABASE_URI": database.db_url(database.DataBaseType.main),
        "SQLALCHEMY_BINDS": {
            database.DataBaseType.ml: database.db_url(database.DataBaseType.ml)
        },
    })

    db = SQLAlchemy(app)

    main_eng = database.engine(database.DataBaseType.main)
    connector = database.MainDbConnector()
    session = connector.new_session()

    table = connector.get_table(table_name=database.TableName.Users.value)
    user = session.query(table).first()
    print("user:", user.dwollaId)
