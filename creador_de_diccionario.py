import itertools
import time  # Importar la biblioteca para medir tiempo

# Configuración: caracteres y longitud
chars = "abc123456789"  # Caracteres a usar
min_length = 1     # Longitud mínima de las contraseñas
max_length = 6     # Longitud máxima de las contraseñas
output_file = "diccionario_generado.txt"  # Nombre del archivo de salida

# Inicio de la medición del tiempo
start_time = time.time()

# Crear el archivo de diccionario
with open(output_file, "w") as f:
    for length in range(min_length, max_length + 1):
        for combination in itertools.product(chars, repeat=length):
            # Escribir cada combinación en el archivo
            f.write("".join(combination) + "\n")

# Fin de la medición del tiempo
end_time = time.time()

# Calcular el tiempo transcurrido
elapsed_time = end_time - start_time
print(f"Diccionario generado con éxito en {output_file}")
print(f"Tiempo total: {elapsed_time:.2f} segundos")
