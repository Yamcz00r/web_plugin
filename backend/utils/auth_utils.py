import jwt
import models.user_model as user_model
import schemas.user_schema as user_schema
import services.user_service as user_service
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from utils.database_utils import get_db
from fastapi import Depends, HTTPException, status
from typing import Annotated
import passlib.hash as hash

oauth2schema = OAuth2PasswordBearer(tokenUrl='token')

jwt_secret = 'da248a94f5caa164afbbf4da48b9c7c3db217a6ff3e1f4fd37a4741ef51ce718'


def verify_password(password: str, hashed_password: str):
    return hash.bcrypt.verify(password, hashed_password)

def authenticate_user(email: str, password: str, db: Session):
    db_user = user_service.get_user_by_email(db, user_email=email)
    print(db_user.email, db_user.hashed_password)
    if db_user is None:
        return False
    if not verify_password(password, db_user.hashed_password):
        return False

    return db_user


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2schema)) -> user_schema.User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, jwt_secret, algorithms=['HS256'])
        user = db.query(user_model.User).get(payload["id"])
    except jwt.PyJWTError:
        raise credentials_exception
    if user is None:
        raise credentials_exception
    return user_schema.User.from_orm(user)


async def create_token(user: user_model.User, secret: str = jwt_secret):
    user_obj = user_schema.User.from_orm(user)
    token = jwt.encode(user_obj.dict(), secret)
    return dict(access_token=token)