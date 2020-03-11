lista = []

Valor1 = int(input('Digite o primeiro valor: '))
Valor2 = int(input('Digite o segundo valor: '))
Valor3 = int(input('Digite o terceiro valor: '))

lista.append(Valor1)
lista.append(Valor2)
lista.append(Valor3)

lista.sort(reverse=True)

print('O maior valor é ', lista[0])
print('O menor valor é ', lista[2])
print('O valor do meio é ', lista[1])