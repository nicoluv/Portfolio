#Titulo: chief hopper
#Link: https://www.hackerrank.com/challenges/chief-hopper/problem

import math
import os
from unittest import TestCase

def chiefHopper(arr):
    energia = 0
    for n in reversed(arr):
        energia = math.ceil((energia + n)/2)
    return energia

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

class Test(TestCase):

    def test_chiefHopper(self):
        result = chiefHopper([1, 6, 4])

        self.assertEqual(3,result)

    def test_chiefHopper1(self):
        result = chiefHopper([4, 4, 4])

        self.assertEqual(4,result)

    def test_chiefHopper2(self):
        result = chiefHopper([3, 4, 3, 2, 4])

        self.assertEqual(4,result)

    def test_chiefHopper3(self):
        result = chiefHopper([0, 0, 0, 0, 0])

        self.assertEqual(0,result)

    def test_chiefHopper4(self):
        result = chiefHopper([-7, -4, -10])

        self.assertEqual(-5,result)

    def test_chiefHopper5(self):
        result = chiefHopper([9, 0, -10])

        self.assertEqual(4,result)