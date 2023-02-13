# List Comprehension
# https://www.w3schools.com/python/python_lists_comprehension.asp

print("Lista de numeros del 1 al 10 multiplicados por 2")
# Forma cotidiana
numbers = []
for element in range(1, 11):
  numbers.append(element * 2)

print(numbers)

# Usando List Comprehension
numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)

print("Lista de numeros pares del 1 al 10 multiplicados por 2")
# Forma cotidiana
numbers = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers.append(i * 2)

print(numbers)

# Usando List Comprehension
numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)

# Reto
# https://www.hackerrank.com/challenges/list-comprehensions/problem