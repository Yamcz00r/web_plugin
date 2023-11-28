from pydantic import BaseModel

class UserBase(BaseModel):
    email:str

class UserCreate(UserBase):
    user_name: str
    password:str

class User(UserBase):
    id:int