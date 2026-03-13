n = int(input("Ingrese un numero: "))
fila = [1] * n

for i in range(n):
    print(fila)
    
    for j in range(1, n):
        fila[j] = fila[j] + fila[j-1]
