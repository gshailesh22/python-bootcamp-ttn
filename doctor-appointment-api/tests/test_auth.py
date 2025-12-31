import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_register_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/auth/register",
            json={
                "email": "test_doctor@test.com",
                "password": "test123",
                "role": "doctor",
                "name": "Test Doctor"
            }
        )

    assert response.status_code == 200
    assert response.json()["message"] == "Registered successfully"


@pytest.mark.asyncio
async def test_login_success():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/auth/login",
            json={
                "email": "test_doctor@test.com",
                "password": "test123"
            }
        )

    assert response.status_code == 200
    assert "access_token" in response.json()


@pytest.mark.asyncio
async def test_login_failure():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/auth/login",
            json={
                "email": "test_doctor@test.com",
                "password": "wrongpassword"
            }
        )

    assert response.status_code == 401
