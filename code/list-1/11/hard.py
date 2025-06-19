# Crie um programa que gere a sequência de Fibonacci até um número `n` fornecido pelo usuário.
n = int(input('Digite um número: '))

x, y = 0, 1
for _ in range(n):
  print(x, end = ' ')
  x, y = y, x + y
