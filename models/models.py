from ..db.database import DataBaseType
from enum import Enum


AppModels = {}


class ModelType(Enum):
    Feature = "Feature"


def setup_models(db):
    class Feature():
        def __init__(self):
            __bind_key__ = DataBaseType.ml.value

            id = db.Column(db.Integer, primary_key=True)
            username = db.Column(db.String(80), unique=True)

    AppModels[ModelType.Feature] = Feature
