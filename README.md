# Proyecto de Encriptador y Desencriptador

## Descripción
Este proyecto es una aplicación gráfica para encriptar y desencriptar archivos utilizando el algoritmo Fernet de la biblioteca Cryptography. También incluye una funcionalidad de ataque de fuerza bruta para intentar descifrar archivos encriptados sin conocer la contraseña.

La aplicación cuenta con una interfaz gráfica de usuario (GUI) desarrollada con Tkinter, permitiendo al usuario interactuar de manera sencilla para realizar las siguientes operaciones:

Encriptar todo el contenido de una carpeta.
Desencriptar todo el contenido de una carpeta.
Realizar un ataque de fuerza bruta para descifrar archivos encriptados utilizando un diccionario de contraseñas.

### Scripts Incluidos
1. **Encriptador.py**: Encripta todos los archivos en el directorio excepto el propio script, el archivo de clave y el script del desencriptador.
2. **Desencriptador.py**: Desencripta los archivos previamente encriptados usando la contraseña proporcionada por el usuario.

---

## Requisitos
### Dependencias
Asegúrate de tener instaladas las siguientes dependencias antes de ejecutar los scripts:

- Python 3.6 o superior
- Biblioteca `cryptography`
- tkinter (viene con Python por defecto)


Puedes instalar la dependencia usando el siguiente comando:

```bash
pip install cryptography
```

---
## Características Principales

# 1. Encriptar Carpeta
Esta funcionalidad permite encriptar todo el contenido de una carpeta seleccionada. Los archivos encriptados se sobrescriben en su ubicación original.

Interfaz:

Botón para seleccionar la carpeta a encriptar.
Solicitud de contraseña mediante un cuadro de diálogo gráfico.
Mensajes de éxito o error.
Implementación:

Algoritmo: Fernet.
Derivación de clave mediante PBKDF2 con SHA-256 (con salt).

# 2. Desencriptar Carpeta
Esta funcionalidad permite desencriptar todo el contenido de una carpeta seleccionada. Los archivos desencriptados se sobrescriben en su ubicación original.

Interfaz:

Botón para seleccionar la carpeta a desencriptar.
Solicitud de contraseña mediante un cuadro de diálogo gráfico.
Mensajes de éxito o error.
Implementación:

Algoritmo: Fernet.
Derivación de clave mediante PBKDF2 con SHA-256 (con salt).

# 3. Ataque de Fuerza Bruta
Permite intentar descifrar un archivo encriptado probando contraseñas desde un diccionario.

Interfaz:

Selección del archivo encriptado.
Selección del archivo de diccionario.
Botón para iniciar el ataque.
Mensajes informativos sobre el resultado del ataque.
Implementación:

Derivación de clave mediante PBKDF2 con SHA-256 (sin salt en este caso).
Gestión de errores cuando la contraseña es incorrecta.

## Cómo Usar la Aplicación
#Paso 1: Ejecución
Ejecuta el archivo principal:

```bash
python main.py
```
# Paso 2: Pantalla Principal
Desde la pantalla principal puedes:

Seleccionar "Encriptar Carpeta" para encriptar todos los archivos de una carpeta.
Seleccionar "Desencriptar Carpeta" para desencriptar todos los archivos de una carpeta.
Seleccionar "Ataque Fuerza Bruta" para intentar descifrar un archivo encriptado.

# Paso 3: Opciones de Encriptar/Desencriptar
Selecciona la carpeta que deseas encriptar/desencriptar.
Introduce una contraseña cuando se solicite.
Espera a que el proceso termine. Se mostrará un mensaje indicando el resultado.

# Paso 4: Ataque de Fuerza Bruta
Selecciona el archivo encriptado que deseas descifrar.
Selecciona el archivo de diccionario con las posibles contraseñas.
Inicia el ataque.
Si se encuentra una contraseña válida, se mostrará en pantalla.
