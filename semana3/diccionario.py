def add(agregar):

    nombre = ""

    while nombre == "":
        nombre = input("Ingrese el nombre (sin apellido): ").strip()
        if nombre == "":
            print("❌ No puede ingresar un dato vacio.")
        else:
            print("✅ Nombre ingresado con exito.")

    apellido = ""

    while apellido == "":
        apellido = input("Ingrese el apellido (sin nombre): ").strip()
        if apellido == "":
            print("❌ No se puede ingresar un dato vacio.")
        else:
            print("✅ Apellido ingresado con exito.")

    valido = False

    while not valido:
        try:
            edad = int(input("Ingrese la edad: "))

            if edad < 17:
                print("❌ La edad no puede ser menor a 17")

            elif edad > 28:
                print("❌ La edad no puede ser mayor a 28")
            
            else:
                print("✅ Edad ingresada exitoso.")
                valido = True

        except ValueError:
            print("⚠️ Porfavor ingrese una edad valida.")

    valido = False

    while not valido:
        try:
            id_riwi = int(input("Ingrese el ID de usuario. Deben ser numeros enteros positivos: "))

            if id_riwi <= 0:
                print("❌ El ID no puede ser menor o igual a 0")
            elif id_riwi in [riwi["TL"][i]['ID'] for i in riwi["TL"]] or id_riwi in [riwi["coders"][i]['ID'] for i in riwi["coders"]]:
                print("⚠️ El ID ya existe en la base de datos. Por favor ingrese un ID unico.")
            else:
                print("✅ ID ingresada exitoso.")
                valido = True

        except ValueError:
            print("⚠️ Porfavor ingrese un ID valido, solo se puede agregar numeros enteros.")

    #Eso es para agregar un TL o un Coder, dependiendo de lo que el usuario elija
    if agregar == 1: #Si es para agregar un TL
       
        area = ""
        while area == "":
            area = input("Ingrese el area del Team Leader: ").strip()
            if area == "":
                print("❌ No puede ingresar un dato vacio.")
        print("✅ Area ingresada con exito.")
                    
        return nombre, apellido, edad, id_riwi, area

    
    elif agregar == 2: #Si es para agregar un Coder

        valido = False

        while not valido:
            try:
                cohorte = int(input("Ingrese el cohorte del coder: "))

                if cohorte <= 0:
                    print("❌ El cohorte no puede ser menor o igual a 0")
                
                else:
                    print("✅ Cohorte ingresado con exitoso.")
                    valido = True
                    return nombre, apellido, edad, id_riwi, cohorte

            except ValueError:
                print("⚠️ Porfavor ingrese un numero valido.")

print("=" * 40)
print(" " * 6, "🏢 RIWI - BARRANQUILLA 🏢")
print("=" * 40)

print("👋 Bienvenido a la base de datos Riwi Barranquilla")

riwi= { 
    "TL":{},
    "coders":{}
}

opcion = ""

