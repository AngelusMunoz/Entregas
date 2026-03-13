# Ejercicio 8: Comparación de dos números del usuario.

num1 = float(input("Ingrese el primer número"))
num2 = float(input("Ingrese el segundo número"))

if num1 == num2:
    print(f"El número {num1} y el número {num2} son iguales")
elif num1 > num2:
    print(f"El número {num1} es mayor que el número {num2}")
else:
    print(f"El número {num2} es mayor que el número {num1}")