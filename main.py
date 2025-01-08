import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from modules.encryptor import encrypt_folder
from modules.decryptor import decrypt_folder
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from modules.encryptor import encrypt_folder
from modules.decryptor import decrypt_folder

def pedir_contraseña():
    """Muestra un cuadro de diálogo para que el usuario ingrese una contraseña."""
    return simpledialog.askstring(
        "Contraseña", "Introduce la contraseña:", show="*"
    )

def seleccionar_encriptar():
    folder_path = filedialog.askdirectory(title="Selecciona la carpeta a encriptar")
    if folder_path:
        password = pedir_contraseña()
        if password:
            try:
                mensaje = encrypt_folder(folder_path, password)
                messagebox.showinfo("Éxito", mensaje)
            except Exception as e:
                messagebox.showwarning("Error", f"Error al encriptar: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "No se ingresó una contraseña.")

def seleccionar_desencriptar():
    folder_path = filedialog.askdirectory(title="Selecciona la carpeta a desencriptar")
    if folder_path:
        password = pedir_contraseña()
        if password:
            try:
                mensaje = decrypt_folder(folder_path, password)
                messagebox.showinfo("Éxito", mensaje)
            except Exception as e:
                messagebox.showwarning("Error", f"Error al desencriptar: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "No se ingresó una contraseña.")

# Configurar la ventana principal
def main():
    root = tk.Tk()
    root.title("Encriptador y Desencriptador")
    root.geometry("400x200")

    # Botones para encriptar y desencriptar
    btn_encrypt = tk.Button(root, text="Encriptar Carpeta", command=seleccionar_encriptar, width=20, height=2)
    btn_encrypt.pack(pady=20)

    btn_decrypt = tk.Button(root, text="Desencriptar Carpeta", command=seleccionar_desencriptar, width=20, height=2)
    btn_decrypt.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
