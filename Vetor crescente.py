
def determineSeOrdenado(vet):
    k = 0
    for i in range(1, len(vet)):
        if((i-1) > vet[i]):
            k +=1

    return k

tamanho = int(input())
lista = []
for _ in range(tamanho):
    lista.append(int(input))

if (determineSeOrdenado(lista) == 0):
    print("sim")

else:
    print("nao",determineSeOrdenado(lista))
    
