#20. Club recreativo: control de membresías
#Registrar varias personas en un club.
#Por cada una pedir:
#• nombre
#• edad
#• tipo de plan: básico, premium, familiar
#Reglas:
#• básico = 50000
#• premium = 90000
#• familiar = 130000
#Además:
#• si la persona es menor de 18, mostrar “registro juvenil”
#• si tiene 60 o más, mostrar “beneficio senior”
#Al final mostrar:
#• total recaudado
#• cantidad de personas por plan
#• plan más vendido
#Practica: condicionales, contadores, acumuladores

total_recaudado = 0
contador_basico = 0
contador_premium = 0
contador_familiar = 0

opcion = ""

while opcion != "salir":
    nombre = input("Ingrese el nombre de la persona (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break

    edad = int(input("Ingrese la edad: "))
    tipo_plan = input("Ingrese el tipo de plan (básico, premium, familiar): ").lower()

    if tipo_plan == "basico":
        total_recaudado += 50000
        contador_basico += 1
    elif tipo_plan == "premium":
        total_recaudado += 90000
        contador_premium += 1
    elif tipo_plan == "familiar":
        total_recaudado += 130000
        contador_familiar += 1
    else:
        print("Tipo de plan no válido. Intente nuevamente.")
        continue

    if edad < 18:
        print("Registro juvenil")
    elif edad >= 60:
        print("Beneficio senior")

print(f"\nTotal recaudado: ${total_recaudado}")
print(f"Cantidad de personas con plan básico: {contador_basico}")
print(f"Cantidad de personas con plan premium: {contador_premium}")
print(f"Cantidad de personas con plan familiar: {contador_familiar}")
