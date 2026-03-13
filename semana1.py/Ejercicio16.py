#16. Tienda de mascotas: ventas por categoría
#Registrar ventas de una tienda de mascotas.
#Categorías:
#• alimento
#• juguete
#• accesorio
#Pedir 10 ventas. En cada venta:
#• categoría
#• valor de la compra
#Al final mostrar:
#• cuánto se vendió por cada categoría
#• cuál categoría generó más dinero
#Practica: acumuladores separados.

alimento_total = 0
juguete_total = 0
accesorio_total = 0

for i in range(0, 10, 1):

    categoria = input("Ingrese la categoría (alimento, juguete, accesorio): ")
    valor = int(input("Ingrese el valor de la compra: "))

    if categoria == "alimento":
        alimento_total += valor
    
    elif categoria == "juguete":
        juguete_total += valor

    elif categoria == "accesorio":
        accesorio_total += valor

    else:
        print("Categoría no válida")

print("Total vendido en alimento:", alimento_total)
print("Total vendido en juguete:", juguete_total)
print("Total vendido en accesorio:", accesorio_total)

if alimento_total > juguete_total and alimento_total > accesorio_total:
    print("La categoría que generó más dinero fue: alimento")
elif juguete_total > alimento_total and juguete_total > accesorio_total:
    print("La categoría que generó más dinero fue: juguete")
else:
    print("La categoría que generó más dinero fue: accesorio")