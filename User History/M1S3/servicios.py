# Este file es para tener en orden las funciones a usar

#----------------------------
#    VALIDADOR DE DATOS
#----------------------------

def validar_datos(mensaje, tipo=str, condicion=None, permitir_vacio=False, error="❌ Dato inválido"):
    
    valido = False

    while not valido:
        try:
            entrada = input(mensaje)

            # Permitir Enter vacío
            if permitir_vacio and entrada.strip() == "":
                return None

            valor = tipo(entrada)

            if condicion and not condicion(valor):
                print(error)
                continue

            valido = True
            return valor

        except ValueError:
            print("⚠️ Tipo de dato inválido")

#----------------------------
#       AÑADIR PRODUCTO
#----------------------------

def agregar_producto(stock, nombre, precio, cantidad):

    for producto in stock:
        if nombre.lower() == producto["nombre"].lower():
            print("Ese producto ya esta en stock.")
            print("Se cancelo el ingreso.")
            return

    if precio >= 0 and cantidad >= 0:
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        stock.append(producto)
        print("✔Se ingreso con exito al Stock.\n")
        return
    return

#-----------------------------
#       MOSTRAR STOCK
#-----------------------------

def ver_stock(stock):

    if not stock:
        print("El stock esta vacio.")
        return
    
    print("----STOCK ACTUAL----")
    for producto in stock:
        print(f"Nombre:", producto['nombre'])
        print(f"Precio: ${producto['precio']:.2f}")
        print(f"Cantidad:", producto['cantidad'], "\n")

#-----------------------------
#      BUSCAR PRODUCTO
#-----------------------------

def buscar_producto(stock, buscar):

    if not stock:
        print("El stock esta vacio")
        return
    
    print("\nBuscando Producto..\n")
    for producto in stock:
        if producto["nombre"].lower() == buscar.lower() :
            print("Producto encontrado: ")
            print(f"Nombre:", producto['nombre'])
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad:", producto['cantidad'], "\n")
            return producto
        
    print("Producto no encontrado")
    return None

#------------------------------
#      ACTUALIZAR DATOS
#------------------------------

def actualizar_datos(stock, cambiar, precio_nuevo, cantidad_nuevo):

    if not stock:
        print("El stock esta vacio")
        return
    
    for producto in stock:
        if cambiar.lower() == producto["nombre"].lower():

            if precio_nuevo is not None:
                producto["precio"] = precio_nuevo

            if cantidad_nuevo is not None:
                producto["cantidad"] = cantidad_nuevo

            print("✔Se actualizo con exito.")
            print("\nProducto Actualizado:")
            print(f"Nombre:", producto['nombre'])
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad:", producto['cantidad'], "\n")
            return
    print("❌ Producto no encontrado")
    return

#-----------------------------
#      ELIMINAR PRODUCTO
#-----------------------------

def eliminar_producto(stock, eliminar):

    if not stock:
        print("El stock esta vacio")
        return

    for producto in stock:
        if producto["nombre"].lower() == eliminar.lower():
            print("🔎 Producto encontrado:\n")
            print("Nombre", producto['nombre'])
            print(f"Precio: ${producto['precio']:.2f}")
            print("Cantidad:", producto['cantidad'])

            confirmar = validar_datos("¿Seguro que desea eliminar este producto? (s/n): ", str, lambda x: x.lower() in ["n", "s"]).lower()

            if confirmar == "s":
                stock.remove(producto)
                print("🗑️ El producto se elimino con exito.")
                return

            elif confirmar == "n":
                print("🚫 Cancelado.")
                return

    print("❌ No se encontro ese producto.")
    return None

#-------------------------------
#         ESTADISTICAS
#-------------------------------

def calcular_estadisticas(stock):
    if not stock:
        return None
    
    unidades_totales = 0
    valor_total = 0         

    for producto in stock:
        unidades_totales += producto['cantidad']
        valor_total += producto['precio'] * producto['cantidad']

    producto_mas_caro = stock[0]
    producto_mayor_stock = stock[0]

    for producto in stock:
        if producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto

        if producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

    print("\n📊 ESTADÍSTICAS:")
    print("Unidades totales:", unidades_totales)
    print(f"Valor total: {valor_total:.2f}")
    print("Producto más caro:", producto_mas_caro["nombre"], "-", producto_mas_caro["precio"])
    print("Mayor stock:", producto_mayor_stock["nombre"], "-", producto_mayor_stock["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }
