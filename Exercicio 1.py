from math import *

a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))

Delta = (b**2) - 4*a*c
print(Delta) 

if Delta < 0:
    print("Não existe raiz para Delta menor que 0!")
else:
    raiz = sqrt(Delta)
    x1 =  (-b + sqrt(Delta)) / 2*a
    x2 =  (-b - sqrt(Delta)) / 2*a	
    print("Os resultados da raiz de Delta são: ")
    print("%d e %d" %(x1 , x2))


