from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

items = {}

@app.post("/items/")
def create_item(item: Item):
    if item.name in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.name] = item
    return item

@app.get("/items/{item_name}")
def read_item(item_name: str):
    if item_name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_name]
