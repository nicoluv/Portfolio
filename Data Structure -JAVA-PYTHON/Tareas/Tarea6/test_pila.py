from unittest import TestCase
from pila import Pila


class TestPila(TestCase):

    def test_push_par(self):
        e = Pila()
        e.push(1)
        e.push(2)
        self.assertEqual(e.size, 2)
        self.assertEqual(e.cabeza.valor,2)


    def test_push_impar(self):
        e = Pila()
        e.push('a')
        e.push('b')
        e.push('c')
        self.assertEqual(e.size, 3)
        self.assertEqual(e.cabeza.valor,'c')


    def test_push_unico(self):
        e = Pila()
        e.push(1.2)
        self.assertEqual(e.size, 1)
        self.assertEqual(e.cabeza.valor,1.2)

    def test_push_strVar(self):
        e = Pila()
        e.push("am")
        e.push("lol")
        e.push("ijk")
        e.push("uysgf")
        e.push("hshd")

        self.assertEqual(e.size, 5)
        self.assertEqual(e.cabeza.valor,"hshd")

    def test_pop_par(self):
        e = Pila()
        e.push(1)
        e.push(2)
        e.pop()
        self.assertEqual(e.size, 1)
        self.assertEqual(e.cabeza.valor,1)


    def test_pop_impar(self):

        e = Pila()
        e.push('a')
        e.push('b')
        e.push('c')
        e.pop()
        self.assertEqual(e.size, 2)
        self.assertEqual(e.cabeza.valor,'b')


    def test_pop_unico(self):
        e = Pila()
        e.push(1.2)
        e.pop()
        self.assertEqual(e.size, 0)

    def test_pop_vacia(self):
        e = Pila()
        e.pop()
        self.assertEqual(e.size, 0)
        self.assertEqual(e.pop(),None)


    def test_pop_strVar(self):
        e = Pila()
        e.push("am")
        e.push("lol")
        e.push("ijk")
        e.push("uysgf")
        e.push("hshd")
        e.pop()

        self.assertEqual(e.size, 4)
        self.assertEqual(e.cabeza.valor,"uysgf")

    def test_isEmpty_true(self):
        e = Pila()
        self.assertEqual(e.size, 0)
        self.assertTrue(e.isEmpty())

    def test_isEmpty_false(self):
        e = Pila()
        e.push(3)
        self.assertEqual(e.size, 1)
        self.assertFalse(e.isEmpty())

    def test_search_final(self):
        e = Pila()
        e.push(1)
        e.push(2)
        self.assertEqual(e.size, 2)
        self.assertEqual(e.search(1),1)


    def test_search_medio(self):
        e = Pila()
        e.push('a')
        e.push('b')
        e.push('c')
        self.assertEqual(e.size, 3)
        self.assertEqual(e.search('b'),1)


    def test_search_unico(self):
        e = Pila()
        e.push(1.2)
        self.assertEqual(e.size, 1)
        self.assertEqual(e.search(1.2),0)

    def test_search_Not_Found_Vacia(self):
        e = Pila()
        self.assertEqual(e.size, 0)
        self.assertEqual(e.search(3),-1)

    def test_search_Not_Found_llena(self):
        e = Pila()
        e.push(1.2)
        e.push(8)
        e.push(9)
        self.assertEqual(e.size,3)
        self.assertEqual(e.search(7),-1)

    def test_search_inicio(self):
        e = Pila()
        e.push("am")
        e.push("lol")
        e.push("ijk")
        e.push("uysgf")
        e.push("hshd")

        self.assertEqual(e.size, 5)
        self.assertEqual(e.search("hshd"),0)

    def test_peek_par(self):
        e = Pila()
        e.push(1)
        e.push(2)
        self.assertEqual(e.size, 2)
        self.assertEqual(e.peek().valor,2)


    def test_peek_impar(self):
        e = Pila()
        e.push('a')
        e.push('b')
        e.push('c')
        self.assertEqual(e.size, 3)
        self.assertEqual(e.peek().valor,'c')


    def test_peek_unico(self):
        e = Pila()
        e.push(1.2)
        self.assertEqual(e.size, 1)
        self.assertEqual(e.peek().valor,1.2)

    def test_peek_vacio(self):
        e = Pila()
        self.assertEqual(e.size, 0)
        self.assertEqual(e.peek(),None)

    def test_peek_strVar(self):
        e = Pila()
        e.push("am")
        e.push("lol")
        e.push("ijk")
        e.push("uysgf")
        e.push("hshd")

        self.assertEqual(e.size, 5)
        self.assertEqual(e.peek().valor,"hshd")



