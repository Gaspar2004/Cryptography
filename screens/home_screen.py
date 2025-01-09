from tkinter import Button
from screens.salt_screen import SaltScreen
from screens.no_salt_screen import NoSaltScreen
from screens.encryption_options_screen import EncryptionOptionsScreen
from screens.decryption_options_screen import DeencryptionOptionsScreen

class HomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Home Screen")
        self.root.geometry("400x220")

        # Botón para opciones de encriptación
        btn_encrypt_options = Button(root, text="Encriptar", command=self.open_encryption_options, width=20, height=2)
        btn_encrypt_options.pack(pady=15)
        btn_encrypt_options = Button(root, text="Desencriptar", command=self.open_decryption_options, width=20, height=2)
        btn_encrypt_options.pack(pady=15)
        btn_encrypt_options = Button(root, text="Ataque de fuerza bruta", command=self.open_decryption_options, width=20, height=2)
        btn_encrypt_options.pack(pady=15)

    def open_encryption_options(self):
        EncryptionOptionsScreen(self.root)
    def open_decryption_options(self):
        DeencryptionOptionsScreen(self.root)

