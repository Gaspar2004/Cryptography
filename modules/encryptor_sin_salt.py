import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
from tkinter import simpledialog, messagebox

def derive_key_from_password(password):
    """
    Deriva una clave de 32 bytes a partir de una contraseña.
    En esta versión no se usa un salt.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"",  # No usar salt en esta versión
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_files_without_salt():
    """
    Encripta todos los archivos en el directorio actual, excluyendo ciertos archivos.
    """
    # Solicitar contraseña mediante interfaz gráfica
    password = simpledialog.askstring("Contraseña", "Introduce una contraseña para encriptar los archivos:", show="*")
    if not password:
        messagebox.showwarning("Advertencia", "No se proporcionó una contraseña. Operación cancelada.")
        return

    key = derive_key_from_password(password)

    # Ignorar ciertos archivos
    script_name = os.path.basename(__file__)
    ignored_files = {
        script_name,
        "Encriptador_sin_salt.py",
        "Desencriptador_sin_salt.py",
        "creador_de_diccionario.py",
        "diccionario_generado.txt",
        "Fuerza_Bruta.py",
        "Desencriptador.py",
        "Encriptador.py",
    }

    # Obtener lista de archivos para encriptar
    files = []
    for file in os.listdir():
        if file in ignored_files or not os.path.isfile(file):
            continue
        files.append(file)

    # Encriptar archivos
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)

    messagebox.showinfo("Éxito", "Archivos encriptados con éxito.")
