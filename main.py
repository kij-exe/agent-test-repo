from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import os

app = FastAPI()


class Item(BaseModel):
    filename: str
    content: Optional[str] = None
    password: str

PASSWORD = 'secret'  # Simple password for demonstrative purposes


def verify_password(password: str):
    if password != PASSWORD:
        raise HTTPException(status_code=401, detail='Incorrect password')
    return True


@app.get('/get-data/')
def get_data(filename: str, password: str = Depends(verify_password)):
    """Fetches data from a file."""
    if not os.path.exists(filename):
        raise HTTPException(status_code=404, detail='File not found')
    with open(filename, 'r') as file:
        data = file.read()
    return {'data': data}


@app.post('/put-data/')
def put_data(item: Item = Depends()):
    verify_password(item.password)
    with open(item.filename, 'w') as file:
        file.write(item.content or '')
    return {'message': 'Data written successfully'}
