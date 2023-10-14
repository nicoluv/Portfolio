class Nodo(object):

    def __init__(self, valor=None, sig=None, anterior=None):
        self.valor = valor
        self.sig = sig
        self.anterior = anterior


class DoblementeEnlazada(object):

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0

    def add(self, valor):

        nuevo = Nodo(valor, None, None)

        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = self.cabeza
        else:
            nuevo.anterior = self.cola
            self.cola.sig = nuevo
            self.cola = nuevo
        self.size += 1

    def add_all(self,listD):

        for x in listD:
            self.add(x)



    def add_indice(self, valor, indice):


        nuevo = Nodo(valor,None,None)

        if (indice < 0):
            return -1

        elif (indice == 0):

            nuevo.sig = self.cabeza;
            self.cabeza.anterior = nuevo;
            self.cabeza = nuevo;

        elif(indice > self.size):
            return -1

        else:

            temp = self.cabeza
            for x in range(0, indice - 1):
                if (temp != None):
                    temp = temp.sig

            if (temp != None):
                nuevo.sig = temp.sig
                nuevo.anterior = temp
                temp.sig = nuevo
                if (nuevo.sig != None):
                    nuevo.sig.anterior = nuevo

        self.size+=1

    def contains(self, valor):

         for nodo in self.__iter__():

            if valor == nodo:
                return True

         return False

    def remove(self, nodo):

        if nodo.anterior is None:
            self.cabeza = nodo.sig
        else:
            nodo.anterior.sig = nodo.sig

        if nodo.sig is None:
            self.cola = nodo.anterior
        else:
            nodo.sig.anterior = nodo.anterior
        self.size-=1

    def get(self, indice):

        actual = self.cabeza

        for x in range(indice):

            if actual is None:
                return None
            actual = actual.sig

        return actual


    def clear(self):

        self.cabeza = None
        self.cola = None
        self.size = 0

    def clone(self,listaD):

        temporal = self.add_all(listaD)


        return temporal

    def index(self, elemento):

        actual = self.cabeza
        indice = 0

        while actual != None:

            if actual.valor == elemento:
                return indice
            actual = actual.sig
            indice += 1
        return -1


    def __next__(self): #R

        if self.cabeza is not None:
            valor = self.cabeza.valor
            self.actual = self.cabeza.sig
            return valor

        else:
            raise StopIteration


    def __iter__(self):

        actual = self.cabeza

        while actual:
            valor = actual.valor
            actual = actual.sig
            yield valor
