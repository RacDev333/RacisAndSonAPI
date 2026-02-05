from sqlalchemy import ARRAY, JSON, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Code(Base):
    __tablename__ = "codes" 

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False, unique=True)
    owner = Column(String, nullable=True)
    sale = Column(Integer, nullable=True, default=0)

    order = relationship("Order", back_populates="discount_code", uselist=False)

