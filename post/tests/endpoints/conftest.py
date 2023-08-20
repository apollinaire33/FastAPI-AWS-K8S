import uuid
import pytest
from unittest.mock import patch, Mock

from fastapi import FastAPI
from httpx import AsyncClient

from post.core.dependencies import get_post_service


@pytest.fixture
def mock_post_service() -> Mock:
    with patch("post.services.post_service.ModelPostService") as mock:
        return mock


@pytest.fixture()
def app(mock_post_service) -> FastAPI:
    from post.main import app

    app.dependency_overrides[get_post_service] = lambda: mock_post_service
    return app


@pytest.fixture()
async def async_api_client(app: FastAPI) -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
