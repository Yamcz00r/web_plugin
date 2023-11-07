from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/users', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = crud.get_user_by_email(db, email=user.email)
    if new_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    return crud.create_user(db, user)

@app.get('/users', response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User is not found!")
    return user

@app.post("/users/{user_id}/items" ,response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item, user_id)

@app.get("/items", response_model = list[schemas.Item])
def get_items(db: Session = Depends(get_db)):
    return crud.get_items(db)
    
              

    