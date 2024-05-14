from bbdd import db_client

# Función para verificar si una subcategoría existe en la base de datos
def subcategoria_existe(subcategory_id):
    try:
        conn = db_client()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM subcategory WHERE subcategory_id = %s", (subcategory_id,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        return {"status": -1, "message": f"Error de conexión: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Función para crear una nueva subcategoría en la base de datos
def crear_subcategoria(subcategory_name, category_id):
    try:
        conn = db_client()
        cursor = conn.cursor()
        sql = "INSERT INTO subcategory (name, category_id) VALUES (%s, %s)"
        cursor.execute(sql, (subcategory_name, category_id))
        conn.commit()
        return cursor.lastrowid
    except Exception as e:
        return {"message": f"Error de conexión: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Función para actualizar el nombre de una subcategoría en la base de datos
def actualizar_subcategoria(subcategory_id, subcategory_name):
    try:
        conn = db_client()
        cursor = conn.cursor()
        sql = "UPDATE subcategory SET name = %s, updated_at = CURRENT_TIMESTAMP WHERE subcategory_id = %s"
        cursor.execute(sql, (subcategory_name, subcategory_id))
        conn.commit()
        return {"message": "Subcategoría actualizada correctamente"}
    except Exception as e:
        return {"status": -1, "message": f"Error de conexión: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
