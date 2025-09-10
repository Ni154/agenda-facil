from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, func, Text
from sqlalchemy.orm import relationship
from backend.config.database import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    document = Column(String, index=True)  # CPF/CNPJ
    email = Column(String, default="")
    phone = Column(String, default="")
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
