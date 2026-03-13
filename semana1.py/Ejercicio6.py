#6. Parqueadero: cobro por horas
#Pide cuántas horas estuvo un carro en un parqueadero.
#Reglas:
#• primera hora = 5000
#• cada hora adicional = 3000
#Muestra el total a pagar.
#Practica: condicionales y operaciones

print("===========================================")
print("                PARQUEADERO                ")
print("===========================================")

hora1 = 5000

horas = int(input("Bienvenido. Ingrese las horas que estuvo su vehiculo en nuestro parqueadero: "))

if horas == 1:
    print(f"Valor a pagar: {hora1}")

elif horas > 1:
    hora_extra = horas -1
    extra = 3000 * hora_extra
    total = hora1 + extra
    print(f"Valor a pagar: {total}")