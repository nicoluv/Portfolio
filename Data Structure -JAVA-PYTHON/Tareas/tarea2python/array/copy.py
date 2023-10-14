import os,psutil,time

#add, append, clear, copy, index, insert, remove, sort, in

if __name__ == '__main__':

    proceso = psutil.Process(os.getpid())

    for x in range(750000, 19500000, 750000):

        mi_arreglo = []
        inicio_ram = proceso.memory_info().rss

        for i in range(x):
            mi_arreglo.append(i)

        tiempo = time.time()
        mi_arreglo.copy()
        transcurso = time.time() - tiempo
        ram_usada = proceso.memory_info().rss - inicio_ram

        print(x, transcurso, ram_usada)

