#18. Centro de idiomas: evaluación de estudiantes
#Registrar varios estudiantes de un curso de inglés.
#Por cada uno pedir:
#• nombre
#• nota speaking
#• nota listening
#• nota reading
#Calcular promedio simple y clasificar:
#• menor de 60 → bajo
#• 60 a 79 → medio
#• 80 o más → alto
#Al final mostrar:
#• promedio general del grupo
#• mejor estudiante
#• cuántos quedaron en cada nivel
#Practica: promedios, máximos, contadores.

total_estudiantes = 0
suma_promedios = 0
contador_bajo = 0
contador_medio = 0
contador_alto = 0
mejor_estudiante = ""
mejor_promedio = 0

opcion = ""

while opcion != "salir":
    nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break

    nota_speaking = float(input("Ingrese la nota de speaking: "))
    nota_listening = float(input("Ingrese la nota de listening: "))
    nota_reading = float(input("Ingrese la nota de reading: "))

    promedio = (nota_speaking + nota_listening + nota_reading) / 3
    suma_promedios += promedio
    total_estudiantes += 1

    if promedio < 60:
        contador_bajo += 1
        nivel = "bajo"
    elif 60 <= promedio < 80:
        contador_medio += 1
        nivel = "medio"
    else:
        contador_alto += 1
        nivel = "alto"

    print(f"{nombre} tiene un promedio de {promedio:.2f} y su nivel es {nivel}.")

    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = nombre

if total_estudiantes > 0:
    promedio_general = suma_promedios / total_estudiantes
    print(f"\nPromedio general del grupo: {promedio_general:.2f}")
    print(f"Mejor estudiante: {mejor_estudiante} con un promedio de {mejor_promedio:.2f}")
    print(f"Estudiantes en nivel bajo: {contador_bajo}")
    print(f"Estudiantes en nivel medio: {contador_medio}")
    print(f"Estudiantes en nivel alto: {contador_alto}")
else:
    print("No se registraron estudiantes.")
