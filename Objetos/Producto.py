from pydantic import BaseModel
from datetime import datetime

class Product(BaseModel):
    product_id: int = None  
    name: str
    description: str
    company: str
    price: float
    units: int
    subcategory_id: int
    created_at: datetime = None
    updated_at: datetime = None
