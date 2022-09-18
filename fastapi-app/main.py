from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, Optional

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.get('/')
def root():
    return {'data': 'blog list'}

@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} blogs from db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': f'blog {id}'}

@app.get('/blog/{id}/comments')
def comments(id: int, limit=10):
    return {'data': f'blog {id}',
            'comments': [i for i in range(limit)]}    

@app.get('/about')
def about():
    return {'Author': 'Walid Ismail'}
    

# to copy updates of this file to a running container, use the following command:
# docker cp main.py b9dc417c8b30:/app/main.py
