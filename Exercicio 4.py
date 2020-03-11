valorFinanciamento = float(input("Qual valor deseja financiar?\n"))
qtdParcelas = float(input("Em quantos anos deseja financiar?\n"))
Salario = float(input("Qual o seu salário mensal?\n"))

valorParcela = valorFinanciamento / (qtdParcelas*12)

if valorParcela > (Salario*0.3):
    print("Desculpe, seu financiamento não pode ser aprovado!")
    print("Não é permitido que o valor da parcela seja maior que 30% do salário!")
    print("A parcela calculada com base em seus dados é de R${:.2f}".format(valorParcela))
    print("Para os dados informados o valor máximo para a parcela é de R${:.2f}".format(Salario*0.3))
else:
    print("PARABÉNS, SEU FINANCIAMENTO FOI APROVADO!")
    print("Informações do parcelamento:")
    print("Quantidade de parcelas: ", (qtdParcelas*12))
    print('Valor da parcela: R$ {:.2f}'.format(valorParcela))
    
