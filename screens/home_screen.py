from tkinter import Button
from screens.encryption_options_screen import EncryptionOptionsScreen
from screens.decryption_options_screen import DeencryptionOptionsScreen
from screens.brute_force_screen import BruteForceScreen

class HomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Encriptador y Desencriptador")
        self.root.geometry("400x300")

        # Botón para encriptar/desencriptar con salt
        btn_salt = Button(root, text="Encriptar", command=self.OpenEncryptionOptionsScreen, width=20, height=2)
        btn_salt.pack(pady=10)

        # Botón para encriptar/desencriptar sin salt
        btn_no_salt = Button(root, text="Desencriptar", command=self.OpendDecryptionOptionsScreen, width=20, height=2)
        btn_no_salt.pack(pady=10)

        # Botón para ataque de fuerza bruta
        btn_brute_force = Button(root, text="Ataque Fuerza Bruta", command=self.open_brute_force_screen, width=20, height=2)
        btn_brute_force.pack(pady=10)

    def OpenEncryptionOptionsScreen(self):
        EncryptionOptionsScreen(self.root)

    def OpendDecryptionOptionsScreen(self):
        DeencryptionOptionsScreen(self.root)

    def open_brute_force_screen(self):
        BruteForceScreen(self.root)
