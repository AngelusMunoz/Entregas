from servicios import validar_datos, agregar_producto, ver_stock, buscar_producto, actualizar_datos, eliminar_producto, calcular_estadisticas
from archivos import guardar_csv, cargar_csv

RUTA_ARCHIVO = "inventario.csv"

print("-" * 40)
print(" " * 14 + "MENU STOCK")
print("-" * 40, "\n")

# CARGA AUTOMÁTICA AL INICIAR
stock = cargar_csv(RUTA_ARCHIVO)

opcion = ""

while opcion != 7:

    print("=" * 40)
    print("¿Que desea hacer?\n")
    print("1. Agregar producto")
    print("2. Stock Actual")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Ver estadisticas")
    print("7. Salir\n")

    opcion = validar_datos("Ingrese un numero (1-7): ", int, lambda x: x in [1,2,3,4,5,6,7])

    if opcion == 1:
        print("=" * 40, "\n")
        print("Selecciono: Agregar Producto \n")

        nombre = validar_datos("Nombre: ", str, lambda x: x.strip() != "")
        precio = validar_datos("Precio: ", float, lambda x: x >= 0)
        cantidad = validar_datos("Cantidad: ", int, lambda x: x >= 0)

        agregar_producto(stock, nombre, precio, cantidad)

        # GUARDADO AUTOMÁTICO
        guardar_csv(stock, RUTA_ARCHIVO)

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
        print("Selecciono: Actualizar Producto\n")

        cambiar = validar_datos("Nombre del producto a actualizar: ", str, lambda x: x.strip() != "")

        precio_nuevo = validar_datos("Precio (Enter para no cambiar): ", float, lambda x: x >= 0, permitir_vacio=True)
        cantidad_nuevo = validar_datos("Cantidad (Enter para no cambiar): ", int, lambda x: x >= 0, permitir_vacio=True)

        actualizar_datos(stock, cambiar, precio_nuevo, cantidad_nuevo)

        #GUARDADO AUTOMÁTICO
        guardar_csv(stock, RUTA_ARCHIVO)

    elif opcion == 5:
        print("=" * 40, "\n")
        print("Selecciono: Eliminar Producto \n")

        eliminar = validar_datos("Nombre del producto a eliminar: ", str, lambda x: x.strip() != "")
        eliminar_producto(stock, eliminar)

        #GUARDADO AUTOMÁTICO
        guardar_csv(stock, RUTA_ARCHIVO)

    elif opcion == 6:
        print("=" * 40, "\n")
        print("Selecciono: Ver Estadisticas \n")
        calcular_estadisticas(stock)

print("=" * 40)
print("\nCerrando sistema...")