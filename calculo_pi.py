def leibniz(iteraciones):
    n = 0
    suma = 0
    while n <= iteraciones:
        termino = ((-1)**n) / (2*n+1)
        suma = suma + termino
        n = n + 1
    return 4 * suma

def wallis(iteraciones):
    n = 1
    prod = 1
    while n <= iteraciones:
        termino = (2*n/(2*n-1))*(2*n/(2*n+1))
        prod = prod * termino
        n = n + 1
    return 2 * prod

if __name__ == '__main__':
    iter = 4000000
    PI_estimado = 3.141592
    leibniz_PI = leibniz(iter)
    print(leibniz_PI,abs(leibniz_PI - PI_estimado))
    wallis_PI = wallis(iter)
    print(wallis_PI, abs(wallis_PI-PI_estimado))