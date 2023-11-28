import models.user_model as user_model
import schemas.user_schema as user_schema
from sqlalchemy.orm import Session
from passlib.hash import bcrypt

def create_user(db: Session, user: user_schema.UserCreate):
    hashed_password = bcrypt.hash(user.password)
    db_user = user_model.User(
        user_name=user.user_name,  
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user
