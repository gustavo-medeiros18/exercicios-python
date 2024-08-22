def calculate(*args, **kwargs):
  choosen_operation = kwargs.get('operation')

  if (choosen_operation == 'sum'):
    result = sum(args)
  elif (choosen_operation == 'mult'):
    result = 1
    for arg in args:
      result *= arg
  else:
    raise ValueError('Invalid operation')

  choosen_print_language = kwargs.get('print_language')

  if (choosen_print_language == 'en'):
    print(f'The result is {result}')
  elif (choosen_print_language == 'pt'):
    print(f'O resultado é {result}')
  else:
    raise ValueError('Invalid print language')

try:
  calculate(1, 2, 3, 4, operation='mult', print_language='pt')
  calculate(2, 0, 2, 4, operation='sum', print_language='en')
  calculate(2, 0, 2, 1, operation='add', print_language='pt')
except ValueError as e:
  print(e)
