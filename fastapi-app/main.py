from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World 2025"}

@app.post("/items")
async def add(item: Item):
    return 'Recevied this: ' + str(item)

@app.get("/about")
def about():
    return {"Author": "Walid Ismail"}
    

# to copy updates of this file to a running container, use the following command:
# docker cp main.py b9dc417c8b30:/app/main.py
