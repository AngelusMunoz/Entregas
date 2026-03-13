#8. Tienda deportiva: contar productos caros
#Pide el precio de 6 productos deportivos
#Al final indica cuántos cuestan más de 100000
#Practica: ciclo, contador, condicional.

print("===========================================")
print("             DEPORTES  ANGELUS             ")
print("===========================================")

contador = 0

for i in range(0, 6, 1):
    precio = int(input("Ingrese el precio del producto: "))

    if precio > 100000:
        contador += 1

print("Cantidad de productos que cuestan más de 100000:", contador)