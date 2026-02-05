from sqlalchemy import ARRAY, Boolean, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Product(Base):
    __tablename__ = "products" 

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    image = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    size = Column(String, nullable=False)
    sale = Column(Integer, nullable=True, default=0)
    version = Column(String, nullable=False)
    is_retro = Column(Boolean, nullable=False, default=True)
    is_availble = Column(Boolean, nullable=False, default=True)
