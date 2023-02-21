# Filter
# https://www.w3schools.com/python/ref_func_filter.asp

numbers = [1, 2, 3, 4, 5]

# Solo los elementos que cumplen con la condicion del filter, van a ser parte de la nueva lista
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)

# Filter no modifica la lista original, simplemente crea una nueva lista.
print(numbers)

# Playground: Retorna solo palabras de 4 letras y más
'''
Para resolver este desafío, tu reto es usar la función filter de Python y una función lambda para filtrar una lista de palabras, retornando una lista solo con las que cumplan con la condición de tener 4 o más letras.

La función filter_by_length recibirá como entrada una lista con palabras. Finalmente, la función retornará la lista filtrada.

Ejemplo 1:

Input: ['amor', 'sol', 'piedra', 'día']
Output: [ 'amor', 'piedra' ]

Ejemplo 2:

Input: ['rosa', 'gol', 'pez', 'día', 'gafas']
Output: [ 'rosa', 'gafas' ]
'''
def filter_by_length(words):
  # Escribe tu solución 👇
  new_words = list(filter(lambda x: len(x) >= 4, words))
  return new_words

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)

words = ['rosa', 'gol', 'pez', 'día', 'gafas']
response = filter_by_length(words)
print(response)