# Crie um programa que receba três números inteiros e exiba a soma, a subtração,
# a multiplicação e a divisão entre eles, formatando a saída de forma clara e alinhada.
value1 = int(input("Digite o primeiro número: "));
value2 = int(input("Digite o segundo número: "));
value3 = int(input("Digite o terceiro número: "));

sum = value1 + value2 + value3;
sub = value1 - value2 - value3;
mult = value1 * value2 * value3;
div = value1 / value2 / value3;

print("Soma: " + str(sum));
print("Subtração: " + str(sub));
print("Multiplicação: " + str(mult));

# Formatação de saída com duas casas decimais
print("Divisão: " + "{:.2f}".format(div));
