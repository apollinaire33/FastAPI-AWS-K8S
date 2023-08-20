from user.repositories.user_repo import TestUserRepo
from user.rest.models.user import User
from user.services.user_service import ModelUserService


async def test_user_service__get_user_by_uuid(user_repo: TestUserRepo, user: User):
    assert user == await ModelUserService(user_repo).get_user_by_uuid(user.uuid)


async def test_user_service__create_user(user_repo: TestUserRepo, user: User):
    assert user == await ModelUserService(user_repo).create_user(user.uuid)
