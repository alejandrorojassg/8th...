def pares_descendentes(n):
  if n < 2:
    return

  if n % 2 == 0:
    print(n)

  for numero in range(n-2, 2, -2):
    print(numero)

n = int(input("Introduce un número natural n ≥ 2: "))
pares_descendentes(n)