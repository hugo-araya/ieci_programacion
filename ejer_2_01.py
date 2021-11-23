def entrada():
    lista = [9, 8, 72, 22, 21, 81, 2, 1, 11, 76, 32, 54]
    return lista

def proceso(l):
    mayor = l[0]
    for nro in l:
        if nro > mayor:
            mayor = nro
    return mayor

def salida(mayor):
    print('El mayor es: ', mayor)

if __name__ == '__main__':
    l = entrada()
    mayor = proceso(l)
    salida(mayor)