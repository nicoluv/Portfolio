import time
from listadoblemente import DoblementeEnlazada
#Para medir el tiempo de ejecucion de mis funciones

if __name__ == '__main__':


    for x in range(75000, 1950000, 75000):

        lista = DoblementeEnlazada()
   #     lista2 = DoblementeEnlazada() para clone y add_all


        for i in range(x):
            lista.add(i)
          #  lista2.add(i)


        tiempo = time.time()
        lista.clear()
        transcurso = time.time() - tiempo

        #print(transcurso)