while opcion != 5:

    print("\n" + "=" * 40)
    print("¿Que desea hacer?\n")
    print("1. ➕ Agregar un dato")
    print("2. 📋 Mostrar base de datos")
    print("3. 🔍 Buscar un dato")
    print("4. 🗑️  Eliminar un usuario")
    print("5. 🚪 Salir")
    print("=" * 40, "\n")

    try:
        opcion = int(input("Ingrese un numero del 1 al 5: "))
        if opcion < 1 or opcion > 5:
            print("⚠️ Porfavor ingrese un numero del 1 al 5.")
    except ValueError:
        print("⚠️ Porfavor ingrese un numero valido.")

    # Agregar un dato a la base de datos
    if opcion == 1:

        print("\n" + "=" * 40)
        print("\nQue desea agregar a la base de datos:\n")
        print("1. 👔 Team Leader")
        print("2. 💻 Coder")
        print("=" * 40)

        valido = False

        while not valido:

            try:        
                agregar = int(input("Ingrese el numero del dato que desea agregar (1 o 2):"))
                if agregar == 1 or agregar == 2:
                    valido = True
                else:
                    print("⚠️ Porfavor ingrese un numero valido (1 o 2)")

            except ValueError:
                print("⚠️ Porfavor ingrese un numero valido (1 o 2).")
        datos = add(agregar) 

        if agregar == 1:
            print("➕ Agregando un Team Leader a la base de datos")

            nombre, apellido, edad, id_riwi, area = datos

            numero = len(riwi["TL"]) + 1
            clave = f"TL{numero}"

            riwi["TL"][clave] = {
                "nombre": nombre,
                "apellido": apellido,
                "edad": edad,
                "ID": id_riwi,
                "area": area
            }

        elif agregar == 2:
            print("➕ Agregando un coder a la base de datos")
            nombre, apellido, edad, id_riwi, cohorte = datos

            numero = len(riwi["coders"]) + 1
            clave = f"Coder{numero}"

            riwi["coders"][clave] = {
                "nombre": nombre,
                "apellido": apellido,
                "edad": edad,
                "ID": id_riwi,
                "cohorte": cohorte
            }

    # Mostrar la base de datos completa, tanto TL como coders    
    elif opcion == 2:

        if not riwi["TL"] and not riwi["coders"]:
            print("📭 No hay datos que mostrar.")

        else:
            print("📋 La base de datos en general es:")

            for i in riwi["TL"]:
                print("\n👔 Riwi - Team Leader:")
                print("Nombre:", riwi["TL"][i]['nombre'])
                print("Apellido:", riwi["TL"][i]['apellido'])
                print("Edad:", riwi["TL"][i]['edad'])
                print("Area:", riwi["TL"][i]['area'])
                print("ID:", riwi["TL"][i]['ID'])

            print("\n" + "=" * 40)

            for i in riwi["coders"]:
                print("\n💻 Riwi - Coder:")
                print("Nombre:", riwi["coders"][i]['nombre'])
                print("Apellido:", riwi["coders"][i]['apellido'])
                print("Edad:", riwi["coders"][i]['edad'])
                print("Cohorte:", riwi["coders"][i]['cohorte'])
                print("ID:", riwi["coders"][i]['ID'])

            print("\n" + "=" * 40)

    # Buscar un dato en la base de datos, ya sea un TL o un Coder
    elif opcion == 3:

        if not riwi["TL"] and not riwi["coders"]:
            print("📭 No hay datos que mostrar.")

        else:
            print("🔍 ¿Que desea buscar en la base de datos?\n")
            print("1. 👔 Team Leader")
            print("2. 💻 Coder")

            valido = False

            while not valido:

                try:        
                    buscar = int(input("Ingrese el numero del dato que desea buscar (1 o 2):"))
                    if buscar == 1 or buscar == 2:
                        valido = True
                    else:
                        print("⚠️ Porfavor ingrese un numero valido (1 o 2)")

                except ValueError:
                    print("⚠️ Porfavor ingrese un numero valido (1 o 2).")

        
            if buscar == 1:

                print("🔍 ==== Buscando un Team Leader en la base de datos ====")

                valido = False
                while not valido:
                        
                    try:
                        id_buscar = int(input("Ingrese el ID del Team Leader que desea buscar: "))

                        if id_buscar <= 0:
                            print("❌ El ID no puede ser menor o igual a 0.")
                        
                        else:
                            print("🔎 Iniciando busqueda del ID...\n")
                            valido = True

                    except ValueError:
                        print("⚠️ Ingrese un ID valido.")

                encontrado = False

                for i in riwi["TL"]:
                    if riwi["TL"][i]['ID'] == id_buscar:
                        print("\n👔 Riwi - Team Leader:")
                        print("Nombre:", riwi["TL"][i]['nombre'])
                        print("Apellido:", riwi["TL"][i]['apellido'])
                        print("Edad:", riwi["TL"][i]['edad'])
                        print("Area:", riwi["TL"][i]['area'])
                        print("ID:", riwi["TL"][i]['ID'])
                        
                        encontrado = True

                if not encontrado:
                    print("❌ No se encontro un TL con ese ID")

                print("\n" + "=" * 40)

            elif buscar == 2:

                print("🔍 ==== Buscando un coder en la base de datos ====")
                
                valido = False
                while not valido:
                        
                    try:
                        id_buscar = int(input("Ingrese el ID del coder que desea buscar: "))

                        if id_buscar <= 0:
                            print("❌ El ID no puede ser menor o igual a 0.")
                        
                        else:
                            print("🔎 Iniciando busqueda del ID")
                            valido = True

                    except ValueError:
                        print("⚠️ Ingrese un ID valido...\n")

                encontrado = False
                for i in riwi["coders"]:
                    if riwi["coders"][i]['ID'] == id_buscar:
                        print("\n💻 Riwi - Coder:")
                        print("Nombre:", riwi["coders"][i]['nombre'])
                        print("Apellido:", riwi["coders"][i]['apellido'])
                        print("Edad:", riwi["coders"][i]['edad'])
                        print("Cohorte:", riwi["coders"][i]['cohorte'])
                        print("ID:", riwi["coders"][i]['ID'])

                        encontrado = True

                if not encontrado:
                    print("❌ No se encontro un coder con ese ID")

                print("\n" + "=" * 40)

    
    elif opcion == 4:

        if not riwi["TL"] and not riwi["coders"]:
            print("📭 No hay datos que mostrar.")

        else:
            valido = False
            while not valido:

                try:
                    eliminar = int(input("ID del usuario a eliminar: "))
                    encontrado = False

                    for grupo in riwi:
                        for clave in list(riwi[grupo]):
                            if riwi[grupo][clave]['ID'] == eliminar:
                                print("🔎 ID encontrado:\n")
                                print("Nombre", riwi[grupo][clave]['nombre'])
                                print("Grupo:", "Team Leader" if grupo == "TL" else "Coder")
                                print("ID:", riwi[grupo][clave]['ID'])

                                confirmar = input("¿Seguro que desea eliminar este usuario? (s/n): ").lower()

                                if confirmar == "s":
                                    del riwi[grupo][clave]
                                    print("🗑️ El usuario se elimino con exito.")

                                elif confirmar == "n":
                                    print("🚫 Cancelado.")

                                else: 
                                    print("⚠️ Opcion no valida. Cancelando eliminacion.")

                                encontrado = True

                    if not encontrado:
                        print("❌ No se encontro ese ID.")

                    valido = True
                except ValueError:
                    print("⚠️ Ingrese un ID valido.")