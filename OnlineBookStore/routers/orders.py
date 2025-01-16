from fastapi import APIRouter,HTTPException,Depends,status
import auth
from models import Book,User,Cart,Order,OrderItem
from database import get_db
from sqlalchemy.orm import Session

router=APIRouter(prefix="/orders",tags=["Orders"])

@router.post("/order_place/")
def order_place(db:Session=Depends(get_db),current_user:User=Depends(auth.get_current_user)):
    cart_item=db.query(Cart).filter(Cart.user_id==current_user.id).all()
    if not cart_item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Cart is Empty")
    
    total_price=0
    for item in cart_item:
        book=db.query(Book).filter(Book.id==item.book_id).first()
        if not book or book.quantity_available<item.quantity:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Not enough stock to complete the order for Book ID {item.book_id}")
        total_price+=book.price*item.quantity

    order=Order(user_id=current_user.id,total_price=total_price,status="pending")
    db.add(order)
    db.commit()
    db.refresh(order)

#order_items
    for item in cart_item:
        book=db.query(Book).filter(Book.id==item.book_id).first()
        book.quantity_available-=item.quantity
        order_item=OrderItem(order_id=order.id,book_id=item.book_id,quantity=item.quantity,price=book.price)
        db.add(order_item)

    db.query(Cart).filter(Cart.user_id==current_user.id).delete()
    db.commit()
    return{"message":"order placed successfully","order_id":order.id}

@router.get("/orders_view")
def view_order(db:Session=Depends(get_db),current_user:User=Depends(auth.get_current_user)):
    orders=db.query(Order).filter(Order.user_id==current_user.id).all()
    order_details=[]
    for order in  orders:
        order_details.append({"order_id":order.id,
                              "total_price":order.total_price,
                              "status":order.status,
                              "create_at":order.created_at
                              })
    return order_details