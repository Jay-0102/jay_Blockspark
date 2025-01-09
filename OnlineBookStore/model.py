from sqlalchemy import Column, Integer, String, Float,Boolean,DateTime
from database import Base
from sqlalchemy import func

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    email = Column(String(30))
    password = Column(String(100))
    is_admin=Column(Boolean,default=False)

class Book(Base):
    __tablename__="books"
    id=Column(Integer,primary_key=True)
    title=Column(String(40),nullable=True)
    author=Column(String(50),nullable=True)
    price=Column(Float,nullable=True)
    qty=Column(Integer,nullable=True)
    create_at=Column(DateTime,default=func.now())

