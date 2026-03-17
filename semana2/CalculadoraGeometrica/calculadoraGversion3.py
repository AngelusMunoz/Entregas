pi = 3.1416

def leer_decimal(mensaje):
    valor = ""                              # MODIFICADO: loop hasta obtener un numero valido
    while valor == "":
        try:
            texto = input(mensaje)
            texto = texto.replace(",", ".")       # MODIFICADO: acepta coma o punto como decimal
            valor = float(texto)
        except ValueError:
            print("⚠ Error: ingrese un numero valido.")
    return valor                              # MODIFICADO: retorna solo cuando el valor es correcto

# Calculadora Geometrica

def menu():
    
    opcion = ""
       
    #sabra Dios como carajos hice para que sirva :D
    
    while opcion != 10:

        print("=================================================")
        print("\n        Calculadora Geometrica\n")
        print("=================================================")
        print("\nSeleccione que figura desea trabajar:\n")
        print("\nFiguras 2D:                    Figuras 3D:\n"   
            "\n1. Triangulo General           6. Cubo\n"
            "\n2. Circulo                     7. Esfera\n"
            "\n3. Rombo                       8. Piramide cuandrangular regular\n"
            "\n4. Rectangulo                  9. Cilindrico\n"
            "\n5. Triangulo Rectangulo        10. Salir\n")

        try:

            opcion = int(input("Ingrese su opcion: "))

            if opcion == 1:
                triangulo()

            elif opcion == 2:
                circulo()

            elif opcion == 3:
                rombo()

            elif opcion == 4:
                rectangulo()

            elif opcion == 5:
                triangulo_rectangulo()

            elif opcion == 6:
                cubo()

            elif opcion == 7:
                esfera()

            elif opcion == 8:
                piramide()
                
            elif opcion == 9:
                cilindrico()

            elif opcion == 10:
                print("¡Gracias por usar la calculadora geometrica, vuelva pronto!")
    
            else:
                print("⚠ Error: ingrese una opcion.")

        except ValueError:
            print("⚠ Error: intente otra vez")

# FUNCIONES SEGUN LA FIGURA

# FIGURAS 2D

def triangulo():

    opcion = ""
        
    while opcion != 5:
        print("\n===FIGURA ACTUAL: TRIANGULO===\n")
        if sistema == "1":
            print("Sistema de medidas: Metrico")
        else:
            print("Sistema de medidas Imperial")
        print("\n¿Que desea calcular? (1-5)\n"
            "1. Perimetro\n" \
            "2. Area\n" \
            "3. Altura\n" \
            "4. Suma de Angulos\n" \
            "5. Regresar a menu")
        
        try:
        
            opcion = int(input(""))

            if opcion == 5:
                return

            elif opcion == 1 or opcion == 3:
                print("Porfavor ingrese los valores del triangulo a trabajar:")
                lado_a = leer_decimal("Lado a: ")
                lado_b = leer_decimal("Lado b (Este lado tambien se tomara como base): ")
                lado_c = leer_decimal("Lado c: ")
                   
                if (lado_a + lado_b <= lado_c) or (lado_a + lado_c <= lado_b) or (lado_b + lado_c <= lado_a):
                    print("Error: Los lados ingresados NO forman un triangulo valido.")
                    continue

                semiperimetro = (lado_a + lado_b + lado_c) / 2
                perimetro = lado_a + lado_b + lado_c
                area = (semiperimetro *(semiperimetro - lado_a)*(semiperimetro - lado_b)*(semiperimetro - lado_c)) ** 0.5
                h = (2 * area) / lado_b
                
                if opcion == 1:
                    if sistema == "2":
                        print(f"El perimetro de las medidas asignadas es de: {perimetro * 0.3937:.2f} in")
                    else:
                        print(f"El perimetro de las medidas asignadas es de: {perimetro:.2f} cm")

                elif opcion == 3:
                    if sistema == "2":
                        print(f"La altura segun los valores asignados es de: {h * 0.3937:.2f} in")
                    else:
                        print(f"La altura segun los valores asignados es de: {h:.2f} cm")
            
            elif opcion == 2:
                base = leer_decimal("Ingrese la base: ")
                h = leer_decimal("Ingrese la altura: ")

                if base <= 0 or h <= 0:
                    print("Error: La base y la altura deben ser mayor que 0.")
                    continue

                area = (base * h) / 2

                if sistema == "2":
                    print(f"El Area es: {area * 0.155:.2f} in²")
                else:
                    print(f"El Area es: {area:.2f} cm²")

            elif opcion == 4:
                angulo_A = leer_decimal("Ingrese el angulo A: ")
                angulo_B = leer_decimal("Ingrese el angulo B: ")
                print("Nota: El angulo C se calculara automaticamente para sumar los angulos.")
                
                if angulo_A <= 0 or angulo_B <= 0:
                    print("Error: los angulos deben ser mayores que 0.")

                elif angulo_B + angulo_A >= 180:
                    print("Error: la suma de los angulos debe ser menor que 180 grados.")

                else:
                    angulo_C = 180 - (angulo_A + angulo_B)
                    suma_angulos = angulo_A + angulo_B + angulo_C
                    print(f"La suma de {angulo_A:.2f}°, {angulo_B:.2f}° y {angulo_C:.2f}° es de {suma_angulos:.2f}°.")

            else:
                print("⚠ Error: ingrese una opcion.")
                continue

        except ValueError:
            print("⚠ Error: intente otra vez")
            continue

