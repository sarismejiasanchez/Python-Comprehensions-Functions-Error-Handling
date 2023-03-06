# Importamos el modulo
import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./app/world_population.csv')
  country = input("Type Country => ")
  
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  
  print(result)

# Módulos como scripts: __name__ y __main__
# Entry point
'''
Este if le dice al main.py, que si el archivo es ejecutado desde la terminal, ejecute el metodo run, pero si es ejecutado desde otro archivo, el metodo run no se ejecutaria.
'''

if __name__ == '__main__':
  run()