#4. Cine: entrada según edad
#El precio de la entrada cambia así:
#• niños menores de 12 → 8000
#• adultos de 12 a 59 → 12000
#• mayores de 60 → 9000
#Pide la edad del cliente y muestra cuánto debe pagar.
#Practica: condicionales.

print("===========================================")
print("             CINEMA  ANGELUS               ")
print("===========================================")

edad = int(input("Bienvenidos, porfavor ingrese su edad: "))

if edad < 12:
    print("Valor a pagar: $8.000")

elif edad >= 12 and edad <= 59:
    print("Valor a pagar: $12.000")

elif edad >= 60:
    print("Valor a pagar: $9.000")