import os
from cryptography.fernet import Fernet
from utils.derive_key import derive_key_from_password

def encrypt_folder(folder_path, password, include_subfolders=False):
    """Encripta los archivos en un directorio, con opción de incluir subcarpetas."""
    salt = os.urandom(16)
    salt_file_path = os.path.join(folder_path, "salt.key")
    with open(salt_file_path, "wb") as salt_file:
        salt_file.write(salt)

    key = derive_key_from_password(password, salt)

    # Obtener archivos para encriptar
    files = []
    if include_subfolders:
        for root, _, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                if "salt.key" not in file_path:  # Ignorar el archivo salt.key
                    files.append(file_path)
    else:
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path) and "salt.key" not in file:
                files.append(file_path)

    # Encriptar archivos
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)

    return "Encriptación completada."
