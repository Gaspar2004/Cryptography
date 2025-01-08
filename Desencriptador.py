import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
from getpass import getpass

# Función para derivar la clave a partir de una contraseña
def derive_key_from_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Solicitar contraseña al usuario
password = getpass("Introduce la contraseña para desencriptar los archivos: ")

# Leer el salt desde el archivo
with open("thekey.key", "rb") as thekey:
    salt = thekey.read()

# Derivar la clave a partir de la contraseña
key = derive_key_from_password(password, salt)

# Lista de archivos a desencriptar
files = []
for file in os.listdir():
    if file in ("thekey.key", "Desencriptador.py","creador_de_diccionario.py","diccionario_generado.txt"):
        continue
    if os.path.isfile(file):
        files.append(file)

# Desencriptar los archivos
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)

print("Archivos desencriptados con éxito.")
