
def cortarCadenaPorEspacios(cadena):
    return cadena.split()


def binarioADecimal(cadena):
    num = cadena
    dec_value = 0
    base = 1
    lenin = len(num)
    i = lenin - 1
    while i >= 0:
        if num[i] == '1':
            dec_value += base
        base = base * 2
        i = i - 1
    return dec_value


def esNumero(cadena):
    try:
        int(cadena)
        return True
    except:
        return False


def calcular(calculos):

    subCadena = cortarCadenaPorEspacios(calculos)
    operadores = []
    operandos = []
    cant = len(subCadena)

    for i in range(cant):
        if esNumero(subCadena[i]):
            operandos.append(binarioADecimal(subCadena[i]))
        else:
            operadores.append(subCadena[i])

    j = 0
    res = operandos[0]
    i = 1
    while i < (len(operandos)):
        if operadores[j] == '+':
            res += operandos[i]
        if operadores[j] == '-':
            res -= operandos[i]
        if operadores[j] == '*':
            res *= operandos[i]
        if operadores[j] == '/':
            res /= operandos[i]

        i = i + 1
        j = j + 1
    return res
