# Map
# https://www.w3schools.com/python/ref_func_map.asp

'''
Vamos a utilizar los conceptos de Higher Order Function y Lambda Functions en funciones directamente construidas por Python.
Una de esas muy importante es la funcion Map:
Su funcion principal es hacer transformaciones a una lista dada de elementos, retornando siempre el mismo numero de elementos de la lista original.
'''

numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers:
  numbers_v2.append(i * 2)

# Usando Map
numbers_v3 = list(map(lambda i: i * 2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

# Iterando y transformando dos listas de diferentes dimensiones con map
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

# Retorna una lista con la dimension de la lista mas pequeña
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(numbers_1)
print(numbers_2)
print(result)