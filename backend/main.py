from fastapi import FastAPI
from sqlalchemy.orm import Session
from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/items/')
def root():
    return {
        "message": "Hello World"
    }