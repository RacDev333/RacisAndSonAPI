import os
from fastapi import FastAPI, BackgroundTasks, Depends, Request
from pydantic import BaseModel
from dotenv import load_dotenv
from email_utils import order_confirmation_email, send_email
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session
import crud
import schemas
import database
import models

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded


load_dotenv()

app = FastAPI(
    title="Racis&Son API",
    description="""
    API umożliwiające obsługę zamówień w serwisie Racis&Son
    """,
    version="0.2.0",
    contact={
        "name": "Racis&Son",
        "url": "https://www.racis.store/contact"
    },
    redirect_slashes=False,
    docs_url=None if os.getenv("ENV") == "production" else "/docs",
    redoc_url=None if os.getenv("ENV") == "production" else "/redoc"
)

origins = [
    "http://localhost:3000",
    "https://racis.store", 
    "https://www.racis.store",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailSchema(BaseModel):
    address: str
    name: str
    message: str


limiter = Limiter(key_func=get_remote_address)

@app.post("/contact/")
@limiter.limit("3/minute")
def send_email_endpoint(request: Request, email: EmailSchema, background_tasks: BackgroundTasks):
    background_tasks.add_task(
        send_email, email.address, email.name, email.message
    )
    return {"status": "Wiadomość w trakcie wysyłania!"}


# Endpoint do pobierania wszystkich zamówień
# @app.get("/orders/")
# def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
#     orders = crud.get_orders(db, skip=skip, limit=limit)
#     return orders

# Endpoint do tworzenia zamówienia
@app.post("/orders/")
@limiter.limit("3/minute")
def create_order(request: Request, order: schemas.OrderCreate, background_tasks: BackgroundTasks, db: Session = Depends(database.get_db)):
    user_email = order.email
    user_name = order.name
    db_order = crud.create_order(db=db, order=order)
    order_num = db_order.order_number
    #wysylanie maila z potwierdzeniem
    #background_tasks.add_task(order_confirmation_email, user_email, user_name, order_num)
    return {"status": "success", "message": "Order created successfully"}

@app.get("/products/", response_model=List[schemas.Product])
@limiter.limit("100/minute")
def get_products(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    print()
    return products

@app.get("/everything/")
@limiter.limit("100/minute")
def get_everything(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    codes = crud.get_codes(db, skip=skip, limit=limit)
    broadcasts = crud.get_broadcasts(db, skip=skip, limit=limit)
    codes_response = [{"id": c.id, "code": c.code, "sale": c.sale} for c in codes]
    broadcasts_response = [{"id": b.id, "text": b.text, "link": b.link} for b in broadcasts]
    return {"products": products, "codes": codes_response, "broadcasts": broadcasts_response}