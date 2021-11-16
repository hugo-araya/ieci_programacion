def entrada():
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    agno = input('Agno: ')
    return nombre, apellido, agno

def proceso(nombre, apellido, agno):
    salida = agno[2:] + nombre[0] + apellido
    return salida

def output(salida):
    print('Lo solicitado es: ', salida)

if __name__ == '__main__':
    nombre, apellido, agno = entrada()
    salida = proceso(nombre, apellido, agno)
    output(salida)

