from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class BookCreate(BaseModel):
    title: str
    author: str
    price: float
    quantity_available: int
    
class UserOut(BaseModel):
    username: str
    email : str
    id : int
    created_at : datetime


