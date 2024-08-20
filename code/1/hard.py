# Crie um dicionário que mapeie nomes de variáveis a valores de diferentes tipos (int, float, string).
# Implemente uma função que receba esse dicionário e retorne uma lista de variáveis do tipo string.
dictionary = {
  'name': 'Gustavo',
  'age': 23,
  'height': 1.73,
  'city': 'Sobral',
  'state': 'Ceara'
}

def get_string_variables(dictionary):
  # return [key for key in dictionary.keys() if type(dictionary[key]) == str]
  return [value for value in dictionary.values() if type(value) == str]

print(get_string_variables(dictionary))
