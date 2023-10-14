#ACM ICPC Team
#Link: https://www.hackerrank.com/challenges/acm-icpc-team/problem
#Resumen: Varias personas asistirán a las Finales Mundiales de ACM-ICPC.
# Dadas las cadenas binarias, determine la cantidad máxima de temas que puede conocer un equipo de 2 personas.
# También determine la cantidad de equipos que conocen la cantidad máxima de temas.

import os


def acmTeam(topic):

    #COMPLEJIDAD
    #Tiempo O(n^4) Dos for iteran la lista y hay un  .count de un string, que es O(n) según
    # https://stackoverflow.com/questions/35855748/whats-the-computational-cost-of-count-operation-on-strings-python  y un max.
    #Espacio O(n)

    arr = []
    for i in range(len(topic)):

        for j in range(i + 1, len(topic)):
            e = int(topic[i]) + int(topic[j])

            arr.append(len(str(e)) - str(e).count("0"))
    n_max = max(arr)
    return [n_max, arr.count(n_max)]

#Main para probar en HackerRank

"""
if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
"""