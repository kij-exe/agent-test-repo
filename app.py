from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import math

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

class Vector:
    def __init__(self, *args):
        self.components = args

    def __repr__(self):
        return f'Vector({", ".join(str(x) for x in self.components)})'

    def __len__(self):
        return len(self.components)

    def dot(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")
        return sum(a * b for a, b in zip(self.components, other.components))

    def cross(self, other):
        if len(self.components) != 3 or len(other.components) != 3:
            raise ValueError("Cross product is defined only for 3D vectors")
        a1, a2, a3 = self.components
        b1, b2, b3 = other.components
        return Vector(a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1)
