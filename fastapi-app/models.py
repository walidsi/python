import os
from datetime import datetime, timezone

from sqlalchemy import inspect, text
from sqlmodel import Field, Session, SQLModel, create_engine

engine = create_engine("sqlite:///blogs.db", echo=os.getenv("DB_ECHO", "").lower() in ("1", "true", "yes"))


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class BlogBase(SQLModel):
    title: str
    body: str
    published: bool = False


class BlogCreate(BlogBase):
    pass


class BlogUpdate(SQLModel):
    title: str | None = None
    body: str | None = None
    published: bool | None = None


class BlogRead(BlogBase):
    id: int
    created_at: datetime
    updated_at: datetime


class Blog(BlogBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    def __repr__(self):
        return f"{self.id} | {self.title} | {self.published}"


def check_db(session: Session) -> None:
    session.exec(text("SELECT 1"))


def _migrate_blog_timestamps() -> None:
    """Add timestamp columns to existing SQLite blog tables when missing."""
    insp = inspect(engine)
    if "blog" not in insp.get_table_names():
        return
    columns = {col["name"] for col in insp.get_columns("blog")}
    with engine.connect() as conn:
        if "created_at" not in columns:
            conn.execute(text("ALTER TABLE blog ADD COLUMN created_at DATETIME"))
        if "updated_at" not in columns:
            conn.execute(text("ALTER TABLE blog ADD COLUMN updated_at DATETIME"))
        conn.execute(text("UPDATE blog SET created_at = CURRENT_TIMESTAMP WHERE created_at IS NULL"))
        conn.execute(text("UPDATE blog SET updated_at = CURRENT_TIMESTAMP WHERE updated_at IS NULL"))
        conn.commit()


def init_db():
    SQLModel.metadata.create_all(engine)
    _migrate_blog_timestamps()

