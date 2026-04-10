#------------------------------
#        GUARDAR CSV
#------------------------------

def guardar_csv(stock, ruta):
    """
    Guarda el inventario en un archivo CSV.

    Combina los productos actuales en memoria con los ya existentes en el archivo,
    evitando duplicados por nombre, y sobreescribe el archivo con el resultado.

    Parámetros:
        stock (list): Lista de diccionarios con los productos en memoria.
                      Cada dict tiene las claves 'nombre', 'precio', 'cantidad'.
        ruta (str): Ruta del archivo CSV donde se guardará el inventario.

    Retorna:
        None
    """
    existentes = cargar_csv(ruta)

    nombres_existentes = [p["nombre"].lower() for p in existentes]

    for producto in stock:
        if producto["nombre"].lower() not in nombres_existentes:
            existentes.append(producto)

    with open(ruta, "w") as archivo:
        archivo.write("nombre,precio,cantidad\n")

        for producto in existentes:
            linea = producto["nombre"] + "," + str(producto["precio"]) + "," + str(producto["cantidad"]) + "\n"
            archivo.write(linea)

    print("Inventario guardado correctamente")
#-------------------------------
#         CARGAR CSV
#-------------------------------

def cargar_csv(ruta):
    """
    Carga el inventario desde un archivo CSV.

    Lee el archivo línea por línea (ignorando el encabezado), construye una lista
    de diccionarios con los productos y la retorna. Si el archivo no existe,
    retorna una lista vacía y muestra un aviso.

    Parámetros:
        ruta (str): Ruta del archivo CSV a leer.

    Retorna:
        list: Lista de diccionarios con los productos cargados.
              Cada dict tiene las claves 'nombre' (str), 'precio' (float), 'cantidad' (int).
              Retorna [] si el archivo no existe o hay un error de lectura.
    """
    productos = []

    try:
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()

            for linea in lineas[1:]:  # salta el encabezado
                datos = linea.strip().split(",")

                if len(datos) != 3:
                    continue

                nombre = datos[0]
                precio = float(datos[1])
                cantidad = int(datos[2])

                producto = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }

                productos.append(producto)

        print("Archivo cargado correctamente")
        return productos

    except FileNotFoundError:
        print("El archivo no existe, se creará uno nuevo al guardar.")
        return []

    except:
        print("Error al leer el archivo")
        return []