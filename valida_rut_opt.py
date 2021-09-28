def revisa_forma(rut):
    contar = rut.count('-')
    if contar != 1:
        status = False
    else:
        lisrut = rut.split('-')
        if len(lisrut)!=2:
            status = False
        else:
            numero = lisrut[0]
            if numero.isdigit() != True:
                status = False
            else:
                dv = lisrut[1]
                if len(dv) != 1:
                    status = False
                else:
                    if dv.lower() == 'k':
                        status = True
                    else:
                        if dv.isdigit() != True:
                            status = False
                        else:
                            status = True
    return status

def revisa_dv(rut):
    factor = "765432765432"
    suma = 0
    lisrut = rut.split('-')
    numero = lisrut[0]
    dv = lisrut[1]
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
        status = True
    else:
        status = False
    return status

if __name__ == "__main__":
    rut = input('Digite un rut: ')
    status = revisa_forma(rut)
    if status == True:
        status = revisa_dv(rut)
        if status == True:
            print ('Rut Correcto')
        else:
            print ('Rut Incorrecto')
    else:
        print ('Rut Incorrecto')




