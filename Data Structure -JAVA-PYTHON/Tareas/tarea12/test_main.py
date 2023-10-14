from unittest import TestCase
from main import fibonacci_mem

class Test(TestCase):
    def test_fibonacci_mem_impares(self):
        result = fibonacci_mem(1)
        result1 = fibonacci_mem(3)
        result2 = fibonacci_mem(5)
        result3 = fibonacci_mem(7)
        result4 = fibonacci_mem(9)
        self.assertEqual(result,1)
        self.assertEqual(result2,5)
        self.assertEqual(result3, 13)
        self.assertEqual(result4, 34)
        self.assertEqual(result1, 2)

    def test_fibonacci_mem2_pares(self):
        result = fibonacci_mem(2)
        result1 = fibonacci_mem(4)
        result2 = fibonacci_mem(6)
        result3 = fibonacci_mem(8)
        result4 = fibonacci_mem(10)
        self.assertEqual(result,1)
        self.assertEqual(result2,8)
        self.assertEqual(result3, 21)
        self.assertEqual(result4, 55)
        self.assertEqual(result1, 3)

    def test_fibonacci_mem2_grande(self):
        result = fibonacci_mem(600)
        result1 = fibonacci_mem(97)
        result2 = fibonacci_mem(88)
        result3 = fibonacci_mem(201)
        result4 = fibonacci_mem(501)
        self.assertEqual(result,110433070572952242346432246767718285942590237357555606380008891875277701705731473925618404421867819924194229142447517901959200)
        self.assertEqual(result2,1100087778366101931)
        self.assertEqual(result3, 453973694165307953197296969697410619233826)
        self.assertEqual(result4, 225591516161936330872512695036072072046011324913758190588638866418474627738686883405015987052796968498626)
        self.assertEqual(result1, 83621143489848422977)