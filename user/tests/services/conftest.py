import pytest

from user.repositories.user_repo import TestUserRepo


@pytest.fixture
def user_repo(user) -> TestUserRepo:
    user_repo = TestUserRepo()
    user_repo.user = user
    return user_repo
