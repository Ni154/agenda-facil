from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, func, Text
from sqlalchemy.orm import relationship
from backend.config.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    sku = Column(String, unique=True, index=True)
    price = Column(Float, default=0.0)
    stock = Column(Float, default=0.0)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
