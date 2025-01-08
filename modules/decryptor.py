import os
from cryptography.fernet import Fernet
from utils import derive_key_from_password
from cryptography.fernet import InvalidToken

def decrypt_folder(folder_path, password):
    """Desencripta todos los archivos en una carpeta."""
    # Verificar que el archivo salt.key existe
    salt_file_path = os.path.join(folder_path, "salt.key")
    if not os.path.isfile(salt_file_path):
        return "Error: No se encontró el archivo salt.key."

    # Leer el salt
    with open(salt_file_path, "rb") as salt_file:
        salt = salt_file.read()

    # Derivar la clave
    key = derive_key_from_password(password, salt)

    # Obtener archivos en la carpeta
    files = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, file)) and file != "salt.key"
    ]

    # Desencriptar archivos
    for file in files:
        try:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(key).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
            print(f"Archivo desencriptado: {file}")
        except InvalidToken:
            return f"Error: Contraseña incorrecta para el archivo {file}."

    return "Desencriptación completada."



