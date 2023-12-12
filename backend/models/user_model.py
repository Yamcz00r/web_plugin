from utils.database_utils import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    user_name: str = Column(String, index=True)
    email: str = Column(String, index=True, unique=True)
    hashed_password: str = Column(String)
