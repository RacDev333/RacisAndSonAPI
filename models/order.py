from sqlalchemy import ARRAY, JSON, Column, ForeignKey, Integer, String, Float, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

order_items = Table(
    "order_items",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.id"), primary_key=True),
    Column("product_id", Integer, ForeignKey("products.id"), primary_key=True)
)

class Order(Base):
    __tablename__ = "orders" 

    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    number = Column(String, nullable=False)
    email = Column(String, nullable=False)

    city = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    street = Column(String, nullable=False)
    building_number = Column(String, nullable=False)

    status = Column(String, nullable=False, default="pending")
    shipping_method = Column(String, nullable=False)
    shipping_notes = Column (String, nullable=True)
    tracking_number = Column(String, nullable=True)

    code_id = Column(Integer, ForeignKey("codes.id"), nullable=True)
    #to ponizej nie jest w bazie, to pythonowe przypisanie zmiennej, teraz bedzie mozna napisac discount_code.sale i zwroci pole sale, nie trzeba po id szukac
    discount_code = relationship("Code", back_populates="order")

    products = relationship("Product", secondary=order_items)

    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
