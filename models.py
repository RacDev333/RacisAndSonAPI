from sqlalchemy import ARRAY, JSON, Boolean, Column, ForeignKey, Integer, String, Float, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Product(Base):
    __tablename__ = "products" 

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    image = Column(JSON, nullable=True)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    size = Column(String, nullable=False)
    sale = Column(Integer, nullable=True, default=0)
    version = Column(String, nullable=False)
    is_retro = Column(Boolean, nullable=False, default=True)
    is_availble = Column(Boolean, nullable=False, default=True)


class Code(Base):
    __tablename__ = "codes" 

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False, unique=True)
    owner = Column(String, nullable=True)
    sale = Column(Integer, nullable=True, default=0)


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
    payment_method = Column(String, nullable=False)
    shipping_notes = Column (String, nullable=True)
    tracking_number = Column(String, nullable=True)

    code_id = Column(Integer, ForeignKey("codes.id"), nullable=True)
    #to ponizej nie jest w bazie, to pythonowe przypisanie zmiennej, teraz bedzie mozna napisac discount_code.sale i zwroci pole sale, nie trzeba po id szukac
    discount_code = relationship("Code", back_populates="order")

    products = relationship("Product", secondary=order_items)

    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

Code.order = relationship("Order", back_populates="discount_code", uselist=False)

class Broadcast(Base):
    __tablename__ = "broadcasts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    link = Column(String, nullable=True)
    is_visible = Column(Boolean, nullable=False, default=True)