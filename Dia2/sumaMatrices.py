# Escribe un programa en Python que sume dos matrices de igual tamaño. Debes pedir al usuario que ingrese las matrices y luego mostrar la matriz resultante.

def sumaMatrices(matriz1, matriz2):
    nuevaMatriz = []
    for i in range(len(matriz1)):
        nuevaMatriz.append([])
        for j in range(len(matriz1[0])):
            nuevaMatriz[i].append(matriz1[i][j] + matriz2[i][j])
    return nuevaMatriz

print("Ingrese el tamaño que van a tener las matrices, recuerde que deben ser cuadradas: ")
tamano = int(input())
matriz1 = []
matriz2 = []

for i in range(tamano):
    matriz1.append([])
    matriz2.append([])
    for j in range(tamano):
        matriz1[i].append(int(input("Ingrese un numero: ")))
        matriz2[i].append(int(input("Ingrese un numero: ")))

print(matriz1)
print("\n\n", matriz2)

print("\n\n", sumaMatrices(matriz1, matriz2))