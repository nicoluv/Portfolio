#Titulo:Bigger is Greater
#Link: https://www.hackerrank.com/challenges/bigger-is-greater/problem


from unittest import TestCase
import os

def biggerIsGreater(w):
    org = w
    w = list(w)
    n = len(w)
    zeta = n
    for i in range(n-2,-1,-1):
        j = [b for b in w[i+1:n] if b>w[i]]
        if len(j)!=0:
            zeta=i
            k = min(j)
            ind = i+(w[i+1:].index(k))+1
            w.insert(i,k)
            del w[ind+1]
            break
    nuevo = ''.join(w[:zeta+1]+sorted(w[zeta+1:n]))
    if nuevo==org:
        nuevo='no answer'
    return nuevo


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()

class Test(TestCase):

    def test_biggerIsGreater(self):
        result = biggerIsGreater("ab")

        self.assertEqual("ba",result)

    def test_biggerIsGreater_igual(self):
        result = biggerIsGreater("bb")

        self.assertEqual("no answer",result)

    def test_biggerIsGreater_dif(self):
        result = biggerIsGreater("hefg")

        self.assertEqual("hegf",result)


    def test_biggerIsGreater_(self):
        result = biggerIsGreater("dhck")

        self.assertEqual("dhkc",result)

    def test_biggerIsGreater_larga(self):
        result = biggerIsGreater("fedcbabcd")

        self.assertEqual("fedcbabdc",result)

    def test_biggerIsGreater_s(self):
       result = biggerIsGreater("dcbb")

       self.assertEqual("no answer", result)
