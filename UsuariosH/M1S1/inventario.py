# Historia de usuario M1S1
# Como usuario quiero poder agregar productos al inventario para llevar un control de los mismos.

print("=" * 40)
print(" " * 12, "INVENTARIO")
print("=" * 40)

print("Bienvenido al sistema de inventario")

inventario = False

# Ciclo principal     
# Dentro de este while ingrese otros whiles para verificar los datos de cada variable

while not inventario:

    # PRIMER WHILE: SE LE PIDE AL USUARIO EL NOMBRE DEL PRODUCTO
    nombre_valido = False
    while not nombre_valido:
        nombre_producto = input("Ingrese el nombre del producto:\n")

        if nombre_producto.strip() == "":
            print("El nombre no puede estar vacío. Intente de nuevo.\n")
        else:
            print("Nombre registrado con éxito👍.\n")
            nombre_valido = True

    # SEGUNDO WHILE: SE LE PIDE AL USUARIO EL PRECIO
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

    # TERCER WHILE: SE LE PIDE AL USUARIO LA CANTIDAD
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

    # Si todo salió bien, se termina el ciclo.
    inventario = True


# Esto es para conseguir el costo total del producto ingresado:
costo_total = precio_producto * cantidad_producto

# ------------------ SALIDA ------------------
print(f"\nEl producto '{nombre_producto}' ha sido agregado al inventario con una cantidad de {cantidad_producto} y un precio de {precio_producto:.2f}.")

print("\nResumen:\n")
print(f"Producto: {nombre_producto} | Precio unitario: {precio_producto:.2f} | Cantidad: {cantidad_producto} | Total: {costo_total:.2f}")

# Este programa solicita al usuario el nombre, precio y cantidad de un producto,
# valida que los datos sean correctos y calcula el costo total del inventario.