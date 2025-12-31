from fastapi import APIRouter
from sqlalchemy import select
from ..database import SessionLocal
from ..models import User, Availability

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.get("")
async def list_doctors():
    async with SessionLocal() as session:
        result = await session.scalars(
            select(User).where(User.role == "doctor")
        )
        return result.all()

@router.get("/{doctor_id}/availability")
async def doctor_availability(doctor_id: int):
    async with SessionLocal() as session:
        slots = await session.scalars(
            select(Availability).where(Availability.doctor_id == doctor_id)
        )
        return slots.all()
