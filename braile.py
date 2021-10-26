def inicializa():
    b = ['.***..', '*.....','*.*...','**....','**.*..','*..*..','***...','****..','*.**..','.**...']
    return b

def lectura(nombre):
    ent = open(nombre)
    cant = int(ent.readline())
    ls1 = ent.readline().rstrip('\n').split(' ')
    ls2 = ent.readline().rstrip('\n').split(' ')
    ls3 = ent.readline().rstrip('\n').split(' ')
    ent.close()
    digi = []
    i = 0
    while i < cant:
        d = ls1[i] + ls2[i] + ls3[i]
        digi.append(d)
        i = i + 1
    return digi

def procesar(nros, digitob):
    cant = len(nros)
    salida = ''
    for elem in nros:
        posi = digitob.index(elem)
        salida = salida + str(posi)
    return salida

def escribir(nombre, salida):
    sal = open(nombre,'w')
    sal.write(salida+'\n')
    sal.close()

if __name__ == "__main__":
    digitob = inicializa()
    nros = lectura('brailedatos.txt')
    salida = procesar(nros, digitob)
    escribir('brailesalida.txt', salida)