def circulo():
    
    opcion = ""
        
    while opcion != 4:
        print("\n===FIGURA ACTUAL: CIRCULO===\n")
        if sistema == "1":
            print("Sistema de medidas: Metrico")
        else:
            print("Sistema de medidas Imperial")
        print("\n¿Que desea calcular? (1-4)\n"
            "1. Diametro\n" \
            "2. Circunferencia\n" \
            "3. Area\n" \
            "4. Regresar a menu")
        
        try:
        
            opcion = int(input(""))

            if opcion == 4:
                return

            elif opcion == 1 or opcion == 2 or opcion == 3:           
                print("Porfavor ingrese los valores de la figura a trabajar:")
                radio = leer_decimal("Radio: ")
            
                if radio <= 0:
                    print("Error. Porfavor ingrese numeros validos el radio.")
                    continue

                diametro = 2 * radio
                circunferencia = 2 * pi * radio
                area = pi * radio ** 2

                if opcion == 1:
                    if sistema == "2":
                        print(f"El Diametro es de: {diametro * 0.3937:.2f} in")
                    else:
                        print(f"El Diametro es de: {diametro:.2f} cm")

                elif opcion == 2:
                    if sistema == "2":
                        print(f"La Circunferencia es de: {circunferencia * 0.3937:.2f} in")
                    else:
                        print(f"La Circunferencia es de: {circunferencia:.2f} cm")

                elif opcion == 3:
                    if sistema == "2":
                        print(f"El Area es de: {area * 0.155:.2f} in²")
                    else:
                        print(f"El Area es de: {area:.2f} cm²")

            else:
                print("⚠ Error: ingrese una opcion.")
                continue

        except ValueError:
            print("⚠ Error: intente otra vez")
            continue

def rombo():
    
    opcion = ""

    while opcion != 4:
        print("\n===FIGURA ACTUAL: ROMBO===\n")
        if sistema == "1":
            print("Sistema de medidas: Metrico")
        else:
            print("Sistema de medidas Imperial")
        print("\n¿Que desea calcular? (1-4)\n"
            "1. Perimetro\n" \
            "2. Area\n" \
            "3. Altura\n" \
            "4. Regresar a menu")
        
        try:
            opcion = int(input(""))

            if opcion == 4:
                return

            elif opcion == 1 or opcion == 2 or opcion == 3:
                print("Porfavor ingrese los valores de la figura a trabajar:")
                lado = leer_decimal("Lado: ")
                diagonalM = leer_decimal("Diagonal mayor: ")
                diagonalm = leer_decimal("Diagonal menor: ")
                
                if lado <= 0 or diagonalM <= 0 or diagonalm <= 0 or diagonalM <= diagonalm:
                    print("Error: Los diagonales y lados no pueden ser menor que 0." \
                    "Y la diagonal mayor no puede ser menor a la diagonal menor.")
                    continue        
                
                perimetro = 4 * lado
                area = (diagonalM * diagonalm) / 2
                h = area / lado

                if opcion == 1:
                    if sistema == "2":
                        print(f"El perimetro es: {perimetro * 0.3937:.2f} in")
                    else:
                        print(f"El perimetro es: {perimetro:.2f} cm")

                elif opcion == 2:
                    if sistema == "2":
                        print(f"El area es: {area * 0.155:.2f} in²")
                    else:
                        print(f"El area es: {area:.2f} cm²")

                elif opcion == 3:
                    if sistema == "2":
                        print(f"La altura es: {h * 0.3937:.2f} in")
                    else:
                        print(f"La altura es: {h:.2f} cm")

            else:
                print("⚠ Error: ingrese una opcion.")
                continue

        except ValueError:
            print("⚠ Error: intente otra vez")
            continue

