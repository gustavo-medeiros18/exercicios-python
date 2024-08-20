# Crie um programa que simule um sistema de autenticação, verificando se o usuário e a
# senha estão corretos e se o usuário possui acesso de administrador.
users_database = {
  "user1": {
    "email": "jamesbond@gmail.com",
    "password": "123456",
    "role": "admin"
  },
  "user2": {
    "email": "linustorvalds@outlook.com",
    "password": "ilovepenguins",
    "role": "common"
  },
  "user3": {
    "email": "robertmartin@gmail.com",
    "password": "iamunclebob",
    "role": "common"
  },
}

while True:
  print("Enter your credentials. Type 'exit' to leave.", end = "\n\n")

  email = input("Email: ")
  if email == "exit":
    print("Goodbye!", end = "\n\n")
    break

  password = input("Password: ")
  if password == "exit":
    print("Goodbye!", end = "\n\n")
    break

  for user in users_database:
    if users_database[user]["email"] == email and users_database[user]["password"] == password:
      print(f"Welcome {user}!", end = "\n")

      while True:
        print("What do you want to do?")
        print("1. Update production database")
        print("2. Just print an image of a cat")
        print("3. Exit")

        option = input("Option: ")

        if option == "1":
          if users_database[user]["role"] == "admin":
            print("Database updated successfully!", end = "\n\n")
          else:
            print("You don't have permission to do that.", end = "\n\n")
        elif option == "2":
          print("Here is an image of a cat:", end = "\n\n")
          print(" /\_/\ ")
          print("( o.o )")
          print(" > ^ <", end = "\n\n")
        elif option == "3":
          print("Goodbye!", end = "\n\n")
          break
        else:
          print("Invalid option. Try again.", end = "\n\n")
      break 
  else:
    print("Invalid email or password. Try again.", end = "\n\n")
