from bbdd import db_client

# Funció per crear un nou profucte
def crear_producto(product):
    try:
        # Ens connectem a la bbdd
        conn = db_client()
        cursor = conn.cursor()
        # Fem un insert de producte
        sql = """
        INSERT INTO product (name, description, company, price, units, subcategory_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        # Executem la comanda
        cursor.execute(sql, (product.name, product.description, product.company, product.price, product.units, product.subcategory_id))
        # Li fem commit
        conn.commit()
        # SI tot va bé retorna un missatge de tot correcte
        return {"message": "S’ha afegit correctement", "product_id": cursor.lastrowid}
    except Exception as e:
        # Si surt malament llença un missatge de malament
        return {"message": f"Error de conexión: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Funció per llegir els productes de la bbdd
def read_productos():
    try:
        #Fem la connexió
        conn = db_client()
        cursor = conn.cursor(dictionary=True)
        # Fem la query
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()
        return products
    except Exception as e:
        #Si va malament fem una exepció
        return {"message": f"Error en la lectura de productos: {e}"}
    finally:
        # Tanquem la connecció
        if conn.is_connected():
            cursor.close()
            conn.close()

# Funció per fer el read per id
def read_producto(product_id):
    try:
        #Fem la connexió a la bbdd
        conn = db_client()
        cursor = conn.cursor(dictionary=True)
        #Fem la query
        cursor.execute("SELECT * FROM product WHERE product_id = %s", (product_id,))
        product = cursor.fetchone()
        return product
    except Exception as e:
        #Misstge de error en cas de no lectura
        return {"message": f"Error en la lectura del producto: {e}"}
    finally:
        #Tanquem la conecció
        if conn.is_connected():
            cursor.close()
            conn.close()

# Funció per actualitzar producte per id
def update_producto(product_id, product):
    try:
        #Connectem a la bbdd
        conn = db_client()
        cursor = conn.cursor()
        #Query
        sql = """
        UPDATE product SET name = %s, description = %s, company = %s, price = %s, units = %s, subcategory_id = %s 
        WHERE product_id = %s
        """
        #Executem QUery
        cursor.execute(sql, (product.name, product.description, product.company, product.price, product.units, product.subcategory_id, product_id))
        conn.commit()
        #Si està bé llençem un missatge
        return {"message": "S’ha modificat correctement"}
    except Exception as e:
        #Si no llençem missatge de error
        return {"message": f"Error en la actualización del producto: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Funció per eliminar producte per id
def delete_producto(product_id):
    try:
        #Conectem a la bbdd
        conn = db_client()
        cursor = conn.cursor()
        #Query
        cursor.execute("DELETE FROM product WHERE product_id = %s", (product_id,))
        conn.commit()
        #Si està bé llençem un missatge
        return {"message": "S’ha borrat correctement"}
    except Exception as e:
        #Si no llençem missatge de error
        return {"message": f"Error a la hora de eliminar el producto: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            
# Funcio per obtenir detalls de productes
def get_product_details():
    try:
        #Connexió a la bbdd
        conn = db_client()
        cursor = conn.cursor(dictionary=True)
        #Query
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
        #Si no va bé llençem missatge de error
        return {"message": f"Error en la lectura de detalles de productos: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
