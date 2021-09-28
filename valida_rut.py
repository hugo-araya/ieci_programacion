status = False
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
                if dv.lower() == 'k':
                    status = True
                else:
                    if dv.isdigit() != True:
                        print('El rut no es valido (5)')
                    else:
                        status = True

if status == True:
    factor = "765432765432"
    suma = 0
    largo = len(numero)
    j = -1
    while j >= largo*-1:
        suma = suma + int(numero[j])*int(factor[j])
        j = j - 1
    resto = suma % 11
    dv1 = 11 - resto
    if dv1 == 10:
        dv1 = "k"
    else:
        dv1 = str(dv1)
    if dv == dv1:
        print("El rut esta correcto")
    else:
        print('El rut no es valido (6)' )