def rectangulo():

    opcion = ""
        
    while opcion != 4:
        print("\n===FIGURA ACTUAL: RECTANGULO===\n")
        if sistema == "1":
            print("Sistema de medidas: Metrico")
        else:
            print("Sistema de medidas Imperial")
        print("\n¿Que desea calcular? (1-4)\n"
            "1. Perimetro\n" \
            "2. Area\n" \
            "3. Diagonal\n" \
            "4. Regresar a menu")
        
        try:
        
            opcion = int(input(""))

            if opcion == 4:
                return
            
            if opcion == 1 or opcion == 2 or opcion == 3:

                print("Porfavor ingrese los valores de la figura a trabajar:")
                base = leer_decimal("Base: ")
                h = leer_decimal("Altura: ")

                if base <= 0 or h <= 0:
                    print("Error, porfavor ingrese valores validos para un rectangulo.")
                    continue

                area = base * h
                perimetro = 2 * (base + h)
                diagonal = ((base ** 2) + (h ** 2)) ** 0.5

                if opcion == 1:
                    if sistema == "2":
                        print(f"El perimetro es: {perimetro * 0.3937:.2f} in")
                    else:
                        print(f"El perimetro es: {perimetro:.2f} cm")

                elif opcion == 2:
                    if sistema == "2":
                        print(f"El area es: {area * 0.155:.2f} in²")
                    else:
                        print(f"El area es: {area:.2f} cm²")

                elif opcion == 3:
                    if sistema == "2":
                        print(f"La diagonal es: {diagonal * 0.3937:.2f} in")
                    else:
                        print(f"La diagonal es: {diagonal:.2f} cm")

            else:
                print("⚠ Error: ingrese una opcion.")
                continue

        except ValueError:
            print("⚠ Error: intente otra vez")
            continue

def triangulo_rectangulo():

    opcion = ""
        
    while opcion != 5:
        print("\n===FIGURA ACTUAL: TRIANGULO RECTANGULO===\n")
        if sistema == "1":
            print("Sistema de medidas: Metrico")
        else:
            print("Sistema de medidas Imperial")
        print("\n¿Que desea calcular? (1-5)\n"
            "1. Hipotenusa\n" \
            "2. Area\n" \
            "3. Perimetro\n" \
            "4. Hallar angulo\n"
            "5. Regresar a menu")
        
        try:
        
            opcion = int(input(""))

            if opcion == 5:
                return
            
            if opcion == 1 or opcion == 2 or opcion == 3:
                
                print("Porfavor ingrese los valores de la figura a trabajar:")

                if opcion != 4:
                    catetoA = leer_decimal("Cateto a: ")
                    catetoB = leer_decimal("Cateto b: ")

                    if catetoA <= 0 or catetoB <= 0:
                        print("Error: los catetos deben ser mayores que 0")
                        continue
            
                hipotenusa = ((catetoA ** 2) + (catetoB ** 2)) ** 0.5
                perimetro = catetoA + catetoB + hipotenusa
                area = (catetoA * catetoB) / 2
                
                if opcion == 1:
                    if sistema == "2":
                        print(f"La hipotenusa es: {hipotenusa * 0.3937:.2f} in")
                    else:
                        print(f"La hipotenusa es: {hipotenusa:.2f} cm")
                
                elif opcion == 2:
                    if sistema == "2":
                        print(f"El area es: {area * 0.155:.2f} in²")
                    else:
                        print(f"El area es: {area:.2f} cm²")

                elif opcion == 3:
                    if sistema == "2":
                        print(f"El perimetro es: {perimetro * 0.3937:.2f} in")
                    else:
                        print(f"El perimetro es: {perimetro:.2f} cm")

            elif opcion == 4:
                anguloA = leer_decimal("Angulo A: ")
                
                if anguloA <= 0 or anguloA >= 90:
                    print("Error: el angulo debe estar entre 0 y 90 grados.")
                    continue

                anguloC = 90
                anguloB = anguloC - anguloA

                print(f"El angulo A es: {anguloA:.2f}°")
                print(f"El angulo B es: {anguloB:.2f}°")
                print(f"El angulo C es: {anguloC:.2f}°")

            else:
                print("⚠ Error: ingrese una opcion.")
                continue

        except ValueError:
            print("⚠ Error: intente otra vez")
            continue

# FIGURAS 3D

