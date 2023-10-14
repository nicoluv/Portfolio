#add, clear, copy, remove, in
import os,psutil,time

if __name__ == '__main__':

    proceso = psutil.Process(os.getpid())

    for x in range(750000, 19500000, 750000):

        mi_set = set()
        inicio_ram = proceso.memory_info().rss

        for i in range(x):
            mi_set.add(i)

        tiempo = time.time()
        mi_set.add(x)
        transcurso = time.time() - tiempo
        fin_ram = proceso.memory_info().rss - inicio_ram

        print(fin_ram)
