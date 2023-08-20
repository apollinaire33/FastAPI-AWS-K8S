import uuid

import pytest

from post.repositories.post_repo import ABCPostRepo
from post.rest.models.post import Post, PostCreate


@pytest.fixture
def post_data(post: Post):
    return PostCreate(**post.model_dump())


async def test_post_repo__get(post_test_repo: ABCPostRepo, post_model: Post):
    assert post_model == await post_test_repo.get(uuid=post_model.uuid)


async def test_post_repo__get__not_found(post_test_repo: ABCPostRepo):
    assert None == await post_test_repo.get(uuid=uuid.uuid4())


async def test_post_repo__create(post_test_repo: ABCPostRepo, post_data: PostCreate):
    post = await post_test_repo.create(post_data)
    assert post == await post_test_repo.get(uuid=post.uuid)
