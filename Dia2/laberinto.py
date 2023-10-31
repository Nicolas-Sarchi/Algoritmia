# El laberinto se representará como una una lista de listas, donde cada lista es una fila del laberinto y cada casilla se representará con un espacio ’ ’ si hay paso o con la letra ‘X’ si hay un muro, tal y como se muestra a continuación:


# laberinto = [
#     [' ', ' ', ' ', ' ', ' '], 
#     [' ', ' ', ' ', ' ', ' '],
#     [' ', ' ', ' ', ' ', ' '], 
#     [' ', ' ', ' ', ' ', ' '], 
#     [' ', ' ', ' ', ' ', 'S']
#     ]

# muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))


# for tupla in muro :
#     fila = tupla[0]
#     col = tupla[1]
#     laberinto[fila][col] = 'X'

print("--------------- Laberinto ----------------\n\n")
   
   
laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', 'X', 'X', 'X'],
    [' ', ' ', ' ', ' ', 'X'], 
    [' ', ' ', 'X', ' ', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ] 


for fila in laberinto:
    print(fila) 

movimientos = ['Abajo']

fila = col = 0

n = len(laberinto)

while (laberinto[fila][col] != 'S'):
    if movimientos[-1] != 'Arriba' and fila + 1 < n and laberinto[fila + 1][col] != 'X':
        fila += 1
        movimientos.append('Abajo')
    elif movimientos[-1] != 'Abajo' and fila - 1 > 0 and laberinto[fila - 1][col] != 'X':
        fila -= 1
        movimientos.append('Arriba')
    elif movimientos[-1] != 'Izquierda' and col + 1 < n and laberinto[fila][col + 1] != 'X':
        col += 1
        movimientos.append('Derecha')
    elif movimientos[-1] != 'Derecha' and col - 1 > 0 and laberinto[fila][col - 1] != 'X':
        col -= 1
        movimientos.append('Izquierda')
    else:
        movimientos.append('No hay salida')

print("\n\nsolucion: \n", movimientos)            
            

