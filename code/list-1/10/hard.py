# Crie um programa que receba uma lista de números inteiros e retorne uma nova lista
# contendo apenas os números pares.
numbers_list = input("Digite uma lista de números inteiros separados por espaço: ").split()
evens_list = []

for number in numbers_list:
  if int(number) % 2 == 0:
    evens_list.append(int(number))

print("Números pares:", evens_list)

