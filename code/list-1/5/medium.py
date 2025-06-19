# Crie um programa que calcule a média de cinco notas fornecidas pelo usuário.
grade1 = float(input("Digite a primeira nota: "));
grade2 = float(input("Digite a segunda nota: "));
grade3 = float(input("Digite a terceira nota: "));
grade4 = float(input("Digite a quarta nota: "));
grade5 = float(input("Digite a quinta nota: "));

average = (grade1 + grade2 + grade3 + grade4 + grade5) / 5;

print(f"A média das notas é: {average:.2f}");
