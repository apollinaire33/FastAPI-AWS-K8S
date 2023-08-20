import asyncio

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from user.core.config import TEST_DATABASE_URL
from user.database.postgresql.models.base import metadata
from user.repositories.user_repo import ABCUserRepo, PgUserRepo
from user.rest.models.user import User, UserCreate

test_engine = create_async_engine(TEST_DATABASE_URL)

async_session_local = sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)


@pytest.fixture
async def test_session() -> None:
    async with async_session_local() as session:
        yield session


@pytest.fixture
async def user_test_repo(test_session) -> ABCUserRepo:
    return PgUserRepo(test_session)


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
async def user_model(user_test_repo: ABCUserRepo, user: User) -> User:
    return await user_test_repo.create(UserCreate(**user.model_dump()))
