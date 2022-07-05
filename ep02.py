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

"""

## parâmetros para o método das congruências lineares:
m = 2**32
a = 22695477
c = 1
anterior = 42
# Continue aqui o seu programa ...
#FUNCOES
def somaDigitos(n):
    soma=0
    digitos=0
    divisor=1
    while(n//divisor>0):
        digitos+=1
        divisor=divisor*10
    while(digitos>0):
        soma+=((n//(10**(digitos-1)))-(n//(10**(digitos))*10))
        digitos+=-1
    return soma

def  rodada(num1,num2):
    while(num1>9):
        num1=somaDigitos(num1)
    while(num2>9):
        num2=somaDigitos(num2)
    if  num1==num2:
        resultadoRodada=1
    else:
        resultadoRodada=0
    return resultadoRodada

#PARTE 1
numJogadas=int(input("Digite o numero de jogadas: "))
numAcertos=0
j=0
while(j<numJogadas):
    n1=int(input("Pessoa 1: digite um numero: "))
    n2=int(input("Pessoa 2: digite um numero: "))
    numAcertos+=rodada(n1,n2)
    j+=1
aleatoriedade=str(input("Deseja simular jogadas aleatorias (S/N)? "))
if(aleatoriedade=="N"):
    afinidade=numAcertos/numJogadas

#PARTE 2
elif(aleatoriedade=="S"):
    h=0
    i=0
    a=22695477
    c=1
    m=2**32
    numero_aleatorio_anterior=anterior
    igualdade=0
    while(i<10000):
        i+=1
        h=0
        RnumAcertos=0
        while(h<numJogadas):
            numero_aleatorio=((a*numero_aleatorio_anterior)+c)%m
            Rn1=numero_aleatorio
            numero_aleatorio_anterior=numero_aleatorio
            numero_aleatorio=((a*numero_aleatorio_anterior)+c)%m
            Rn2=numero_aleatorio
            numero_aleatorio_anterior=numero_aleatorio
            RnumAcertos+=rodada(Rn1,Rn2)
            h+=1
        if(RnumAcertos>=numAcertos):
            igualdade+=1
    p=igualdade/10000
    afinidade=1-p

print("A afinidade de voces e de ",afinidade)
if(afinidade>=0 and afinidade<1/3):
    print("A afinidade de voces e baixa. Que pena!")
elif(afinidade>=1/3 and afinidade<2/3):
    print("A afinidade de voces e mediana!")
else:
    print("Parabens! Voces tem uma bela afinidade!")
          
          





          
