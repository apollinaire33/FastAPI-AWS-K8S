import typing as t
from abc import ABC, abstractmethod

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import expression

from user.database.postgresql.models.user import UserModel
from user.rest.models.user import User, UserCreate

FilterKwargs = dict[t.Any, t.Any]


class ABCUserRepo(ABC):
    @abstractmethod
    async def get(self, **kwargs: FilterKwargs) -> User:
        ...

    @abstractmethod
    async def create(self, data: UserCreate) -> User:
        ...


class TestUserRepo(ABCUserRepo):
    user: User

    async def get(self, **kwargs: FilterKwargs) -> User:
        return self.user

    async def create(self, data: UserCreate) -> User:
        return self.user


class PgUserRepo(ABCUserRepo):
    _table = UserModel

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    def _build_filter_query(self, q: expression, **kwargs: FilterKwargs) -> expression:
        filter_ = [
            getattr(self._table, field) == value for field, value in kwargs.items()
        ]
        return q.where(and_(*filter_))

    @staticmethod
    def _to_repr(user_object: UserModel) -> User:
        return User(
            uuid=user_object.uuid,
            username=user_object.username,
            email=user_object.email,
            age=user_object.age,
        )

    async def get(self, **kwargs: FilterKwargs) -> User | None:
        q = self._build_filter_query(select(self._table), **kwargs)
        result = await self.session.execute(q)
        user_object: UserModel | None = result.scalars().first()
        return self._to_repr(user_object) if user_object else None

    async def create(self, data: UserCreate) -> User:
        user_object = self._table(**data.model_dump())
        self.session.add(user_object)
        await self.session.commit()
        return self._to_repr(user_object)
