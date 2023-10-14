from unittest import TestCase
from main import Grafo

class TestGrafo(TestCase):

    def test_alg_kruskalImp(self):
        g = Grafo(5)
        g.insertarArista(0, 1, 8)
        g.insertarArista(0, 2, 5)
        g.insertarArista(1, 2, 9)
        g.insertarArista(1, 3, 11)
        g.insertarArista(2, 3, 15)
        g.insertarArista(2, 4, 10)
        g.insertarArista(3, 4, 7)

        self.assertListEqual(g.alg_kruskal(),[[0, 2, 5], [3, 4, 7], [0, 1, 8], [2, 4, 10]])

    def test_alg_kruskalSimpleP(self):
        g = Grafo(4)
        g.insertarArista(0, 1, 10)
        g.insertarArista(0, 2, 6)
        g.insertarArista(0, 3, 5)
        g.insertarArista(1, 3, 15)
        g.insertarArista(2, 3, 4)

        self.assertListEqual(g.alg_kruskal(),[[2, 3, 4], [0, 3, 5], [0, 1, 10]])

    def test_alg_kruskalSimplePeq(self):
        g = Grafo(2)
        g.insertarArista(0, 1, 10)
        g.insertarArista(2, 2, 60)
        g.insertarArista(4, 3, 150)

        self.assertListEqual(g.alg_kruskal(),[[0, 1, 10]])

    def test_alg_kruskalSimple10(self):
        g = Grafo(9)
        g.insertarArista(0, 1, 10)
        g.insertarArista(0, 2, 6)
        g.insertarArista(1, 3, 15)
        g.insertarArista(1, 4, 10)
        g.insertarArista(3, 5, 6)
        g.insertarArista(4, 6, 15)
        g.insertarArista(5, 7, 10)
        g.insertarArista(6, 8, 6)
        g.insertarArista(7, 10, 15)

        self.assertListEqual(g.alg_kruskal(),[[0, 2, 6], [3, 5, 6], [6, 8, 6], [0, 1, 10], [1, 4, 10], [5, 7, 10], [1, 3, 15], [4, 6, 15]])
