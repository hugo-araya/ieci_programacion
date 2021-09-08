rut = input('Digite un rut: ')
contar = rut.count('-')
if contar != 1:
    print('El rut no es valido (1)')
else:
    lisrut = rut.split('-')
    if len(lisrut)!=2:
        print('El rut no es valido (2)')
    else:
        numero = lisrut[0]
        if numero.isdigit() != True:
            print('El rut no es valido (3)')
        else:
            dv = lisrut[1]
            if len(dv) != 1:
                print('El rut no es valido (4)')
            else:
                if dv == 'k':
                    print('El rut es correcto')
                else:
                    if dv.isdigit() != True:
                        print('El rut no es valido (5)')
                    else:
                        print('El rut es correcto')