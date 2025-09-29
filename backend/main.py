# backend/main.py
from fastapi import FastAPI
from database import init_db

app = FastAPI()

# створюємо таблиці при старті
@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/items")
def read_items():
    from .models import Item
    from .database import SessionLocal

    db = SessionLocal()
    items = db.query(Item).all()
    db.close()
    return items
