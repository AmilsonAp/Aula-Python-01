valorFinanciamento = float(input("Qual valor deseja financiar?\n"))
qtdParcelas = float(input("Em quantos anos deseja financiar?\n"))
Salario = float(input("Qual o seu sal�rio mensal?\n"))

valorParcela = valorFinanciamento / (qtdParcelas*12)

if valorParcela > (Salario*0.3):
    print("Desculpe, seu financiamento n�o pode ser aprovado!")
    print("N�o � permitido que o valor da parcela seja maior que 30% do sal�rio!")
    print("A parcela calculada com base em seus dados � de R${:.2f}".format(valorParcela))
    print("Para os dados informados o valor m�ximo para a parcela � de R${:.2f}".format(Salario*0.3))
else:
    print("PARAB�NS, SEU FINANCIAMENTO FOI APROVADO!")
    print("Informa��es do parcelamento:")
    print("Quantidade de parcelas: ", (qtdParcelas*12))
    print('Valor da parcela: R$ {:.2f}'.format(valorParcela))
    
