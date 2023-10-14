# Titulo: Castle on the Grid
# Link: https://www.hackerrank.com/challenges/castle-on-the-grid/problem


import os
from collections import deque
from unittest import TestCase

def movimientosMin(grid, startX, startY, goalX, goalY):


    cola = deque()
    cola.appendleft((startX, startY, 0))
    nodosv = set()
    nodos_ady = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while cola:

        (x_actual, y_actual, distancia) = cola.pop()

        for n in nodos_ady:

            x = x_actual + n[0]
            y = y_actual + n[1]

            while (0 <= y < len(grid)) and (0 <= x < len(grid)) and (grid[x][y] != 'X'):

                if x == goalX and y == goalY:
                    return distancia + 1

                elif (x, y) not in nodosv:

                    cola.appendleft((x, y, distancia + 1))
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



class Test(TestCase):

    def test_movimientos_minImpar(self):
        result = movimientosMin(['.X.', '.X.', '...'],0,0,0,2)

        self.assertEqual(3,result)

    def test_movimientos_minUnicoPar(self):
        result = movimientosMin(['...', '.X.', '...'],0,0,1,2)

        self.assertEqual(2,result)

    def test_movimientos_minUnico(self):
        result = movimientosMin(['....', '....', '.X.'],0,0,2,0)

        self.assertEqual(1,result)

    def test_movimientos_minGoaly0(self):
        result = movimientosMin(['....', '....', '.X.'],0,0,1,0)

        self.assertEqual(1,result)

    def test_movimientos_minGoalx0(self):
        result = movimientosMin(['...X..', '..X..', '.X.'],0,0,0,1)

        self.assertEqual(1,result)

    def test_movimientos_minxyValor(self):
        result = movimientosMin(['...X..', '..X..', '..X.','.X.'],1,2,2,0)

        self.assertEqual(2,result)

    def test_movimientos_minxyValorC(self):
        result = movimientosMin(['...X..', '..X.','.X.'],1,2,2,2)

        self.assertEqual(1,result)

    def test_movimientos_minonlyY(self):
        result = movimientosMin(['....', '...X.','..','..','...'],0,1,0,3)

        self.assertEqual(1,result)

    def test_movimientos_minonlyX(self):
        result = movimientosMin(['....', '...X.','.X.','..','..','...'],1,0,3,0)

        self.assertEqual(1,result)