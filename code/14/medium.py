# Crie um dicionário com informações de um aluno (nome, idade, notas) e calcule a média das notas.

def calculate_average(student):
  grades = student["grades"]

  average = sum(grades.values()) / len(grades)
  return average

student = {
  "name": "John",
  "age": 25,
  "grades": {
    "test1": 9.0,
    "test2": 7.0,
    "test3": 8.0
  }
}

print("Média do aluno:", calculate_average(student))
