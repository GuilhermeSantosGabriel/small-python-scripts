"""
(nesse exemplo os quadrantes não são assim, começa na verdade no canto superior direito só pra facilitar na hora de criar a matriz)

                    |3
                    |           <-X (x,y)
    2 quadrante     |2   1 quadrante
                    |
                    |1  
                    |
-------------------------------------------
   -3   -2    -1    |   1   2   3
                    |-1
                    |
    3 quadrante     |-2  4 quadrante
                    |
                    |-3
                    |

O quadrante que o drone está, bem como o quadrante onde o drone está se dirigindo não terá seus objetos alterados de lugar
"""
#só pra visualizar o procedimento 

import random

#lista com a posição inicial de todos os objetos (nesse caso, como é uma matriz, não vai ter posições negativas na representação,
#então a origem está no canto superior esquerdo)

matriz = [['.' for i in range(6)] for j in range(6)]
objetos = [[0,1], [-4, 2], [5, 1], [5,5]]

for objeto in objetos:
    matriz[objeto[0]][objeto[1]] = "O"

for l in matriz:
    print(" ".join(l))

posicoes_ocupadas = []

for objeto in objetos:
    posicoes_ocupadas.append(objeto)

#mudando a posição dos objetos
while(True):
    input("Digite qualquer tecla para continuar")
    
    for i in range(len(objetos)):
        print("------------------------------------------------------")
        print("objeto: ", objetos[i])


        while(True):
            novo_valor = [random.randint(0, 5), random.randint(0, 5)]
            print("tentativa de posicao: ", novo_valor)
            print("posicoes proibidas", posicoes_ocupadas)
            
            if not(novo_valor in posicoes_ocupadas):
                posicoes_ocupadas.remove(objetos[i])
                objetos[i] = novo_valor
                #muda posição
                posicoes_ocupadas.append(objetos[i])
                print("Posicao valida!")
                break

            print("Posicao invalida, tentando novamente")
            input()


    matriz = [['.' for i in range(6)] for j in range(6)]
    for objeto in objetos:
        matriz[objeto[0]][objeto[1]] = "O"

    for l in matriz:
        print(" ".join(l))

