# Crie uma função que receba uma lista de números e retorne a média deles.

def calculate_average(list):
  return sum(list) / len(list)

list = [1, 2, 3, 4, 5]
print(f"Valor da média: {calculate_average(list):.2f}")
