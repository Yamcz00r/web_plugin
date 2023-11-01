from fastapi import FastAPI, status, HTTPException
from typing import Annotated
from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    password: str

users = []

app = FastAPI()


@app.get('/user')
async def get_users() -> list[User]:
    if len(users) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There are no users")
    return {
       users
    }

@app.post('/user/create')
async def login(user_data: User):
    for user in users:
        if user_data.id == user.id:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="User is already existing")
    users.append(user_data)
    return {
        "message": "Succesfully created a user",
        "data": user_data
    }  
    


    


    










# Reciving a headers
# @app.get('/items/')
# def user_agent(
#     user_agent: Annotated[str | None, Header()] = None, host: Annotated[str | None, Header()] = None,
#     accept: Annotated[str | None, Header()] = None
#     ):
#     return {"User-Agent": user_agent, "host": host, "accept": accept}




    
            
