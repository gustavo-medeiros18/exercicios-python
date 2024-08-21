# Crie uma função lambda que receba uma lista de números e filtre apenas os números pares.
filter_even = lambda numbers_list: list(filter(lambda number: number % 2 == 0, numbers_list))

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Números pares:", filter_even(numbers_list))
