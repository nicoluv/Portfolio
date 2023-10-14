import os,psutil,time


if __name__ == '__main__':

    proceso = psutil.Process(os.getpid())

    for x in range(750000, 19500000, 750000):

        mi_arreglo = []
        inicio_ram = proceso.memory_info().rss

        for i in range(x):
            mi_arreglo.append(i)

        tiempo = time.time()
        mi_arreglo.remove(x/2)# pos 0, luego en, len(mi_arreglo)/2,len(mi_arreglo)-1 al final
        transcurso = time.time() - tiempo
        ram_usada = proceso.memory_info().rss - inicio_ram

        print(transcurso)

