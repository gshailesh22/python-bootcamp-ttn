from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from ..database import SessionLocal
from ..models import User
from ..schemas import RegisterRequest, LoginRequest
from ..auth import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(data: RegisterRequest):
    async with SessionLocal() as session:
        existing = await session.scalar(
            select(User).where(User.email == data.email)
        )
        if existing:
            raise HTTPException(400, "Email already registered")

        user = User(
            email=data.email,
            password_hash=hash_password(data.password),
            role=data.role,
            name=data.name
        )
        session.add(user)
        await session.commit()
        return {"message": "User registered successfully"}

@router.post("/login")
async def login(data: LoginRequest):
    async with SessionLocal() as session:
        user = await session.scalar(
            select(User).where(User.email == data.email)
        )

        if not user or not verify_password(
            data.password, user.password_hash
        ):
            raise HTTPException(401, "Invalid credentials")

        token = create_access_token(
            {"sub": user.id, "role": user.role}
        )
        return {"access_token": token, "token_type": "bearer"}

@router.post("/forgot-password")
async def forgot_password():
    return {"message": "Password reset initiated (mock)"}
