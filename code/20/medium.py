# Crie uma função lambda que receba dois números e retorne o maior deles.
biggest = lambda x,y : x if x > y else y

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

print("O maior número é:", biggest(x, y))
