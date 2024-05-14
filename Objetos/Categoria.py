from pydantic import BaseModel
from datetime import datetime

class Category(BaseModel):
    category_id: int = None
    name: str
    created_at: datetime = None
    updated_at: datetime = None
