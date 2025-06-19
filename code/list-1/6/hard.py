# Crie um programa que receba uma frase e conte quantas palavras começam com uma vogal.
string = input("Digite uma frase: ");

words = string.split(" ");
vowels = "aeiou";

count = 0;
for word in words:
  if word[0].lower() in vowels:
    count += 1;

print(f"A frase tem {count} palavras que começam com uma vogal.");
