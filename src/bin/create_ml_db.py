from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from ..db.database import db_url, DataBaseType
from ..models.models import setup_models, AppModels


def create_tables():
    app = Flask(__name__)

    app.config.update({
        "SQLALCHEMY_DATABASE_URI": db_url(DataBaseType.ml),
        "SQLALCHEMY_TRACK_MODIFICATIONS": True,
    })

    SQLAlchemy(app)
    engine = create_engine(db_url(db_type=DataBaseType.ml))
    Base = declarative_base()
    setup_models(Base)
    Base.metadata.create_all(engine)
