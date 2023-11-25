from database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"

    id:int = Column(Integer, primary_key=True, index=True)
    username:str = Column(String, unique=True, index=True)
    email:str = Column(String, unique=True, index=True)
    password:str = Column(String) #pasuje zrobic szyfrowane haslo :/
    
