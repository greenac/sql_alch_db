import sys
sys.path.append("..")

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ..db.database import db_url, DataBaseType
from ..models.models import setup_models, AppModels


app = Flask(__name__)

app.config.update({
    "SQLALCHEMY_DATABASE_URI": db_url(DataBaseType.ml),
})

db = SQLAlchemy(app)

print("app models:", AppModels)

setup_models(db)

print("after app models:", AppModels)
