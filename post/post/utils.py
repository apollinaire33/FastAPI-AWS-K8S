import uuid

import httpx

from post.rest.models.post import Author


async def get_author_details_by_uuid(author_uuid: uuid.UUID) -> Author:
    async with httpx.AsyncClient() as client:
        url = f"http://user_app_1:8000/users/{str(author_uuid)}"
        result: httpx.Response = await client.get(url)
        return result.json()
