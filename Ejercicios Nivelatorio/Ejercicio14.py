# Ejercicio 14: Sumar hasta ingresar 0.

print("Bienvenidos")

suma = 0
numero = int(input("Ingresa un número (0 para terminar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingresa otro número (0 para terminar): "))

print("La suma total es:", suma)