import pyodbc
import pickle
from lib.encryptor_decryptor import load_key, encrypt_password, decrypt_password
import os

USER_DATA_FILE = "user_data.dat"
KEY_FILE_PATH = "keys/key.key"

def save_user_data(username, password):
    """
    Guarda las credenciales de usuario en un archivo binario.
    """
    try:
        with open(USER_DATA_FILE, "wb") as file:
            pickle.dump({"username": username, "password": password}, file)
    except Exception as e:
        print(f"Error al guardar los datos de usuario: {e}")

def load_user_data():
    """
    Carga las credenciales de usuario desde un archivo binario.
    Devuelve un diccionario con 'username' y 'password', o None si el archivo está vacío/no existe.
    """
    if not os.path.exists(USER_DATA_FILE):
        return None
    try:
        with open(USER_DATA_FILE, "rb") as file:
            return pickle.load(file)
    except Exception as e:
        print(f"Error al cargar los datos de usuario: {e}")
        return None

def delete_user_data():
    """
    Elimina el archivo que contiene las credenciales de usuario.
    """
    try:
        if os.path.exists(USER_DATA_FILE):
            os.remove(USER_DATA_FILE)
    except Exception as e:
        print(f"Error al eliminar los datos de usuario: {e}")

def get_connection():
    """
    Establece y devuelve una conexión a la base de datos.
    """
    server = 'YOSHWA\\SQLEXPRESS' 
    database = 'TraitorTranslator'  
    username = 'jose'  
    password = '12345678'  

    try:
        connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password}"
        )
        connection = pyodbc.connect(connection_string)
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def validate_user(username, password):
    """
    Verifica si el usuario y contraseña son válidos en la base de datos.
    """
    connection = get_connection()
    if not connection:
        return False

    try:
        cursor = connection.cursor()
        query = "SELECT contrasenya FROM usuaris WHERE nom = ?"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        if result:
            database_password = result[0]
            database_password = decrypt_password(database_password, KEY_FILE_PATH)
            database_password = database_password.decode()
            return database_password == password
        return False
    except Exception as e:
        print(f"Error durante la validación del usuario: {e}")
        return False
    finally:
        connection.close()

def register_user(id, username, password, email):
    """
    Registra un nuevo usuario en la base de datos.
    """
    connection = get_connection()
    if not connection:
        return False

    try:
        encrypted_password = encrypt_password(password, KEY_FILE_PATH).decode('utf-8')
        cursor = connection.cursor()
        query = "INSERT INTO usuaris (id_usuari, nom, contrasenya, email) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (id, username, encrypted_password, email))
        connection.commit()
        return True
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return False
    finally:
        connection.close()