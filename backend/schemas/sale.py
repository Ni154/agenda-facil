from pydantic import BaseModel
from typing import Optional
class SaleIn(BaseModel):
    customer_id: Optional[int] = None
    total: float
    description: str = ""
class SaleOut(SaleIn):
    id: int
