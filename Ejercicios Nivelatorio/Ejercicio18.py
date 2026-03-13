# Ejercicio 18: Suma de los primeros N números naturales

print("Bienvenidos")

N = int(input("Ingresa un número: "))

suma = 0

for i in range(1, N + 1):
    suma += 1

print("La suma es:", suma)