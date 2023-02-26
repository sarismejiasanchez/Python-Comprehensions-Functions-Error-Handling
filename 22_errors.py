# Manejo de excepciones
# https://www.w3schools.com/python/python_try_except.asp

'''
Cada que vez que Python encuentra errores, vamos a controlarlo y manejarlo para evitar que se detenga la operacion del programa
'''

'''
# Cualquier error que pase en este bloque, va a ser capturado y podemos manejarlo
try:
  print(0 / 0)
except ZeroDivisionError as error:
  print(error)

try:
  assert 1 != 1, "Uno no es igual que uno"
except AssertionError as error:
  print(error)

# Capturar una excepcion propia
try:
  age = 10
  if age < 18:
    raise Exception("No se permiten menores de edad")
except Exception as error:
  print(error)
'''
# Unificando el manejo de excepciones en un solo bloque
'''
Al unificar los errores en un solo bloque, este se ejecuta hasta que se de la primera excepcion, cuando eso sucede, sale del bloque y continúa ejecutando el resto del programa.
'''
try:
  print(0 / 0)
  assert 1 != 1, "Uno no es igual que uno"
  age = 10
  if age < 18:
    raise Exception("No se permiten menores de edad")
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)
  
print("Hola")
print("Hola 2")

'''
También hay sentencias en el manejo de errores como else y finally.

try:
    pass
except Exception as e:
    raise
else:
    pass
finally:
    pass
.
El bloque else se ejecuta cuando todo lo del bloque ‘try’ se ejecuta correctamente, es decir, sin excepciones.
.
El bloque finally se ejecuta haya o no excepciones en el bloque ‘try’, es decir, que su ejecución es obligatoria
'''

# Playground: Captura la excepción: ZeroDivisionError
'''
Para resolver este desafío, debes utilizar la función my_divide, que recibe dos parámetros de entrada que representan los números a dividir. Dentro de esta función, debes implementar la lógica necesaria para capturar la excepción ZeroDivisionError. También, debes retornar un mensaje que diga No se puede dividir por 0 cuando esta excepción ocurra.

Ejemplo 1:

Input: 10, 2
Output: 5.0

Ejemplo 2:

Input: 10, 0
Output: No se puede dividir por 0
'''

def my_divide(a, b):
   # Escribe tu solución 👇
  try:
    result = a / b
  except ZeroDivisionError:
    return "No se puede dividir por 0"
  return result
    
response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0