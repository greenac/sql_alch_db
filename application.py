from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import db.database as database
#from db.database import db_url, DataBaseType
from db.model import User


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = database.db_url(database.DataBaseType.main)

db = SQLAlchemy(app)

main_eng = database.engine(database.DataBaseType.main)
connector = database.MainDbConnector()
session = connector.new_session()

user = session.query(User).first()
print("user:", user.email)
