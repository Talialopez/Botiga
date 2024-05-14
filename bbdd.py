import mysql.connector
from mysql.connector import Error

#Se realiza la configuración para la BBDD Botiga
configuracio = {
    "user": "dam_app",
    "password": "1234",
    "database": "Botiga",
    "host": "localhost",
    "port": "3306"
}

#Nos conectamos a la Base de Datos
def connect():
    conn = None
    try:
        conn = mysql.connector.connect(**configuracio)

        # Verificamos que la conexión haya sido correcta mediante un cursos que nos enseñe las tablas existentes en la BBDD.
        if conn.is_connected():
            print('Conexión exitosa.')
            cursor = conn.cursor()
            cursor.execute("SHOW TABLES")

            # Se imprimen los resultados de las tablas encontradas en la pantalla.
            for table in cursor:
                print(table)

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")


if __name__ == '__main__':
    connect()
