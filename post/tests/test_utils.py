from unittest.mock import AsyncMock

import httpx

from post.rest.models.post import Post
from post.utils import get_author_details_by_uuid


async def test_get_author_details_by_uuid(mock_httpx_async_client, author: dict[str, str], post: Post):
    mock_httpx_async_client.get = AsyncMock(return_value=httpx.Response(200, json=author))
    author_details = await get_author_details_by_uuid(author_uuid=post.author_uuid)
    assert author_details == author
