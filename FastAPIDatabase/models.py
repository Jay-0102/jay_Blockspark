from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DatabaseUrl="mysql+pymysql://admin:Direction%40700@122.164.127.154:3306/bookstore"

#Sqlalchemy stetup 
Base=declarative_base()#create database table
engine=create_engine(DatabaseUrl)#connection  databaseurl
sessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)#intrect with database and bind->intrect with all databse

#user Model
class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    name=Column(String(20),nullable=True)
    email=Column(String(50),nullable=True,unique=True)

#create a table
Base.metadata.create_all(bind=engine)