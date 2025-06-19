# Crie um programa que leia três variáveis, faça um cálculo matemático com elas
# (como a fórmula de Bhaskara) e exiba o resultado.
import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b**2 - 4*a*c

if delta < 0:
  print('Delta é negativo, a equação não possui raízes reais.')
else:
  bhascara1 = (-b + math.sqrt(delta)) / (2*a)
  bhascara2 = (-b - math.sqrt(delta)) / (2*a)
  print('O resultado da fórmula de Bhaskara é: ', bhascara1, ' e ', bhascara2)
