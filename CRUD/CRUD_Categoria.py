from bbdd import db_client

# Función para verificar si una categoría existe en la base de datos
def categoria_existe(category_id):
    try:
        conn = db_client()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM category WHERE category_id = %s", (category_id,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        return {"status": -1, "message": f"Error de conexión: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Función para crear una nueva categoría en la base de datos
def crear_categoria(category_name):
    try:
        conn = db_client()
        cursor = conn.cursor()
        sql = "INSERT INTO category (name) VALUES (%s)"
        cursor.execute(sql, (category_name,))
        conn.commit()
        return cursor.lastrowid
    except Exception as e:
        return {"status": -1, "message": f"Error de conexión: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Función para actualizar el nombre de una categoría en la base de datos
def actualizar_categoria(category_id, category_name):
    try:
        conn = db_client()
        cursor = conn.cursor()
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
