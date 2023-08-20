from fastapi import APIRouter

from user.rest.api.endpoints.user import user_router

router = APIRouter()
router.include_router(router=user_router)
