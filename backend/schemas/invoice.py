from pydantic import BaseModel
from typing import Optional
class InvoiceOut(BaseModel):
    id: int
    type: str
    status: str
    protocol: str | None = None
