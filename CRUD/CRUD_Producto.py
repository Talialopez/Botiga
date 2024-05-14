from bbdd import db_client

def crear_producto(product):
    try:
        conn = db_client()
        cursor = conn.cursor()
        sql = """
        INSERT INTO product (name, description, company, price, units, subcategory_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (product.name, product.description, product.company, product.price, product.units, product.subcategory_id))
        conn.commit()
        return {"message": "S’ha afegit correctement", "product_id": cursor.lastrowid}
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
        cursor.execute("SELECT * FROM product")
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
        cursor.execute("SELECT * FROM product WHERE product_id = %s", (product_id,))
        product = cursor.fetchone()
        return product
    except Exception as e:
        return {"message": f"Error en la lectura del producto: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def update_producto(product_id, product):
    try:
        conn = db_client()
        cursor = conn.cursor()
        sql = """
        UPDATE product SET name = %s, description = %s, company = %s, price = %s, units = %s, subcategory_id = %s 
        WHERE product_id = %s
        """
        cursor.execute(sql, (product.name, product.description, product.company, product.price, product.units, product.subcategory_id, product_id))
        conn.commit()
        return {"message": "S’ha modificat correctement"}
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
        cursor.execute("DELETE FROM product WHERE product_id = %s", (product_id,))
        conn.commit()
        return {"message": "S’ha borrat correctement"}
    except Exception as e:
        return {"message": f"Error a la hora de eliminar el producto: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def get_product_details():
    try:
        conn = db_client()
        cursor = conn.cursor(dictionary=True)
        sql = """
        SELECT p.name as product_name, p.company as product_company, p.price as product_price,
               c.name as category_name, sc.name as subcategory_name
        FROM product p
        JOIN subcategory sc ON p.subcategory_id = sc.subcategory_id
        JOIN category c ON sc.category_id = c.category_id
        """
        cursor.execute(sql)
        products = cursor.fetchall()
        return products
    except Exception as e:
        return {"message": f"Error en la lectura de detalles de productos: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
