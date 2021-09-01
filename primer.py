# -*- coding: utf-8 -*-
contador = 0
while contador < 3:
    a = float(input('Coeficiente a: '))
    b = float(input('Coeficiente b: '))
    c = float(input('Coeficiente c: '))
    if a == 0:
        print("No se puede dividir por cero")
    else:
        x = (c - b)/a
        print ("El resultado es: ", x)
    contador = contador + 1
print("Fin ...")