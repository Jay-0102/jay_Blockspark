from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, database, auth
from database import get_db

router = APIRouter(prefix="/books",tags=["Books"])

@router.post("/books", tags=["Books"])
def create_book(book: schemas.BookCreate,db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),):
    # Check if the current user is an admin
    if current_user.role != "admin":  # Role extracted from the JWT token
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can create books.",
        )
    
    # Admin is allowed to create books
    new_book = models.Book(**book.dict())
    if not new_book.title:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Title is Required")
    if not new_book.author:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Author name is Required")
    if not new_book.price:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Price is Required")
    if not new_book.quantity_available:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Quantity is Required")
    if new_book.title.isdigit():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Please Enter Valid Book Name")
    for char in new_book.author:
        if not (char.isalpha()):
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Please Enter Valid Author Name")    
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@router.get("/GET")
def get_books(db: Session = Depends(database.get_db)):
    return db.query(models.Book).all()

@router.get("GET_ID/{id}")
def get_books(id:int,db:Session=Depends(database.get_db)):
    db_book=db.query(models.Book).filter(models.Book.id==id).first()
    return db_book

@router.post("/Delete/{id}")
def delete_book(id:int,db:Session=Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)):
    # Check if the current user is an admin
    if current_user.role != "admin":  # Role extracted from the JWT token
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can create books.",
        )
    db_book=db.query(models.Book).filter(models.Book.id==id).first()
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message":"Book Delete Successfully"}

@router.post("/Update/{id}")
def update_book(id:int, title:str=None, author:str=None, price:int=None, qty:int=None, db:Session=Depends(database.get_db),
                current_user: models.User = Depends(auth.get_current_user)):
    # Check if the current user is an admin
    if current_user.role != "admin":  # Role extracted from the JWT token
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can create books.",
        )
    db_book=db.query(models.Book).filter(models.Book.id==id).first()
    if not db_book:
        raise HTTPException(status_code=404,detail="Book Not Found")
    if title:
        db_book.title=title
    if author:
        db_book.author=author
    if price:
        db_book.price=price
    if qty:
        db_book.quantity_available=qty
    db.commit()
    db.refresh(db_book)
    return db_book
