import os
import time, random,string,psutil
from collections import Counter

proceso = psutil.Process(os.getpid())


for x in range(750000, 19500000, 750000):

    letters = string.ascii_lowercase
    inicio_ram = proceso.memory_info().rss

    for i in range(x):
        cadena = ''.join(random.choice(letters) for i in range(random.randint(30,300)))

    tiempo = time.time()
    Counter(cadena)
    transcurso = time.time() - tiempo
    ram_usada = proceso.memory_info().rss - inicio_ram

    print(ram_usada)


