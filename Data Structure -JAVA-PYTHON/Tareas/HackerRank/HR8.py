#Titulo:Cutting Boards
#Link: https://www.hackerrank.com/challenges/board-cutting/problem


import os
from unittest import TestCase


def boardCutting(cost_y, cost_x):
    cost = 0
    seg = [1,1]
    y = sorted(cost_y,reverse=True)
    x = sorted(cost_x,reverse=True)

    for a in range(len(x)+len(y)):
        if len(x) is 0:
            cost+=(seg[0]*y[0])%(10**9+7)
            y.pop(0)
            seg[1]+=1
        elif len(y) is 0:
            cost+=(seg[1]*x[0])%(10**9+7)
            x.pop(0)
            seg[0]+=1
        else:
            if x[0]>y[0]:
                cost+=(seg[1]*x[0])%(10**9+7)
                x.pop(0)
                seg[0]+=1
            elif y[0]>x[0]:
                cost+=(seg[0]*y[0])%(10**9+7)
                y.pop(0)
                seg[1]+=1
            else:
                if seg[1]>seg[0]:
                    cost+=(seg[0]*y[0])%(10**9+7)
                    y.pop(0)
                    seg[1]+=1
                else:
                    cost+=(seg[1]*x[0])%(10**9+7)
                    x.pop(0)
                    seg[0]+=1

    return int(cost%(10**9+7))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        mn = input().split()

        m = int(mn[0])

        n = int(mn[1])

        cost_y = list(map(int, input().rstrip().split()))

        cost_x = list(map(int, input().rstrip().split()))

        result = boardCutting(cost_y, cost_x)

        fptr.write(str(result) + '\n')

    fptr.close()

class Test(TestCase):

    def test_boardCutting(self):
        result = boardCutting([5,3,1,2,4],[1,3,2])

        self.assertEqual(47 ,result)

    def test_boardCutting1(self):
        result = boardCutting([1,1,1],[1,1,1])

        self.assertEqual(15 ,result)

    def test_boardCutting2(self):
        result = boardCutting([2,2,2],[4,4,4])

        self.assertEqual(36,result)

    def test_boardCutting3(self):
        result = boardCutting([7],[14])

        self.assertEqual(28,result)

    def test_boardCutting4(self):
        result = boardCutting([0,0,0,0],[0,0,0,0])

        self.assertEqual(0,result)

    def test_boardCutting5(self):
        result = boardCutting([-2,-4,-9],[-10,3,-6])

        self.assertEqual(999999913,result)