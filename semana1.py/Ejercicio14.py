#14. Cine: control de sala
#Pedir la capacidad total de una sala de cine y luego registrar cuántas
#personas ingresan.
#Por cada persona pedir edad y clasificar:
#• niño
#• adulto
#• adulto mayor
#Al final mostrar:
#• total de personas ingresadas
#• cuántos niños
#• cuántos adultos
#• cuántos adultos mayores
#• si la sala se llenó o no
#Practica: ciclos con límite, contadores.

capacidad = int(input("Ingrese la capacidad total de la sala: "))
contador_personas = 0
contador_ninos = 0
contador_adultos = 0
contador_adultos_mayores = 0

while contador_personas < capacidad:
    edad = int(input("Ingrese la edad de la persona: "))
    
    if edad < 18:
        contador_ninos += 1
        categoria = "niño"
    elif 18 <= edad < 60:
        contador_adultos += 1
        categoria = "adulto"
    else:
        contador_adultos_mayores += 1
        categoria = "adulto mayor"

    contador_personas += 1
    print(f"Persona ingresada: {categoria}")
    
print("Resumen:")
print(f"Total de personas ingresadas: {contador_personas}")
print(f"Niños: {contador_ninos}")
print(f"Adultos: {contador_adultos}")
print(f"Adultos mayores: {contador_adultos_mayores}")
if contador_personas == capacidad:
    print("La sala se llenó.")
else:
    print("La sala no se llenó.")