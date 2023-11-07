from sqlalchemy.orm import Session
import bcrypt
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    salt = bcrypt.gensalt()
    passwd_bytes = user.password.encode('utf-8')
    hashed_password = bcrypt.hashpw(passwd_bytes, salt)
    new_user = models.User(email = user.email, hashed_password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Items).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate, user_id: int):
    new_item = models.Items(**item.dict(), owner_id = user_id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

    
