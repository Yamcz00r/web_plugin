import models.user_model as user_model
import schemas.user_schema as user_schema
from sqlalchemy.orm import Session
import bcrypt
from fastapi import HTTPException


def create_user(db: Session, user: user_schema.UserCreate):
    password_bytes = bytes(user.password, 'utf-8')
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    db_user = user_model.User(
        user_name=user.user_name,  
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


def get_user_by_id(db:Session, user_id: int) -> user_model.User:
    return db.query(user_model.User).filter(user_model.User.id == user_id).scalar()


def get_user_by_email(db:Session, user_email: str) -> user_model.User:
    return db.query(user_model.User).filter(user_model.User.email == user_email).scalar()


def delete_user(db:Session, user_id: int) -> user_model.User:
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    else:
         raise HTTPException(
            status_code=400, detail=f"user not found"
         )
