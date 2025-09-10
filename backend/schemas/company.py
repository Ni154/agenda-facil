from pydantic import BaseModel
from typing import Optional

class CompanyIn(BaseModel):
    name: str
    cnpj: str
    regime: str = "Simples Nacional"
    serie: str = "1"
    csc_csrt: str = ""
    natureza_operacao: str = "Venda de mercadoria"
    cfop_padrao: str = "5102"
    municipio: str = ""
    uf: str = ""
    ambiente: str = "homologacao"
    certificado_tipo: str = "A1"  # A1 ou A3
    certificado_info: Optional[str] = None

class CompanyOut(CompanyIn):
    id: int
