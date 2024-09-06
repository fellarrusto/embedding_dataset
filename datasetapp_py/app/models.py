from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Dataset(Base):
    __tablename__ = 'dataset'
    id = Column(Integer, primary_key=True, index=True)
    anchor = Column(String, index=True)
    positive = Column(String)

class DataEntry(BaseModel):
    anchor: str
    positive: str
