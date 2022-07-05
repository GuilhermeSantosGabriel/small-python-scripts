
#def conjunto_representantes(n, vet, conjunto):

vet = [3,3,1]
n = 3 #so pra dps
conjunto = []
lenConjunto = 0
k = 0


while(k < n):
    isContido = False
    j = 0
    while(j < lenConjunto):
        if (vet[k] == conjunto[j]):
            isContido = True
            break
        j += 1
    if not(isContido):
        conjunto.append(vet[k])
        lenConjunto +=1
        j += 1

    k += 1

