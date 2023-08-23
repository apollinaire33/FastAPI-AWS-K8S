import uuid

from fastapi import APIRouter, Depends, HTTPException

from post.core.dependencies import get_post_service
from post.rest.models.post import Post, PostCreate, PostWithAuthor
from post.services.post_service import ModelPostService

post_router = APIRouter(prefix="/posts")


@post_router.get("/")
async def get_base():
    return {"ping": "pong"}


@post_router.get("/{post_uuid}", response_model=PostWithAuthor)
async def get_post_details(
    post_uuid: uuid.UUID,
    post_service: ModelPostService = Depends(get_post_service),
):
    post = await post_service.get_post_by_uuid(post_uuid)
    if post is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return post


@post_router.post("/", response_model=Post)
async def create_post(
    payload: PostCreate,
    post_service: ModelPostService = Depends(get_post_service),
):
    post = await post_service.create_post(payload)
    return post
