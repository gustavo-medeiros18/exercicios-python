# Crie um programa que leia um arquivo que não existe e capture a exceção apropriada.
try:
  open('input.txt')
except FileNotFoundError:
  print('O arquivo não foi encontrado ou não existe')
