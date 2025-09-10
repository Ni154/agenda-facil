from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.config.database import get_db
from backend.schemas.auth import LoginRequest, LoginResponse
from backend.core.security import create_access_token, verify_password, hash_password
from backend.models.user import User
from backend.core.settings import settings

router = APIRouter()

@router.on_event("startup")
def seed_admin():
    from backend.config.database import SessionLocal
    db = SessionLocal()
    try:
        existing = db.query(User).filter(User.email == settings.ADMIN_EMAIL).first()
        if not existing:
            u = User(email=settings.ADMIN_EMAIL, password_hash=hash_password(settings.ADMIN_PASSWORD), plan="premium", full_name="Admin")
            db.add(u)
            db.commit()
    finally:
        db.close()

@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email, User.deleted_at.is_(None)).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = create_access_token({"user_id": user.id, "email": user.email, "plan": user.plan})
    return LoginResponse(access_token=token, plan=user.plan, email=user.email)
