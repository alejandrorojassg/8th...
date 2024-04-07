def potencia_de_dos(n):

  potencia = 1
  for i in range(n):
    potencia *= 2
  return potencia

def main():

  n = int(input("Introduzca un exponente: "))

  potencia = potencia_de_dos(n)

  print(f"2 elevado a la potencia {n} es igual a {potencia}")

if __name__ == "__main__":
  main()