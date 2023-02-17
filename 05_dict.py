# Dictionary Comprehension

dict = {}
for i in range(1, 6):
  dict[i] = i * 2

print(dict)

# Usando dict comprehension
dict_v2 = { i: i * 2 for i in range(1, 6) }
print(dict)


# Generar diccionario a partir de una lista
import random
countries = ["col", "mex", "bol", "peru"]
population = {}
for country in countries:
  population[country] = random.randint(1, 100)

print(population)

population_v2 = { country: random.randint(1, 100) for country in countries }

print(population_v2)


# Iterar dos listas para generar un diccionario
names = ["nico", "zule", "santi"]
ages = [12, 56, 98]

# Unir listas
print(list(zip(names, ages)))

# Generar diccionario
new_dict = { name: age for (name, age) in zip(names, ages) }
print(new_dict)