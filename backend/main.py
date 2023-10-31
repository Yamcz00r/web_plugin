from fastapi import FastAPI, Header
from typing import Annotated



# class Item(BaseModel):
#     id: int
#     name: str
#     price: int
#     description: str | None = None

items = []

app = FastAPI()

@app.get('/items/')
def user_agent(
    user_agent: Annotated[str | None, Header()] = None, host: Annotated[str | None, Header()] = None,
    accept: Annotated[str | None, Header()] = None
    ):
    return {"User-Agent": user_agent, "host": host, "accept": accept}




    
            
