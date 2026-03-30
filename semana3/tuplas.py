
def tuplas():
    #Tuplas para practicar
    print("ejemplo #1")

    A = [1, 2, 3, 4, 5] #Lista

    B = (1, 2, 3, 4, 5) #Tupla


    print(type(A))
    print(type(B))

    #Las tuplas no pueden ser modificadas, son inmutables
    #B[0] = 10 #Esto no se puede hacer, da error
    #Pero se pueden acceder a sus elementos

    print("ejemplo #2")
    print(B[0]) #Imprime 1
    print(B[4]) #Imprime 5

    #Las tuplas pueden contener cualquier tipo de dato

    print("ejemplo #3")
    C = (1, "Hola", 3.14, [1, 2, 3], (4, 5, 6))
    print(C)
    print(C[4]) #Imprime (4, 5, 6)

    #Las tuplas pueden ser anidadas

    print("ejemplo #4")
    D = ((1, 2), (3, 4), (5, 6))
    print(D)
    print(D[0]) #Imprime 
    print(D[2])
    print(D[2][1])

    #Las tuplas pueden ser desempaquetadas
    print("ejemplo #5")
    E = (1, 2, 3)
    a, b, c = E
    print(a)
    print(b)
    print(c)

    #Puedes darle cualquier valor y desempaquetar

    print("ejemplo #6")
    F = ("Mary", 15, "Barranquilla")
    a, b, c, = F
    print(a)
    print(b)
    print(c)

    #Python puede identificar una dupla con darle datos a una variable
    print("ejemplo #7")
    datos = 1, 2, 3
    print(type(datos))
    print(datos)

#Crear una matriz llena de letra, de 5 x 5 con letras, y montrarla como matriz
#n = tamaño de entrada (pedir)
#m = tamaño de salida
#Usar el ciclo for para recorrer
#Debes usar listas

tuplas()

def matriz():
    abc = ["a", "b", "c", "d", "e", "f", "g"]

    n = int(input("Columnas: "))
    m = int(input("Filas: "))
    L = ""
    #________________________________________________-

    for i in range(0, n, 1):
        for j in range (0, m, 1):
            L[i][j] = input("Dame la letra para la posición [" + str(i) + "][" + str(j) + "]: ")

    for i in range (0, n, 1):
        for j in range (0, m, 1):
            print(L[i][j])
        print("")
    #________________________________________________-

    for i in range(int(m)):
        for j in range(int(m)):
            print(abc, end=" ")
        print()

n = 3
m = 5

# Pre-inicializamos la matriz con ceros (n filas por m columnas)
# Esto crea los "espacios" necesarios en memoria para poder asignar por índice.
matrix = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = input(f"Digite el valor [{i}][{j}] del arreglo: ")

print("\nMatriz resultante:")
for i in range(n):
    print(matrix[i])
