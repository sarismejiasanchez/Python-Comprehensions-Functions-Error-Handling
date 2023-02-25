# Importamos el modulo
import utils

data = [
  {
    "Country": "Colombia",
    "Population": 500
  },
  {
    "Country": "Bolivia",
    "Population": 400
  }
]

def run():
  keys, values = utils.get_population()
  print(keys, values)
  country = input("Type Country => ")
  result = utils.population_by_country(data, country)
  print(result)

# Módulos como scripts: __name__ y __main__
# Entry point
'''
Este if le dice al main.py, que si el archivo es ejecutado desde la terminal, ejecute el metodo run, pero si es ejecutado desde otro archivo, el metodo run no se ejecutaria.
'''

if __name__ == '__main__':
  run()
  