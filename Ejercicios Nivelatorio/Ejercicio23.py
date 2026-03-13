#Ejercicio 23: Simular un banco/cajero con dos cuentas

cuenta1 = 10000
cuenta2 = 8000

def calcular_comision(monto):
    return monto * 0.004

opcion = ""

while opcion != "4":

    print("\n--- CAJERO AUTOMÁTICO BANCOANGEL ---")
    print("Cuentas disponibles: Cuenta 1, Cuenta 2.")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Cancelar")

    opcion = input("Seleccione una opción: ")

    # CONSULTAR
    if opcion == "1":
        try:
            cuenta = int(input("Escoga que cuenta desea ver el saldo. No tendrá ningun cobro: "))
            if cuenta == 1:
                print("Saldo cuenta 1:", cuenta1)
                continue

            elif cuenta == 2:
                print("Saldo cuenta 2:", cuenta2)
                continue
            
            else:
                print("No se encontró esa cuenta, ingrese una cuenta válida.")
                continue

        except ValueError:
            print("Cuenta no válida. Debe ingresar 1 o 2.")

    # DEPOSITAR
    elif opcion == "2":
        try:
            cuenta = int(input("¿Qué cuenta desea usar? (1 o 2): "))
            monto = float(input("Ingrese el monto a depositar: "))

            if monto <= 0:
                print("El monto debe ser mayor que 0.")
                continue

            comision = calcular_comision(monto)

            if cuenta == 1:

                cuenta1 += monto

                if cuenta1 >= comision:
                    cuenta1 -= comision
                    print("Depósito exitoso en cuenta 1.")
                    print("Comisión cobrada en cuenta 1.")
                elif cuenta2 >= comision:
                    cuenta2 -= comision
                    print("Depósito exitoso en cuenta 1.")
                    print("Comisión cobrada en cuenta 2.")
                else:
                    cuenta1 -= monto
                    print("No hay saldo para cubrir la comisión. Operación cancelada.")

            elif cuenta == 2:
                   cuenta2 += monto

                   if cuenta2 >= comision:
                      cuenta2 -= comision
                      print("Depósito exitoso en cuenta 2.")
                      print("Comisión cobrada en cuenta 2.")
                   elif cuenta1 >= comision:
                       cuenta1 -= comision
                       print("Depósito exitoso en cuenta 2.")
                       print("Comisión cobrada en cuenta 1.")
                   else:
                       cuenta2 -= monto
                       print("No hay saldo para cubrir la comisión. Operación cancelada.")

            else:
                print("Cuenta inválida.")

        except ValueError:
            print("Entrada no válida.")

    # RETIRAR
    elif opcion == "3":
        try:
            cuenta = input("¿Qué cuenta desea usar? (1 o 2): ")
            monto = float(input("Ingrese el monto a retirar: "))

            if monto <= 0:
                print("El monto debe ser mayor que 0.")
                continue

            comision = calcular_comision(monto)

            if cuenta == "1":

                if cuenta1 < monto:
                    print("Saldo insuficiente para el retiro.")
                    continue

                cuenta1 -= monto

                if cuenta1 >= comision:
                    cuenta1 -= comision
                    print("Retiro exitoso desde cuenta 1.")
                    print("Comisión cobrada en cuenta 1.")
                elif cuenta2 >= comision:
                    cuenta2 -= comision
                    print("Retiro exitoso desde cuenta 1.")
                    print("Comisión cobrada en cuenta 2.")
                else:
                    cuenta1 += monto
                    print("No hay saldo para cubrir la comisión. Operación cancelada.")

            elif cuenta == "2":

                if cuenta2 < monto:
                    print("Saldo insuficiente para el retiro.")
                    continue

                cuenta2 -= monto

                if cuenta2 >= comision:
                    cuenta2 -= comision
                    print("Retiro exitoso desde cuenta 2.")
                    print("Comisión cobrada en cuenta 2.")
                elif cuenta1 >= comision:
                    cuenta1 -= comision
                    print("Retiro exitoso desde cuenta 2.")
                    print("Comisión cobrada en cuenta 1.")
                else:
                    cuenta2 += monto
                    print("No hay saldo para cubrir la comisión. Operación cancelada.")

            else:
                print("Cuenta inválida.")

        except ValueError:
            print("Entrada no válida.")

    # CANCELAR PROCESO
    elif opcion == "4":
            print("Gracias por usar el cajero automático BancoAngel")

    else:
        print("Opción inválida.")