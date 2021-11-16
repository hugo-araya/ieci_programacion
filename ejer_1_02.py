def proceso(nombre, apellido, agno):
    salida = agno[2:] + nombre[0] + apellido
    return salida

if __name__ == '__main__':
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    agno = input('Agno: ')
    salida = proceso(nombre, apellido, agno)
    print('Lo solicitado es: ', salida)