def cubo():
         
    opcion = ""
        
    while opcion != 6:
        print("\n===FIGURA ACTUAL: CUBO===\n")
        if sistema == "1":
            print("Sistema de medidas: Metrico")
        else:
            print("Sistema de medidas Imperial")
        print("\n¿Que desea calcular? (1-6)\n"
            "1. Volumen\n" \
            "2. Area superficial\n" \
            "3. Perimetro total\n" \
            "4. Diagonal de una cara\n"
            "5. Diagonal espacial\n"
            "6. Regresar a menu")
        
        try:
        
            opcion = int(input(""))

            if opcion == 6:
                return
            
            elif opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:

                print("Porfavor ingrese los valores de la figura a trabajar:")
                lado = leer_decimal("Lado: ")
                
                if lado <= 0:
                    print("Error. Ingrese un valor mayor que 0")
                    continue

                volumen = lado ** 3
                area_superficial = 6 * (lado ** 2)
                perimetro = 12 * lado
                diagonal_cara = lado * (2 ** 0.5)
                diagonal_espacial = lado * (3 ** 0.5)

                if opcion == 1:
                    if sistema == "2":
                        print(f"El volumen es: {volumen * 0.061:.2f} in³")
                    else:
                        print(f"El volumen es: {volumen:.2f} cm³")

                elif opcion == 2:
                    if sistema == "2":
                        print(f"El area superficial es: {area_superficial * 0.155:.2f} in²")
                    else:
                        print(f"El area superficial es: {area_superficial:.2f} cm²")

                elif opcion == 3:
                    if sistema == "2":
                        print(f"El perimetro total es: {perimetro * 0.3937:.2f} in")
                    else:
                        print(f"El perimetro total es: {perimetro:.2f} cm")

                elif opcion == 4:
                    if sistema == "2":
                        print(f"La diagonal de una cara es: {diagonal_cara * 0.3937:.2f} in")
                    else:
                        print(f"La diagonal de una cara es: {diagonal_cara:.2f} cm")

                elif opcion == 5:
                    if sistema == "2":
                        print(f"La diagonal espacial es: {diagonal_espacial * 0.3937:.2f} in")
                    else:
                        print(f"La diagonal espacial es: {diagonal_espacial:.2f} cm")

            else:
                print("⚠ Error: ingrese una opcion.")
                continue

        except ValueError:
            print("⚠ Error: intente otra vez")
            continue

def esfera():
    
    opcion = ""
        
    while opcion != 6:
        print("\n===FIGURA ACTUAL: ESFERA===\n")
        if sistema == "1":
            print("Sistema de medidas: Metrico")
        else:
            print("Sistema de medidas Imperial")
        print("\n¿Que desea calcular? (1-6)\n"
            "1. Volumen\n" \
            "2. Area superficial\n" \
            "3. Diametro\n" \
            "4. Circunferencia maxima\n"
            "5. Area circulo maximo\n"
            "6. Regresar a menu")
        
        try:
        
            opcion = int(input(""))

            if opcion == 6:
                return
            
            elif opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:

                print("Porfavor ingrese los valores de la figura a trabajar:")
                radio = leer_decimal("Radio: ")

                if radio <= 0:
                    print("Error. Ingrese un valor mayor que 0.")
                    continue

                volumen = (4/3) * (pi * (radio ** 3))
                area_superficial = 4 * (pi * (radio ** 2))
                Circunferencia_max = 2 * (pi * radio)
                diametro = 2 * radio
                area_max = pi * (radio ** 2)

                if opcion == 1:
                    if sistema == "2":
                        print(f"El volumen es: {volumen * 0.061:.2f} in³")
                    else:
                        print(f"El volumen es: {volumen:.2f} cm³")
                
                elif opcion == 2:
                    if sistema == "2":
                        print(f"El area superficial es: {area_superficial * 0.155:.2f} in²")
                    else:
                        print(f"El area superficial es: {area_superficial:.2f} cm²")

                elif opcion == 3:
                    if sistema == "2":
                        print(f"El diametro es: {diametro * 0.3937:.2f} in")
                    else:
                        print(f"El diametro es: {diametro:.2f} cm")

                elif opcion == 4:
                    if sistema == "2":
                        print(f"La circunferencia maxima es: {Circunferencia_max * 0.3937:.2f} in")
                    else:
                        print(f"La circunferencia maxima es: {Circunferencia_max:.2f} cm")

                elif opcion == 5:
                    if sistema == "2":
                        print(f"El area maxima es: {area_max * 0.155:.2f} in²")
                    else:
                        print(f"El area maxima es: {area_max:.2f} cm²")

            else:
                print("⚠ Error: ingrese una opcion.")
                continue

        except ValueError:
            print("⚠ Error: intente otra vez")
            continue

