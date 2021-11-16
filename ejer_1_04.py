def entrada(archivo):
    ent = open(archivo)
    nombre = ent.readline().rstrip('\n')
    apellido = ent.readline().rstrip('\n')
    agno = ent.readline().rstrip('\n')
    return nombre, apellido, agno

def proceso(nombre, apellido, agno):
    salida = agno[2:] + nombre[0] + apellido
    return salida

def output(salida):
    print('Lo solicitado es: ', salida)

if __name__ == '__main__':
    nombre, apellido, agno = entrada('datos.txt')
    salida = proceso(nombre, apellido, agno)
    output(salida)

