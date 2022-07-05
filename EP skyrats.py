from cmath import cos, pi, sin, sqrt
import random
import math
#só pra simular que o drone está armado:
isReadyToFly = True

print("Bem vindo ao simulador de package delivery!")

def choose_environment():
    environments = ["Floresta", "Cidade", "Deserto"]
    chosen_environment = environments[random.randint(0,2)]
    print("Ambiente randomizado: ", chosen_environment)

    #ordem: trajetoria, velocidade, altura
    match chosen_environment:
        case "Floresta":
            return ("trajetoria circular", 5, 5)
        case "Cidade":
            return ("trajetoria manhattan", 3, 10)
        case "Deserto":
            return ("trajetoria retilinea", 8, 3)

def change_pos(drone, x_init, y_init, x_goal, y_goal, trajectory_type, speed, height):
    print("Altura de %.1d metros atingida." %(height))

    match trajectory_type:
        case "trajetoria retilinea":
            print("Iniciando trajetória retilínea com velocidade de %.1fm/s" %(speed))
            #O ângulo é o arctan da reta formada pelas coordenadas de partida e chegada. Esse ângulo determina a 
            #velocidade em x (com cosseno do ângulo) e a velocidade em y (com o seno do ângulo)
            angle = math.atan2((y_goal - y_init),(x_goal - x_init))
            trajectory = math.sqrt((x_goal - x_init)**2 + (y_goal - y_init)**2)
            for t in range(1, int(trajectory/speed) + 1):
                x_current = x_init + math.cos(angle)*speed*t
                y_current = y_init + math.sin(angle)*speed*t    
                print(drone, "(%.4f, %.4f) em %1d seg." %(x_current, y_current, t))
            print(drone, "chegou em (%.0f, %.0f)" %(x_goal, y_goal))
            print(drone, "entregou o pacote com sucesso!")

        case "trajetoria manhattan":
            print("Iniciando trajetória manhattan com velocidade de %.1fm/s" %(speed))
            #alterando a posição em x
            print("Ajustando a posição em X")
            y_current = y_init
            x_current = x_init
            if(x_init < x_goal):
                for t in range(1, int(abs(x_goal - x_init)/speed) + 1):
                    x_current = x_init + speed*t
                    print(drone, "(%.4f, %.4f) em %1d seg." %(x_current, y_current, t))
            elif(x_init > x_goal):
                for t in range(1, int(abs(x_goal - x_init)/speed) + 1):
                    x_current = x_init - speed*t
                    print(drone, "(%.4f, %.4f) em %1d seg." %(x_current, y_current, t))
            print(drone, "chegou em (%.0f, %.0f)" %(x_goal, y_init))
            
            #alterando a posição em y
            if(y_init < y_goal):
                for t in range(1, int(abs(y_goal - y_init)/speed) + 1):
                    y_current = y_init + speed*t
                    print(drone, "(%.4f, %.4f) em %1d seg." %(x_current, y_current, t))
            elif(y_init > y_goal):
                for t in range(1, int(abs(y_goal - y_init)/speed) + 1):
                    y_current = y_init - speed*t
                    print(drone, "(%.4f, %.4f) em %1d seg." %(x_current, y_current, t))
            print(drone, "chegou em (%.0f, %.0f)" %(x_goal, y_goal))
            print(drone, "entregou o pacote com sucesso!")

        case "trajetoria circular":
            print("Iniciando trajetória circular com velocidade de %.1fm/s" %(speed))
            radius = math.sqrt((x_goal - x_init)**2 + (y_goal - y_init)**2)/2
            radial_velocity = speed/radius
            w0 = math.atan2((y_goal - y_init),(x_goal - x_init)) + math.pi
            circunference_center = [(x_goal + x_init)/2, (y_goal + y_init)/2]
            for t in range(1, int(math.pi*radius/speed) + 1):
                x_current = radius*math.cos(radial_velocity*t + w0) + circunference_center[0]
                y_current = radius*math.sin(radial_velocity*t + w0) + circunference_center[1]
                print(drone, "(%.4f, %.4f) em %1d seg." %(x_current, y_current, t))
            print(drone, "chegou em (%.0f, %.0f)" %(x_goal, y_goal))
            print(drone, "entregou o pacote com sucesso!")

def main():
    #Input do usuário
    drone = input("Qual drone estaremos voando? \nDrone:")
    print("De onde o drone partirá?")
    x_init = float(input("x: "))
    y_init = float(input("y: "))
    print("E onde fará a entrega?")
    x_goal = float(input("x: "))
    y_goal = float(input("y: "))

    if(isReadyToFly):
        print("O drone foi armado e está pronto para voar")
        environment_tuple = choose_environment()
        print("Nesse ambiente, o drone seguirá uma", environment_tuple[0], "!")
        change_pos(drone, x_init, y_init, x_goal, y_goal, environment_tuple[0], environment_tuple[1], environment_tuple[2])
        while():
            user_input = input("Existe outra entrega no local? (1 p/ sim e 2p/ não)")
            if(user_input == "1"):
                print("E onde fará a entrega?")
                x_init = x_goal
                y_init = y_goal
                x_goal = float(input("x: "))
                y_goal = float(input("y: "))
                environment_tuple = choose_environment()
                print("Nesse ambiente, o drone seguirá uma", environment_tuple[0], "!")
                change_pos(drone, x_init, y_init, x_goal, y_goal, environment_tuple[0], environment_tuple[1], environment_tuple[2])

            elif(user_input == "2"):
                print("Obrigado por usar esse programa!")
                break

    else:
        print("O drone não foi armado corretamente")

main()


"""""
TESTES DA FUNÇÃO change_pos() BASEADOS NA IMAGEM DO EP
change_pos("S1000", 0,0,25,30,"trajetoria retilinea",10,3)

change_pos("S1000", 25,30,47,63,"trajetoria retilinea",10,3)

change_pos("S1000", 47,63,70,81,"trajetoria manhattan",5,5)

change_pos("S1000", 70,81,90,96,"trajetoria retilinea",10,3)

change_pos("S1000", 90,96,110,120,"trajetoria circular",3,8)
"""