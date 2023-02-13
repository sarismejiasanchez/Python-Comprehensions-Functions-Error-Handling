# Modificando conjuntos

set_countries = {"col", "mex", "bol"}

# Tamaño del conjunto
size = len(set_countries)
print(size)

# Preguntar por un elemento en especifico
print("col" in set_countries)
print("pe" in set_countries)

# Agregar un elemento al conjunto 
# add()
set_countries.add("pe")
print(set_countries)

# Aunque lo agregue varias veces, conserva su regla de no duplicados
set_countries.add("pe")
print(set_countries)

# Actualizar los elementos
# Es muy similar a agregar elementos
# update()
set_countries.update({"ar", "ec", "pe"})
print(set_countries)

# Elimir elementos
# remove()
set_countries.remove("col")
print(set_countries)

set_countries.remove("ar")
print(set_countries)

# Remover un elemento que no existe
# remove()
#set_countries.remove("arg")

# discard()
'''
Con este método, si el elemento existe lo elimina,
en caso contrario, no genera error por no encontrarlo
'''
set_countries.discard("arg")
print(set_countries)

# Agregamos argentina
set_countries.add("arg")
print(set_countries)

# Limpiar el conjunto, elimina todos los elementeos
# clear()
set_countries.clear()
print(set_countries)