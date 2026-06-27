from datetime import UTC, datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.core.config import get_settings

_pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return _pwd.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return _pwd.verify(password, hashed)

def create_token(subject: str, token_type: str = "access", minutes: int | None = None) -> str:
    settings = get_settings()
    expire = datetime.now(UTC) + timedelta(minutes=minutes or settings.access_token_minutes)
    return jwt.encode({"sub": subject, "type": token_type, "exp": expire}, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
