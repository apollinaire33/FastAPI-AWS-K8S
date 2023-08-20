from fastapi import APIRouter

from post.rest.api.endpoints.post import post_router

router = APIRouter()
router.include_router(router=post_router)
