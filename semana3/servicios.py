# Este file es para tener en orden las funciones a usar

#----------------------------
#    VALIDADOR DE DATOS
#----------------------------

def validar_datos(mensaje, tipo=str, condicion=None, permitir_vacio=False, error="❌ Dato inválido"):
    """
    Solicita y valida un dato ingresado por el usuario desde la consola.

    Repite la solicitud hasta que el valor ingresado sea del tipo correcto
    y cumpla con la condición indicada. Opcionalmente permite un valor vacío.

    Parámetros:
        mensaje (str): Texto que se muestra al usuario para pedir el dato.
        tipo (type): Tipo de dato al que se intentará convertir la entrada. Por defecto str.
        condicion (callable, opcional): Función lambda o función que recibe el valor
                                        convertido y retorna True si es válido.
        permitir_vacio (bool): Si es True, al presionar Enter sin escribir nada retorna None.
                               Por defecto False.
        error (str): Mensaje a mostrar cuando el valor no cumple la condición.
                     Por defecto "❌ Dato inválido".

    Retorna:
        El valor ingresado convertido al tipo indicado, o None si se permitió vacío
        y el usuario presionó Enter sin escribir nada.
    """
    
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
    """
    Agrega un nuevo producto al stock en memoria.

    Verifica que no exista ya un producto con el mismo nombre (sin distinguir
    mayúsculas/minúsculas) y que precio y cantidad sean valores no negativos.
    Si el producto ya existe, cancela la operación y avisa al usuario.

    Parámetros:
        stock (list): Lista de diccionarios que representa el inventario actual.
        nombre (str): Nombre del producto a agregar.
        precio (float): Precio del producto. Debe ser >= 0.
        cantidad (int): Cantidad en stock del producto. Debe ser >= 0.

    Retorna:
        None
    """

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
    """
    Muestra por consola todos los productos del inventario.

    Imprime nombre, precio y cantidad de cada producto. Si el stock
    está vacío, muestra un aviso y termina.

    Parámetros:
        stock (list): Lista de diccionarios que representa el inventario actual.
                      Cada dict tiene las claves 'nombre', 'precio', 'cantidad'.

    Retorna:
        None
    """

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
    """
    Busca un producto en el stock por nombre exacto (sin distinguir mayúsculas/minúsculas).

    Recorre el inventario y, si encuentra una coincidencia, imprime los datos
    del producto y lo retorna. Si no lo encuentra, informa al usuario.

    Parámetros:
        stock (list): Lista de diccionarios que representa el inventario actual.
        buscar (str): Nombre del producto a buscar.

    Retorna:
        dict: Diccionario del producto encontrado con las claves 'nombre', 'precio', 'cantidad'.
        None: Si el producto no existe o el stock está vacío.
    """

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
    """
    Actualiza el precio y/o la cantidad de un producto existente en el stock.

    Busca el producto por nombre (sin distinguir mayúsculas/minúsculas).
    Solo actualiza los campos que no sean None, permitiendo modificar
    uno o ambos valores de forma independiente.

    Parámetros:
        stock (list): Lista de diccionarios que representa el inventario actual.
        cambiar (str): Nombre del producto a actualizar.
        precio_nuevo (float o None): Nuevo precio a asignar. Si es None, no se modifica.
        cantidad_nuevo (int o None): Nueva cantidad a asignar. Si es None, no se modifica.

    Retorna:
        None
    """

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
    """
    Elimina un producto del stock tras mostrar sus datos y pedir confirmación.

    Busca el producto por nombre (sin distinguir mayúsculas/minúsculas),
    muestra su información y solicita al usuario confirmar con 's' o cancelar con 'n'.
    Si confirma, lo elimina de la lista en memoria.

    Parámetros:
        stock (list): Lista de diccionarios que representa el inventario actual.
        eliminar (str): Nombre del producto a eliminar.

    Retorna:
        None: En todos los casos (eliminación, cancelación o producto no encontrado).
    """

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
    """
    Calcula y muestra estadísticas generales del inventario.

    Recorre el stock para obtener: total de unidades, valor total del inventario
    (precio × cantidad de cada producto), el producto más caro y el de mayor stock.
    Imprime los resultados por consola y los retorna en un diccionario.

    Parámetros:
        stock (list): Lista de diccionarios que representa el inventario actual.
                      Cada dict tiene las claves 'nombre', 'precio', 'cantidad'.

    Retorna:
        dict: Diccionario con las claves:
              - 'unidades_totales' (int): Suma de todas las cantidades.
              - 'valor_total' (float): Suma de precio * cantidad de cada producto.
              - 'producto_mas_caro' (dict): Producto con el precio más alto.
              - 'producto_mayor_stock' (dict): Producto con la mayor cantidad.
        None: Si el stock está vacío.
    """
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