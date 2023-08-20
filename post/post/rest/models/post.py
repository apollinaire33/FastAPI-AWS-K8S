from uuid import UUID
import datetime

from pydantic import BaseModel


class Author(BaseModel):
    uuid: UUID
    username: str
    email: str
    age: int


class Post(BaseModel):
    uuid: UUID
    author_uuid: UUID
    subject: str
    text: str
    created_at: datetime.datetime


class PostWithAuthor(BaseModel):
    uuid: UUID
    subject: str
    text: str
    created_at: datetime.datetime
    author: Author


class PostCreate(BaseModel):
    author_uuid: UUID
    subject: str
    text: str
