from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, func
from backend.config.database import Base

class ChangeLog(Base):
    __tablename__ = "change_logs"
    id = Column(Integer, primary_key=True, index=True)
    entity = Column(String, index=True)   # e.g., "empresa", "cliente"
    entity_id = Column(Integer, index=True)
    action = Column(String)               # "create", "update", "delete"
    before = Column(Text, nullable=True)
    after = Column(Text, nullable=True)
    user_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
