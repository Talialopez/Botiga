from fastapi import FastAPI, HTTPException, UploadFile, File
import csv
import io
from typing import List
from Objetos.Producto import Product
from CRUD.CRUD_Producto import crear_producto, read_productos, read_producto, update_producto, delete_producto, get_product_details
from CRUD.CRUD_Categoria import categoria_existe, crear_categoria, actualizar_categoria
from CRUD.CRUD_Subcategoria import subcategoria_existe, crear_subcategoria, actualizar_subcategoria

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Product API"}

# CRUD para productos
@app.get("/product/")
async def read_products():
    return read_productos()

@app.get("/product/{product_id}")
async def read_product(product_id: int):
    result = read_producto(product_id)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/product/")
async def add_product(product: Product):
    subcategory = subcategoria_existe(product.subcategory_id)
    if not subcategory:
        raise HTTPException(status_code=400, detail="Subcategory does not exist")
    result = crear_producto(product)
    if "product_id" in result:
        return result
    raise HTTPException(status_code=400, detail=result["message"])

@app.put("/product/{product_id}")
async def update_product_endpoint(product_id: int, product: Product):
    result = update_producto(product_id, product)
    if "message" in result and result["message"] == "S’ha modificat correctement":
        return result
    raise HTTPException(status_code=500, detail=result["message"])

@app.delete("/product/{product_id}")
async def delete_product_endpoint(product_id: int):
    result = delete_producto(product_id)
    if "message" in result and result["message"] == "S’ha borrat correctement":
        return result
    raise HTTPException(status_code=500, detail=result["message"])

@app.get("/productAll/")
async def get_all_product_details():
    return get_product_details()

# Ruta para cargar productos desde un archivo CSV
@app.post("/loadProducts")
async def load_products(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        csv_data = io.StringIO(contents.decode("utf-8"))
        reader = csv.DictReader(csv_data)

        category_id_set = set()
        subcategory_id_set = set()

        for row in reader:
            category_id = int(row["id_categoria"])
            category_name = row["nom_categoria"]
            subcategory_id = int(row["id_subcategoria"])
            subcategory_name = row["nom_subcategoria"]
            product_id = int(row["id_producto"])
            product_name = row["nom_producto"]
            product_description = row["descripcion_producto"]
            product_company = row["companyia"]
            product_price = float(row["precio"])
            product_units = int(row["unidades"])

            if category_id not in category_id_set:
                if categoria_existe(category_id):
                    actualizar_categoria(category_id, category_name)
                else:
                    crear_categoria(category_name)
                category_id_set.add(category_id)

            if subcategory_id not in subcategory_id_set:
                if subcategoria_existe(subcategory_id):
                    actualizar_subcategoria(subcategory_id, subcategory_name)
                else:
                    crear_subcategoria(subcategory_name, category_id)
                subcategory_id_set.add(subcategory_id)

            if read_producto(product_id):
                update_producto(product_id, Product(
                    product_id=product_id,
                    name=product_name,
                    description=product_description,
                    company=product_company,
                    price=product_price,
                    units=product_units,
                    subcategory_id=subcategory_id
                ))
            else:
                crear_producto(Product(
                    product_id=product_id,
                    name=product_name,
                    description=product_description,
                    company=product_company,
                    price=product_price,
                    units=product_units,
                    subcategory_id=subcategory_id
                ))

        return {"message": "S'ha carregat correctament"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
