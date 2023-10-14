# Balanced Brackets
# link del problema: https://www.hackerrank.com/challenges/balanced-brackets/problem

# Resumen: Debemos crear un programa que se asegure de que los corchetes, parentesis,etc. de una sentencia estan en equilibrio.
# Una secuencia de corchetes está equilibrada si :
# No contiene corchetes incomparables.
# El subconjunto de corchetes encerrados dentro de los límites de un par de corchetes coincidentes también es un par de corchetes emparejados.
# Si una cadena está balanceada, devuelve YES. De lo contrario, devuelva NO.

def valido(izq, der):# O(1) tiempo y espacio

    bandera = False
    if izq == '(' and der == ')':
         bandera = True
    elif izq == '[' and der == ']':
        bandera = True
    elif izq == '{' and der == '}':
        bandera = True

    return bandera


def isBalanced(cadena):

    #COMPLEJIDAD
    #Tiempo O(n)
    #Espacio O(n)

    pila = []

    for caracter in cadena:

        if caracter == '{' or caracter == '(' or caracter == '[':
            pila.append(caracter)

        else:
            if len(pila) == 0:
                return False
            last = pila.pop()
            if not valido(last, caracter):
                return False

    if len(pila) != 0:
        return False

    return True


if __name__ == '__main__':

        s = input()
        if isBalanced(s):
            print("YES")
        else:
            print("NO")
