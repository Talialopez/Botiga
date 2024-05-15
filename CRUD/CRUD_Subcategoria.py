from bbdd import db_client

# FFuncio per verificar si existeix la subcategoria
def subcategoria_existe(subcategory_id):
    try:
        #Ens conectem a la bbdd
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

# Funció per crear subcategoria
def crear_subcategoria(subcategory_name, category_id):
    try:
        #Ens conectem a la bbdd
        conn = db_client()
        cursor = conn.cursor()
        # Fem un insert dels values
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

# Funció per actualitzar la subcategoria per id
def actualizar_subcategoria(subcategory_id, subcategory_name):
    try:
        # Ens connectem a la bbdd
        conn = db_client()
        cursor = conn.cursor()
        # Fem un update
        sql = "UPDATE subcategory SET name = %s, updated_at = CURRENT_TIMESTAMP WHERE subcategory_id = %s"
        # Executem la comanda
        cursor.execute(sql, (subcategory_name, subcategory_id))
        conn.commit()
        # Si tot va bé llençem un missatge
        return {"message": "Subcategoría actualizada correctamente"}
    except Exception as e:
        # Si surt malament també
        return {"status": -1, "message": f"Error de conexión: {e}"}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
