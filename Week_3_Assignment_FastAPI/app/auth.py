from datetime import datetime, timedelta
from passlib.context import CryptContext
import hashlib
from jose import jwt

SECRET_KEY = "SECRET123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def _sha256(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def hash_password(password: str) -> str:
    print("PASSWORD LENGTH:", len(password.encode("utf-8")))
    return pwd_context.hash(_sha256(password))

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(_sha256(plain_password), hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
