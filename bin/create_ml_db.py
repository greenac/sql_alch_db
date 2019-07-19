from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ..db.database import db_url, DataBaseType


app = Flask(__name__)

app.config.update({
    "SQLALCHEMY_DATABASE_URI": db_url(DataBaseType.ml),
})

db = SQLAlchemy(app)
db.create_all()