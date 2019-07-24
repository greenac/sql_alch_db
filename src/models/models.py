from ..db.database import DataBaseType
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from enum import Enum


AppModels = {}


class ModelType(Enum):
    feature = "Feature"


def setup_models(Base):
    class Feature(Base):
        __tablename__ = ModelType.feature.value
        __bind_key__ = DataBaseType.ml.value

        id = Column(Integer, primary_key=True)
        type = Column(String(80), unique=True)

    AppModels[ModelType.feature] = Feature
