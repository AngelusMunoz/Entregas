#11. Heladería: factura de varios clientes
#Una heladería quiere registrar varios clientes hasta que el usuario
#decida salir.
#Productos:
#• cono = 3000
#• vaso = 4000
#• banana split = 9000
#Por cada cliente:
#• pedir producto
#• pedir cantidad
#• calcular total
#Al final mostrar:
#• total vendido
#• cuántos clientes se atendieron
#• cuál producto se pidió más veces
#Practica: ciclos, acumuladores, contadores

print("===========================================")
print("            HELADERIA  ANGELUS             ")
print("===========================================")

total_vendido = 0
contador_clientes = 0
contador_cono = 0
contador_vaso = 0
contador_banana_split = 0
opcion = ""

while opcion != "salir":
    
    print("Productos disponibles:")
    print("1. Cono - $3000")
    print("2. Vaso - $4000")
    print("3. Banana Split - $9000")

    producto = input("Ingrese el producto (cono, vaso, banana split) o 'salir' para terminar: ")
    if producto.lower() == 'salir':
        break

    cantidad = int(input("Ingrese la cantidad: "))

    if producto.lower() == 'cono':
        total_vendido += 3000 * cantidad
        contador_cono += cantidad
    elif producto.lower() == 'vaso':
        total_vendido += 4000 * cantidad
        contador_vaso += cantidad
    elif producto.lower() == 'banana split':
        total_vendido += 9000 * cantidad
        contador_banana_split += cantidad
    else:
        print("Producto no válido. Intente nuevamente.")
        continue

    contador_clientes += 1

# Mostrar resultados
print(f"Total vendido: {total_vendido}")
print(f"Cantidad de clientes atendidos: {contador_clientes}")
if contador_cono >= contador_vaso and contador_cono >= contador_banana_split:
    print("El producto más pedido fue el cono.")
elif contador_vaso >= contador_banana_split:
    print("El producto más pedido fue el vaso.")
else:
    print("El producto más pedido fue el banana split.")