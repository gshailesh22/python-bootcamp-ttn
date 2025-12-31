from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, doctors, appointments

app = FastAPI(title="Doctor Appointment API")

app.include_router(auth.router)
app.include_router(doctors.router)
app.include_router(appointments.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
