# Map con diccionarios

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

# Transformamos para obtener una lista solo de los precios
prices = list(map(lambda item: item['price'], items))
print(prices)

products = list(map(lambda item: item['product'], items))
print(products)

# Agregamos un nuevo atributo al diccionario
def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

new_items = list(map(add_taxes, items)) 
print(new_items)

'''
Map es una de las funciones que se considera que no modifica el estado del array original, por el contrario, crea uno nuevo.
Sin embargo, aqui se evidencia una modificacion en el array, que tiene que ver con una referencia en memoria.
'''
print("*" * 10)
print(items)