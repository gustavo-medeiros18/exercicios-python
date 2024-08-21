# TODO: Otimizar o código usando zip para não usar tanto print

# Crie um programa que peça ao usuário seu nome, idade e cidade.
# Depois, exiba essas informações em um formato de tabela.
# Exemplo:
# +------+-------+-----------+
# | Nome | Idade | Cidade    |
# +------+-------+-----------+
# | João | 20    | São Paulo |
# +------+-------+-----------+
def print_separator(column1_length, column2_length, column3_length):
  print("+" + "-" * column1_length + "+" + "-" * column2_length + "+" + "-" * column3_length + "+")

name = input("Digite seu nome: ")
age = input("Digite sua idade: ")
city = input("Digite sua cidade: ")

column1_length = len(name) + 2 if len(name) > len("Nome") else len("Nome") + 2
column2_length = len(age) + 2 if len(age) > len("Idade") else len("Idade") + 2
column3_length = len(city) + 2 if len(city) > len("Cidade") else len("Cidade") + 2

print_separator(column1_length, column2_length, column3_length)
print("| " + "Nome" + " " * (column1_length - len("Nome") - 1) + "| " + "Idade" + " " * (column2_length - len("Idade") - 1) + "| " + "Cidade" + " " * (column3_length - len("Cidade") - 1) + "|")

print_separator(column1_length, column2_length, column3_length)
print("| " + name + " " * (column1_length - len(name) - 1) + "| " + age + " " * (column2_length - len(age) - 1) + "| " + city + " " * (column3_length - len(city) - 1) + "|")

print_separator(column1_length, column2_length, column3_length)
