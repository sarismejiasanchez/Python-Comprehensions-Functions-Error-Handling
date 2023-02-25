# Iterables
# https://www.w3schools.com/python/python_iterators.asp

for i in range(1, 11):
  print(i)

my_iterable = iter(range(1, 4))
print(my_iterable)
# Iterando manualmente
# De esta manera optimizamos el rendimiento, porque el rango completo no se genera directamente, sino que lo genera progresivamente, lo que hace que el recurso en memoria no sea tan alto.
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
# Cuando genero una iteracion que sobrepase el rango me genera la excepcion StopIteration
print(next(my_iterable))