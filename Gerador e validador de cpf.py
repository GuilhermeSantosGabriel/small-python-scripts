
import random

def verificarCPF(cpf):
    digitosIni=cpf[:-2]
    somaDigitos=0
    for i in range(0,len(digitosIni)):
        somaDigitos=somaDigitos+int(digitosIni[i])*(10-i)
    if (11-(somaDigitos%11)>9):
        digitosIni=digitosIni+'0'
    else:
        digitosIni=digitosIni+str(11-(somaDigitos%11))
    somaDigitos=0
    for i in range(0,len(digitosIni)):
        somaDigitos=somaDigitos+int(digitosIni[i])*(11-i)
    if (11-(somaDigitos%11)>9):
        digitosIni=digitosIni+'0'
    else:
        digitosIni=digitosIni+str(11-(somaDigitos%11))
    if(digitosIni==cpf):
        return print('valido')
    else:
        return print('invalido')
    
def gerarCPF():
    digitos=[]
    soma=0
    string=''
    while(len(digitos)<9):
        digitos.append(random.randrange(0,10))
    for i in range(0,len(digitos)):
        soma+=digitos[i]*(10-i)
    if(11-(soma%11)>9):
        digitos.append(0)
    else:
        digitos.append(11-(soma%11))
    soma=0
    for i in range(0,len(digitos)):
        soma+=digitos[i]*(11-i)
    if(11-(soma%11)>9):
        digitos.append(0)
    else:
        digitos.append(11-(soma%11))
    for i in range(0,len(digitos)):
        string+=str(digitos[i])
    return string


