import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def derive_key_from_password(password: str, salt: bytes) -> bytes:
    """
    Deriva una clave de 32 bytes a partir de una contraseña y un salt usando PBKDF2 con SHA-256.

    Args:
        password (str): La contraseña proporcionada por el usuario.
        salt (bytes): El salt utilizado para la derivación de la clave.

    Returns:
        bytes: La clave derivada codificada en base64.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Longitud de la clave en bytes
        salt=salt,
        iterations=100000,  # Iteraciones para aumentar la seguridad
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))
