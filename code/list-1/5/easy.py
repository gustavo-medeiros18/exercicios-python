# Crie um programa que calcule a soma, subtração, multiplicação e
# divisão de dois números fornecidos pelo usuário.
number1 = float(input('Digite o primeiro número: '));
number2 = float(input('Digite o segundo número: '));

sum = number1 + number2;
subtraction = number1 - number2;
multiplication = number1 * number2;
division = number1 / number2;

print(f'Soma: {sum}');
print(f'Subtração: {subtraction}');
print(f'Multiplicação: {multiplication}');
print(f'Divisão: {division:.2f}');
