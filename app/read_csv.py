# Leer un CSV

# https://www.w3schools.com/python/python_file_open.asp
# https://www.kaggle.com/
# https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset

import csv
'''
def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    # Convertir lista de registro a diccionario
    header = next(reader)
    print(header)
    for row in reader:
      print("***" * 5)
      print(row)
'''
# Convertir lista de registro a diccionario
def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    # Convertir lista de registro a diccionario
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      #print(list(iterable))
      # Generar diccionario
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/world_population.csv')
  print(data[0])
