
class TablaAccDirecto: #Creando clase para construir tabla de acceso directo

    def __init__(self):
        self.tabla = [0] * 52
        self.size = 0

    def getIndex(self, caracter):
        #Complejidad
        #Tiempo:O(1)
        #Espacio:O(1)
        if caracter.islower():
            return ord(caracter.lower()) - 71
        return ord(caracter.upper()) - 65

    def buscar_elemento(self, caracter):
        #Complejidad
        #Tiempo:O(1)
        #Espacio:O(1)
        ind = self.getIndex(caracter)
        return self.tabla[ind]

    def insertar(self, caracter, cant_elementos):
        #Complejidad
        #Tiempo:O(1)
        #Espacio:O(1)
        if self.size > 4:
            raise IndexError("NO puede introducirmás de 5 elementos")
        ind = self.getIndex(caracter)
        self.tabla[ind] = cant_elementos
        self.size += 1
        return cant_elementos

    def eliminar(self, caracter):
        #Complejidad
        #Tiempo:O(1)
        #Espacio:O(1)
        ind = self.getIndex(caracter)
        self.tabla[ind] = 0
        self.size -= 1

    def insertarNgrams(self,texto):
        #Complejidad
        #Tiempo:O(N), Recorre el string
        #Espacio:O(1)
        for c in texto:
            cant = self.buscar_elemento(c)
            self.insertar(c, cant + 1)





