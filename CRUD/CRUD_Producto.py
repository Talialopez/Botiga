from Objetos.Producto import Product
from bbdd import db_client

def crear_producto(product: Product):
    try:
        conn = db_client()
        cursor = conn.cursor()
        sql = """
        INSERT INTO products (name, description, company, price, units, subcategory_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (product.name, product.description, product.company, product.price, product.units, product.subcategory_id))
        conn.commit()
        return {"message": "Producto creado correctamente", "product_id": cursor.lastrowid}
    except Exception as e:
        return {"message": f"Error de conexión: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def read_productos():
    try:
        conn = db_client()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        return products
    except Exception as e:
        return {"message": f"Error en la lectura de productos: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def read_producto(product_id):
    try:
        conn = db_client()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products WHERE product_id = %s", (product_id,))
        product = cursor.fetchone()
        return product
    except Exception as e:
        return {"message": f"Error en la lectura del producto: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def update_producto(product_id, name, description, company, price, units, subcategory_id):
    try:
        conn = db_client()
        cursor = conn.cursor()
        sql = """
        UPDATE products SET name = %s, description = %s, company = %s, price = %s, units = %s, subcategory_id = %s 
        WHERE product_id = %s
        """
        cursor.execute(sql, (name, description, company, price, units, subcategory_id, product_id))
        conn.commit()
        return {"message": "Producto actualizado"}
    except Exception as e:
        return {"message": f"Error en la actualización del producto: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def delete_producto(product_id):
    try:
        conn = db_client()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
        conn.commit()
        return {"message": "Producto eliminado"}
    except Exception as e:
        return {"status": -1, "message": f"Error a la hora de eliminar el producto: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()




