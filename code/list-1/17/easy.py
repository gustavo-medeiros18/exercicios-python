# Crie uma função que receba qualquer número de argumentos e retorne a soma deles usando `*args`.

def sum_with_args(*args):
  return sum(args)

print("Valor da soma com três argumentos:", sum_with_args(1, 2, 3))
print("Valor da soma com dois argumentos:", sum_with_args(1, 2))
print("Valor da soma com cinco argumentos:", sum_with_args(1, 2, 3, 4, 5))
