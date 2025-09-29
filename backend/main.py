from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db, get_items

app = FastAPI()

# Дозволяємо frontend робити запити до backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # в продакшені краще вказати конкретний домен
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ініціалізація БД при старті
@app.on_event("startup")
def startup_event():
    init_db()

# Маршрут для отримання списку
@app.get("/items")
def read_items():
    return get_items()  # повертає список dict: [{"id": 1, "itemname": "Item1"}, ...]
