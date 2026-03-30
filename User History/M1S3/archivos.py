#------------------------------
#        GUARDAR CSV
#------------------------------

def guardar_csv(stock, ruta):
    if not stock:
        print("No hay datos para guardar")
        return

    with open(ruta, "w") as archivo:
        archivo.write("nombre,precio,cantidad\n")

        for producto in stock:
            linea = producto["nombre"] + "," + str(producto["precio"]) + "," + str(producto["cantidad"]) + "\n"
            archivo.write(linea)

    print("Inventario guardado correctamente")

#-------------------------------
#         CARGAR CSV
#-------------------------------

def cargar_csv(ruta):
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
        print("El archivo no existe")
        return []

    except:
        print("Error al leer el archivo")
        return []
