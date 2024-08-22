# Crie uma função que receba uma lista de números e retorne o maior valor usando recursão.
def biggest(numbers_list, list_begin=0):
  if list_begin == len(numbers_list) - 1:
    return numbers_list[list_begin]

  next_number = biggest(numbers_list, list_begin + 1)

  return numbers_list[list_begin] if numbers_list[list_begin] > next_number else next_number

print(biggest([1, 2, 3, 4, 5]))
print(biggest([5, 4, 3, 2, 1]))
print(biggest([1, 2, 3, 5, 4]))
print(biggest([1, 2, 5, 3, 4]))
