from fastapi import FastAPI, BackgroundTasks, Depends
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
    redirect_slashes=False
)

origins = [
    "http://localhost:3000",
    "https://racis.store", 
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

@app.post("/contact/")
def send_email_endpoint(email: EmailSchema, background_tasks: BackgroundTasks):
    background_tasks.add_task(
        send_email, email.address, email.name, email.message
    )
    return {"status": "Wiadomość w trakcie wysyłania!"}


# Endpoint do pobierania wszystkich zamówień
@app.get("/orders/")
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders

# Endpoint do tworzenia zamówienia
@app.post("/orders/")
def create_order(order: schemas.OrderCreate, background_tasks: BackgroundTasks, db: Session = Depends(database.get_db)):
    user_email = order.email
    user_name = order.name
    db_order = crud.create_order(db=db, order=order)
    order_num = db_order.order_number
    #wysylanie maila z potwierdzeniem
    #background_tasks.add_task(order_confirmation_email, user_email, user_name, order_num)
    return {"status": "success", "message": "Order created successfully"}

@app.get("/products/", response_model=List[schemas.Product])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    print()
    return products

@app.get("/everything/")
def get_everything(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    codes = crud.get_codes(db, skip=skip, limit=limit)
    broadcasts = crud.get_broadcasts(db, skip=skip, limit=limit)
    codes_response = [{"id": c.id, "code": c.code, "sale": c.sale} for c in codes]
    broadcasts_response = [{"id": b.id, "text": b.text, "link": b.link} for b in broadcasts]
    return {"products": products, "codes": codes_response, "broadcasts": broadcasts_response}