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
password = getpass("Introduce una contraseña para encriptar los archivos: ")

# Generar un salt único
salt = os.urandom(16)

# Derivar la clave a partir de la contraseña
key = derive_key_from_password(password, salt)

# Guardar el salt para usarlo al desencriptar
with open("thekey.key", "wb") as thekey:
    thekey.write(salt)

# Lista de archivos a encriptar
script_name = os.path.basename(__file__)
files = []
for file in os.listdir():
    if file in ("Encriptador.py", "thekey.key", "Desencriptador.py", script_name):
        continue
    if os.path.isfile(file):
        files.append(file)

# Encriptar los archivos
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

# Encriptar el propio script
with open(script_name, "rb") as lastfile:
    contents = lastfile.read()
lastfile_encrypted = Fernet(key).encrypt(contents)
with open(script_name, "wb") as lastfile:
    lastfile.write(lastfile_encrypted)

print("Archivos encriptados con éxito.")
