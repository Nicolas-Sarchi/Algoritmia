# En esta pequeña tarea se te da una cadena de números separados por espacios, y tienes que devolver el número más alto y el más bajo.

# Ejemplos
# alto_y_bajo("1 2 3 4 5") # devuelve "5 1"
# high_and_low("1 2 -3 4 5") # devuelve "5 -3"
# high_and_low("1 9 3 4 -5") # devuelve "9 -5"
# Notas
# Todos los números son Int32 válidos, no es necesario validarlos.
# Siempre habrá al menos un número en la cadena de entrada.
# La cadena de salida debe tener dos números separados por un espacio, y el número más alto es el primero.


def high_and_low(numbers):
    numList = []
    numbers = numbers.split(" ")
    for i in numbers:
        numList.append(int(i))
    
    numbers = f"{max(numList)} {min(numList)}"    
    return numbers


print(high_and_low("1 2 3 -3"))

