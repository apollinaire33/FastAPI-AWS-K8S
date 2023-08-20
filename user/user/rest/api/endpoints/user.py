import uuid

from fastapi import APIRouter, Depends, HTTPException

from user.core.dependencies import get_user_service
from user.services.user_service import ModelUserService
from user.rest.models.user import User, UserCreate

user_router = APIRouter(prefix="/users")


@user_router.get("/{user_uuid}", response_model=User)
async def get_user_details(
    user_uuid: uuid.UUID,
    user_service: ModelUserService = Depends(get_user_service),
):
    user = await user_service.get_user_by_uuid(user_uuid)
    if user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return user


@user_router.post("/", response_model=User)
async def create_user(
    payload: UserCreate,
    user_service: ModelUserService = Depends(get_user_service),
):
    user = await user_service.create_user(payload)
    return user
