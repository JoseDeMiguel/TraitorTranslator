from cryptography.fernet import Fernet
import os

def create_key(path):   
    if not os.path.exists(path):
        with open(path, "wb") as key_file:
            key = Fernet.generate_key()
            key_file.write(key)
        
        
def load_key(path):
    with open(path, "rb") as key_file:
        return key_file.read()
    
    
def encrypt_password(password, key_path):
    key = load_key(key_path)  # Asegúrate de que este método existe y funciona
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())  # Esto devuelve bytes
    return encrypted_password


def decrypt_password(encrypted_password, path):
    key = load_key(path)
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password)
    
    return decrypted_password



