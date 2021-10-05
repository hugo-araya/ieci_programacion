import matplotlib.pyplot as plt

def lectura(nombre):
    ar = open(nombre)
    linea1 = ar.readline()
    linea2 = ar.readline()
    ar.close()
    X = linea1.split(',')
    Y1 = linea2.split(',')
    Y = []
    largo = len(Y1)
    i = 0
    while i < largo:
        Y.append(float(Y1[i]))
        i = i + 1
    return X, Y

def Graficar(X, Y):
    plt.plot(Y)
    plt.title('Hecho por Haraya')
    plt.show()

def Finalizar(X, Y):
    largo = len(X)
    i = 0
    while i < largo:
        print(X[i],' -- ', Y[i])
        i = i + 1

if __name__ == '__main__':
    X, Y = lectura('TotalesNacionalesResumen.csv') 
    Graficar (X, Y)
    Finalizar (X, Y)