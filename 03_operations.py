# Operaciones con conjuntos
# https://www.w3schools.com/python/python_ref_set.asp

set_a = {"col", "mex", "bol"}
set_b = {"per", "bol"}

# union: une los elementos de los conjuntos sin repetirlos

# Union usando metodo
set_c = set_a.union(set_b)
print(set_c)
# Union usando operador |
print(set_a | set_b)

# Intersection: Elementos en comun
set_c = set_a.intersection(set_b)
print(set_c)
# Intersection usando operador &
print(set_a & set_b)

# Difference: dejar los elemntos del primer conjunto removiendo los elementos del segundo
set_c = set_a.difference(set_b)
print(set_c)
# Difference usando operador -
print(set_a - set_b)

# Symetric Difference: union sin los elementos en comun
set_c = set_a.symmetric_difference(set_b)
print(set_c)
# Symetric difference usando operador ^
print(set_a ^ set_b)

# Playground: Elimina elementos duplicados usando conjuntos

'''
Para resolver este desafío, debes escribir un algoritmo que elimine los elementos repetidos para obtener un conjunto único llamado new_set.

Este algoritmo recibirá como entrada cuatro conjuntos de países, estos países serán de todo el continente americano divididos de la siguiente manera:

countries - Países del continente en general.
northAmerica - Países del norte de América.
centralAmerica - Países del centro de América.
southAmerica - Países del sur de América.
En resumen, el algoritmo deberá eliminar los elementos repetidos de los cuatro conjuntos de países y obtener un conjunto único llamado new_set.

Ejemplo 1:

Input: 
{"MX", "COL", "ARG", "USA"},
{"USA", "CA"},
{"MX", "GT", "BZ"},
{"COL", "BZ", "ARG"}

Output:
{'ARG', 'USA', 'CANADA', 'GT', 'COL', 'MX', 'BZ'}

Ejemplo 2:

Input:
{"BOL"},
{"CA"},
{"MX"},
{"COL"}

Output:

{'COL', 'CA', 'BOL', 'MX'}
'''

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# Escribe tu solución 👇

new_set = countries.union(northAm).union(centralAm).union(southAm)
print(new_set)
print(countries | northAm | centralAm | southAm)