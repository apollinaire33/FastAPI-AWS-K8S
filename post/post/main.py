from fastapi import FastAPI

from post.core.config import PROJECT_NAME
from post.rest.api.router import router

app = FastAPI(title=PROJECT_NAME)

app.include_router(router)
