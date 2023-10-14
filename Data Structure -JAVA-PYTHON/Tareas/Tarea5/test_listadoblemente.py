from unittest import TestCase
from listadoblemente import DoblementeEnlazada


class TestDoblementeEnlazada(TestCase):

    def test_add1(self):
        e = DoblementeEnlazada()
        e.add(1)
        self.assertEqual(e.size, 1)

    def test_add_par(self):
        e = DoblementeEnlazada()
        e.add(1)
        e.add(3)
        self.assertEqual(e.size,2)

    def test_addVarios(self):
        e = DoblementeEnlazada()
        e.add(1)
        e.add(2)
        self.assertEqual(e.size, 2)
        e.add(3)
        self.assertEqual(e.size, 3)

    def test_add_all_varios(self):
        elemento = DoblementeEnlazada()

        elemento.add('P')
        elemento.add('T')
        elemento.add('C')
        elemento.add('Q')
        elemento.add('N')

        vacia = DoblementeEnlazada()
        vacia.add_all(elemento)
        self.assertEqual(vacia.size, 5)

    def test_add_all_uno(self):
        elemento = DoblementeEnlazada()
        elemento.add('P')
        vacia = DoblementeEnlazada()
        vacia.add_all(elemento)
        self.assertEqual(vacia.size, 1)

    def test_add_indice_primero(self):
        lista = DoblementeEnlazada()
        lista.add(1)
        lista.add(2)
        lista.add(3)
        self.assertEqual(lista.size, 3)
        lista.add_indice(8,0)
        self.assertEqual(lista.size, 4)
        self.assertEqual(lista.get(0).valor,8)


    def test_add_indice_medio(self):

        list = DoblementeEnlazada()
        list.add('n')
        list.add('p')
        list.add('l')
        self.assertEqual(list.size, 3)
        list.add_indice('nic',1)
        self.assertEqual(list.size, 4)
        self.assertEqual(list.get(1).valor,'nic')

    def test_add_indice_final(self):

        list = DoblementeEnlazada()
        list.add('n')
        list.add('p')
        list.add('l')
        self.assertEqual(list.size, 3)
        list.add_indice('nicol',2)
        self.assertEqual(list.size, 4)
        self.assertEqual(list.get(2).valor,'nicol')

    def test_add_indice_OutBound(self):

        list = DoblementeEnlazada()
        list.add('n')
        list.add('p')
        list.add('l')
        self.assertEqual(list.size, 3)
        self.assertEqual( list.add_indice('nicol',5),-1)

    def test_add_indice_Menor0(self):

        list = DoblementeEnlazada()
        list.add('n')
        list.add('p')
        list.add('l')
        self.assertEqual(list.size, 3)
        self.assertEqual( list.add_indice('nicol',-5),-1)


    def test_containsTrue(self):

        lista = DoblementeEnlazada()
        lista.add(1)
        lista.add(2)
        lista.add(3)
        self.assertTrue(lista.contains(2))

    def test_containsFalse(self):

        lista = DoblementeEnlazada()
        lista.add(1)
        lista.add(2)
        lista.add(3)
        self.assertFalse(lista.contains(4))

    def test_remove_inicio(self):
        list = DoblementeEnlazada()
        list.add(1)
        list.add(2)
        list.add(3)

        list.remove(list.get(0))

        self.assertEqual(list.size, 2)

    def test_remove_medio(self):
        list = DoblementeEnlazada()
        list.add(1)
        list.add(2)
        list.add(3)

        list.remove(list.get(1))

        self.assertEqual(list.size, 2)

    def test_remove_final(self):
        list = DoblementeEnlazada()
        list.add(1)
        list.add(2)
        list.add(3)
        list.add(4)

        list.remove(list.get(3))

        self.assertEqual(list.size, 3)

    def test_get_inicio(self):

        list = DoblementeEnlazada()
        list.add(1)
        list.add(2)
        list.add(3)

        self.assertEqual(list.get(0).valor, 1)

    def test_get_medio(self):

        list = DoblementeEnlazada()
        list.add(1)
        list.add(2)
        list.add(3)

        self.assertEqual(list.get(1).valor, 2)

    def test_get_final(self):

        list = DoblementeEnlazada()
        list.add(1)
        list.add(2)
        list.add(3)

        self.assertEqual(list.get(2).valor, 3)

    def test_clear_uno(self):

        list = DoblementeEnlazada()
        list.add(1)


        self.assertEqual(list.size, 1)
        list.clear()
        self.assertEqual(list.size, 0)

    def test_clear_varios(self):

        list = DoblementeEnlazada()
        list.add(1)
        list.add(2)
        list.add(3)

        self.assertEqual(list.size, 3)
        list.clear()
        self.assertEqual(list.size, 0)

    def test_clone_variosItems(self):

        list = DoblementeEnlazada()
        vacia = DoblementeEnlazada()
        list.add(1)
        list.add(2)
        list.add(3)

        vacia.clone(list)
        self.assertEqual(vacia.size, 3)
        self.assertEqual(list.size, 3)
        self.assertEqual(vacia.get(0).valor, 1)

    def test_clone_un_Item(self):

        list = DoblementeEnlazada()
        vacia = DoblementeEnlazada()
        list.add(5)

        vacia.clone(list)
        self.assertEqual(vacia.size, 1)
        self.assertEqual(list.size, 1)
        self.assertEqual(vacia.get(0).valor, 5)

    def test_clone_vacio(self):

        list = DoblementeEnlazada()
        vacia = DoblementeEnlazada()

        vacia.clone(list)
        self.assertEqual(vacia.size, 0)
        self.assertEqual(list.size, 0)


    def test_next_inicio(self):

        list = DoblementeEnlazada()
        list.add('n')
        list.add('p')
        list.add('l')

        self.assertEqual(list.__next__(), 'n')

    def test_iter_(self):

        list = DoblementeEnlazada()
        list.add('n')
        list.add('p')
        list.add('l')
        vacia = DoblementeEnlazada()

        for node in list.__iter__():
            vacia.add(node)

        self.assertEqual(vacia.size, 3)



    def test_index_inicio(self):

        list = DoblementeEnlazada()
        list.add(1)
        list.add(2)
        list.add(3)

        self.assertEqual(list.index(1), 0)

    def test_index_medio(self):

        list = DoblementeEnlazada()
        list.add(1)
        list.add(2)
        list.add(3)

        self.assertEqual(list.index(2), 1)

    def test_index_final(self):

        list = DoblementeEnlazada()
        list.add(1)
        list.add(2)
        list.add(3)

        self.assertEqual(list.index(3), 2)

    def test_index_Not_FoundPos(self):

        list = DoblementeEnlazada()
        list.add(1)
        list.add(2)
        list.add(3)

        self.assertEqual(list.index(8), -1)

    def test_index_Not_FoundNeg(self):

        list = DoblementeEnlazada()
        list.add(1)
        list.add(2)
        list.add(3)

        self.assertEqual(list.index(-12), -1)



