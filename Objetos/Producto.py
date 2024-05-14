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

def product_schema(product) -> dict:
    return {
        "product_id": product["product_id"],
        "name": product["name"],
        "description": product["description"],
        "company": product["company"],
        "price": product["price"],
        "units": product["units"],
        "subcategory_id": product["subcategory_id"],
        "created_at": product["created_at"],
        "updated_at": product["updated_at"]
    }

def products_schema(products) -> list:
    return [product_schema(product) for product in products]
