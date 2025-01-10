import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
from cryptography.fernet import InvalidToken

def derive_key_from_password(password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"",  # Sin salt
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def brute_force_attack(encrypted_file, dictionary_file):
    if not os.path.exists(encrypted_file):
        return None

    with open(encrypted_file, "rb") as file:
        encrypted_contents = file.read()

    with open(dictionary_file, "r") as dict_file:
        for password in dict_file:
            password = password.strip()
            key = derive_key_from_password(password)
            fernet = Fernet(key)
            try:
                fernet.decrypt(encrypted_contents)
                return password
            except InvalidToken:
                continue

    return None
