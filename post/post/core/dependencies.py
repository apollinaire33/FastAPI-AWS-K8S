from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from post.database.postgresql.setup_db import get_db
from post.services.post_service import ModelPostService
from post.repositories.post_repo import ABCPostRepo, PgPostRepo


async def get_post_repo(session: AsyncSession = Depends(get_db)) -> ABCPostRepo:
    return PgPostRepo(session)


async def get_post_service(
    post_repo: ABCPostRepo = Depends(get_post_repo)
) -> ModelPostService:
    return ModelPostService(post_repo)
