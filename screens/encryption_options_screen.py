from tkinter import Toplevel, Button, Label, Radiobutton, IntVar, filedialog, messagebox, simpledialog
from modules.encryptor import encrypt_folder
from modules.encryptor_sin_salt import encrypt_files_without_salt

class EncryptionOptionsScreen:
    def __init__(self, parent):
        self.root = Toplevel(parent)
        self.root.title("Opciones de Encriptación")
        self.root.geometry("400x400")

        # Variables para las opciones
        self.include_subfolders = IntVar(value=0)
        self.use_salt = IntVar(value=1)  # Por defecto, usar salt

        # Título
        Label(self.root, text="¿Incluir subcarpetas?").pack(pady=10)

        # Opciones referente a si se decide encriptar todas las subcarpetas
        Radiobutton(self.root, text="Sí, incluir subcarpetas", variable=self.include_subfolders, value=1).pack()
        Radiobutton(self.root, text="No, solo archivos en el directorio", variable=self.include_subfolders, value=0).pack()

        # Título para usar salt o no
        Label(self.root, text="¿Usar salt?").pack(pady=10)

        # Opciones referentes a si se quiere usar salt o no
        Radiobutton(self.root, text="Sí, usar salt", variable=self.use_salt, value=1).pack()
        Radiobutton(self.root, text="No, no usar salt", variable=self.use_salt, value=0).pack()

        # Botón para seleccionar carpeta
        Button(self.root, text="Seleccionar carpeta y Encriptar", command=self.encrypt).pack(pady=20)

    def encrypt(self):
        folder_path = filedialog.askdirectory(title="Selecciona la carpeta a encriptar")
        if folder_path:
            # Solicitar la contraseña al usuario
            password = simpledialog.askstring("Contraseña", "Introduce una contraseña para encriptar:", show="*")
            if password:
                include_subfolders = self.include_subfolders.get() == 1
                use_salt = self.use_salt.get() == 1

                # Elegir la función según la opción de usar salt o no
                #if use_salt:
                message = encrypt_folder(folder_path, password, include_subfolders)
                #else:
                #    message = encrypt_folder_no_salt(folder_path, password, include_subfolders)

                # Mostrar el resultado al usuario
                messagebox.showinfo("Resultado", message)
