from unittest import TestCase
from pila import isBalanced


class Test(TestCase):

    def test_is_balancedParUnico(self):
        prueba = isBalanced("()")
        self.assertTrue(prueba)

    def test_is_balancedUnico(self):
        prueba = isBalanced(")")
        self.assertFalse(prueba)

    def test_is_balancedVariosT(self):
        prueba = isBalanced("{[()]}")
        self.assertTrue(prueba)

    def test_is_balancedVariosF(self):
        prueba = isBalanced("{(([()]}")
        self.assertFalse(prueba)

    def test_is_balancedIgualesT(self):
        prueba = isBalanced("(((((())))))")
        self.assertTrue(prueba)

    def test_is_balancedIgualesF(self):
        prueba = isBalanced("((((())))))")
        self.assertFalse(prueba)

    def test_is_balancedIzquierda(self):
        prueba = isBalanced("{[((")
        self.assertFalse(prueba)

    def test_is_balancedDerecha(self):
        prueba = isBalanced("}])")
        self.assertFalse(prueba)