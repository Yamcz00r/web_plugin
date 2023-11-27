from utils.database_utils import get_db
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models.user_model as user_model
import schemas.user_schema as user_schema
from services.user_service import create_user

app = FastAPI()



@app.post("/create_user/")
def create_user_endpoint(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    created_user = create_user(db, user)
    return {"message": "User created successfully", "user_id": created_user.id}