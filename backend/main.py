from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    price: int
    description: str | None = None

items = []

app = FastAPI()

users = []

@app.get("/items/")
async def get_items():
    if len(items) == 0:
        return "Your list is currently empty!"
    
    return items

@app.post("/items/")
async def create_item(item: Item):
    for existing_item in items:
        if (existing_item.id == item.id):
            return {
                "message": "The item is currently stored!"
            }
    items.append(item)
    return {
        "message": "Succesfully added an Item",
        "item": item
    }
