#Titulo:Non-Divisible Subset
#Link: https://www.hackerrank.com/challenges/non-divisible-subset/problem

import os
from unittest import TestCase

def nonDivisibleSubset(k, S):
    res = [0 for i in range (0, k)]
    for i in S:
        res[i%k] += 1
    maxN = 1 if res[0]>0 else 0
    for i in range(1,k//2+1):
        if i != k-i:
            maxN += max(res[i],res[k-i])
        else:
            maxN += 1
    return maxN

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()


class Test(TestCase):

    def test_nonDivisibleSubset(self):
        result = nonDivisibleSubset(3, [1, 7, 2, 4])

        self.assertEqual(3,result)

    def test_nonDivisibleSubset2(self):
        result = nonDivisibleSubset(7, [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436])

        self.assertEqual(11,result)

    def test_nonDivisibleSubset_par(self):
        result = nonDivisibleSubset(4, [2, 6, 8, 12])

        self.assertEqual(2,result)

    def test_nonDivisibleSubset_impar(self):
        result = nonDivisibleSubset(1, [3, 7, 9, 15])

        self.assertEqual(1,result)

    def test_nonDivisibleSubset_(self):
        result = nonDivisibleSubset(10, [ 900, 10500])

        self.assertEqual(2,result)