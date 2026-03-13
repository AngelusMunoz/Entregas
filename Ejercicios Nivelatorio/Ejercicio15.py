# Ejercicio 15: Adivinar un numero secreto

print("Bienvenidos")

numero_secreto = 7
intento = int(input("Adivina el número secreto del 1 al 10: "))

while intento != numero_secreto:
    print("Incorrecto, intenta otra vez.")

    intento = int(input("Adivina el número secreto: "))

print("¡Correcto! Adivinaste el número.")