#1. Heladería: sabor más pedido
#Una heladería quiere registrar 5 pedidos.
#Por cada cliente, el programa debe pedir el sabor elegido:
# • vainilla
# • chocolate
# • fresa
#Al final debe mostrar cuántas veces se pidió cada sabor.
#Practica: ciclos, condicionales, contadores

total1 = 0
total2 = 0
total3 = 0

print("===========================================")
print("             HELADERIA ANGELUS             ")
print("===========================================")

print("Sabores disponibles:")
print("1. Sabor Vainilla")
print("2. Sabor Chocolate")
print("3. Sabor Fresa")

for i in range(0, 5, 1):
    sabor = int(input("Seleccione un sabor (1-3): "))

    if sabor == 1:
        total1 += 1

    elif sabor == 2:
        total2 += 1

    elif sabor == 3:
        total3 += 1

print("===========================================")
print("             HELADERIA ANGELUS             ")
print("===========================================")

print("Resultados:")

print(f"Se escogieron {total1} veces el sabor vainilla")
print(f"Se escogieron {total2} veces el sabor chocolate")
print(f"Se escogieron {total3} veces el sabor fresa")

