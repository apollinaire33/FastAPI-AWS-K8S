import uuid

from user.repositories.user_repo import ABCUserRepo
from user.rest.models.user import User, UserCreate


class ModelUserService:
    def __init__(self, repo: ABCUserRepo) -> None:
        self._repo = repo

    async def get_user_by_uuid(self, user_uuid: uuid.UUID) -> User:
        return await self._repo.get(uuid=user_uuid)

    async def create_user(self, data: UserCreate) -> User:
        # we can put business rules validation here instead of views or DAL class
        return await self._repo.create(data=data)
