from fastapi import FastAPI
from Objetos.Producto import Product  # Asegúrate de que las importaciones coincidan con la estructura de tu proyecto
from CRUD.CRUD_Producto import crear_producto, read_productos, read_producto, update_producto, delete_producto

app = FastAPI()

@app.post("/product/")
async def add_product(product: Product):
    return crear_producto(product)

@app.get("/products/")
async def read_products():
    return read_productos()

@app.get("/product/{product_id}")
async def read_product(product_id: int):
    return read_producto(product_id)

@app.put("/product/{product_id}")
async def update_product_endpoint(product_id: int, product: Product):
    return update_producto(product_id, product)

@app.delete("/product/{product_id}")
async def delete_product_endpoint(product_id: int):
    return delete_producto(product_id)
