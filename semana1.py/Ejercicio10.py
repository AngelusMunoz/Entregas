#10. Academia de baile: asistencia
#Pide la cantidad de clases asistidas por un estudiante en un mes.
#Reglas:
#• menos de 5 → asistencia baja
#• entre 5 y 8 → asistencia media
#• 9 o más → asistencia alta
#Practica: clasificación por rangos.

print("===========================================")
print("             ACADEMIA   ANGELUS            ")
print("===========================================")

clases = int(input("Ingrese la cantidad de clases asistidas en el mes: "))

if clases < 5:
    print("asistencia baja")
elif 5 <= clases <= 8:
    print("asistencia media")
else:
    print("asistencia alta")