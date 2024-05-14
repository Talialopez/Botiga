from pydantic import BaseModel
from datetime import datetime

class Subcategory(BaseModel):
    subcategory_id: int = None
    name: str
    category_id: int
    created_at: datetime = None
    updated_at: datetime = None