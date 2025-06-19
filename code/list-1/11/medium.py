# Crie um loop `while` que continue pedindo números ao usuário até que ele digite um número negativo.
while True:
  number = int(input("Digite um número: "))
  if number < 0:
    print("Número negativo digitado. Encerrando o programa.")
    break
