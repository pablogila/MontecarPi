import random as r
import math as m

# Número de granos que cae dentro del círculo
dentro = 0

print(" Este programa realiza un cálculo aproximado del valor de pi \n mediante la simulación de la tirada de granos de arroz virtuales \n por el método de Montecarlo.")
print("Más información:  https://twitter.com/pgilah/status/1246148100894400512?s=20 \n")
print("Número total de granos de arroz a lanzar:")
total=int(input())

 
print("Haciendo la paella...")
for i in range(0, total):
    # Generamos una posición aleatoria, con x e y entre 0 y 1
    x2 = r.random()**2
    y2 = r.random()**2
    # Si el grano ha caído en el círculo, le contamos
    if m.sqrt(x2 + y2) < 1.0:
        dentro += 1

# dentro / total = pi / 4
pi = (float(dentro) / total) * 4

print("El valor de pi calculado es: ",pi)
