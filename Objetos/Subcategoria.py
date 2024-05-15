from pydantic import BaseModel
from datetime import datetime

# Definición de la clase Subcategory que hereda de BaseModel
class Subcategory(BaseModel):
    subcategory_id: int = None
    name: str
    category_id: int
    created_at: datetime = None
    updated_at: datetime = None

# Función para convertir un objeto de subcategoría en un diccionario
def subcategory_schema(subcategory) -> dict:
    return {
        "subcategory_id": subcategory["subcategory_id"],
        "name": subcategory["name"],
        "category_id": subcategory["category_id"],
        "created_at": subcategory["created_at"],
        "updated_at": subcategory["updated_at"]
    }

# Función para convertir una lista de objetos de subcategoría en una lista de diccionarios
def subcategories_schema(subcategories) -> list:
    return [subcategory_schema(subcategory) for subcategory in subcategories]
