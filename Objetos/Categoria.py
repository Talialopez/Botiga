from pydantic import BaseModel
from datetime import datetime

class Category(BaseModel):
    category_id: int = None
    name: str
    created_at: datetime = None
    updated_at: datetime = None

def category_schema(category) -> dict:
    return {
        "category_id": category["category_id"],
        "name": category["name"],
        "created_at": category["created_at"],
        "updated_at": category["updated_at"]
    }

def categories_schema(categories) -> list:
    return [category_schema(category) for category in categories]
