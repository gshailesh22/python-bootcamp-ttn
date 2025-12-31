from fastapi import APIRouter, HTTPException
from sqlalchemy import select, and_
from ..database import SessionLocal
from ..models import Appointment
from ..schemas import AppointmentCreate

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("")
async def book_appointment(
    data: AppointmentCreate,
    patient_id: int 
):
    async with SessionLocal() as session:
        conflict = await session.scalar(
            select(Appointment).where(
                and_(
                    Appointment.doctor_id == data.doctor_id,
                    Appointment.start_time < data.end_time,
                    Appointment.end_time > data.start_time
                )
            )
        )

        if conflict:
            raise HTTPException(
                status_code=409,
                detail="Appointment slot already booked"
            )

        appt = Appointment(
            doctor_id=data.doctor_id,
            patient_id=patient_id,
            start_time=data.start_time,
            end_time=data.end_time
        )

        session.add(appt)
        await session.commit()
        return {"message": "Appointment booked successfully"}
