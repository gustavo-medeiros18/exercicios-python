# Crie um programa que troque os valores de duas variáveis sem usar uma terceira variável temporária.
# Dica: Pesquise sobre a operação XOR.
a = 15
b = 10

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)
