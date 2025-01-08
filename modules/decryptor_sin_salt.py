import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
from getpass import getpass
from cryptography.fernet import InvalidToken

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
password = getpass("Introduce la contraseña para desencriptar los archivos: ")
key = derive_key_from_password(password)

# Ignorar ciertos archivos
ignored_files= {"Encriptador_sin_salt.py", "Desencriptador_sin_salt.py","creador_de_diccionario.py","diccionario_generado.txt","Fuerza_Bruta.py","Desencriptador.py","Encriptador.py"}
#Lista de todos los archivos, es útil si queda encriptado algo por accidente
all_files={"Desencriptador_sin_salt.py","creador_de_diccionario.py","diccionario_generado.txt","Desencriptador.py","elperro.txt","Encriptador_sin_salt.py","Encriptador.py","Fuerza_Bruta.py","thekey.key"}
# Lista de archivos para desencriptar
files = []
for file in os.listdir():
    if file in ignored_files:
        continue
    if os.path.isfile(file):
        files.append(file)

# Desencriptar archivos
for file in files:
    try:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(key).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    except InvalidToken:
        print(f"Contraseña incorrecta. No se pudo desencriptar el archivo: {file}")
        break
else:
    print("Archivos desencriptados con éxito.")
