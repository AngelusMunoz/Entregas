#15. Parqueadero: control de vehículos
#Registrar 8 vehículos en un parqueadero.
#Por cada uno pedir:
#• placa
#• tipo: carro o moto
#• horas parqueado
#Tarifas:
#• carro: 4000 por hora
#• moto: 2000 por hora
#Al final mostrar:
#• total recaudado
#• cuántos carros ingresaron
#• cuántas motos ingresaron
#• cuál vehículo pagó más
#Practica: ciclos, máximos, acumuladores.

total_recaudado = 0
contador_carros = 0
contador_motos = 0
vehiculo_mayor_pago = ""
mayor_pago = 0

for i in range(0, 8, 1):
    placa = input("Ingrese la placa del vehículo: ")
    tipo = input("Ingrese el tipo de vehículo (carro o moto): ")
    horas = int(input("Ingrese las horas parqueado: "))

    if tipo == "carro":
        tarifa = 4000
        contador_carros += 1
    elif tipo == "moto":
        tarifa = 2000
        contador_motos += 1
    else:
        print("Tipo de vehículo no válido")
        continue

    pago = tarifa * horas
    total_recaudado += pago

    if pago > mayor_pago:
        mayor_pago = pago
        vehiculo_mayor_pago = placa
        
print("Total recaudado:", total_recaudado)
print("Cantidad de carros ingresados:", contador_carros)
print("Cantidad de motos ingresadas:", contador_motos)
print("El vehículo que pagó más fue:", vehiculo_mayor_pago, "con un pago de:", mayor_pago)

