#Castle on the Grid
#Link: https://www.hackerrank.com/challenges/castle-on-the-grid/problem
#Resumen: Se le da una cuadrícula con algunas celdas abiertas (.) Y algunas bloqueadas (X).
# Su pieza de juego puede moverse a lo largo de cualquier fila o columna hasta que alcance el borde de la cuadrícula o una celda bloqueada.
# Dada una cuadrícula, un comienzo y una meta, determine el número mínimo de movimientos para llegar a la meta.

import os
from collections import deque


def movimientosMin(grid, startX, startY, goalX, goalY):

    #COMPLEJIDAD
    #Tiempo O(n^3)
    #Espacio O(n^2)

    cola = deque()
    cola.appendleft((startX, startY, 0))
    nodosv = set()
    nodos_ady = [(-1, 0),(1, 0),(0, -1),(0, 1)]


    while cola:
        
        (x_actual, y_actual, distancia) = cola.pop()
      
        
        for n in nodos_ady:
            
            x = x_actual + n[0]
            y = y_actual + n[1]

            while (0 <= y < len(grid)) and (0 <= x < len(grid)) and (grid[x][y] != 'X'):

                if x == goalX and y == goalY:
                    return distancia + 1

                elif (x, y) not in nodosv:
                    
                    cola.appendleft((x, y,  distancia + 1))
                    nodosv.add((x, y))
                    
                x += n[0]
                y += n[1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    cuadricula = []

    for _ in range(n):
        cuadricula_item = input()
        cuadricula.append(cuadricula_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = movimientosMin(cuadricula, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()

