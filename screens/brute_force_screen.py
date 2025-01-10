import os
from tkinter import Toplevel, Button, Label, filedialog, messagebox, simpledialog
from modules.brute_force_attack import brute_force_attack

class BruteForceScreen:
    def __init__(self, parent):
        self.root = Toplevel(parent)
        self.root.title("Ataque de Fuerza Bruta")
        self.root.geometry("500x300")

        # Variables para guardar las rutas de los archivos
        self.encrypted_file = None
        self.dictionary_file = None

        # Etiquetas para mostrar las rutas seleccionadas
        self.encrypted_label = Label(self.root, text="Archivo encriptado: No seleccionado", wraplength=400)
        self.encrypted_label.pack(pady=10)

        self.dictionary_label = Label(self.root, text="Diccionario: No seleccionado", wraplength=400)
        self.dictionary_label.pack(pady=10)

        # Botón para seleccionar archivo encriptado
        btn_select_encrypted = Button(self.root, text="Seleccionar Archivo Encriptado", command=self.select_encrypted_file)
        btn_select_encrypted.pack(pady=5)

        # Botón para seleccionar diccionario
        btn_select_dictionary = Button(self.root, text="Seleccionar Diccionario", command=self.select_dictionary_file)
        btn_select_dictionary.pack(pady=5)

        # Botón para iniciar ataque de fuerza bruta
        btn_start_attack = Button(self.root, text="Iniciar Ataque", command=self.start_attack)
        btn_start_attack.pack(pady=20)

    def select_encrypted_file(self):
        """Permite al usuario seleccionar el archivo encriptado."""
        self.encrypted_file = filedialog.askopenfilename(title="Selecciona el archivo encriptado")
        if self.encrypted_file:
            self.encrypted_label.config(text=f"Archivo encriptado: {self.encrypted_file}")

    def select_dictionary_file(self):
        """Permite al usuario seleccionar el archivo de diccionario."""
        self.dictionary_file = filedialog.askopenfilename(title="Selecciona el archivo de diccionario")
        if self.dictionary_file:
            self.dictionary_label.config(text=f"Diccionario: {self.dictionary_file}")

    def start_attack(self):
        """Inicia el ataque de fuerza bruta."""
        if not self.encrypted_file or not self.dictionary_file:
            messagebox.showwarning("Advertencia", "Por favor, selecciona el archivo encriptado y el diccionario.")
            return

        # Confirmar inicio del ataque
        confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de iniciar el ataque de fuerza bruta?")
        if not confirm:
            return

        # Ejecutar ataque
        result = brute_force_attack(self.encrypted_file, self.dictionary_file)
        if result:
            messagebox.showinfo("Éxito", f"Contraseña encontrada: {result}")
        else:
            messagebox.showerror("Error", "No se encontró ninguna contraseña válida en el diccionario.")
