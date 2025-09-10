from pydantic import BaseModel
from typing import Optional
class CustomerIn(BaseModel):
    name: str
    document: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
class CustomerOut(CustomerIn):
    id: int
