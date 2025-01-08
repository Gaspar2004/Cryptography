import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
from getpass import getpass

# Función para derivar clave de la contraseña con salt
def derive_key_from_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Función para encriptar los archivos en una carpeta
def encriptar_carpeta():
    # Solicitar la ruta de la carpeta al usuario
    ruta_carpeta = input("Introduce la ruta de la carpeta a encriptar: ")
    
    # Verificar si la carpeta existe
    if not os.path.isdir(ruta_carpeta):
        print("La ruta proporcionada no es una carpeta válida.")
        return

    # Generar un salt aleatorio
    salt = os.urandom(16)

    # Guardar el salt en un archivo dentro de la carpeta
    salt_file_path = os.path.join(ruta_carpeta, "salt.key")
    with open(salt_file_path, "wb") as salt_file:
        salt_file.write(salt)

    print(f"Salt generado y guardado en: {salt_file_path}")

    # Solicitar contraseña al usuario
    password = getpass("Introduce una contraseña para encriptar los archivos: ")
    key = derive_key_from_password(password, salt)

    # Obtener lista de archivos en la carpeta
    files = []
    for file in os.listdir(ruta_carpeta):
        file_path = os.path.join(ruta_carpeta, file)
        if os.path.isfile(file_path) and file != "salt.key":
            files.append(file_path)

    # Encriptar los archivos
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
        print(f"Archivo encriptado: {file}")

    print("Todos los archivos en la carpeta han sido encriptados con éxito.")

# Llamar a la función
if __name__ == "__main__":
    encriptar_carpeta()
