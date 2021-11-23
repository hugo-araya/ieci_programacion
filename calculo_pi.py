def leibniz(iteraciones):
    n = 0
    suma = 0
    while n <= iteraciones:
        termino = ((-1)**n) / (2*n+1)
        suma = suma + termino
        n = n + 1
    return 4 * suma

def wallis(iteraciones):
    # ....
    return 2 * prod

if __name__ == '__main__':
    leibniz_PI = leibniz(100000)
    print(leibniz_PI)
    wallis_PI = wallis(100000)
    print(wallis_PI)
    

