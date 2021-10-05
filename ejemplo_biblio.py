import math

if __name__ == '__main__':
    ar = open('numeros.txt')
    numero = ar.readline()
    while numero != '':
        numero = float(numero)
        raiz = math.sqrt(numero)
        print('La raiz cuadrada de', numero,'es:', raiz)
        numero = ar.readline()
