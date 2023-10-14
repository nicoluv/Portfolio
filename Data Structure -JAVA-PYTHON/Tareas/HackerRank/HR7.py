#Titulo: making-candies
#Link: https://www.hackerrank.com/challenges/making-candies/problem



import math
import os
from unittest import TestCase

def minimumPasses(m, w, p, n):
    dias = 0
    candies = 0
    res = math.ceil(n / (m * w))

    while dias < res:
        if p > candies:
            diasNecesarios = math.ceil((p - candies) / (m * w))
            candies += diasNecesarios * m * w
            dias += diasNecesarios

        dif = abs(m - w)
        disp = candies // p
        comp = min(dif, disp)

        if m < w:
            m += comp
        else:
            w += comp

        rest = disp - comp
        m += rest // 2
        w += rest - rest // 2
        candies -= disp * p

        candies += m * w
        dias += 1

        restantes = max(n - candies, 0)
        res = min(res, dias + math.ceil(restantes / (m * w)))

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mwpn = input().split()

    m = int(mwpn[0])

    w = int(mwpn[1])

    p = int(mwpn[2])

    n = int(mwpn[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()

class Test(TestCase):

    def test_minimumPasses(self):
        result = minimumPasses(3, 1, 2, 12)

        self.assertEqual(3,result)

    def test_minimumPasses2(self):
        result = minimumPasses(30, 10, 20, 120)

        self.assertEqual(1,result)

    def test_minimumPasses3(self):
        result = minimumPasses(6, 11, 32, 812)

        self.assertEqual(8,result)

    def test_minimumPasses4(self):
        result = minimumPasses(20, 10, 30, 7)

        self.assertEqual(1,result)

    def test_minimumPasses5(self):
        result = minimumPasses(1, 1, 1, 1)

        self.assertEqual(1,result)

    def test_minimumPasses6(self):
        result = minimumPasses(6,6 , 6, 6)

        self.assertEqual(1,result)

    def test_minimumPasses6(self):
        result = minimumPasses(-1,-5 , -10, 1)

        self.assertEqual(1,result)