import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

def derive_key_from_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def decrypt_folder(folder_path, password, include_subfolders):
    """Desencripta los archivos de una carpeta, con opción de incluir subcarpetas."""
    # Verificar si existe el archivo thekey.key
    salt_path = os.path.join(folder_path, "salt.key")
    if not os.path.exists(salt_path):
        return "Error: No se encontró el archivo 'salt.key'."

    # Leer el salt
    with open(salt_path, "rb") as salt_file:
        salt = salt_file.read()

    # Derivar la clave
    key = derive_key_from_password(password, salt)

    # Obtener archivos para desencriptar
    files = []
    if include_subfolders:
        for root, _, filenames in os.walk(folder_path):
            for filename in filenames:
                if filename != "salt.key":
                    files.append(os.path.join(root, filename))
    else:
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path) and file != "salt.key":
                files.append(file_path)

    # Desencriptar archivos
    failed_files = []
    for file in files:
        try:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(key).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
        except Exception:
            failed_files.append(file)

    if failed_files:
        return f"Error al desencriptar los siguientes archivos: {', '.join(failed_files)}"
    return "Desencriptación completada con éxito."
