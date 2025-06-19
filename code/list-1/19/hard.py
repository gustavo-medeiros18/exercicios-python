# Crie um programa que receba uma lista de números e tente converter
# cada elemento para inteiro, capturando e tratando exceções de conversão.
user_input = input("Digite uma lista de números separados por espaço: ")
numbers = user_input.split()

for number in numbers:
  try:
    print(int(number))
  except ValueError:
    print(f"Erro ao converter {number} para inteiro.")
