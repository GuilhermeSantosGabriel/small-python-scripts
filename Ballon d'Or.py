
def votar(dicionario):
    ponto = 6
    premiado = input()
    #Loop inicial
    isInDicionario = False
    for key, value in dicionario.items():
        if (key == premiado):
            dicionario.update({key:(6 + value)})
            isInDicionario = True
    if not(isInDicionario):
        dicionario[premiado] = 6

    #Proximos loops
    for i in range(2, 4):
        premiado = input()
        isInDicionario = False
        for key, value in dicionario.items():
            if (key == premiado):
                dicionario.update({key:(6 - i + value)})
                isInDicionario = True
        if not(isInDicionario):
            dicionario[premiado] = 6 - i
    return dicionario

def lerDicionario(dicionario):
    print(dicionario)
    keys = list(dicionario.keys())
    values = list(dicionario.values())
    lista = []
    for i in range(len(keys)):
        lista.append([keys[i],values[i]])
    lista.sort(key = lambda item: item[1])
    lista.reverse()

    for candidato in lista:
        print(candidato[0] + ": " + str(candidato[1]))


def main():
    #numero de jornalistas
    n_jornalistas = int(input())
    k = 0
    #dicionario vazio
    dicionario = {}
    while(n_jornalistas > k):
        k += 1    
        dicionario = votar(dicionario)
    lerDicionario(dicionario)

main()