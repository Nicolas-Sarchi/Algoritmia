# Dada una matriz de unos y ceros, convierta el valor binario equivalente a un número entero.

# Por ejemplo: [0, 0, 0, 1] se trata como 0001, que es la representación binaria de 1.

# Ejemplos:

# Pruebas: [0, 0, 0, 1] ==> 1
# Probando: [0, 0, 1, 0] ==> 2
# Pruebas: [0, 1, 0, 1] ==> 5
# Probando: [1, 0, 0, 1] ==> 9
# Probando: [0, 0, 1, 0] ==> 2
# Probando: [0, 1, 1, 0] ==> 6
# Probando: [1, 1, 1, 1] ==> 15
# Probando: [1, 0, 1, 1] ==> 11
# Sin embargo, las matrices pueden tener distintas longitudes, no sólo limitarse a 4.


binary = [1, 0, 0, 1, 1, 0]

def binary_array_to_number(arr):
    result = 0
    for i, e in enumerate(reversed(arr)):
        if e != 0:
            result += 2 ** i
    return result
print(binary_array_to_number(binary))        