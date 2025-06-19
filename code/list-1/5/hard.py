# Crie um programa que resolva uma equação de segundo grau (ax^2 + bx + c = 0) usando a fórmula de Bhaskara.
def calculate_delta(a, b, c):
  return b ** 2 - 4 * a * c

def calculate_roots(a, b, c):
  delta = calculate_delta(a, b, c)

  roots = []

  if (delta == 0):
    roots.append(-b / (2 * a))
  elif (delta > 0):
    roots.append((-b + delta ** 0.5) / (2 * a))
    roots.append((-b - delta ** 0.5) / (2 * a))

  return roots

equation_string = input("Enter the equation in the form of 'ax^2 + bx + c': ")
equation_parts = equation_string.split()

try:
  a_component = equation_parts[0]
  b_component = equation_parts[2]
  c_component = equation_parts[4]

  a_is_negative = False
  if (a_component[0] == "-"):
    a_is_negative = True
    a_component = a_component[1:]

  b_is_negative = equation_parts[1] == "-"
  c_is_negative = equation_parts[3] == "-"

  a = 1 if a_component[0] == "x" else int(a_component[0])
  b = 1 if b_component[0] == "x" else int(b_component[0])
  c = int(c_component)

  a = -a if a_is_negative else a
  b = -b if b_is_negative else b
  c = -c if c_is_negative else c

  roots = calculate_roots(a, b, c)

  if (len(roots) == 0):
    print(f"Equation {equation_string} has no real roots.")
  elif (len(roots) == 1):
    print(f"Root of the equation {equation_string} is: {roots[0]:.2f}")
  else:
    print(f"Roots of the equation {equation_string} are: {roots[1]:.2f} and {roots[0]:.2f}")
except Exception as e:
  print("Error: ", e)
