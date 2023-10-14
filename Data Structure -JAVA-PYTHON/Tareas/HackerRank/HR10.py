#Titulo: fraudulent activity notififications
#Link: https://www.hackerrank.com/challenges/fraudulent-activity-notififications/problem

from unittest import TestCase


import os

def activitynotififications(expenditure, d):
    freq = {}
    notif = 0

    def encontrar(ind):
        total = 0
        for i in range(201):
            if i in freq:
                total = total + freq[i]
            if total >= ind:
                return i

    for i in range(len(expenditure) - 1):
        if expenditure[i] in freq:
            freq[expenditure[i]] += 1
        else:
            freq[expenditure[i]] = 1

        if i >= d - 1:
            if d % 2 == 0:
                m = (encontrar(d // 2) + encontrar(d // 2 + 1)) / 2
            else:
                m = encontrar(d / 2)

            if expenditure[i + 1] >= (m * 2):
                notif += 1

            freq[expenditure[i - d + 1]] -= 1

    return notif


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activitynotififications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()


class Test(TestCase):

    def test_activitynotififications(self):
        result = activitynotififications([2, 3, 4, 2, 3, 6, 8, 4, 5],5)
        self.assertEqual(2,result)

    def test_activitynotififications1(self):
        result = activitynotififications([10, 100, 4, 200, 3, 8, 5],6)
        self.assertEqual(0,result)

    def test_activitynotififications2(self):
        result = activitynotififications([10, 20, 30, 40, 50],3)
        self.assertEqual(1,result)

    def test_activitynotififications3(self):
        result = activitynotififications([0, 0, 0, 0, 0],4)
        self.assertEqual(1,result)

    def test_activitynotififications4(self):
        result = activitynotififications([10, -6, -9, 7],7)
        self.assertEqual(0,result)

    def test_activitynotififications5(self):
        result = activitynotififications([2, 2, 2],3)
        self.assertEqual(0,result)