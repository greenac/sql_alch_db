from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import db.database as database
#from db.database import db_url, DataBaseType


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
