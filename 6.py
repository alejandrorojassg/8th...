def potencia(x, n):

  potencia = 1
  for i in range(n):
    potencia *= x
  return potencia

def main():

  n = int(input("Introduzca un número natural: "))

  x = float(input("Introduzca un dato real: "))

  potencia = potencia(x, n)

  print(f"{x} elevado a la potencia {n} es igual a {potencia}")

if __name__ == "__main__":
  main()