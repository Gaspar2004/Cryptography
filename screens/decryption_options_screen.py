from tkinter import Toplevel, Button, Label, Radiobutton, IntVar, filedialog, messagebox, simpledialog
from modules.encryptor import encrypt_folder
from modules.encryptor_sin_salt import encrypt_files_without_salt
from modules.decryptor import decrypt_folder

class DeencryptionOptionsScreen:
    def __init__(self, parent):
        self.root = Toplevel(parent)
        self.root.title("Desencriptar")
        self.root.geometry("400x400")

        # Título
        Label(self.root, text="¿Incluir subcarpetas?").pack(pady=10)
        self.include_subfolders = IntVar(value=0)
        # Opciones referente a si se decide encriptar todas las subcarpetas
        Radiobutton(self.root, text="Sí, incluir subcarpetas", variable=self.include_subfolders, value=1).pack()
        Radiobutton(self.root, text="No, solo archivos en el directorio", variable=self.include_subfolders, value=0).pack()

        # Botón para seleccionar carpeta
        Button(self.root, text="Seleccionar carpeta y Encriptar", command=self.decrypt).pack(pady=20)

    def decrypt(self):
        folder_path = filedialog.askdirectory(title="Selecciona la carpeta a desencriptar")  # Cambiar mensaje
        if folder_path:
            # Solicitar la contraseña al usuario
            password = simpledialog.askstring("Contraseña", "Introduce una contraseña para desencriptar:", show="*")
            if password:
                include_subfolders = self.include_subfolders.get() == 1
                # Llamar a la función decrypt_folder con los argumentos correctos
                message = decrypt_folder(folder_path, password, include_subfolders)

                # Mostrar el resultado al usuario
                messagebox.showinfo("Resultado", message)


