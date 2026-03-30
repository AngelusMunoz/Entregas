# Historia de usuario M1S2
# Agregar, mostrar, eliminar y modificar productos en el inventario.

print("=" * 40)
print(" " * 12, "INVENTARIO")
print("=" * 40)

print("Bienvenido al sistema de inventario")

inventario = []

opcion = ""

#Bucles

while opcion != 4:

    #acciones

    print("\n¿Que desea hacer? (1-4)\n")
    print("1. Agregar producto\n"
        "2. Mostrar inventario\n" 
        "3. Calcular estadisticas\n" 
        "4. Salir\n")

    try: 
        opcion = int(input("Ingrese el numero: "))

    except ValueError:
        print("Ingrese un numero del 1 al 4. Intente otra vez")

    if opcion == 1:

        nombre_valido = False
        while not nombre_valido:
            nombre_producto = input("Ingrese el nombre del producto:\n")

            if nombre_producto.strip() == "":
                print("El nombre no puede estar vacío. Intente de nuevo.\n")
            else:
                print("Nombre registrado con éxito👍.\n")
                nombre_valido = True

        # SE LE PIDE AL USUARIO EL PRECIO
        precio_valido = False
        while not precio_valido:
            try:
                precio_producto = float(input("Ingrese el precio del producto:\n"))

                if precio_producto <= 0:
                    print("El precio debe ser mayor a 0.\n")
                else:
                    print("Precio registrado con éxito👍.\n")
                    precio_valido = True

            except ValueError:
                print("Ingrese un número válido.\n")

        # SE LE PIDE AL USUARIO LA CANTIDAD
        cantidad_valida = False
        while not cantidad_valida:
            try:
                cantidad_producto = int(input("Ingrese la cantidad del producto:\n"))

                if cantidad_producto <= 0:
                    print("La cantidad debe ser mayor a 0.\n")
                else:
                    print("Cantidad registrada con éxito👍.\n")
                    cantidad_valida = True

            except ValueError:

                print("Ingrese un número entero válido.\n")
        
        costo_total = precio_producto * cantidad_producto

        producto = {
            "nombre": nombre_producto,
            "precio": precio_producto,
            "cantidad": cantidad_producto,
            "total": costo_total
                            }
        inventario.append(producto)
        print("Se agrego con exito el producto✨✔.")
        
    elif opcion == 2:
        numero = 1
        indice = len(inventario)
        print("\nInvetario actual:\n")

        if inventario == []:
            print("No hay ningun producto en el inventario.")

        else:
            for i in inventario:
                print(f"Producto - {numero}")
                numero += 1

                print("Producto:", i['nombre'], "|", "Precio:", i['precio'], "|", "Cantidad:", i['cantidad'], "\n")

    elif opcion == 3:
        numero = 1
        indice = len(inventario)
        print("\nInvetario actual:\n")

        if inventario == []:
            print("No hay ningun producto en el inventario.")

        else:
            for i in inventario:
                print(f"Producto - {numero}")
                numero += 1

                print("Producto:", i['nombre'], "|", "Precio:", i['precio'], "|", "Cantidad:", i['cantidad'], "|", "Total:", i['total'], "\n")
