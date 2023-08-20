from unittest.mock import AsyncMock, Mock

from httpx import AsyncClient

from post.rest.models.post import Post, PostCreate, PostWithAuthor


async def test_get_post(
    mock_post_service: Mock,
    async_api_client: AsyncClient,
    post_with_author: PostWithAuthor,
):
    mock_post_service.get_post_by_uuid = AsyncMock(return_value=post_with_author)

    response = await async_api_client.get(f"/posts/{post_with_author.uuid}")
    content = response.json()

    assert response.status_code == 200
    assert PostWithAuthor(**content) == post_with_author
    mock_post_service.get_post_by_uuid.assert_called_once_with(post_with_author.uuid)


async def test_get_post_404(mock_post_service: Mock, async_api_client: AsyncClient, post: Post):
    mock_post_service.get_post_by_uuid = AsyncMock(return_value=None)

    response = await async_api_client.get(f"/posts/{post.uuid}")
    content = response.json()

    assert response.status_code == 404
    assert content["detail"] == "Item not found"
    mock_post_service.get_post_by_uuid.assert_called_once_with(post.uuid)


async def test_create_post(mock_post_service: Mock, async_api_client: AsyncClient, post: Post):
    mock_post_service.create_post = AsyncMock(return_value=post)
    payload = {
        "author_uuid": str(post.author_uuid),
        "subject": post.subject,
        "text": post.text,
    }

    response = await async_api_client.post("/posts/", json=payload)
    content = response.json()

    assert response.status_code == 200
    assert content == {
        "uuid": str(post.uuid),
        "created_at": post.created_at.isoformat(),
        **payload,
    }
    mock_post_service.create_post.assert_called_once_with(PostCreate(**payload))