def piramide():

    opcion = ""
        
    while opcion != 4:
        print("\n===FIGURA ACTUAL: PIRAMIDE===\n")
        if sistema == "1":
            print("Sistema de medidas: Metrico")
        else:
            print("Sistema de medidas Imperial")
        print("\n¿Que desea calcular? (1-4)\n"
            "1. Perimetro\n" \
            "2. Area base\n" \
            "3. Volumen\n" \
            "4. Regresar a menu")
        
        try:
        
            opcion = int(input(""))

            if opcion == 4:
                return
                        
            elif opcion == 1 or opcion == 2 or opcion == 3:
                print("Porfavor ingrese los valores de la figura a trabajar:")

                lado = leer_decimal("Lado: ")
                h = leer_decimal("Altura: ")

                if lado <= 0 or h <= 0:
                    print("Error. Los valores deben ser mayor que 0")
                    continue

                perimetro = lado * 4
                volumen = (1/3) * ((lado ** 2) * h)
                area_base = lado ** 2
                
                if opcion == 1:
                    if sistema == "2":
                        print(f"El perimetro es: {perimetro * 0.3937:.2f} in")
                    else:
                        print(f"El perimetro es: {perimetro:.2f} cm")
                
                elif opcion == 2:
                    if sistema == "2":
                        print(f"El area de la base es: {area_base * 0.155:.2f} in²")
                    else:
                        print(f"El area de la base es: {area_base:.2f} cm²")

                elif opcion == 3:
                    if sistema == "2":
                        print(f"El volumen es: {volumen * 0.061:.2f} in³")
                    else:
                        print(f"El volumen es: {volumen:.2f} cm³")

            else:
                print("⚠ Error: ingrese una opcion.")
                continue

        except ValueError:
            print("⚠ Error: intente otra vez")
            continue

def cilindrico():
     
    opcion = ""
        
    while opcion != 6:
        print("\n===FIGURA ACTUAL: CILINDRO===\n")
        if sistema == "1":
            print("Sistema de medidas: Metrico")
        else:
            print("Sistema de medidas Imperial")
        print("\n¿Que desea calcular? (1-6)\n"
            "1. Volumen\n" \
            "2. Area base\n" \
            "3. Area lateral\n" \
            "4. Area total\n" \
            "5. Circunferencia\n" \
            "6. Regresar a menu")
        
        try:
        
            opcion = int(input(""))

            if opcion == 6:
                return
            
            elif opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
                
                print("Porfavor ingrese los valores de la figura a trabajar:")
                radio = leer_decimal("Radio: ")
                h = leer_decimal("Altura: ")

                if radio <= 0 or h <= 0:
                    print("Error. Los valores deben ser mayor que 0")
                    continue

                volumen = pi * (radio ** 2) * h
                area = pi * (radio ** 2)
                area_lateral = (2 * pi) * (radio * h)
                area_total = 2 * pi * radio * (radio + h)
                circunferencia = 2 * pi * radio
    
                if opcion == 1:
                    if sistema == "2":
                        print(f"El volumen es: {volumen * 0.061:.2f} in³")
                    else:
                        print(f"El volumen es: {volumen:.2f} cm³")
                
                elif opcion == 2:
                    if sistema == "2":
                        print(f"El area base es: {area * 0.155:.2f} in²")
                    else:
                        print(f"El area base es: {area:.2f} cm²")

                elif opcion == 3:
                    if sistema == "2":
                        print(f"El area lateral es: {area_lateral * 0.155:.2f} in²")
                    else:
                        print(f"El area lateral es: {area_lateral:.2f} cm²")

                elif opcion == 4:
                    if sistema == "2":
                        print(f"El area total es: {area_total * 0.155:.2f} in²")
                    else:
                        print(f"El area total es: {area_total:.2f} cm²")

                elif opcion == 5:
                    if sistema == "2":
                        print(f"La circunferencia/perimetro es: {circunferencia * 0.3937:.2f} in")
                    else:
                        print(f"La circunferencia/perimetro es: {circunferencia:.2f} cm")

            else:
                print("⚠ Error: ingrese una opcion.")
                continue

        except ValueError:
            print("⚠ Error: intente otra vez")
            continue

#ESTO ES PARA QUE CORRA

sistema = ""
while sistema != "1" and sistema != "2":
    print("=================================================")
    print("\n        Calculadora Geometrica\n")
    print("=================================================")
    print("\nSistema de medidas:\n"
    "\n1. Metrico\n"
    "\n2. Imperial\n")
    sistema = input("")
    if sistema != "1" and sistema != "2":
        print("⚠ Error: ingrese 1 o 2.")

if sistema == "2":
    print("\n⚠ Nota: Ingrese los valores en cm. El resultado se convertirá automáticamente a pulgadas (in).\n")
    
menu()

#Listo :D