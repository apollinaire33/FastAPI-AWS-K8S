from abc import ABC, abstractmethod
import typing as t

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import expression

from post.database.postgresql.models.post import PostModel
from post.rest.models.post import Post, PostCreate

FilterKwargs = dict[t.Any, t.Any]


class ABCPostRepo(ABC):
    @abstractmethod
    async def get(self, **kwargs: FilterKwargs) -> Post:
        ...
    
    @abstractmethod
    async def create(self, data: PostCreate) -> Post:
        ...


class TestPostRepo(ABCPostRepo):
    post: Post

    async def get(self, **kwargs: FilterKwargs) -> Post:
        return self.post
    
    async def create(self, data: PostCreate) -> Post:
        return self.post


class PgPostRepo(ABCPostRepo):
    _table = PostModel

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    def _build_filter_query(self, q: expression, **kwargs: FilterKwargs) -> expression:
        filter_ = [
            getattr(self._table, field) == value for field, value in kwargs.items()
        ]
        return q.where(and_(*filter_))
    
    @staticmethod
    def _to_repr(post_object: PostModel) -> Post:
        return Post(
            uuid=post_object.uuid,
            author_uuid=post_object.author_uuid,
            subject=post_object.subject,
            text=post_object.text,
            created_at=post_object.created_at,
        )

    async def get(self, **kwargs: FilterKwargs) -> Post | None:
        q = self._build_filter_query(select(self._table), **kwargs)
        result = await self.session.execute(q)
        post_object: PostModel | None = result.scalars().first()
        return self._to_repr(post_object) if post_object else None

    async def create(self, data: PostCreate) -> Post:
        post_object = self._table(**data.model_dump())
        self.session.add(post_object)
        await self.session.commit()
        return self._to_repr(post_object)
