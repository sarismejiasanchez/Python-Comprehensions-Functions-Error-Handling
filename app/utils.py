# Mis propios módulos
'''
Los modulos en Python son cualquier archivo con extension .py
Dentro de un modulo nosotros podemos definir Funciones, Clases o Variables
'''

def get_population():
  keys = ["col", "bol"]
  values = [300, 400]
  return keys, values

def population_by_country(data, country):
  result = list(filter(lambda item: item["Country"] == country, data))
  return result