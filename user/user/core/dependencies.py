from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from user.database.postgresql.setup_db import get_db
from user.repositories.user_repo import ABCUserRepo, PgUserRepo
from user.services.user_service import ModelUserService


async def get_user_repo(session: AsyncSession = Depends(get_db)) -> ABCUserRepo:
    return PgUserRepo(session)


async def get_user_service(
    user_repo: ABCUserRepo = Depends(get_user_repo)
) -> ModelUserService:
    return ModelUserService(user_repo)


# async def get_test_user_service(
#     user_repo: PgUserRepo = Depends(get_user_repo), session: AsyncSession = Depends(get_test_db)
# ) -> ModelUserService:
#     return ModelUserService(repo=user_repo, session=session)
