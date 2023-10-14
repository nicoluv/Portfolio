from unittest import TestCase
from main import ArbolRojoNegro
from main import Nodo


class Test(TestCase):

    def test_insertar(self):
        arbol = ArbolRojoNegro()
        self.assertEqual(0, arbol.size)  # no se han insertado
        n1 = Nodo(1)
        arbol.insertar(n1)
        self.assertEqual(1, arbol.size)  # se ha insertado 1

        n2 = Nodo(3)
        n3 = Nodo(2)
        arbol.insertar(n2)
        arbol.insertar(n3)
        self.assertEqual(3, arbol.size)  # impar

        n4 = Nodo(10)
        arbol.insertar(n4)
        self.assertEqual(4, arbol.size)  # par

        n5 = Nodo(9)
        n6 = Nodo(4)
        n7 = Nodo(6)
        n8 = Nodo(5)
        n9 = Nodo(7)
        n10 = Nodo(15)
        arbol.insertar(n5)
        arbol.insertar(n6)
        arbol.insertar(n7)
        arbol.insertar(n8)
        arbol.insertar(n9)
        arbol.insertar(n10)
        self.assertEqual(10, arbol.size)  # multiples

    def test_eliminar(self):

        arbol2 = ArbolRojoNegro()
        n1 = Nodo(1)
        arbol2.insertar(n1)
        self.assertEqual(1, arbol2.size)  # no se han eliminado

        n2 = Nodo(3)
        arbol2.insertar(n2)
        arbol2.eliminar(n2)
        self.assertEqual(2, arbol2.size)  # se elimina 1

        n4 = Nodo(10)
        arbol2.insertar(n4)
        arbol2.eliminar(n1)
        arbol2.eliminar(n4)
        self.assertEqual(1, arbol2.size)

        n5 = Nodo(9)
        n6 = Nodo(4)
        n7 = Nodo(6)

        arbol2.insertar(n5)
        arbol2.insertar(n6)
        arbol2.insertar(n7)

        arbol2.eliminar(n5)
        arbol2.eliminar(n6)
        arbol2.eliminar(n7)
        self.assertEqual(3, arbol2.size)

        n8 = Nodo(15)
        arbol2.insertar(n8)
        arbol2.eliminar(n8)
        arbol2.eliminar(n7)
        self.assertEqual(2, arbol2.size)

    def test_obtener_hijo_de_nodo(self):
        ar= ArbolRojoNegro()
        n1 = Nodo(1)
        n5 = Nodo(9)
        n6 = Nodo(4)
        n7 = Nodo(6)
        n8 = Nodo(5)
        n9 = Nodo(7)
        ar.insertar(n1)
        ar.insertar(n5)
        ar.insertar(n6)
        ar.insertar(n7)
        ar.insertar(n8)
        ar.insertar(n9)
        self.assertEqual(n6, ar.obtener_hijo_de_nodo(n1)) # nodo mas peq
        self.assertEqual(n8, ar.obtener_hijo_de_nodo(n6)) # nodo medio
        self.assertEqual(n5, ar.obtener_hijo_de_nodo(n9)) # nodo mayor

    def test_obtener_padre_de_nodo(self):
        ar= ArbolRojoNegro()
        n1 = Nodo(1)
        n5 = Nodo(9)
        n6 = Nodo(4)
        n7 = Nodo(6)
        n8 = Nodo(5)
        n9 = Nodo(7)
        ar.insertar(n1)
        ar.insertar(n5)
        ar.insertar(n6)
        ar.insertar(n7)
        ar.insertar(n8)
        ar.insertar(n9)

        self.assertEqual(n6.valor, ar.obtener_padre_de_nodo(n7))
        self.assertEqual(n6.valor, ar.obtener_padre_de_nodo(n8))
        self.assertEqual(n7.valor, ar.obtener_padre_de_nodo(n5))
        self.assertEqual(n7.valor, ar.obtener_padre_de_nodo(n9))

    def test_rotaciones_cambiosColor(self):
        ar= ArbolRojoNegro()
        n1 = Nodo(1)
        n5 = Nodo(9)
        n6 = Nodo(4)
        n7 = Nodo(6)
        n8 = Nodo(5)
        n9 = Nodo(7)
        ar.insertar(n1)
        ar.insertar(n5)
        ar.insertar(n6)
        ar.insertar(n7)
        ar.insertar(n8)
        ar.insertar(n9)

        self.assertTupleEqual((10,3),ar.obtener_rotaciones_cambiosColor())

        ar.eliminar(n1)
        ar.eliminar(n5)
        self.assertTupleEqual((13,4),ar.obtener_rotaciones_cambiosColor())

        n2= Nodo(110)
        n20 = Nodo(113)
        ar.insertar(n2)
        ar.insertar(n20)
        ar.eliminar(n2)
        self.assertTupleEqual((15,5),ar.obtener_rotaciones_cambiosColor())




