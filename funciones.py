def max(numero1, numero2):
    if numero1 > numero2:
        mayor = numero1
    else:
        mayor = numero2
    return mayor

def MAX_DE_TRES(NUMERO1, NUMERO2, NUMERO3):
    if NUMERO1>=NUMERO2 and NUMERO1>=NUMERO3:
        MAYOR=NUMERO1
    if NUMERO2>=NUMERO1 and NUMERO2>=NUMERO3:
        MAYOR=NUMERO2
    if NUMERO3>=NUMERO1 and NUMERO3>=NUMERO2:
        MAYOR=NUMERO3
    return MAYOR

def max_de_tres(numero1, numero2, numero3):
    if numero1 > numero2:
        if numero1 > numero3:
            return numero1
        else:
            return numero3
    else:
        if numero2 > numero3:
            return numero2
        else:
            return numero3

def max_de_tres_o(numero1, numero2, numero3):
    candidato = max(numero1, numero2)
    mayor = max(candidato, numero3)
    return mayor

def max_de_tres_x(numero1, numero2, numero3):
    return max(max(numero1, numero2), numero3)

if __name__ == '__main__':
    n1 = 5
    n2 = 2
    n3 = 5
    mayor = MAX_DE_TRES(n1,n2,n3)
    print(mayor)
    mayor = max_de_tres(n1,n2,n3)
    print(mayor)
    mayor = max_de_tres_o(n1,n2,n3)
    print(mayor)
    mayor = max_de_tres_x(n1,n2,n3)
    print(mayor)