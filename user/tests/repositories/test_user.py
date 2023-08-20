import uuid

import pytest

from user.repositories.user_repo import ABCUserRepo
from user.rest.models.user import User, UserCreate


@pytest.fixture
def user_data(user: User):
    return UserCreate(**user.model_dump())


async def test_user_repo__get(user_test_repo: ABCUserRepo, user_model: User):
    assert user_model == await user_test_repo.get(uuid=user_model.uuid)


async def test_user_repo__get__not_found(user_test_repo: ABCUserRepo):
    assert None == await user_test_repo.get(uuid=uuid.uuid4())


async def test_user_repo__create(user_test_repo: ABCUserRepo, user_data: UserCreate):
    user = await user_test_repo.create(user_data)
    assert user == await user_test_repo.get(uuid=user.uuid)
