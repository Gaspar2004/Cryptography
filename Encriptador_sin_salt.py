import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
from getpass import getpass

def derive_key_from_password(password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"",
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Solicitar contraseña
password = getpass("Introduce una contraseña para encriptar los archivos: ")
key = derive_key_from_password(password)

# Ignorar ciertos archivos
script_name = os.path.basename(__file__)
ignored_files = {"Encriptador_sin_salt.py", "Desencriptador_sin_salt.py","creador_de_diccionario.py","diccionario_generado.txt","Fuerza_Bruta.py","Desencriptador.py","Encriptador.py"}

# Lista de archivos para encriptar
files = []
for file in os.listdir():
    if file in ignored_files:
        continue
    if os.path.isfile(file):
        files.append(file)

# Encriptar archivos
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
"""
# Encriptar el propio script
with open(script_name, "rb") as lastfile:
    contents = lastfile.read()
lastfile_encrypted = Fernet(key).encrypt(contents)
with open(script_name, "wb") as lastfile:
    lastfile.write(lastfile_encrypted)
"""
print("Archivos encriptados con éxito.")
