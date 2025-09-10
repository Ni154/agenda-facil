from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, func, Text
from sqlalchemy.orm import relationship
from backend.config.database import Base

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, default="nfe")  # nfe/nfse
    status = Column(String, default="pending")  # pending/authorized/canceled/error
    protocol = Column(String, default="")
    authorized_at = Column(DateTime, nullable=True)
    canceled_at = Column(DateTime, nullable=True)
    error_message = Column(Text, nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=True)
    sale_id = Column(Integer, ForeignKey("sales.id"), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
