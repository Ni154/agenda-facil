from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, func, Text
from sqlalchemy.orm import relationship
from backend.config.database import Base

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    service = Column(String, default="")
    scheduled_for = Column(DateTime, server_default=func.now())
    notes = Column(Text, default="")
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
