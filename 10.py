import math

def arctan_aproximacion(x, n):
  
  if abs(x) > 1:
    raise ValueError("El valor de x debe estar en el rango [-1, 1]")
  
  suma = 0
  for i in range(n):
    suma += (-1)**i * (x**(2*i + 1)) / (2*i + 1)
  
  return suma

def main():
  
  x = 0.5
  n = 5

  aproximacion = arctan_aproximacion(x, n)
  valor_real = math.atan(x)

  diferencia = abs(aproximacion - valor_real)

  print(f"Aproximación de arctan({x}) con {n} términos: {aproximacion}")
  print(f"Valor real: {valor_real}")
  print(f"Diferencia: {diferencia}")

if __name__ == "__main__":
  main()