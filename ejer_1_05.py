def entrada(archivo):
    ent = open(archivo)
    linea = ent.readline().rstrip('\n')
    lista = linea.split(',')
    return lista[0], lista[1], lista[2]

def proceso(nombre, apellido, agno):
    salida = agno[2:] + nombre[0] + apellido
    return salida

def output(salida):
    print('Lo solicitado es: ', salida)

if __name__ == '__main__':
    nombre, apellido, agno = entrada('datos.txt')
    salida = proceso(nombre, apellido, agno)
    output(salida)

