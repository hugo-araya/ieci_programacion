def proceso(nombre):
    ent = open(nombre)
    sal = open('datos_salida.txt', 'w')
    for objeto in ent:
        if 'i' in objeto:
            sal.write('N'+'\n')
        else:
            sal.write('S'+'\n')
    ent.close()
    sal.close()

if __name__ == "__main__":
    proceso('datos_laino.txt')
