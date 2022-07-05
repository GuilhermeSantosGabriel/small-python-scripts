"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Guilherme Santos Gabriel
  NUSP : 12554925
  Turma: 7
  Prof.: Sinai Robins

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort
  
  Referências:
  - As funções adicionais ordenacaoInsercao e pertence (busca binária)
  foram retiradas do guia de estudo da semana 10,disponíveis em
  https://www.ime.usp.br/~mac2166/2021/semana10
"""
  
###############################################################################
# Funções Adicionais 
# Se quiser, escreva aqui funções adicionais para ajudar na resolução do EP.
###############################################################################

### ESCREVA AQUI AS FUNÇÕES ADICIONAIS
    
def ordenacaoInsercao(seq):
  n = len(seq)
  for i in range(0,n-1):
    # Insere seq[i+1] em seq[0],...,seq[i].
    x = seq[i+1]
    j = i
    while j >= 0 and seq[j] > x:
      seq[j+1] = seq[j]
      j -= 1
    seq[j+1] = x
  return seq 
    
# Busca binária:
def pertence(x, L):
  n = len(L)
  inic = 0
  fim = n-1
  while inic <= fim:
    meio = (inic+fim)//2
    if x == L[meio]:
      return True
    elif x > L[meio]:
      inic = meio+1
    else:
      fim = meio-1
 
  return False
  
###############################################################################
# Funções Obrigatórias
# Devem ser implementadas sem alterar os parâmetros e tipo do valor de retorno.
###############################################################################
def obtemPalavrasProximas(palavra, vocabulario):
    """ Devolve uma lista de palavras que diferem da palavra do parâmetro 
    em apenas uma letra.
    Na lista, primeiro devem aparecer as palavras que diferem na primeira
    letra à esquerda, depois as que diferem na segunda letra à esquerda, e 
    assim por diante.
    As palavras da lista devolvida devem existir na lista de palavras do 
    vocabulário passada como parâmetro para a função.
    
    Parâmetros:
    palavra -- a palavra da qual se deseja encontrar as palavras próximas
    vocabulario -- lista das palavras do vocabulário"""    
    
    ### ESCREVA AQUI O CORPO DA FUNÇÃO
    palavrasDesordenadas=[]
    for i in range(len(vocabulario)):
        letrasIguais=0
        if (len(vocabulario[i])==len(palavra)):
            for j in range(len(palavra)):
                if (vocabulario[i][j]==palavra[j]):
                    letrasIguais+=1
            if (letrasIguais==len(palavra)-1):
                palavrasDesordenadas.append(vocabulario[i])
    palavrasProximas=[]
    for i in range(len(palavra)):
        check=False
        listaApoio=[]
        for j in range(len(palavrasDesordenadas)):
            if (palavrasDesordenadas[j][i]!=palavra[i]):
                check=True
                listaApoio.append(palavrasDesordenadas[j])
        if (check):
            listaApoio=ordenacaoInsercao(listaApoio)
            for k in range(len(listaApoio)):
                    palavrasProximas.append(listaApoio[k])    
    return palavrasProximas  # lista das palavras próximas


def criaArvoreDeBusca(inicio, fim, vocabulario):
    """ Devolve uma lista com os nós da árvore de busca de caminho entre as
    palavras inicio e fim. Cada nó é uma lista contendo uma palavra e a 
    posição do seu nó pai. Portanto, a função devolve uma lista de listas.
    Os nós possuem apenas palavras existentes na lista de palavras do 
    vocabulário passada no parâmetro.
    
    Parâmetros:
    inicio -- palavra de início do caminho a ser buscado
    fim -- palavra de fim do caminho a ser buscado
    vocabulario -- lista das palavras do vocabulário"""
    
    ### ESCREVA AQUI O CORPO DA FUNÇÃO
    ### VOCÊ DEVE USAR A obtemPalavrasProximas() NA IMPLEMENTAÇÃO
    indice=-1
    arvore=[[inicio,-1]]
    ramo=[inicio]
    while(len(ramo)!=0):
        proximoRamo=[]
        for i in range(len(ramo)):
            indice+=1
            palavrasProximas=obtemPalavrasProximas(ramo[i],vocabulario)
            for j in range(len(palavrasProximas)):
                if(palavrasProximas[j]==fim):
                    arvore.append([palavrasProximas[j],indice])
                    return arvore
                else:
                    contem=False
                    for k in arvore:
                        if(k[0]==palavrasProximas[j]):
                            contem=True
                    if (contem==False):
                        arvore.append([palavrasProximas[j],indice])
                        proximoRamo.append(palavrasProximas[j])
        ramo=proximoRamo
    return arvore  # lista da arvore de busca do caminho


def obtemCaminho(inicio, fim, vocabulario):
    """Devolve uma lista com as palavras do caminho entre as palavras inicio
    e fim. O caminho contém apenas palavras existentes na lista  vocabulário
    passada no parâmetro e inclui as palavras inicio e fim.
    Caso não haja caminho entre inicio e fim, a função devolve uma lista 
    vazia.
        
    Parâmetros:
    inicio -- palavra de início do caminho a ser buscado
    fim -- palavra de fim do caminho a ser buscado
    vocabulario -- lista das palavras do vocabulário"""

    ### ESCREVA AQUI O CORPO DA FUNCAO   
    ### VOCÊ DEVE USAR A criaArvoreDeBusca() NA IMPLEMENTAÇÃO
    arvore=criaArvoreDeBusca(inicio,fim,vocabulario)
    caminho=[inicio]
    if(arvore[len(arvore)-1][0]==fim):
        palavra=arvore[len(arvore)-1]
        while(palavra[1]!=-1):
            caminho.append(palavra[0])
            palavra=arvore[palavra[1]]
        reversa=[]
        for i in range(1,len(caminho)+1):
            reversa.append(caminho[-1*i]) 
    else:
        return[]
    caminho=reversa
    return caminho  # lista das palavras do caminho

 
def main():
    """Esta função faz a interação com o usuário (ou seja, cuida da entrada
    e saída de dados). Ela possibilita a execução de testes sobre as três 
    funções obrigatórias -- obtemPalavrasProximas(), criaArvoreDeBusca(), 
    obtemCaminho() -- do EP4."""
    
    # Nome do arquivo de vocabulário
    nome_arquivo = "./vocabulario.txt"
    
    ### ESCREVA AQUI O CORPO DA FUNÇÃO
    vocabulario=[]
    arquivo=open(nome_arquivo,'r')
    palavraVocabulario = arquivo.readline()
    while (palavraVocabulario != ""):
        vocabulario.append(palavraVocabulario.split('\n')[0])
        palavraVocabulario=arquivo.readline()
    escolha=-1
    while (escolha!=0):
        escolha=int(input("Digite a opcao: "))
        if(escolha==1):
            palavra=str(input("Digite uma palavra: "))
            resposta=obtemPalavrasProximas(palavra,vocabulario)
            print("Palavras proximas de",palavra+":",resposta)
        if(escolha==2):
            palavraInicial=str(input("Digite a palavra de inicio: "))
            palavraFinal=str(input("Digite a palavra de fim: "))
            resposta=criaArvoreDeBusca(palavraInicial,palavraFinal,vocabulario)
            print("Quantidade de nos da arvore:",len(resposta))
            print("Arvore:",resposta)
        if(escolha==3):
            palavraInicial=str(input("Digite a palavra de inicio: "))
            palavraFinal=str(input("Digite a palavra de fim: "))
            caminho=(obtemCaminho(palavraInicial,palavraFinal,vocabulario))
            caminhoBonitinho=palavraInicial
            if(caminho==[]):
                print("Nao existe caminho entre",palavraInicial,"e",palavraFinal)
            else:
                for i in range(len(caminho)):
                    if(i!=len(caminho)-1):
                        caminhoBonitinho=caminhoBonitinho+" -> "+caminho[i]
                print("A distancia entre",palavraInicial,"e",palavraFinal,"é",len(caminho)-1)
                print(caminhoBonitinho)
    return


# NÃO REMOVA AS LINHAS A SEGUIR
if __name__ == '__main__':
    main()
