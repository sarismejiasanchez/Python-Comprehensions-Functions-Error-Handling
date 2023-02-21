# Reto: map con inmutabilidad

'''
Map es una de las funciones que se considera que no modifica el estado del array original, por el contrario, crea uno nuevo.
Sin embargo, aqui se evidencia una modificacion en el array, que tiene que ver con una referencia en memoria.
¿Por qué ocurre?
Cuando trabajamos con un diccionario, hay una referencia, es decir un espacio en nuestra computadora, que tiene este diccionario.
Cuando hacemos operaciones con numeros primitivos, es decir un array de numeros, un array de strings y hacemos transformaciones, allí lo que hacemos es que en esa transformacion se está calculando un nuevo valor, por ejemplo multiplicarlo por 2, y ese valor es asignado al array. Pero cuando trabajamos con diccionarios, no se asigna como un nuevo valor, el diccionario se asigna como una referencia en memoria, entonces al hacer una modificacion, se hace una modificación tanto para el array original como para el nuevo. Estamos modificando los dos array, porque los dos comparten la misma referencia en memoria.

¿Como hago para poder sacar esa referencia en memoria?
Creamos una copia del diccionario original, haciendo uso de la funcion copy. Esto copia todos los valores de ese diccionario, pero no se trae esa referencia.
'''

# Lista de diccionarios
items = [
  {
    'product': 'camisa',
    'price': 100
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'chaqueta',
    'price': 600
  }
]

# Agregamos un nuevo atributo al diccionario
def add_taxes(item):
  new_item = item.copy()
  new_item['taxes'] = new_item['price'] * .19
  return new_item

new_items = list(map(add_taxes, items)) 
print("New list")
print(new_items)
print("Old list!")
print(items)