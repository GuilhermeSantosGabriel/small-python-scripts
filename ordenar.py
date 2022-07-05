
def determineIndiceDoMenor(vetor, ini, n):

    menor = vetor[ini]
    indice = ini

    for i in range(ini, n):
        if (vetor[i] < menor):
            menor = vetor[i]
            indice = i

    return indice

#Pegar valores
tamanho = int(input())
dados = []

for _ in range(tamanho):
    dados.append(int(input()))

#Hora de ordenar
for ini in range(len(dados)):

    indice = determineIndiceDoMenor(dados, ini, len(dados))

    print(indice, dados[indice])

    trocar_ini = dados[ini]
    trocar_indice = dados[indice]

    dados[ini] = trocar_indice
    dados[indice] = trocar_ini


stringBonita = str(dados[0])

for i in range(1, len(dados)):
    stringBonita = stringBonita + " " + str(dados[i])

print(stringBonita)