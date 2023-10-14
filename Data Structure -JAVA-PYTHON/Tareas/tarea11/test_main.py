from unittest import TestCase
from main import TablaAccDirecto


class TestTablaAccDirecto(TestCase):

    def test_tableMin(self):
        tabla = TablaAccDirecto()
        tabla.insertarNgrams("asgvd")
        self.assertEqual(tabla.getIndex("a"),26)
        self.assertEqual(tabla.getIndex("s"), 44)
        self.assertEqual(tabla.getIndex("g"), 32)
        self.assertEqual(tabla.getIndex("v"), 47)
        self.assertEqual(tabla.getIndex("d"), 29)

    def test_tableMay(self):
        tabla = TablaAccDirecto()
        tabla.insertarNgrams("BBZWM")
        self.assertEqual(tabla.getIndex("B"),1)
        self.assertEqual(tabla.getIndex("Z"), 25)
        self.assertEqual(tabla.getIndex("W"), 22)
        self.assertEqual(tabla.getIndex("M"), 12)

    def test_tableMayMin(self):
        tabla = TablaAccDirecto()
        tabla.insertarNgrams("Nicol")
        self.assertEqual(tabla.getIndex("N"),13)
        self.assertEqual(tabla.getIndex("i"), 34)
        self.assertEqual(tabla.getIndex("c"), 28)
        self.assertEqual(tabla.getIndex("o"), 40)
        self.assertEqual(tabla.getIndex("l"), 37)

    def test_tableMayMin2(self):
        tabla = TablaAccDirecto()
        tabla.insertarNgrams("CRiSs")
        self.assertEqual(tabla.getIndex("C"), 2)
        self.assertEqual(tabla.getIndex("R"), 17)
        self.assertEqual(tabla.getIndex("i"), 34)
        self.assertEqual(tabla.getIndex("s"), 44)
        self.assertEqual(tabla.getIndex("S"), 18)

    def test_Unico(self):
        tabla = TablaAccDirecto()
        tabla.insertarNgrams("J")
        self.assertEqual(tabla.getIndex("J"), 9)

    def test_table2Num(self):
        tabla = TablaAccDirecto()
        tabla.insertarNgrams("34ffd")
        self.assertEqual(tabla.size,5)
        self.assertEqual(tabla.getIndex("f"), 31)
        self.assertEqual(tabla.getIndex("d"), 29)

