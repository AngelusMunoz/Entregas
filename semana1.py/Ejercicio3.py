#3. Cafetería: total de una compra sencilla
#En una cafetería venden:
#• café = 4000
#• té = 3500
#• jugo = 5000
#Pide al usuario qué bebida quiere y cuántas unidades desea comprar.
#Luego muestra el total a pagar.
#Practica: condicionales, variables, multiplicación.

print("===========================================")
print("           CAFETERIA  ANGELUS              ")
print("===========================================")

cafe = 4000
te = 3500
jugo = 5000

 
print("Bienvenido a la cafeteria Angelus")
print("Nuestro menú es:")
print("1. Café: $4000")
print("2. Té: $3500")
print("3. Jugo: $5000")

opcion = int(input("Seleccione que desea comprar (1-3)"))
cantidad = int(input("¿Cuantas unidades desea llevar?: "))

if opcion == 1:
    total = cafe * cantidad
    print(f"El total a pagar es de ${total}") 
elif opcion == 2:
    total = te * cantidad
    print(f"El total a pagar es de ${total}") 
elif opcion == 3:
    total = jugo * cantidad
    print(f"El total a pagar es de ${total}")