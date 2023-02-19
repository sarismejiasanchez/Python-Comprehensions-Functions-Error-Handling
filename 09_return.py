# Parámetros por defecto y múltiples returns

# Definiendo valores por defecto para cada parametro de la funcion
def find_volume(length=1, width=1, depth=1):
  # Puedo retornar multiples valores separados por coma
  return length * width * depth, width, "Hola"

# Llamar la funcion enviando alguno de sus argumentos
result = find_volume(width=10)

# Llamar la funcion enviando todos sus argumentos
result = find_volume(10, 20, 30)

# Al retornar multiples valores, estos se almacenan en una tupla ()
# Imprimir la tupla completa
print(result)

# Pruedo almacenar cada valor de la tupla en una variable independiente
result, width, string = find_volume(10, 20, 30)
print(result)
print(width)
print(string)
