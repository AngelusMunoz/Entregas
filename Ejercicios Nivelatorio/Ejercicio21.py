#Ejercicio 21:

contrasena_correcta = "Angelus"

contrasena = input("Ingrese una contraseña de 7 caracteres:")

array1 = list(contrasena_correcta)
array2 = list(contrasena)

len(array1) == len(array2)

incorrecto = 0
acierto = 0

for i in range(len(array1)):
  if array1[i] == array2[i]:
    acierto += 1

    print("El digito", array1[i], "con el digito", array2[i])
    print("La cantidad de digitos correctos es:", acierto)
  
  else:
    incorrecto += 1
  
    print("El digito", array1[i], "con el digito", array2[i])
    print("La cantidad de digitos incorrectos es", incorrecto)


if acierto == len(array1):
  print("Contraseña correcta, acceso concedido")
else:
  print("Contraseña incorrecta, acceso denagado")