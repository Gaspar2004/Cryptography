import os
from cryptography.fernet import Fernet
from utils import derive_key_from_password

def encrypt_folder(folder_path, password):
    """Encripta todos los archivos en una carpeta."""
    # Generar un salt y guardarlo
    salt = os.urandom(16)
    salt_file_path = os.path.join(folder_path, "salt.key")
    with open(salt_file_path, "wb") as salt_file:
        salt_file.write(salt)

    # Derivar la clave
    key = derive_key_from_password(password, salt)

    # Obtener archivos en la carpeta
    files = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, file)) and file != "salt.key"
    ]

    # Encriptar archivos
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
        print(f"Archivo encriptado: {file}")

    return "Encriptación completada."
