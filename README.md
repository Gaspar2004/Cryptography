# Proyecto de Encriptador y Desencriptador

## Descripción
Este proyecto consiste en dos scripts de Python que permiten encriptar y desencriptar archivos utilizando una contraseña personalizada. La encriptación se realiza con el algoritmo de cifrado simétrico **Fernet**, proporcionado por la biblioteca `cryptography`. Además, los scripts garantizan la seguridad al derivar la clave de cifrado de una contraseña introducida por el usuario y un `salt` único.

### Scripts Incluidos
1. **Encriptador.py**: Encripta todos los archivos en el directorio excepto el propio script, el archivo de clave y el script del desencriptador.
2. **Desencriptador.py**: Desencripta los archivos previamente encriptados usando la contraseña proporcionada por el usuario.

---

## Requisitos
### Dependencias
Asegúrate de tener instaladas las siguientes dependencias antes de ejecutar los scripts:

- Python 3.6 o superior
- Biblioteca `cryptography`

Puedes instalar la dependencia usando el siguiente comando:

```bash
pip install cryptography
```

---

## Uso

### Encriptador
#### Propósito
El script **Encriptador.py** encripta todos los archivos del directorio actual, incluyendo el propio script, utilizando una contraseña proporcionada por el usuario.

#### Ejecución
1. Coloca el archivo `Encriptador.py` en el directorio donde se encuentran los archivos que deseas encriptar.
2. Ejecuta el script:

   ```bash
   python Encriptador.py
   ```

3. Introduce una contraseña cuando se te solicite. Esta contraseña se usará para derivar la clave de encriptación.
4. El script generará un archivo `thekey.key` que contiene el `salt` necesario para derivar la clave.
5. Todos los archivos en el directorio serán encriptados, incluyendo el script mismo.

---

### Desencriptador
#### Propósito
El script **Desencriptador.py** desencripta los archivos previamente encriptados, utilizando la misma contraseña que se empleó durante la encriptación.

#### Ejecución
1. Coloca el archivo `Desencriptador.py` en el mismo directorio donde se encuentran los archivos encriptados.
2. Asegúrate de que el archivo `thekey.key` esté presente en el directorio.
3. Ejecuta el script:

   ```bash
   python Desencriptador.py
   ```

4. Introduce la contraseña utilizada durante la encriptación.
5. Los archivos serán desencriptados y restaurados a su estado original.

---

## Detalles Técnicos

### Encriptación
- El script utiliza el algoritmo **Fernet** de la biblioteca `cryptography`.
- La clave de encriptación se deriva a partir de la contraseña del usuario mediante el algoritmo **PBKDF2** con los siguientes parámetros:
  - Algoritmo hash: SHA-256
  - Longitud de clave: 32 bytes
  - Iteraciones: 100,000
  - Salt: 16 bytes generado aleatoriamente

### Seguridad
- El `salt` se almacena en el archivo `thekey.key`, lo que permite derivar la clave de encriptación/desencriptación en el futuro.
- La contraseña nunca se almacena directamente; solo se utiliza para derivar la clave.

---

## Precauciones
- **Respalda tus archivos**: Antes de usar el script, realiza una copia de seguridad de los archivos, ya que la pérdida de la contraseña o el archivo `thekey.key` hará que los datos sean irrecuperables.
- **Mantén segura la clave**: El archivo `thekey.key` y la contraseña son necesarios para desencriptar los archivos. No los compartas ni los pierdas.
- **Evita interrupciones**: Asegúrate de que el proceso de encriptación/desencriptación no sea interrumpido para evitar corrupciones en los archivos.

---

## Estructura del Proyecto
```
├── Encriptador.py
├── Desencriptador.py
├── thekey.key (se genera después de ejecutar el Encriptador.py)
├── README.md
└── Archivos a encriptar
```

---

## Ejemplo de Ejecución
### Encriptador
```
$ python Encriptador.py
Introduce una contraseña para encriptar los archivos: ********
Archivos encriptados con éxito.
```

### Desencriptador
```
$ python Desencriptador.py
Introduce la contraseña para desencriptar los archivos: ********
Archivos desencriptados con éxito.
```

---

## Posibles Errores y Soluciones

1. **Error: Archivo `thekey.key` no encontrado**
   - Asegúrate de que el archivo `thekey.key` esté en el mismo directorio que los archivos encriptados.

2. **Error: Contraseña incorrecta**
   - Introduce la misma contraseña que usaste para encriptar los archivos. Si la contraseña es incorrecta, la desencriptación fallará.

3. **Error: Archivos corruptos después de interrupción**
   - Asegúrate de no interrumpir la ejecución del script para evitar corrupciones. Respalda los archivos antes de ejecutar los scripts.

---

## Licencia
Este proyecto se distribuye bajo la Licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente, siempre que se otorgue crédito al autor original.

