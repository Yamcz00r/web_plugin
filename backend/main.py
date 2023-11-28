# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database_utils import get_db
from services.user_service import create_user
import schemas.user_schema as user_schema
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": os.environ.get("DB_CONNECTION_URL", "No DB Connection URL")}

@app.post("/create_user/")
def create_user_endpoint(db: Session = Depends(get_db)):
    user_data = {
        "user_name": "testuser",  # Dodane pole user_name
        "email": "testuser@example.com",
        "password": "testpassword",
    }
    user_create = user_schema.UserCreate(**user_data)
    return create_user(db, user_create)
