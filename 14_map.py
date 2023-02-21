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

# Playgroud: Multiplica todos los elementos por dos
'''
Para resolver este desafío, tu reto es utilizar la función map de Python y una función lambda para transformar una lista de números. Debes retornar una lista en la que cada número de la lista original sea multiplicado por dos.

La función multiply_numbers recibirá como entrada una lista con números. Finalmente, la función retornará la lista transformada.

Ejemplo 1:

Input: [2, 4, 5, 6, 8]
Output: [4, 8, 10, 12, 16]

Ejemplo 2:

Input: [1, 1, -2, -3]
Output: [1, 1, -4, -6]
'''

def multiply_numbers(numbers):
  # Escribe tu solución 👇
  result = list(map(lambda x: x * 2, numbers))
  return result
  
numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print("*" * 10)
print(response)