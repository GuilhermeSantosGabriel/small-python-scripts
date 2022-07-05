check = True
print ("^checarei se sua sequencia e aritmetica")
n = int(input("quantos numeros na sequencia?: "))
while (n <=2):
    n = int(input("sua sequencia deve ter mais de dois numeros: "))
a0 = float(input("Digite seu primeiro numero da sequencia: "))
a1 = float(input("Digite o proximo numero da sequencia: "))
ak = a1
k = 1
r = a1 - a0

while(ak == a0 + r*k and k + 1 < n):
    k = k + 1
    ak = float(input("Digite o proximo numero da sequencia: "))
    
if (ak == a0 + r*k and k + 1 == n):
    print("Deu bom")
else:
    print("Deu ruim")
