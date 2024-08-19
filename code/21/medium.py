# Use `filter` para filtrar os números pares de uma lista.
numbers_list = [1, 2, 3, 4, 5, 5, 6, 7, 8]
even_numbers_list = list(filter(lambda x: x % 2 == 0, numbers_list))

print(even_numbers_list)
