# Use `map` e `filter` em conjunto para primeiro dobrar e depois filtrar os números pares de uma lista.
numbers_list = [1, 2, 3.5, 4, 5, 6, 7, 8, 9, 10]
modified_list = list(filter(lambda number: number % 2 == 0, list(map(lambda number: number * 2, numbers_list))))

print(modified_list)
