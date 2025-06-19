# Crie um programa que tente dividir dois números e capture uma possível exceção de divisão por zero.
try:
  print(10 / 0)
except ZeroDivisionError:
  print("Divisão por zero")
