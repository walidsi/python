import stat
from turtle import title
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from typing import Union, Optional
import uvicorn
import models

class Blog(BaseModel):
     title: str
     body: str
     published: Optional[bool]

app = FastAPI()

@app.get('/')
def root():
    blogs = models.session.query(models.Blog).all()
    return {'data': blogs}

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
    blog = models.session.get(models.Blog, id)
    return {'data': blog}

@app.get('/blog/{id}/comments')
def comments(id: int, limit: int = 10):
    return {'data': f'blog {id}',
            'comments': [i for i in range(limit)]}
    
@app.post('/blog', status_code=status.HTTP_200_OK)
def create_blog(blog: Blog):
    new_blog = models.Blog(title=blog.title, body=blog.body, published=blog.published)
    models.session.add(new_blog)
    models.session.commit()
    return {'data': f'Blog is created with {blog}'}
    
@app.get('/about')
def about():
    return {'Author': 'Walid Ismail'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=9000)
    

# to copy updates of this file to a running container, use the following command:
# docker cp main.py b9dc417c8b30:/app/main.py
