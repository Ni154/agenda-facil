from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from backend.config.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    plan = Column(String, default="basic")  # "basic" or "premium"
    full_name = Column(String, default="")
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
