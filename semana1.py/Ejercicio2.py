#2. Gimnasio: acceso por edad
#Un gimnasio ofrece clases según la edad:
#• menor de 13 → no puede ingresar
#• de 13 a 17 → clase juvenil
#• de 18 a 59 → clase general
#• 60 o más → clase senior
#Pide la edad de una persona y muestra a qué grupo pertenece.
#Practica: if, elif, else

print("===========================================")
print("             GIMNASIO ANGELUS              ")
print("===========================================")


edad = int(input("Bienvenido al Gimnacio Angelus. Porfavor, ingrese su edad para ingresarlo a un plan: "))

if edad < 13:
    print(f"Usted tiene {edad}, no puede ingresar al Gimnacio Angelus. Gracias por visitarnos")

elif edad >= 13 and edad <= 17:
    print(f"Su edad es de {edad}, fue asignado a la clase juvenil")

elif edad >= 18 and edad <= 59:
    print(f"Su edad es de {edad}, fue asignado a la clase general")

elif edad >= 60:
    print(f"Su edad es mayor de 60, fue asignado a la clase senior")