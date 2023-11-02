from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session

import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close() 

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User with this email is already existing")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User cannot be found")
    return db_user

@app.post("/users/{user_id}/items", response_model=schemas.Item)
def create_item(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, user_id=user_id)

@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

    


    










# Reciving a headers
# @app.get('/items/')
# def user_agent(
#     user_agent: Annotated[str | None, Header()] = None, host: Annotated[str | None, Header()] = None,
#     accept: Annotated[str | None, Header()] = None
#     ):
#     return {"User-Agent": user_agent, "host": host, "accept": accept}




    
            
