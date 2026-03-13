# Ejercicio 16: Validar una contraseña

print("Bienvenidos")

contrasena_correcta = "python123"
contrasena = input("Ingresa la contraseña: ")

while contrasena != contrasena_correcta:
    print("Contraseña incorrecta. Intenta de nuevo.")
    contrasena = input("Ingresa la contraseña: ")

print("Acceso concedido.")