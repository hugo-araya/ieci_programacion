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

def largo(lista):
    contador = 0
    for elem in lista:
        contador = contador + 1
    return contador

def es_vocal_1(carac):
    if carac == 'a' or carac == 'e' or carac == 'i' or carac == 'o' or carac == 'u':
        return True
    else:
        return False

def es_vocal_2(carac):
    if carac == 'a' or carac == 'e' or carac == 'i' or carac == 'o' or carac == 'u' or carac == 'A' or carac == 'E' or carac == 'I' or carac == 'O' or carac == 'U':
        return True
    else:
        return False

def es_vocal_3(carac):
    vocales = 'aeiouAEIOU'
    if carac in vocales:
        return True
    else:
        return False

def es_vocal_4(carac):
    vocales = 'AEIOU'
    if carac.upper() in vocales:
        return True
    else:
        return False

if __name__ == '__main__':
    caracter = 'a'
    resultado = es_vocal_4(caracter)
    print(resultado)