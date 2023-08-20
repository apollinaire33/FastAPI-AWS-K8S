from unittest.mock import Mock, patch

import pytest

from post.repositories.post_repo import TestPostRepo
from post.rest.models.post import Author


@pytest.fixture
def post_repo(post) -> TestPostRepo:
    post_repo = TestPostRepo()
    post_repo.post = post
    return post_repo


@pytest.fixture
def mock_get_author_details_by_uuid(author: Author) -> Mock:
    with patch("post.services.post_service.get_author_details_by_uuid") as mock:
        mock.return_value = author
        yield mock
