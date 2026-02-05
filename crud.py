import secrets
import string
from sqlalchemy.orm import Session, joinedload
import models
import schemas

QUANTITY_THRESHOLD = 3      # od ilu produktów zniżka
QUANTITY_DISCOUNT_PERCENT = 15  # ile procent zniżki


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()

def create_order(db: Session, order: schemas.OrderCreate):
    chars = string.ascii_uppercase + string.digits
    order_num = f"RS-{''.join(secrets.choice(chars) for _ in range(8))}"
    
    db_products = db.query(models.Product).filter(models.Product.id.in_(order.product_id)).all()
    if not db_products:
        return None
    
    # 1. Obliczenie ceny bazowej ze wszystkich produktów (z ich rabatami z pola sale)
    base_price = sum(p.price * (1 - ((p.sale or 0) / 100.0)) for p in db_products)
    
    # Tworzymy zmienną pomocniczą na cenę po rabatach
    current_price = base_price
    

    # 2. Sprawdzenie zniżki za ilość (3 lub więcej produktów)
    # Naliczamy ją jako drugą od ceny po rabatach produktu
    if len(db_products) >= QUANTITY_THRESHOLD:
        discount_amount = current_price * (QUANTITY_DISCOUNT_PERCENT / 100.0)
        current_price -= discount_amount


    # 3. Obsługa kodu rabatowego
    # Naliczamy go od ceny, która została po poprzednich rabatach
    if order.code_id:
        db_code = db.query(models.Code).filter(models.Code.id == order.code_id).first()
        if db_code and db_code.sale:
            # Sale z kodu liczy się od current_price
            promo_discount_amount = current_price * (db_code.sale / 100.0)
            current_price -= promo_discount_amount

    # 4. Wyliczenie ceny końcowej
    # Zabezpieczenie: cena nie może być ujemna
    final_price = max(0.0, current_price)

    # 5. Wykluczenie pól, których nie ma w modelu bazy danych
    # Dodaj tu wszystkie dodatkowe pola z frontendu, których nie chcesz w tabeli 'orders'
    exclude_fields = {"product_id"} 
    order_data = order.dict(exclude=exclude_fields)
    
    db_order = models.Order(
        **order_data,
        order_number=order_num,
        price=round(float(final_price), 2)
    )

    db_order.products = db_products

    db.add(db_order)
    db.commit()
    
    return db_order

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).filter(models.Product.is_availble == True).offset(skip).limit(limit).all()

def get_codes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Code).offset(skip).limit(limit).all()

def get_broadcasts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Broadcast).filter(models.Broadcast.is_visible == True).offset(skip).limit(limit).all()