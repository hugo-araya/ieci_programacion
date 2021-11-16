def entrada(archivo):
    ent = open(archivo)
    datos = []
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split(',')
        datos.append(lista)
    return datos

def proceso(datos):
    datos_salida = []
    for elemento in datos:
        nombre = elemento[0]
        apellido = elemento[1]
        agno = elemento[2]
        salida = agno[2:] + nombre[0] + apellido
        datos_salida.append(salida)
    return datos_salida

def output(datos_salida):
    for elemento in datos_salida:
        print('Lo solicitado es: ', elemento)

if __name__ == '__main__':
    datos = entrada('datos.txt')
    datos_salida = proceso(datos)
    output(datos_salida)

