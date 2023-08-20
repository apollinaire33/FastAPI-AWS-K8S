from fastapi import FastAPI

from user.core.config import PROJECT_NAME
from user.rest.api.router import router

app = FastAPI(title=PROJECT_NAME)

app.include_router(router)
