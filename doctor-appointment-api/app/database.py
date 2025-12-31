from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = (
    "mysql+aiomysql://doctor_user:doctor_pass@db:3306/doctor_db"
)

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass
