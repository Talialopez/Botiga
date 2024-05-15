from fastapi import FastAPI, HTTPException, UploadFile, File
import csv
import io
from typing import List
from Objetos.Producto import Product
from CRUD.CRUD_Producto import crear_producto, read_productos, read_producto, update_producto, delete_producto, get_product_details
from CRUD.CRUD_Categoria import categoria_existe, crear_categoria, actualizar_categoria
from CRUD.CRUD_Subcategoria import subcategoria_existe, crear_subcategoria, actualizar_subcategoria

app = FastAPI()

# Endpoint para obtenir llista de productes en les taules
@app.get("/product/")
def read_products():
    #Truquem a la funció read_productos
    return read_productos()

# Endpoint per obtenir un producte per ID
@app.get("/product/{product_id}")
def read_product(product_id: int):
    # Truca a la funcio per obtenir un producte per ID
    result = read_producto(product_id)
    if result:
        return result
    # Si el producte no es troba fa una excepció
    raise HTTPException(status_code=404, detail="Product not found")

# Endpoint per crear un nou producte
@app.post("/product/")
def add_product(product: Product):
    # Verifica si la subcategoria posada existeix
    subcategory = subcategoria_existe(product.subcategory_id)
    if not subcategory:
        # Si no existeix la subcategoria llença exepció
        raise HTTPException(status_code=400, detail="Subcategory does not exist")
    # Truca a la funció per crear producte
    result = crear_producto(product)
    if "product_id" in result:
        return result
    # Si hi ha algun error per crear el producte fa una excepció
    raise HTTPException(status_code=400, detail=result["message"])

# Endpoint per modificar un producte per id
@app.put("/product/{product_id}")
def update_product_endpoint(product_id: int, product: Product):
    # Truca a la funció modificar per id
    result = update_producto(product_id, product)
    if "message" in result and result["message"] == "S’ha modificat correctement":
        return result
    # Si hi ha algun error per modificar el producte fa una excepció
    raise HTTPException(status_code=500, detail=result["message"])

# Endpoint per eliminar un producte per id
@app.delete("/product/{product_id}")
def delete_product_endpoint(product_id: int):
    # Truca a la funció eliminar per id
    result = delete_producto(product_id)
    if "message" in result and result["message"] == "S’ha borrat correctement":
        return result
    # Si hi ha algun error per eliminar el producte fa una excepció
    raise HTTPException(status_code=500, detail=result["message"])

# Endpoint pe saber tots els detalls de tots els productes
@app.get("/productAll/")
def get_all_product_details():
    # Truca a la funcio per els detalls dels productes
    return get_product_details()

# Endpoint per insertar productes desde un CSV
@app.post("/loadProducts")
def load_products(file: UploadFile = File(...)):
    try:
        # Llegeix el contingut del arxiu
        contents = file.file.read()
        # Decodifica el contingur i en fa stringIO
        csv_data = io.StringIO(contents.decode("utf-8"))
        reader = csv.DictReader(csv_data)

        category_id_set = set()
        subcategory_id_set = set()

        # Fem un for per cada linia del arxiu
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

        # Si tot surt be fa un return de un misstge
        return {"message": "S'ha carregat correctament"}

    except Exception as e:
        # Si no va be fa una exepcio
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
