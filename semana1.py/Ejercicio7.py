#7. Peluquería: turno del día
#Pide la hora de llegada de un cliente en formato entero de 0 a 23.
#Mostrar:
#• mañana si está entre 6 y 11
#• tarde si está entre 12 y 17
#• noche si está entre 18 y 22
#• fuera de horario en cualquier otro caso
#Practica: rangos con condicionales

print("===========================================")
print("           PELUQUERIA  ANGELUS             ")
print("===========================================")

hora = int(input("Porfavor ingrese la hora de su ingreso a la peluqueria: "))

if 6 <= hora <= 11:
    print("mañana")
elif 12 <= hora <= 17:
    print("tarde")
elif 18 <= hora <= 22:
    print("noche")
else:
    print("fuera de horario")