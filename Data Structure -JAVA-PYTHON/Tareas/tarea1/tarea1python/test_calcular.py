from unittest import TestCase
from Main import calcular

class TestCalcular(TestCase):

    def test_calcularSumaSimple(self):

        result = calcular("0101 + 0101")
        self.assertEqual(result, 10)

    def test_calcularrestaSimple(self):

        result = calcular("0101 - 0101")
        self.assertEqual(result, 0)

    def test_calcularMultSimple(self):

        result = calcular("1010 * 1010")
        self.assertEqual(result, 100)

    def test_calcularDivtSimple(self):

        result = calcular("1010 / 0010")
        self.assertEqual(result, 5)

    def test_calcularOperacionesMultiplesIguales(self):

        resultDiv = calcular("1010 /  0010 / 0001")
        result = calcular("1010 * 0010 * 1010")
        resultSum = calcular("1010 +  0010 + 0001")
        resultREs = calcular("1010 -  0010 - 0001")
        self.assertEqual(result, 200)
        self.assertEqual(resultDiv, 5)
        self.assertEqual(resultSum, 13)
        self.assertEqual(resultREs, 7)

    def test_calcularOperacionesMultiplesDiferentes(self):

        result = calcular("1010 * 0010 / 1010")
        resultDiv = calcular("1010 /  0010 - 0001")
        resultSum = calcular("1010 +  0010 * 0001")
        resultREs = calcular("1010 -  0010 + 0001 * 0001 / 0101")
        self.assertEqual(result, 2.0)
        self.assertEqual(resultDiv, 4)
        self.assertEqual(resultSum, 12)
        self.assertEqual(resultREs, 1.8)

    def test_calcularTodosOperadores(self):

        result = calcular("1010 -  0101 + 0001 * 0010 / 0010")
        self.assertEqual(result, 6)

    def test_calcularOPGrande(self):

        result = calcular("1010 + 1010 + 1010 + 1010 + 1010 + 1010 + 1010 + 1010 + 1010 + 1010 * 0001")
        self.assertEqual(result, 100)

    def test_noBinario(self):

        result = calcular("1010 + 2 + 1010")
        self.assertEqual(result, 20)

    def test_errorOperador(self):

        result = calcular("1010 = 1010")
        self.assertEqual(result, 10)