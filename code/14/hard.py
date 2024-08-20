# Crie um programa que receba um dicionário de produtos e seus
# preços e permita ao usuário adicionar, remover ou alterar produtos.
products_database = {}

def print_menu():
  print("---------- Options avaliable ----------")
  print("1 - Add product")
  print("2 - List products")
  print("3 - Remove product")
  print("4 - Edit product")
  print("5 - Exit")

def list_products():
  print("---------- Products available ----------")
  for product in products_database:
    print(f"{product} - R$ {products_database[product]:.2f}")

  print()

def add_product(product, price):
  products_database[product] = price

def remove_product(product):
  if product in products_database:
    del products_database[product]
    print(f"{product} removed successfully!")
  else:
    print(f"{product} not found!")

def edit_product(product, price):
  if product in products_database:
    products_database[product] = price
    print(f"{product} edited successfully!")
  else:
    print(f"{product} not found!")

while True:
  print_menu()

  try:
    option = int(input("Choose an option: "))

    if option == 1:
      product = input("Product (case sensitive): ")
      price = float(input("Price: "))
      add_product(product, price)
    elif option == 2:
      list_products()
    elif option == 3:
      product = input("Product (case sensitive): ")
      remove_product(product)
    elif option == 4:
      product = input("Product (case sensitive): ")
      price = float(input("Price: "))
      edit_product(product, price)
    elif option == 5:
      break
    else:
      print("Invalid option!")
  except ValueError:
    print("Invalid input! Please try again")
