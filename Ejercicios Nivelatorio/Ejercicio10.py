# Ejercicio 10: Verificar si es positivo, negativo o cero el numero del usuario.

print("Bienvenidos")

num1 = float(input("Ingrese un número"))

if num1 == 0:
    print(f"El número ingresado es cero")
elif num1 > 0:
    print(f"El número ingresado es positivo")
else:
    print(f"El número ingresado es negativo")
