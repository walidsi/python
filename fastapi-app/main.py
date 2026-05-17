from contextlib import asynccontextmanager
from typing import Optional

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from sqlmodel import Session, select

import models


@asynccontextmanager
async def lifespan(app: FastAPI):
    models.init_db()
    yield


app = FastAPI(lifespan=lifespan)


def get_session():
    with Session(models.engine) as session:
        yield session


@app.get("/")
def root(session: Session = Depends(get_session)):
    blogs = session.exec(select(models.Blog)).all()
    return {"data": [models.BlogRead.model_validate(blog) for blog in blogs]}


@app.get("/blog")
def index(
    limit: int = 10,
    published: Optional[bool] = None,
    sort: Optional[str] = None,
    session: Session = Depends(get_session),
):
    statement = select(models.Blog).limit(limit)
    if published is not None:
        statement = statement.where(models.Blog.published == published)
    blogs = session.exec(statement).all()
    return {"data": [models.BlogRead.model_validate(blog) for blog in blogs]}


@app.get("/blog/unpublished")
def unpublished(session: Session = Depends(get_session)):
    blogs = session.exec(select(models.Blog).where(models.Blog.published == False)).all()
    return {"data": [models.BlogRead.model_validate(blog) for blog in blogs]}


@app.get("/blog/{id}")
def show(id: int, session: Session = Depends(get_session)):
    blog = session.exec(select(models.Blog).where(models.Blog.id == id)).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return {"data": models.BlogRead.model_validate(blog)}


@app.get("/blog/{id}/comments")
def comments(id: int, limit: int = 10):
    return {"data": f"blog {id}", "comments": [i for i in range(limit)]}


@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(blog: models.BlogCreate, session: Session = Depends(get_session)):
    db_blog = models.Blog.model_validate(blog)
    session.add(db_blog)
    session.commit()
    session.refresh(db_blog)
    return {"data": models.BlogRead.model_validate(db_blog)}


@app.get("/about")
def about():
    return {"Author": "Walid Ismail"}


@app.get("/health")
def health():
    return {"status": "OK"}


@app.get("/health2")
def health2():
    return {"status": "service down"}


@app.get("/health3")
def health3():
    return "Hello World"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)


# to copy updates of this file to a running container, use the following command:
# docker cp main.py b9dc417c8b30:/app/main.py
