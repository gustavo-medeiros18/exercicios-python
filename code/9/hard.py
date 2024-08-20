products_database = {
  "Banana": 0.25,
  "Bread": 0.70,
  "Cheese": 0.90,
  "Ham": 1.20,
  "Patty": 1.70,
  "Cereal": 2.00,
  "Milk": 2.50,
  "Eggs": 3.00,
  "Butter": 3.50,
}

def print_menu():
  print("---------- Products available ----------")
  for product in products_database:
    print(f"{product} - R$ {products_database[product]:.2f}")

  print()

while True:
  print_menu()
  user_input = input("Enter desired product and amount (e.g. 'Banana 3'). Type 'exit' to leave: ")

  if user_input.lower() == "exit":
    print("Goodbye!")
    break

  try:
    picked_product, amount = user_input.split()
    amount = int(amount)
  except:
    print("Invalid input. Try again.", end = "\n\n")
    continue

  over_five_units = True if amount > 5 else False

  for product in products_database:
    if product.lower() == picked_product.lower():
      price = products_database[product] * amount

      if over_five_units:
        price *= 0.9

      print(f"Total price: R$ {price:.2f}", end = "\n\n")
      break
  else:
    print("Product not found. Try again.", end = "\n\n")
