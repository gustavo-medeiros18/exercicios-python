# Crie um programa que receba a nota de um aluno e imprima "Aprovado", "Recuperação" ou "Reprovado"
# com base em critérios predefinidos.
grade1 = float(input('Digite a nota do AP1: '))
grade2 = float(input('Digite a nota do AP2: '))
grade3 = float(input('Digite a nota do AP3: '))

average = (grade1 + grade2 + grade3) / 3

if average >= 7:
  print('Aprovado')
elif average >= 4:
  print('Recuperação')

  extra_grade = float(input('Digite a nota da NAF: '))

  if extra_grade >= 5:
    print('Aprovado por nota')
  else:
    print('Reprovado')
else:
  print('Reprovado')
