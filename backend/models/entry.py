from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, func, Text
from sqlalchemy.orm import relationship
from backend.config.database import Base

class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, default="despesa")  # receita/despesa
    description = Column(String, default="")
    amount = Column(Float, default=0.0)
    date = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
