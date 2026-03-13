#13. Cafetería: descuento por consumo
#Registrar varios pedidos en una cafetería hasta que el usuario escriba
#“salir”.
#Productos:
#• café = 4000
#• capuchino = 7000
#• pastel = 6000
#Reglas:
#• si la compra supera 20000, aplicar 10% de descuento
#• si no, cobrar normal
#Mostrar total por cliente y al final total acumulado del día.
#Practica: menú simple, ciclos, descuentos.

total_acumulado = 0

total_cliente = 0

print("Menú de productos:")
print("1. Café - $4000")
print("2. Capuchino - $7000")
print("3. Pastel - $6000")
print("Escriba 'salir' para terminar el pedido del cliente.")

pedido = input("Ingrese el número del producto que desea pedir: ")

while pedido != "salir":

    if pedido == "1":
        total_cliente += 4000
    elif pedido == "2":
        total_cliente += 7000
    elif pedido == "3":
        total_cliente += 6000
    else:
        print("Opción no válida.")

    pedido = input("Ingrese otro producto o 'salir' para terminar: ")

if total_cliente > 20000:
    descuento = total_cliente * 0.10
    total_cliente = total_cliente - descuento
    print("Descuento aplicado:", descuento)

print("Total del cliente:", total_cliente)

total_acumulado += total_cliente
print("Total acumulado del día:", total_acumulado)
