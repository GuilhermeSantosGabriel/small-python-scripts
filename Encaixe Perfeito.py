"""
Esse joguinho consiste em duas peças com tamanhos diferentes, algo como:

 #####      #   #
  ##      ### ####
   #     ##########
 peça1    peça2

O objetivo do jogo é encaixar a peça um na peça dois, com o menor espaço entre as duas peças. A peça dois pode ser invertida.
O código determina o melhor encaixe possível. Segue parte do enunciado explicando o código:

Seu programa receberá como entrada um número inteiro positivo N, indicando a quantidade de partidas do jogo que serão jogadas. 
Para cada partida, seu programa receberá duas linhas. A primeira linha apresentará P1 números inteiros positivos separados por 
espaços, indicando a altura em cada região da peça 1 (da esquerda para direita). Na segunda linha, seu programa receberá P2 n-
úmeros inteiros positivos separados por espaços, indicando a altura em cada região da peça 2 (também da esquerda para direita).

Como saída, seu programa deverá informar, para cada partida, a melhor pontuação obtida, a partir de que posição da peça 2 o enc
aixe da peça 1 foi realizado e se a peça 1 foi invertida ou não. Caso seja possível realizar o encaixe perfeito, ou seja, obter
uma pontuação igual a zero, então a mensagem Encaixe Perfeito! também deverá ser exibida. Caso existam múltiplos encaixes que 
resultem na melhor pontuação, a jogada sem inverter a peça 1 tem prioridade sobre a jogada com a peça 1 invertida. Caso o empate 
ainda persista, então o encaixe na posição mais a esquerda na peça 2 deve ser utilizado como critério de desempate.

"""

# Leitura do número de partidas

N = int(input())

def maiorValor(lista):
    maior = lista[0]
    for i in range(1,len(lista)):
        if (lista[i] > maior):
            maior = lista[i]
    return maior

def encaixe(P1, P2):
    pontuacao = []

    for i in range(len(P2) - len(P1) + 1):
        lista = []
        pontos = 0
        for j in range(len(P1)):
            lista.append(P1[j] + P2[j + i])
        maior = maiorValor(lista)
        for k in lista:
            pontos += maior - k
        pontuacao.append(pontos)

    return pontuacao

for _ in range (N):
# Leitura das peças 1 e 2
    P1 = [int(i) for i in input().split()]
    P2 = [int(i) for i in input().split()]

# Processamento das possibilidades de encaixe
    pontuacao = encaixe(P1,P2)
    P1.reverse()
    pontuacao.extend(encaixe(P1,P2))
    check = True
    melhorPontuacao = pontuacao[0]
    print(pontuacao)
    print(len(pontuacao))
    for i in range(len(pontuacao)):
        if (pontuacao[i] == 0):
            check = False
            print("Encaixe Perfeito!")
            if(i + 1 <= len(pontuacao)/2):
                print("Posicao de Encaixe:", i+1)
                print("Peca 1: Normal")
                
            else:
                print("Posicao de Encaixe:", i//2)
                print("Peca 1: Invertida")
            break
        else:
            if(pontuacao[i] < melhorPontuacao):
                melhorPontuacao = pontuacao[i]

    if check:
        for i in pontuacao:
            if (i == melhorPontuacao):
                print("Pontuacao:", melhorPontuacao)
                if(i + 1 <= len(pontuacao)/2):
                    print("Posicao de Encaixe", i+1)
                    print("Peca 1: Normal")
                else:
                    print("Posicao de Encaixe", i//2)
                    print("Peca 1: invertida")
                break