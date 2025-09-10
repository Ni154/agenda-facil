from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, func, Text
from sqlalchemy.orm import relationship
from backend.config.database import Base

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cnpj = Column(String, unique=True, index=True)
    regime = Column(String, default="Simples Nacional")
    serie = Column(String, default="1")
    csc_csrt = Column(String, default="")
    natureza_operacao = Column(String, default="Venda de mercadoria")
    cfop_padrao = Column(String, default="5102")
    municipio = Column(String, default="")
    uf = Column(String, default="")
    ambiente = Column(String, default="homologacao")  # ou "producao"

    certificado_tipo = Column(String, default="A1")  # A1 ou A3
    certificado_pfx = Column(Text, nullable=True)    # bytes base64(encrypted) - opcional
    certificado_info = Column(Text, nullable=True)   # instruções A3, etc.

    owner_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
