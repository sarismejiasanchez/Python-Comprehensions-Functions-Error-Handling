# Módulos
# https://www.w3schools.com/python/python_modules.asp
# https://platzi.com/cursos/expresiones-regulares/

# Para preguntar por el sistema operativo
import sys
# Muestra en donde estoy ejecutando el archivo
print(sys.path)

# Expresiones Regulares
import re

texto = "Mi numero de telefono es 3001112233, el codigo del pais es 57, mi numero de la suerte es el 12"
# Obtener solo los string que coincidan con lo que es un numero
result = re.findall('[0-9]+', texto)
print(result)

# Manejo de Fecha y Horas
import time

timestamp = time.time()
print(timestamp) # Formato unix

local = time.localtime()
result = time.asctime(local)
print(result)

# Utilidad para manejar listas
import collections

numbers = [1, 1, 2, 3, 4, 3, 5, 1, 5, 4]

# Frecuencia de un numero en la lista
counter = collections.Counter(numbers)
print(counter)
