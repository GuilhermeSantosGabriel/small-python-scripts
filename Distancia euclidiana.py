import math

def distanciaEuclidiana(n , v1, v2):
    x = 0
    for i in range(n):
        x +=(v1[i] - v2[i])**2

    return math.sqrt(x)

n = int(input())

v1 = list(map(float, input().split()))

v2 = list(map(float, input().split()))

raiz = distanciaEuclidiana(n, v1, v2)

print("%10.5f" % raiz)