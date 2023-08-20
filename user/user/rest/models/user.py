import uuid

from pydantic import BaseModel


class User(BaseModel):
    uuid: uuid.UUID
    username: str
    email: str
    age: int


class UserCreate(BaseModel):
    username: str
    email: str
    age: int
