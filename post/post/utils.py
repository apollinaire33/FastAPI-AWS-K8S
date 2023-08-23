import uuid
import os

import httpx

from post.rest.models.post import Author

user_service_domain = os.environ.get("USER_SERVICE_DOMAIN", "user_app_1:8000")


async def get_author_details_by_uuid(author_uuid: uuid.UUID) -> Author:
    async with httpx.AsyncClient() as client:
        url = f"http://{user_service_domain}/users/{str(author_uuid)}"
        result: httpx.Response = await client.get(url)
        return result.json()
