

diccionario = {} # dict. para la memoizacion

def fibonacci_mem(num): #fibonacci recursivo
    if num not in diccionario.keys():

        if num < 2:
            diccionario[num] = num
        else:
            diccionario[num] = fibonacci_mem(num - 1) + fibonacci_mem(num - 2)

    return diccionario[num]


