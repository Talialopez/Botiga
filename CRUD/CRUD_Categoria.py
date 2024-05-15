from bbdd import db_client

# Funció per saber si categoria existeix
def categoria_existe(category_id):
    try:
        #Conectar a la bbdd
        conn = db_client()
        cursor = conn.cursor(dictionary=True)
        #Query
        cursor.execute("SELECT * FROM category WHERE category_id = %s", (category_id,))
        result = cursor.fetchone()
        #Retornem el que hem obtingut
        return result
    except Exception as e:
        #SI va malament retornem exception
        return {"status": -1, "message": f"Error de conexión: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Funció per crear categoria
def crear_categoria(category_name):
    try:
        #Conectem a la bbdd
        conn = db_client()
        cursor = conn.cursor()
        #Query
        sql = "INSERT INTO category (name) VALUES (%s)"
        cursor.execute(sql, (category_name,))
        conn.commit()
        #Return de la query
        return cursor.lastrowid
    except Exception as e:
        #Si hi ha error al return, llençem un missatge
        return {"status": -1, "message": f"Error de conexión: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Funció per actualitzar categoria
def actualizar_categoria(category_id, category_name):
    try:
        #Conectar a la bbdd
        conn = db_client()
        cursor = conn.cursor()
        #Query
        sql = "UPDATE category SET name = %s, updated_at = CURRENT_TIMESTAMP WHERE category_id = %s"
        cursor.execute(sql, (category_name, category_id))
        conn.commit()
        return {"message": "Categoría actualizada correctamente"}
    except Exception as e:
        return {"status": -1, "message": f"Error de conexión: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
