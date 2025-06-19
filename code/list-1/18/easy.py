# Crie uma variável global e uma função que a altere.
global_variable = 10

def update_global_variable():
    global global_variable
    global_variable = 20

print("Valor da var. global antes da função:", global_variable)
update_global_variable()
print("Valor da var. global após a função:", global_variable)
