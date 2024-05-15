from pydantic import BaseModel
from datetime import datetime

# Definición de la clase Category que hereda de BaseModel
class Category(BaseModel):
    category_id: int = None
    name: str
    created_at: datetime = None
    updated_at: datetime = None

# Función para convertir un objeto de categoría en un diccionario
def category_schema(category) -> dict:
    return {
        "category_id": category["category_id"],
        "name": category["name"],
        "created_at": category["created_at"],
        "updated_at": category["updated_at"]
    }

# Función para convertir una lista de objetos de categoría en una lista de diccionarios
def categories_schema(categories) -> list:
    return [category_schema(category) for category in categories]
