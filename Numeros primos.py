
def encontrarPrimos(limite):
    lista = [2]
    listaPrimos = [2]
    for numero in range(3, limite + 1, 2):
        lista.append(numero)

    for i in range(1, len(lista)):
        check = False
        n = 0
        while(n < i):
            if (lista[i] % lista[n] == 0):
                check = True
                break
            n += 1
        if not(check):
            listaPrimos.append(lista[i])

    print(listaPrimos)
    print(len(listaPrimos))

encontrarPrimos(100000)