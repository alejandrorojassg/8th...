def factorial(n):
  
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)

def main():
  
  n = int(input("Introduzca un número natural: "))

  for i in range(1, n + 1):
    print(f"{i}! = {factorial(i)}")

if __name__ == "__main__":
  main()