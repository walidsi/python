import os

from sqlmodel import Field, SQLModel, create_engine

engine = create_engine("sqlite:///blogs.db", echo=os.getenv("DB_ECHO", "").lower() in ("1", "true", "yes"))


class BlogBase(SQLModel):
    title: str
    body: str
    published: bool = False


class BlogCreate(BlogBase):
    pass


class BlogRead(BlogBase):
    id: int


class Blog(BlogBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    def __repr__(self):
        return f"{self.id} | {self.title} | {self.published}"


def init_db():
    SQLModel.metadata.create_all(engine)
