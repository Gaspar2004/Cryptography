import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
from cryptography.fernet import InvalidToken
import time

# Función para derivar clave de la contraseña
def derive_key_from_password(password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"",  # Sin salt
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Ruta al archivo a desencriptar
encrypted_file = "elperro.txt"  # Reemplaza con el archivo que deseas atacar
dictionary_file = "diccionario_generado.txt"  # Archivo con posibles contraseñas, una por línea
ignored_files=
start_time = time.time()
# Verificar que el archivo cifrado existe
if not os.path.exists(encrypted_file):
    print(f"El archivo {encrypted_file} no existe.")
    exit()

# Verificar que el diccionario existe
if not os.path.exists(dictionary_file):
    print(f"El archivo {dictionary_file} no existe.")
    exit()

# Leer el contenido cifrado
with open(encrypted_file, "rb") as file:
    encrypted_content = file.read()

# Leer las posibles contraseñas desde el archivo de diccionario
with open(dictionary_file, "r") as file:
    passwords = file.read().splitlines()
start_time = time.time()
# Realizar el ataque de fuerza bruta
for password in passwords:
    try:
        key = derive_key_from_password(password)  # Derivar clave con la contraseña actual
        fernet = Fernet(key)
        decrypted_content = fernet.decrypt(encrypted_content)  # Intentar desencriptar
        print(f"¡Contraseña encontrada!: {password}")
        print("Contenido desencriptado:\n", decrypted_content.decode())
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Tiempo total: {elapsed_time:.2f} segundos")
        break
    except InvalidToken:
        # La contraseña no es válida, continuar con la siguiente
        print(f"Contraseña incorrecta: {password}")
        continue
else:
    print("No se encontró una contraseña válida.")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo total: {elapsed_time:.2f} segundos")
