from tkinter import Tk
from screens.home_screen import HomeScreen

def main():
    root = Tk()  # Crear la ventana principal
    HomeScreen(root)  # Inicializar la pantalla inicial
    root.mainloop()  # Ejecutar el bucle principal de Tkinter

if __name__ == "__main__":
    main()
