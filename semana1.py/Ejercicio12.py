#12. Gimnasio: promedio de rendimiento semanal
#Registrar 5 personas en un gimnasio.
#Por cada una pedir:
#• nombre
#• días asistidos en la semana
#• minutos promedio entrenados por día
#Clasificar:
#• menos de 3 días → bajo compromiso
#• 3 a 4 días → compromiso medio
#• 5 o más → compromiso alto
#Al final mostrar cuántas personas quedaron en cada categoría.
#Practica: ciclos, contadores, condicionales.

print("===========================================")
print("             GIMNASIO ANGELUS              ")
print("===========================================")

bajo = 0
medio = 0
alto = 0

for i in range(0, 5, 1):

    nombre = input("Ingrese el nombre de la persona: ")
    dias = int(input("Ingrese los días asistidos en la semana: "))
    minutos = int(input("Ingrese los minutos promedio entrenados por día: "))

    if dias < 3:
        print(nombre, "tiene bajo compromiso")
        bajo += 1
    elif 3 <= dias <= 4:
        print(nombre, "tiene compromiso medio")
        medio += 1
    else:
        print(nombre, "tiene compromiso alto")
        alto += 1

print("Personas con bajo compromiso:", bajo)
print("Personas con compromiso medio:", medio)
print("Personas con compromiso alto:", alto)