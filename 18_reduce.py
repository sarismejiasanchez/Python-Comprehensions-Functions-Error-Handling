# Reduce
# Reduce una lista a un solo valor

import functools
import random

numbers = [1, 2, 3, 4]

def accum(counter, item):
  print("counter =>", counter)
  print("item =>", item)
  return counter + item

result = functools.reduce(accum, numbers)
print("reduce function", result)


result = functools.reduce(lambda counter, item: counter + item, numbers)
print("reduce lambda", result)

def mayor(counter, item):
  if counter <= item:
    return item
  else:
    return counter
    
# Mayor valor de una lista de numeros random entre 1 y 10
numbers = [random.randint(1, 10) for i in range(1, 10)]
print(numbers)
result = functools.reduce(mayor, numbers)
print("Mayor valor =>", result)

# Usando la funcion max
result = functools.reduce(max, numbers)
print("Mayor valor =>", result)