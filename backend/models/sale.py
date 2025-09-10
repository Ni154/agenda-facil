from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, func, Text
from sqlalchemy.orm import relationship
from backend.config.database import Base

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    total = Column(Float, default=0.0)
    description = Column(Text, default="")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
    nfe_id = Column(Integer, ForeignKey("invoices.id"), nullable=True)
