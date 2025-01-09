from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
#from typing import Optional

SECRET_KEY = "9486e8062ee3d9e09e7f7ddca75088e503a8f02aafbab81016d0f88b064cff78"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAY = 1

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnowt() + timedelta(days=365*ACCESS_TOKEN_EXPIRE_DAY)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
