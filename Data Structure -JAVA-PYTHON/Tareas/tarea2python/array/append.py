import os,psutil,time

# X3insert, X3remove, X3in,

if __name__ == '__main__':

    proceso = psutil.Process(os.getpid())

    for x in range(75000000, 1950000000, 75000000):

        mi_arreglo = []
        inicio_ram = proceso.memory_info().rss

        for i in range(x):
            mi_arreglo.append(i)

        tiempo = time.time()
        mi_arreglo.append(x)
        transcurso = time.time() - tiempo
        fin_ram = proceso.memory_info().rss - inicio_ram

        print(x,transcurso,fin_ram)


