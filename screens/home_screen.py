from tkinter import Button
from screens.salt_screen import SaltScreen
from screens.no_salt_screen import NoSaltScreen

class HomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Encriptador y Desencriptador")
        self.root.geometry("400x200")

        # Botón para encriptar/desencriptar con salt
        btn_salt = Button(root, text="Con Salt", command=self.open_salt_screen, width=20, height=2)
        btn_salt.pack(pady=20)

        # Botón para encriptar/desencriptar sin salt
        btn_no_salt = Button(root, text="Sin Salt", command=self.open_no_salt_screen, width=20, height=2)
        btn_no_salt.pack(pady=20)

    def open_salt_screen(self):
        # Llamar a la pantalla para encriptar/desencriptar con salt
        SaltScreen(self.root)

    def open_no_salt_screen(self):
        # Llamar a la pantalla para encriptar/desencriptar sin salt
        NoSaltScreen(self.root)
