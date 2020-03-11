ladoA = int(input('Digite um valor para o lado A do triângulo!\n'))
ladoB = int(input('Digite um valor para o lado B do triângulo!\n'))
ladoC = int(input('Digite um valor para o lado C do triângulo!\n'))

if ladoA == ladoB and ladoB == ladoC:
    print('Essas medidas formam um triângulo EQUILATERO!')
elif ladoA != ladoB and ladoB != ladoC and ladoC != ladoA:
    print('Essas medidas formam um triângulo ESCALENO!')
else:
    print('Essas medidas formam um triângulo ISÓSCELES!')