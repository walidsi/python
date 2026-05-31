from contextlib import asynccontextmanager
from typing import Optional

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Response, status
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


def get_blog_or_404(id: int, session: Session) -> models.Blog:
    blog = session.get(models.Blog, id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog


@app.get("/health")
def health(session: Session = Depends(get_session)):
    try:
        models.check_db(session)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"status": "unhealthy", "database": "disconnected", "error": str(exc)},
        ) from exc
    return {"status": "ok", "database": "connected"}

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
    blog = get_blog_or_404(id, session)
    return {"data": models.BlogRead.model_validate(blog)}


@app.get("/blog/{id}/comments")
def comments(id: int, limit: int = 10):
    return {"data": f"blog {id}", "comments": [i for i in range(limit)]}


@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(blog: models.BlogCreate, session: Session = Depends(get_session)):
    now = models.utc_now()
    db_blog = models.Blog.model_validate(blog, update={"created_at": now, "updated_at": now})
    session.add(db_blog)
    session.commit()
    session.refresh(db_blog)
    return {"data": models.BlogRead.model_validate(db_blog)}


@app.patch("/blog/{id}")
def update_blog(id: int, blog: models.BlogUpdate, session: Session = Depends(get_session)):
    db_blog = get_blog_or_404(id, session)
    update_data = blog.model_dump(exclude_unset=True)
    if not update_data:
        return {"data": models.BlogRead.model_validate(db_blog)}
    for key, value in update_data.items():
        setattr(db_blog, key, value)
    db_blog.updated_at = models.utc_now()
    session.add(db_blog)
    session.commit()
    session.refresh(db_blog)
    return {"data": models.BlogRead.model_validate(db_blog)}


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, session: Session = Depends(get_session)):
    db_blog = get_blog_or_404(id, session)
    session.delete(db_blog)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get("/about")
def about():
    return {"Author": "Walid Ismail"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)


# to copy updates of this file to a running container, use the following command:
# docker cp main.py b9dc417c8b30:/app/main.py
