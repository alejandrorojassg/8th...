import math

def exp_maclaurin(x, n):

  aproximacion = 1.0
  for i in range(1, n + 1):
    aproximacion += (x**i) / math.factorial(i)
  return aproximacion

def error(aproximacion, valor_real):
  
  return abs(aproximacion - valor_real)


x = float(input("Introduzca el valor de x: "))
n = int(input("Introduzca el número de términos: "))

aproximacion = exp_maclaurin(x, n)
valor_real = math.exp(x)

print(f"Aproximación: {aproximacion}")
print(f"Valor real: {valor_real}")
print(f"Error: {error(aproximacion, valor_real)}")


n = 1
while error(exp_maclaurin(x, n), math.exp(x)) >= 0.001:
  n += 1

print(f"Para un error menor al 0.1%, se necesitan {n} términos.")