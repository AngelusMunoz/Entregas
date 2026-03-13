#19. Tienda de ropa deportiva: inventario crítico
#Registrar 10 productos.
#Por cada producto pedir:
#• nombre
#• cantidad disponible
#Clasificar:
#• 0 → agotado
#• 1 a 5 → stock bajo
#• 6 o más → stock normal
#Al final mostrar:
#• cuántos están agotados
#• cuántos tienen stock bajo
#• cuántos están normales
#Practica: clasificación por rangos, ciclo

contador_agotados = 0
contador_stock_bajo = 0
contador_stock_normal = 0

for i in range(0, 10, 1):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))

    if cantidad == 0:
        contador_agotados += 1
        estado = "agotado"
    elif 1 <= cantidad <= 5:
        contador_stock_bajo += 1
        estado = "stock bajo"
    else:
        contador_stock_normal += 1
        estado = "stock normal"

    print(f"{nombre} tiene un estado de {estado}.")
    
print(f"Productos agotados: {contador_agotados}")
print(f"Productos con stock bajo: {contador_stock_bajo}")
print(f"Productos con stock normal: {contador_stock_normal}")