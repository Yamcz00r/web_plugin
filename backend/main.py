# main.py

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from utils.database_utils import get_db
from services.user_service import create_user, get_user_by_emial
import schemas.user_schema as user_schema
import os
from utils.database_utils import Base, engine

app = FastAPI()

BaseEngine =  Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hello": os.environ.get("DB_CONNECTION_URL", "No DB Connection URL")}

@app.post("/create_user/")
def create_user(user_data: user_schema.UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_emial(db, user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Użytkownik o tej nazwie już istnieje",
        )

    return create_user(db, user_data)

# @app.post("/delete_user/${update_user_id}")
# async def delete_user(db: Session, )