from unittest import TestCase
from cola import movimientosMin

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

