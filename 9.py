import math

def aproximacion_seno(x, n):

  seno_real = math.sin(x)

  suma = 0
  for i in range(n):
    suma += (-1)**i * x**(2*i + 1) / math.factorial(2*i + 1)

  diferencia = seno_real - suma

  return suma, diferencia

x = float(input("Ingrese el valor de x: "))
n = int(input("Ingrese el número de términos de la serie de Maclaurin: "))

aproximacion, diferencia = aproximacion_seno(x, n)

print(f"Aproximación del seno: {aproximacion}")
print(f"Diferencia entre el valor real y la aproximación: {diferencia:.10f}")