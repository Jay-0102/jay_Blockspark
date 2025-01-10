from fastapi import APIRouter,HTTPException,Depends,status
from database import get_db
from models import User,Cart,Book
from schemas import CartItem
import auth
from sqlalchemy.orm import Session

router=APIRouter(prefix="/carts",tags=["Cart"])

@router.post("/Add/")
def add_cart(id:int,quantity:int,db:Session=Depends(get_db),current_user:User=Depends(auth.get_current_user)):
    if current_user.role!="user":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only Users can Access")
    db_cart=db.query(Book).filter(Book.id==id).first()
    if not db_cart:
        raise HTTPException(status_code=404,detail="Book not Found")
    cart_item=db.query(Cart).filter(Cart.user_id==current_user.id,Cart.book_id==id).first()
    if cart_item:
        cart_item.quantity+=quantity
    else:
        cart_item=Cart(user_id=current_user.id,book_id=id,quantity=quantity)
        db.add(cart_item)
    db.commit()
    return {"message":"Book add to cart"}
    
@router.get("/View/")
def view_cart(db:Session=Depends(get_db),current_user:User=Depends(auth.get_current_user)):
    if current_user.role != "user":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only Users can Access")
    db_cart=db.query(Cart).filter(User.id==current_user.id).all()
    details=[]
    for item in db_cart:
        db_book=db.query(Book).filter(Book.id==item.book_id).first()
        if db_book:
            details.append({
                "book_id":item.book_id,
                "title":db_book.title,
                "quantity":item.quantity,
                "added_at":item.created_at
            })
    return details

@router.post("/update")
def update_cart(book_id:int,quantity:int,db:Session=Depends(get_db),current_user:User=Depends(auth.get_current_user)):
    if current_user.role!="user":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only Users can Access")
    db_cart=db.query(Cart).filter(Cart.user_id==current_user.id,Cart.book_id==book_id).first()
    if not db_cart:
        raise HTTPException(status_code=404,detail="Itmes not available cart")
    if quantity<=0:
        db.delete(db_cart)
    else:
        db_cart.quantity=quantity
    
    db.commit()
    db.refresh(db_cart)
    return db_cart

@router.post("/delete/{id}")
def delete_cart(id:int,db:Session=Depends(get_db),current_user:User=Depends(auth.get_current_user)):
    if current_user.role!="user":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only Users can Access")
    db_cart=db.query(Cart).filter(Cart.user_id==current_user.id,Cart.book_id==id).first()
    if not db_cart:
        raise HTTPException(status_code=404,detail="Items not in cart")
    db.delete(db_cart)
    db.commit()
    return {"message":"Delete Successfully"}
        
