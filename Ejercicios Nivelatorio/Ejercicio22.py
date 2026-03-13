#Ejercicio 22: Simular un banco/cajero
saldo = 10000
opcion = ""

while opcion != "4":
    print("--- CAJERO AUTOMÁTICO BANCOANGEL ---")
    print("¿Qué desea hacer?:")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Cancelar")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Saldo actual:", saldo)

    elif opcion == "2":
        try:
            monto = float(input("Ingrese el monto a depositar: "))
            if monto <= 0:
                print("El monto debe ser mayor que cero.")
            else:
                saldo += monto
                print("Depósito exitoso. Nuevo saldo:", saldo)
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

    elif opcion == "3":
        try:
            monto = float(input("Ingrese el monto a retirar: "))
            if monto <= 0:
                print("El monto debe ser mayor que cero.")
            elif monto > saldo:
                print("No tiene suficiente saldo.")
            else:
                saldo -= monto
                print("Retiro exitoso. Nuevo saldo:", saldo)
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

    elif opcion == "4":
        print("Gracias por usar el cajero automático BancoAngel.")

    else:
        print("Opción inválida. Intente nuevamente.")