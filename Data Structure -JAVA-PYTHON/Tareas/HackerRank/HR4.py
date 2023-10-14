# Titulo : Balanced Brackets
# link del problema: https://www.hackerrank.com/challenges/balanced-brackets/problem

from unittest import TestCase

def valido(izq, der):# O(1) tiempo y espacio

    bandera = False
    if izq == '(' and der == ')':
         bandera = True
    elif izq == '[' and der == ']':
        bandera = True
    elif izq == '{' and der == '}':
        bandera = True

    return bandera


def isBalanced(cadena):

    pila = []

    for caracter in cadena:

        if caracter == '{' or caracter == '(' or caracter == '[':
            pila.append(caracter)

        else:
            if len(pila) == 0:
                return False
            last = pila.pop()
            if not valido(last, caracter):
                return False

    if len(pila) != 0:
        return False

    return True


if __name__ == '__main__':

        s = input()
        if isBalanced(s):
            print("YES")
        else:
            print("NO")



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