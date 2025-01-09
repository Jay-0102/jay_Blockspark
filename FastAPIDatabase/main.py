from fastapi import FastAPI,HTTPException
#from sqlalchemy.orm import Session
from models import User,sessionLocal

app=FastAPI()

#create a user
@app.post("/users/")
async def create_user(name:str,email:str):
    db=sessionLocal()#create a session
    try:
        db_user=db.query(User).filter(User.email==email).first()
        if db_user:
            raise HTTPException(status_code=400,detail="Email already register")
        new_user=User(name=name,email=email)#create new user
        db.add(new_user)#add new user
        db.commit()
        db.refresh(new_user)
        return new_user
    finally:
        db.close()#close session

# Get all users
@app.get("/users/")
async def get_users():
    db = sessionLocal()  # Create a new database session
    try:
        # Fetch all users
        return db.query(User).all()
    finally:
        db.close()  # Close the session

#Get one data fetch
@app.get("/users/{id}")
async def get_users(id:int):
    db=sessionLocal()
    try:
        user=db.query(User).filter(User.id==id).first()
        if not user:
            raise HTTPException(status_code=404,detail="User not Found")
        return user
    finally:
        db.close()