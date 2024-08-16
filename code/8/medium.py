# Crie um programa que receba a idade de uma pessoa e verifique se ela é criança,
# adolescente, adulta ou idosa.
age = int(input('Digite a idade: '))

if age < 13:
  print('Criança')
elif age < 18:
  print('Adolescente')
elif age < 60:
  print('Adulto')
else:
  print('Idoso')
