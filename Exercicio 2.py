ladoA = int(input('Digite um valor para o lado A do tri�ngulo!\n'))
ladoB = int(input('Digite um valor para o lado B do tri�ngulo!\n'))
ladoC = int(input('Digite um valor para o lado C do tri�ngulo!\n'))

if ladoA == ladoB and ladoB == ladoC:
    print('Essas medidas formam um tri�ngulo EQUILATERO!')
elif ladoA != ladoB and ladoB != ladoC and ladoC != ladoA:
    print('Essas medidas formam um tri�ngulo ESCALENO!')
else:
    print('Essas medidas formam um tri�ngulo IS�SCELES!')