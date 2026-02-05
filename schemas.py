from pydantic import BaseModel, EmailStr
from typing import Any, List, Optional
from datetime import datetime


class OrderBase(BaseModel):
    name: str
    surname: str
    number: str
    email: EmailStr
    city: str
    postal_code: str
    street: str
    building_number: str
    shipping_method: str
    payment_method: str
    shipping_notes: Optional[str] = None
    code_id: Optional[int] = None
    product_id: List[int]

# Schemat do tworzenia (POST)
class OrderCreate(OrderBase):
    pass

# Schemat do odczytu (GET) - zawiera pola generowane przez DB
class Order(OrderBase):
    id: int
    order_number: str
    status: str
    price: float
    tracking_number: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True # Pozwala Pydanticowi czytać dane z modeli SQLAlchemy

class ProductBase(BaseModel):
    id: int
    title: str
    image: str
    price: int
    description: str
    size: str
    sale: Optional[int] = 0
    version: str
    is_retro: bool
    is_availble: bool

class Product(ProductBase):
    pass

class Code(BaseModel):
    id: int
    code: str
    sale: Optional[int] = 0

    class Config:
        from_attributes = True

class Broadcast(BaseModel):
    id: int
    text: str
    link: Optional[str] = None

    class Config:
        from_attributes = True