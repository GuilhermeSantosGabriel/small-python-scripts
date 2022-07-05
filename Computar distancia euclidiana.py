import math

def distanciaEuclidiana(v1, v2):
    distancia = 0
    for i in range(len(v1)):
        distancia += (v1[i] - v2[i])**2
    distancia = math.sqrt(distancia)
    return distancia

def calcula_produto(matriz, vetor):
    resultado = []

    for linha in range(len(matriz)):
        soma = 0
        for coluna in range(len(matriz)):
            soma += matriz[linha][coluna] * vetor[coluna]
        resultado.append(soma)
    return resultado

def main():
    matriz = []
    vetor = []
    m = int(input())
    n = m
    k = n
    while(m > 0):
        n = k
        m += -1
        coluna = []

        while(n > 0):
            n += -1
            coluna.append(float(input()))
        matriz.append(coluna)

    m = k
    while(m > 0):
        m += -1
        vetor.append(float(input))

    print(vetor)
    print(distanciaEuclidiana(calcula_produto(matriz), vetor))
    
main()