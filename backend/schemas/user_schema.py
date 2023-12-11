from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    user_name: str
    password: str


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
