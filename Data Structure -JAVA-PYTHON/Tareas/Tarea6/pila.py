class Nodo(object):

    def __init__(self, valor=None, sig=None, anterior=None):
        self.valor = valor
        self.sig = sig
        self.anterior = anterior

class Pila(object):

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0

    def push(self, valor): #Complejidad de tiempo O(1)

        nuevo = Nodo(valor, None, None)

        if self.cabeza is None:
            self.cabeza = Nodo(valor, None, None)

        else:
            self.cabeza.anterior = nuevo
            nuevo.sig = self.cabeza
            nuevo.anterior = None
            self.cabeza = nuevo
        self.size+=1


    def pop(self): #Complejidad de tiempo O(1)

        if self.cabeza is None:
            return None

        elif self.cabeza.sig is None:
            actual = self.cabeza.valor
            self.cabeza = None
            self.size -= 1
            return actual
        else:
            actual = self.cabeza.valor
            self.cabeza = self.cabeza.sig
            self.cabeza.anterior = None
            self.size-=1
            return actual


    def isEmpty(self): #Complejidad de tiempo O(1)

        if self.cabeza is None:
            return True
        else:
            return False

    def peek(self): #Complejidad de tiempo O(1)

        if self.isEmpty():
            return None
        else:
            return self.cabeza

    def search(self,elemento):#Complejidad de tiempo O(n)

        indice = 0
        actual = self.cabeza

        while actual:
            if actual.valor == elemento:
                return indice
            actual = actual.sig
            indice +=1
        return -1
