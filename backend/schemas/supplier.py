from pydantic import BaseModel
from typing import Optional
class SupplierIn(BaseModel):
    name: str
    document: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
class SupplierOut(SupplierIn):
    id: int
