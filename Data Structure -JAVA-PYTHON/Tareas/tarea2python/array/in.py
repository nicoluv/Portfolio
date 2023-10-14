import os,psutil,time

if __name__ == '__main__':

    proceso = psutil.Process(os.getpid())

    for x in range(750000, 19500000, 750000):

        mi_arreglo = []
        inicio_ram = proceso.memory_info().rss

        for i in range(x):
            mi_arreglo.append(i)

        tiempo = time.time()
        0 in mi_arreglo #x, x/2, 0,
        transcurso = time.time() - tiempo
        fin_ram = proceso.memory_info().rss - inicio_ram

        print(transcurso)