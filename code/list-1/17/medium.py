# Crie uma função que receba `**kwargs` e imprima os pares chave-valor.

def print_kwargs(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

  print()

print_kwargs(nome="João", idade=25, cidade="São Paulo")
print_kwargs(nome="Maria", idade=30, cidade="Rio de Janeiro")
print_kwargs(nome="José", idade=35)
