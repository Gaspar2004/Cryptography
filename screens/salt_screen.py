from tkinter import Toplevel, Button, filedialog, messagebox, simpledialog
from modules.encryptor import encrypt_folder
from modules.decryptor import decrypt_folder

class SaltScreen:
    def __init__(self, parent):
        self.root = Toplevel(parent)
        self.root.title("Encriptador con Salt")
        self.root.geometry("400x200")

        # Botón para encriptar carpeta
        btn_encrypt = Button(self.root, text="Encriptar Carpeta", command=self.encriptar, width=20, height=2)
        btn_encrypt.pack(pady=20)

        # Botón para desencriptar carpeta
        btn_decrypt = Button(self.root, text="Desencriptar Carpeta", command=self.desencriptar, width=20, height=2)
        btn_decrypt.pack(pady=20)

    def pedir_contraseña(self):
        return simpledialog.askstring("Contraseña", "Introduce la contraseña:", show="*")

    def encriptar(self):
        folder_path = filedialog.askdirectory(title="Selecciona la carpeta a encriptar")
        if folder_path:
            password = self.pedir_contraseña()
            if password:
                mensaje = encrypt_folder(folder_path, password)
                messagebox.showinfo("Éxito", mensaje)

    def desencriptar(self):
        folder_path = filedialog.askdirectory(title="Selecciona la carpeta a desencriptar")
        if folder_path:
            password = self.pedir_contraseña()
            if password:
                mensaje = decrypt_folder(folder_path, password)
                messagebox.showinfo("Éxito", mensaje)
