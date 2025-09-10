from pydantic import BaseModel
from typing import Optional
class ProductIn(BaseModel):
    name: str
    sku: str
    price: float
    stock: float = 0
class ProductOut(ProductIn):
    id: int
