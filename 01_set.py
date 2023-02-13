# Sets
# https://platzi.com/clases/2884-notacion-matematica/47333-conjuntos/
# https://www.w3schools.com/python/python_sets.asp

'''
- Se pueden modificar
- No tienen un orden
- No permite duplicados
'''

'''
Se definen también con {} pero en este caso no tiene un par key:value
sino directamente va a tener los elementos
'''
set_countries = {"col", "mex", "bol"}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
# Aunque el 2 está repetido, al imprimir lo muestra solo una vez
print(set_numbers)

set_types = {1, "Hola", False, 12.12}
# En este caso se imprime en otro orden
print(set_types)

# Creamos un conjunto a partir de un string
set_from_string = set("Hola")
print(set_from_string)

# Creamos un conjunto a partir de una tupla
set_from_tuples = set(("abc", "cbv", "as", "abc"))
print(set_from_tuples)

# Creamos un conjunto a partir de una lista
set_from_list = set([1, 2, 3, 1, 2, 3, 4])
print(set_from_list)

'''
En Python podemos tener una lista de numeros o valores duplicados,
los cuales si transformamos en conjuntos (set) conservaríamos solo los valores únicos.
'''

# Pasamos un diccionario a una lista

unique_numbers = list(set_from_list)
print(unique_numbers)
print(type(unique_numbers))