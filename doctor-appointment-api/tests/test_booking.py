import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_appointment_booking_and_conflict():
    async with AsyncClient(app=app, base_url="http://test") as client:

        # Register doctor
        await client.post(
            "/auth/register",
            json={
                "email": "doc_booking@test.com",
                "password": "doc123",
                "role": "doctor",
                "name": "Booking Doctor"
            }
        )

        # Register patient
        await client.post(
            "/auth/register",
            json={
                "email": "patient_booking@test.com",
                "password": "pat123",
                "role": "patient",
                "name": "Booking Patient"
            }
        )

        # Login patient
        login_response = await client.post(
            "/auth/login",
            json={
                "email": "patient_booking@test.com",
                "password": "pat123"
            }
        )

        token = login_response.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        # Book appointment (SUCCESS)
        booking_response = await client.post(
            "/appointments",
            headers=headers,
            json={
                "doctor_id": 1,
                "start_time": "2025-01-10T10:00:00",
                "end_time": "2025-01-10T10:30:00"
            }
        )

        assert booking_response.status_code == 200
        assert booking_response.json()["message"] == "Appointment booked"

        # Book same slot again (CONFLICT)
        conflict_response = await client.post(
            "/appointments",
            headers=headers,
            json={
                "doctor_id": 1,
                "start_time": "2025-01-10T10:00:00",
                "end_time": "2025-01-10T10:30:00"
            }
        )

        assert conflict_response.status_code == 409
        assert "already booked" in conflict_response.json()["detail"]
