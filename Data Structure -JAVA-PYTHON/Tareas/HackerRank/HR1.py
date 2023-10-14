# TITULO: Plus Minus
# LINK: https://www.hackerrank.com/challenges/plus-minus/problem

from unittest import TestCase


def plusMinus(arr):
    pos = sum(x > 0 for x in arr) / len(arr)
    neg = sum(x < 0 for x in arr) / len(arr)
    cero = sum(x == 0 for x in arr) / len(arr)

    return (pos, neg, cero)


class Test(TestCase):

    def test_plusMinus_todo(self):
        result = plusMinus([-4, 3, -9, 0, 4, 1])
        self.assertTupleEqual((0.5, 0.3333333333333333, 0.16666666666666666), result)

    def test_plusMinus_t_par(self):
        result = plusMinus([-2, 6, -90, 0, 4, 0])
        self.assertTupleEqual((0.3333333333333333, 0.3333333333333333, 0.3333333333333333), result)

    def test_plusMinus_pos_neg(self):
        result = plusMinus([-8, 3, -1, 10, -4, 1])
        self.assertTupleEqual((0.5, 0.5, 0.0), result)

    def test_plusMinus_pos(self):
        result = plusMinus([4, 3, 9, 0, 4, 1])
        self.assertTupleEqual((0.8333333333333334, 0.0, 0.16666666666666666), result)

    def test_plusMinus_neg(self):
        result = plusMinus([-40, -30, -9, -8, -4, -10])
        self.assertTupleEqual((0.0, 1.0, 0.0), result)

    def test_plusMinus_cero(self):
        result = plusMinus([0, 0, 0, 0, 0, 0])
        self.assertTupleEqual((0.0, 0.0, 1.0), result)
