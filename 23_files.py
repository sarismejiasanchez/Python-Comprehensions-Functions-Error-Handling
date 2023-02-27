# Leer un archivo de texto

file = open("./text.txt")
'''
# Leer todo el archivo
print(file.read())

# Leer linea a linea
print(file.readline())
print(file.readline())

'''
# Iterar sobre las lineas del archivo (ocupa menos espacio en memoria)
for line in file:
  print(line)

file.close()

'''
Hay una instrucción en Python a la cual le indicamos que abra el archivo y una vez terminadas las intrucciones que hayan allí, Python automaticamente cerrará el archivo.

https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/
'''

with open("./text.txt") as file:
  print(file.read())
