# Ejercicio 9: Comparación de tres números del usuario.

num1 = float(input("Ingrese el primer número"))
num2 = float(input("Ingrese el segundo número"))
num3 = float(input("Ingrese el tercer número"))

if num1 == num2 and num1 == num3:
    print(f"Los 3 numeros ingresados son iguales")
elif num1 > num2 and num1 > num3:
    print(f"El número {num1} es mayor entre los 3 números ingresados")
elif num2 > num1 and num2 > num3:
    print(f"El número {num2} es mayor entre los 3 números ingresados")
else:
    print(f"El número {num3} es mayor entre los 3 números ingresados")