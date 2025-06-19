# Crie um programa que use variáveis globais e locais para calcular o valor de uma expressão matemática.
import math

def calculate_area(radius):
  global pi

  pi = math.pi
  area = pi * (radius ** 2)

  return area

def calcula_perimeter(radius):
  perimeter = 2 * pi * radius

  return perimeter

print(f"{calculate_area(10):.2f}")
print(f"{calcula_perimeter(10):.2f}")
