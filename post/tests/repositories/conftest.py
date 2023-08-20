import asyncio

import pytest

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from post.core.config import test_database_url
from post.database.postgresql.models.base import metadata
from post.repositories.post_repo import ABCPostRepo, PgPostRepo
from post.rest.models.post import Post, PostCreate

test_engine = create_async_engine(test_database_url)

async_session_local = sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)


@pytest.fixture
async def test_session() -> None:
    async with async_session_local() as session:
        yield session


@pytest.fixture
async def post_test_repo(test_session) -> ABCPostRepo:
    return PgPostRepo(test_session)


@pytest.fixture(scope="package")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True, scope="package")
async def prepare_database():
    async with test_engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)


@pytest.fixture
async def post_model(post_test_repo: ABCPostRepo, post: Post) -> Post:
    return await post_test_repo.create(PostCreate(**post.model_dump()))
