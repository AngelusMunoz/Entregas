from servicios import validar_datos, agregar_producto, ver_stock, buscar_producto, actualizar_datos, eliminar_producto, calcular_estadisticas
from archivos import guardar_csv, cargar_csv
# App - Menu

print("-" * 40)
print(" " * 14 + "MENU STOCK")
print("-" * 40, "\n")

stock = []
opcion = ""

while opcion != 9:

    print("=" * 40)
    print("¿Que desea hacer?\n")
    print("1. Agregar producto")
    print("2. Stock Actual")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Ver estadisticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir\n")

    opcion = validar_datos("Ingrese un numero (1-9): ", int, lambda x: x in [1,2,3,4,5,6,7,8,9])

    if opcion == 1:
        print("=" * 40, "\n")
        print("Selecciono: Agregar Producto \n")
        print("Porfavor ingrese correctamente los valores:")
        nombre = validar_datos("Nombre: ", str, lambda x: x.strip() != "")
        print("✔Se ingreso con exito.")
        precio = validar_datos("Precio: ", float, lambda x: x >= 0)
        print("✔Se ingreso con exito.")
        cantidad = validar_datos("Cantidad: ", int, lambda x: x >= 0)
        print("✔Se ingreso con exito.\n")

        print("Agregando producto al stock..")
        agregar_producto(stock, nombre, precio, cantidad)

    elif opcion == 2:
        print("=" * 40, "\n")
        print("Selecciono: Stock Actual \n")
        ver_stock(stock)

    elif opcion == 3:
        print("=" * 40, "\n")
        print("Selecciono: Buscar Producto \n")
        buscar = validar_datos("Nombre del producto a buscar: ", str, lambda x: x.strip() != "")
        buscar_producto(stock, buscar)
    
    elif opcion == 4:
        print("=" * 40, "\n")
        print("Selecciono: Actualizar Producto")
        print("\nIniciando Actualizacion..\n")
        cambiar = validar_datos("Nombre del producto a actualizar: ", str, lambda x: x.strip() != "")

        print("--ACTUALIZANDO--")

        precio_nuevo = validar_datos("Precio (Presione Enter para no cambiar): ", float, lambda x: x >= 0, permitir_vacio=True)
        cantidad_nuevo = validar_datos("Cantidad (Presione Enter para no cambiar):", int, lambda x: x >= 0, permitir_vacio=True)

        actualizar_datos(stock, cambiar, precio_nuevo, cantidad_nuevo)

    elif opcion == 5:
        print("=" * 40, "\n")
        print("Selecciono: Eliminar Producto \n")
        print("\nIniciando Eliminacion de Datos..\n")
        eliminar = validar_datos("Nombre del producto a eliminar: ", str, lambda x: x.strip() != "")
        
        print("\n---DELETE---")
        eliminar_producto(stock, eliminar)

    elif opcion == 6:
        print("=" * 40, "\n")
        print("Selecciono: Ver Estadisticas \n")
        calcular_estadisticas(stock)

    elif opcion == 7:
        print("=" * 40, "\n")
        print("Selecciono: Guardar CSV \n")
        ruta = validar_datos("Ingrese el nombre del archivo (ej: inventario.csv): ")
        guardar_csv(stock, ruta)

    elif opcion == 8:
        print("=" * 40, "\n")
        print("Selecciono: Cargar CSV \n")
        ruta = validar_datos("Ingrese el nombre del archivo: ")

        nuevos = cargar_csv(ruta)

        if nuevos:
            stock = nuevos

print("=" * 40)
print("\nCerrando sistema...")
            

