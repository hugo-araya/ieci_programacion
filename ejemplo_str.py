

if __name__ == '__main__':
    ar = open('notas_ficticias.csv')
    sal = open('salida.txt', 'w')
    linea = ar.readline()
    while linea != '':
        linea = linea.rstrip('\n')
        lista = linea.split(';')
        sal.write('Numero de lista: ' + lista[2] + '\n')
        sal.write('Nombre: ' + lista[0] + '\n')
        sal.write('Nota: ' + lista[1] + '\n')
        sal.write('---------------------------\n')
        linea = ar.readline()
    ar.close()
    sal.close()

