import uuid

import pytest

from user.rest.models.user import User


@pytest.fixture
def user():
    return User(
        uuid=uuid.uuid4(),
        username="test_username",
        email="test_email@duck.com",
        age=27,
    )
