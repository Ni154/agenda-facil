from pydantic import BaseModel, Field
from typing import Optional

class Pagination(BaseModel):
    page: int = 1
    size: int = 10
    q: Optional[str] = None
