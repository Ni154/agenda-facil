from pydantic import BaseModel
from typing import Optional
class AppointmentIn(BaseModel):
    customer_id: Optional[int] = None
    service: str
    notes: Optional[str] = ""
class AppointmentOut(AppointmentIn):
    id: int
