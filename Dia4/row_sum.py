# Dado el triángulo de números impares consecutivos:

#              1
#           3 5
#        7 9 11
#    13 15 17 19
# 21 23 25 27 29
# ...
# Calcular la suma de los números de la enésima fila de este triángulo (empezando por el índice 1) por ejemplo: (Entrada --> Salida)

# 1 --> 1
# 2 --> 3 + 5 = 8

def row_sum_odd_numbers(n):
    return n ** 3