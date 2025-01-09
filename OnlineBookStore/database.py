from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DatabaseURL = "mysql+pymysql://admin:Direction%40700@122.164.127.154:3306/bookstore"

Base = declarative_base()
engine = create_engine(DatabaseURL)
sessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

