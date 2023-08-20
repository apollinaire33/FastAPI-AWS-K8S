import uuid
import datetime
from unittest.mock import patch, Mock
from typing import Any

import pytest

from post.rest.models.post import Post, PostWithAuthor


@pytest.fixture
def mock_httpx_async_client():
    with patch("httpx.AsyncClient") as mock_async_client_manager:
        mock_async_client = Mock()
        mock_async_client_manager.return_value.__aenter__.return_value = mock_async_client
        yield mock_async_client


@pytest.fixture
def author(post: Post) -> dict[str, Any]:
    return {
        "uuid": str(post.author_uuid),
        "username": "test_test",
        "email": "test_test@duck.com",
        "age": 27,
    }


@pytest.fixture
def post() -> Post:
    return Post(
        uuid=uuid.uuid4(),
        author_uuid=uuid.uuid4(),
        subject="ducks! ducks! ducks!",
        text="I love ducks so hard! I can't even describe what I feel, my love is enormous!",
        created_at=datetime.datetime.now(),
    )


@pytest.fixture
def post_with_author(post: Post, author: dict[str, Any]) -> PostWithAuthor:
    return PostWithAuthor(**post.model_dump(), author=author)
