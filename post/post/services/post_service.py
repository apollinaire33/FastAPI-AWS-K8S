import uuid

from post.repositories.post_repo import ABCPostRepo
from post.rest.models.post import Post, PostCreate, PostWithAuthor
from post.utils import get_author_details_by_uuid


class ModelPostService:
    def __init__(self, repo: ABCPostRepo) -> None:
        self._repo = repo

    async def get_post_by_uuid(self, post_uuid: uuid.UUID) -> PostWithAuthor:
        post: Post = await self._repo.get(uuid=post_uuid)
        author = None
        if post is not None:
            author = await get_author_details_by_uuid(post.author_uuid)
        return PostWithAuthor(**post.model_dump(), author=author)

    async def create_post(self, data: PostCreate) -> Post:
        # we can put business rules validation here instead of views or DAL class
        return await self._repo.create(data=data)
