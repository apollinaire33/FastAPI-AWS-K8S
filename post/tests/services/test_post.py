from post.repositories.post_repo import TestPostRepo
from post.rest.models.post import Post, PostWithAuthor
from post.services.post_service import ModelPostService


async def test_post_service__get_post_by_uuid(
    mock_get_author_details_by_uuid,
    post_repo: TestPostRepo,
    post_with_author: Post,
):
    assert post_with_author == await ModelPostService(post_repo).get_post_by_uuid(
        post_with_author.uuid
    )


async def test_post_service__create_post(post_repo: TestPostRepo, post: Post):
    assert post == await ModelPostService(post_repo).create_post(post.uuid)
