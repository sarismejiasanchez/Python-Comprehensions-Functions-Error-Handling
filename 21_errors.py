# Errores en Python
# https://www.w3schools.com/python/python_ref_exceptions.asp

'''
SyntaxError: unmatched ')'
print(0 / 0)) 

ZeroDivisionError: division by zero
print(0 / 0)

NameError: name 'result' is not defined
print(result)

AssertionError
assert suma(2, 2) == 5
'''
print("Hola")

suma = lambda x, y: x + y
assert suma(2, 2) == 4

# Generar un error personalizado
age = 10
if age < 18:
  raise Exception("No se permite menores de edad")

'''
Cuando se generan errores en Python el programa se detiene y no ejecuta nada de lo que se encuentra a continuación.
'''

print("Hola 2")