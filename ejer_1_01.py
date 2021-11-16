def proceso(nombre, apellido, agno):
    salida = agno[2:] + nombre[0] + apellido
    return salida

if __name__ == '__main__':
    nombre = 'Nolberto'
    apellido = 'Gonzalez'
    agno = '2020'
    salida = proceso(nombre, apellido, agno)
    print('Lo solicitado es: ', salida)
