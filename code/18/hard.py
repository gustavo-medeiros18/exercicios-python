# Crie um programa que tenha múltiplas funções, algumas das quais alteram variáveis
# globais, e mostre como o escopo afeta essas variáveis.
counter = 10

def increment_global():
  global counter
  counter += 1

def decrement_global():
  global counter
  counter -= 1

def change_local(value):
  counter = value
  print(f"Local counter value: {counter}")

print(f"Initial counter value: {counter}")

print("Incrementing global counter...")
increment_global()
print(f"Counter value after incrementing globally: {counter}")

print("Decrementing global counter...")
decrement_global()
print(f"Counter value after decrementing globally: {counter}")

print("Setting a custom value to the local counter...")
change_local(200)
print(f"Counter value after custom value set locally: {counter}")
