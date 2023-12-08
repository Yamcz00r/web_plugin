from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from utils.database_utils import get_db
from services.user_service import create_user, get_user_by_email, delete_user
import schemas.user_schema as user_schema
import os
from utils.database_utils import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://127.0.0.1:8000", "http://localhost:8000","http://127.0.0.1:3000", "http://localhost:3000" ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": os.environ.get("DB_CONNECTION_URL")}

@app.post("/users/create_user/")
def create_user_endpoint(user_data: user_schema.UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email address already exists",
        )

    return create_user(db, user_data)

@app.post("/users/delete_user/{delete_user_id}")
def delete_user_endpoint(delete_user_id: int, db: Session = Depends(get_db)):
    return delete_user(db=db, user_id=delete_user_id)
