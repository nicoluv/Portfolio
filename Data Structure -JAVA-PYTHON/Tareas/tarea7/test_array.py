from unittest import TestCase



class Test(TestCase):

    def test_for_testacm_team(self):
        t = "10101 11110 00010"

        result = ForTestacmTeam(t.split())
        self.assertEqual([5,1],result)

    def test_for_testacm_team2(self):
        t = "11101 10101 11001 10111 10000 01110"

        result = ForTestacmTeam(t.split())
        self.assertEqual([5,6],result)

    def test_for_testacm_team3(self):
        t = "11101 00010"

        result = ForTestacmTeam(t.split())
        self.assertEqual([5,1],result)

    def test_for_testacm_team4(self):
        t = "11101 00010 10111 10000 01110 10101 11110 00010"

        result = ForTestacmTeam(t.split())
        self.assertEqual([5,9],result)

    def test_for_testacm_team5(self):
        t = "11101"

        result = ForTestacmTeam(t)
        self.assertEqual([1,10],result)


def ForTestacmTeam(topic):

    arr = []
    for i in range(len(topic)):

        for j in range(i + 1, len(topic)):
            e = int(topic[i]) + int(topic[j])

            arr.append(len(str(e)) - str(e).count("0"))
    n_max = max(arr)
    return [n_max, arr.count(n_max)]




