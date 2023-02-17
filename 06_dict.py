# Dictionary Comprehension: condition

import random
countries = ["col", "mex", "bol", "peru"]
population_v2 = { country: random.randint(1, 100) for country in countries }

print(population_v2)

# Generar nuevo diccionario con los paises que tengan una poblacion mayor que 20
result = { country: population for(country, population) in population_v2.items() if population > 20 }

print(result)

# Diccionario con las volales de un texto
text = "Hola, soy Sara"
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)

# Diccionario con el contador de apariciones de la vocal en el texto
counts = { c: text.count(c) for c in text if c in 'aeiou' }
print(counts)
