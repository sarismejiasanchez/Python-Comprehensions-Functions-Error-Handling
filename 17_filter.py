# Filter
# https://www.w3schools.com/python/ref_func_filter.asp

numbers = [1, 2, 3, 4, 5]

# Solo los elementos que cumplen con la condicion del filter, van a ser parte de la nueva lista
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)

# Filter no modifica la lista original, simplemente crea una nueva lista.
print(numbers)
