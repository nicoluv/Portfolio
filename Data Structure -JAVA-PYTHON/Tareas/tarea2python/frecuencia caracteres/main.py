from collections import Counter

if __name__ == '__main__':


    print("Bienvenido, digita tu string y te diremos la frecuencia de sus caracteres")
    cadena=input()

    print(Counter(cadena))