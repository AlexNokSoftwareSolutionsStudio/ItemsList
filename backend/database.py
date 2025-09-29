from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    itemname = Column(String, index=True)

def init_db():
    Base.metadata.create_all(bind=engine)
    # додати кілька записів для перевірки
    session = SessionLocal()
    if not session.query(Item).first():
        session.add_all([Item(itemname="Item1"), Item(itemname="Item2")])
        session.commit()
    session.close()

def get_items():
    session = SessionLocal()
    items = session.query(Item).all()
    session.close()
    return [{"id": i.id, "itemname": i.itemname} for i in items]
