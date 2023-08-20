from unittest.mock import AsyncMock, Mock

from httpx import AsyncClient

from user.rest.models.user import User, UserCreate


async def test_get_user(mock_user_service: Mock, async_api_client: AsyncClient, user: User):
    mock_user_service.get_user_by_uuid = AsyncMock(return_value=user)

    response = await async_api_client.get(f"/users/{user.uuid}")
    content = response.json()

    assert response.status_code == 200
    assert content["uuid"] == str(user.uuid)
    mock_user_service.get_user_by_uuid.assert_called_once_with(user.uuid)


async def test_get_user_404(mock_user_service: Mock, async_api_client: AsyncClient, user: User):
    mock_user_service.get_user_by_uuid = AsyncMock(return_value=None)

    response = await async_api_client.get(f"/users/{user.uuid}")
    content = response.json()

    assert response.status_code == 404
    assert content["detail"] == "Item not found"
    mock_user_service.get_user_by_uuid.assert_called_once_with(user.uuid)


async def test_create_user(mock_user_service: Mock, async_api_client: AsyncClient, user: User):
    mock_user_service.create_user = AsyncMock(return_value=user)
    payload = {
        "username": user.username,
        "email": user.email,
        "age": user.age,
    }

    response = await async_api_client.post("/users/", json=payload)
    content = response.json()

    assert response.status_code == 200
    assert content == {
        "uuid": str(user.uuid),
        **payload,
    }
    mock_user_service.create_user.assert_called_once_with(UserCreate(**payload))
