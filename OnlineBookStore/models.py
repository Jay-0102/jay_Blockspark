from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime,func
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True, index=True)
    email = Column(String(30), unique=True, index=True)
    type = Column(String(30), default=0)  # "admin" or "customer"
    password = Column(String(100))
    created_at = Column(DateTime, default=func.now())

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30), index=True)
    author = Column(String(30))
    price = Column(Float)
    quantity_available = Column(Integer)
    created_at = Column(DateTime, default=func.now())

# class Cart(Base):
#     _tablename_ = "carts"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     book_id = Column(Integer, ForeignKey("books.id"))
#     quantity = Column(Integer)
#     created_at = Column(DateTime, default=datetime.utcnow)

# class Order(Base):
#     _tablename_ = "orders"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     total_price = Column(Float)
#     status = Column(String)
#     created_at = Column(DateTime, default=datetime.utcnow)