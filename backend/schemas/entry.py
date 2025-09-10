from pydantic import BaseModel
from typing import Optional
class EntryIn(BaseModel):
    type: str
    description: str
    amount: float
class EntryOut(EntryIn):
    id: int
