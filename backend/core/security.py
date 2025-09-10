from datetime import datetime, timedelta, timezone
from typing import Optional, Literal
from fastapi import HTTPException, status, Depends
from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.config.database import get_db
from backend.models.user import User
from backend.core.settings import settings

ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    return pwd_context.verify(password, password_hash)

class TokenData(BaseModel):
    user_id: int
    email: str
    plan: Literal["basic", "premium"]

def create_access_token(data: dict, expires_minutes: Optional[int] = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes or settings.JWT_EXPIRES_MIN)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=ALGORITHM)

def get_current_user(db: Session = Depends(get_db), token: str | None = None, authorization: str | None = None):
    # Support "Authorization: Bearer <token>"
    if authorization and authorization.lower().startswith("bearer "):
        token = authorization.split(" ", 1)[1]
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.id == user_id, User.deleted_at.is_(None)).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

def require_plan(required: Literal["basic", "premium"]):
    def checker(user: User = Depends(get_current_user)):
        plan_order = {"basic": 1, "premium": 2}
        if plan_order[user.plan] < plan_order[required]:
            raise HTTPException(status_code=403, detail=f"Plano {user.plan} não permite esta ação")
        return user
    return checker
